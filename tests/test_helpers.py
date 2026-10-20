"""Shared test helpers, environment discovery, and validation utilities."""

import os
import sys
import struct
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional, Tuple, List

# Target repository default
TARGET_REPO_ROOT = Path(os.environ.get("TARGET_REPO", r"c:\Users\renu5\Downloads\manim_video_repo")).resolve()
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

CANDIDATE_BLENDER_PATHS = [
    r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe",
    r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe",
    r"C:\Program Files\Blender Foundation\Blender 5.0\blender.exe",
    r"C:\Program Files\Blender Foundation\Blender 4.3\blender.exe",
    r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe",
    r"C:\Program Files\Blender Foundation\Blender 4.1\blender.exe",
    r"C:\Program Files\Blender Foundation\Blender 4.0\blender.exe",
    os.path.expanduser("~/blender/blender"),
    "/usr/bin/blender",
    "/usr/local/bin/blender",
]

CANDIDATE_FFMPEG_PATHS = [
    r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe",
    r"C:\ffmpeg\bin\ffmpeg.exe",
]

CANDIDATE_FFPROBE_PATHS = [
    r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Links\ffprobe.exe",
    r"C:\ffmpeg\bin\ffprobe.exe",
]


def find_blender_binary() -> Optional[str]:
    """Locate the Blender executable across PATH and known system locations."""
    env_bin = os.environ.get("BLENDER_BIN") or os.environ.get("BLENDER_PATH")
    if env_bin and os.path.isfile(env_bin):
        return env_bin

    which_bin = shutil.which("blender")
    if which_bin:
        return which_bin

    for candidate in CANDIDATE_BLENDER_PATHS:
        if os.path.isfile(candidate):
            return candidate

    return None


def find_ffmpeg_binary() -> Optional[str]:
    """Locate the FFmpeg executable."""
    which_bin = shutil.which("ffmpeg")
    if which_bin:
        return which_bin
    for candidate in CANDIDATE_FFMPEG_PATHS:
        if os.path.isfile(candidate):
            return candidate
    return None


def find_ffprobe_binary() -> Optional[str]:
    """Locate the FFprobe executable."""
    which_bin = shutil.which("ffprobe")
    if which_bin:
        return which_bin
    for candidate in CANDIDATE_FFPROBE_PATHS:
        if os.path.isfile(candidate):
            return candidate
    return None


def run_blender_script(
    script_path: str,
    extra_args: Optional[List[str]] = None,
    timeout: int = 120,
    cwd: Optional[str] = None
) -> subprocess.CompletedProcess:
    """Execute a python script headlessly inside Blender."""
    blender_bin = find_blender_binary()
    if not blender_bin:
        raise FileNotFoundError("Blender binary not found on this system.")

    cmd = [blender_bin, "-b", "-P", str(script_path)]
    if extra_args:
        cmd.extend(extra_args)

    return subprocess.run(
        cmd,
        cwd=cwd or str(WORKSPACE_ROOT),
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False
    )


def validate_png_header(file_path: str) -> Dict[str, Any]:
    """
    Parse and validate PNG binary header and IHDR chunk.
    Returns:
        dict with keys: valid, width, height, bit_depth, color_type, file_size, error
    """
    if not os.path.exists(file_path):
        return {"valid": False, "error": f"File does not exist: {file_path}"}

    file_size = os.path.getsize(file_path)
    if file_size < 24:
        return {"valid": False, "error": f"File too small ({file_size} bytes)"}

    with open(file_path, "rb") as f:
        header = f.read(24)

    # Standard PNG magic bytes: \x89PNG\r\n\x1a\n
    expected_magic = b"\x89PNG\r\n\x1a\n"
    if header[:8] != expected_magic:
        return {
            "valid": False,
            "error": f"Invalid PNG signature: {header[:8]!r}",
            "file_size": file_size
        }

    # IHDR chunk: length (4 bytes) + chunk type (4 bytes) + width (4) + height (4) + bit_depth (1) + color_type (1)
    ihdr_len, ihdr_type = struct.unpack(">I4s", header[8:16])
    if ihdr_type != b"IHDR":
        return {
            "valid": False,
            "error": f"First chunk is not IHDR: {ihdr_type!r}",
            "file_size": file_size
        }

    width, height, bit_depth, color_type = struct.unpack(">IIBB", header[16:26])
    return {
        "valid": True,
        "width": width,
        "height": height,
        "bit_depth": bit_depth,
        "color_type": color_type,
        "file_size": file_size,
        "error": None
    }


def calculate_matrix_chunks(total_frames: int, chunk_size: int) -> List[Dict[str, Any]]:
    """
    Reference matrix chunk planner calculation.
    Divides total_frames into chunk_size pieces with continuous 1-based indexing.
    """
    import math
    if total_frames <= 0 or chunk_size <= 0:
        return []

    num_chunks = math.ceil(total_frames / chunk_size)
    chunks = []
    for i in range(num_chunks):
        start_frame = i * chunk_size + 1
        end_frame = min((i + 1) * chunk_size, total_frames)
        chunks.append({
            "id": f"{i:02d}",
            "start": start_frame,
            "end": end_frame,
            "frame_count": end_frame - start_frame + 1
        })
    return chunks
