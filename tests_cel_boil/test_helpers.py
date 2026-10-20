"""
E2E Test Helpers & Verification Oracles
Manim 05-Cel-Boil Audiobook Summary Replication
"""

import os
import sys
import json
import wave
import subprocess
from pathlib import Path
import numpy as np

# Workspace paths
WORKSPACE_ROOT = Path(r"c:\Users\renu5\Downloads\priyanshu readme")
TARGET_REPO = Path(r"C:\Users\renu5\Downloads\mg-styles-15-test\manim-port")
TESTS_DIR = Path(__file__).resolve().parent

# Reference assets
EXPLORER_AUDIO = WORKSPACE_ROOT / ".agents" / "teamwork" / "explorer_survey_2" / "test_audio_clean_30s.wav"
EXPLORER_SFX = WORKSPACE_ROOT / ".agents" / "teamwork" / "explorer_survey_2" / "test_sfx_no_siren.wav"

# Executables
FFMPEG_BIN = Path(r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe")
FFPROBE_BIN = Path(r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffprobe.exe")
VENV_PYTHON = Path(r"C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe")

# Color palette tokens
PALETTE = {
    "cream": "#f4e9d0",
    "ink": "#1c1613",
    "red": "#e5402b",
    "yel": "#ffc425",
    "hi": "#fff6e2",
    "pencil": "#d9573f",
}

# Banned legacy strings (slate, exposure counters, peg bar)
BANNED_LEGACY_STRINGS = [
    "SC. 05",
    "AUDIOBOOK SUMMARY",
    "No. 074",
    "CEL BOIL ANIMATION",
    "on 2s",
    "drawPencil",
    "peg_hole",
    "peg bar",
    "peg_bar",
]


def find_ffprobe() -> Path:
    """Return the absolute path to Gyan FFprobe binary."""
    if FFPROBE_BIN.exists():
        return FFPROBE_BIN
    raise FileNotFoundError(f"Mandatory FFprobe binary not found at: {FFPROBE_BIN}")


def find_ffmpeg() -> Path:
    """Return the absolute path to Gyan FFmpeg binary."""
    if FFMPEG_BIN.exists():
        return FFMPEG_BIN
    raise FileNotFoundError(f"Mandatory FFmpeg binary not found at: {FFMPEG_BIN}")


def probe_media_file(file_path: Path | str) -> dict:
    """Execute ffprobe and return parsed JSON metadata."""
    probe_bin = find_ffprobe()
    target = Path(file_path)
    if not target.exists():
        raise FileNotFoundError(f"Media file does not exist: {target}")

    cmd = [
        str(probe_bin),
        "-v", "error",
        "-show_entries", "format=duration,size,bit_rate,format_name",
        "-show_entries", "stream=codec_name,codec_type,sample_rate,channels,width,height,r_frame_rate,avg_frame_rate,pix_fmt,duration",
        "-of", "json",
        str(target),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def synthesize_police_siren_signal(sample_rate: int = 48000, duration: float = 1.4) -> np.ndarray:
    """Synthesize the exact police siren signal as defined in reference audio.py:15-22.
    
    f(t) = 850 + 260 * sin(2*pi*1.5*t)
    phase = 2*pi*cumsum(f)/sr
    sig = 0.45*sin(phase) + 0.2*sin(2*phase)
    env = min(t/0.08, 1.0) * min((dur-t)/0.15, 1.0)
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    f = 850.0 + 260.0 * np.sin(2.0 * np.pi * 1.5 * t)
    phase = 2.0 * np.pi * np.cumsum(f) / sample_rate
    sig = 0.45 * np.sin(phase) + 0.2 * np.sin(2.0 * phase)
    env = np.minimum(t / 0.08, 1.0) * np.minimum((duration - t) / 0.15, 1.0)
    return (sig * env).astype(np.float32)


def analyze_audio_siren_omission(wav_path: Path | str) -> dict:
    """Perform mathematical spectral cross-correlation check for police siren omission.
    
    Target window: t = 8.16s to t = 9.56s (1.4 seconds duration).
    Returns metrics including sample count, cosine similarity, and boolean has_siren.
    """
    target = Path(wav_path)
    if not target.exists():
        raise FileNotFoundError(f"Audio WAV file does not exist: {target}")

    with wave.open(str(target), "rb") as wf:
        sample_rate = wf.getframerate()
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        n_frames = wf.getnframes()
        raw_bytes = wf.readframes(n_frames)

    dtype = np.int16 if sampwidth == 2 else np.int32
    audio_data = np.frombuffer(raw_bytes, dtype=dtype)
    if n_channels > 1:
        audio_data = audio_data.reshape(-1, n_channels)
        mono_signal = audio_data[:, 0].astype(np.float32) / (32768.0 if sampwidth == 2 else 2147483648.0)
    else:
        mono_signal = audio_data.astype(np.float32) / (32768.0 if sampwidth == 2 else 2147483648.0)

    # Window at 8.16s - 9.56s
    siren_dur = 1.4
    start_idx = int(8.16 * sample_rate)
    siren_samples = int(siren_dur * sample_rate)
    end_idx = start_idx + siren_samples

    if len(mono_signal) < end_idx:
        raise ValueError(f"Audio signal too short ({len(mono_signal)} samples) to inspect 8.16s window")

    segment = mono_signal[start_idx:end_idx]
    siren_template = synthesize_police_siren_signal(sample_rate, siren_dur)

    norm_seg = np.linalg.norm(segment)
    norm_sir = np.linalg.norm(siren_template)

    if norm_seg < 1e-9:
        cosine_sim = 0.0
    else:
        cosine_sim = float(np.dot(segment, siren_template) / (norm_seg * norm_sir))

    # Fast Fourier Transform energy in the FM siren modulation corridor [590 Hz, 1110 Hz]
    fft_spec = np.abs(np.fft.rfft(segment))
    freqs = np.fft.rfftfreq(len(segment), 1.0 / sample_rate)
    siren_band_mask = (freqs >= 580) & (freqs <= 1120)
    siren_band_energy = float(np.sum(fft_spec[siren_band_mask] ** 2))
    total_energy = float(np.sum(fft_spec ** 2)) + 1e-12
    siren_band_ratio = siren_band_energy / total_energy

    # If siren is present, cosine similarity is typically > 0.35, up to 0.99
    # In clean audio without siren, cosine similarity is < 0.05
    has_siren = (cosine_sim > 0.15)

    return {
        "sample_rate": sample_rate,
        "n_frames": n_frames,
        "duration": n_frames / sample_rate,
        "cosine_similarity": cosine_sim,
        "siren_band_ratio": siren_band_ratio,
        "has_siren": has_siren,
    }


def parse_mp4_box_headers(mp4_path: Path | str) -> list[tuple[str, int, int]]:
    """Inspect top-level MP4 atom (box) headers without external libraries.
    
    Returns list of tuples: (box_type, box_size, file_offset)
    """
    target = Path(mp4_path)
    if not target.exists():
        raise FileNotFoundError(f"MP4 file does not exist: {target}")

    boxes = []
    file_size = target.stat().st_size
    with open(target, "rb") as f:
        offset = 0
        while offset < file_size:
            header = f.read(8)
            if len(header) < 8:
                break
            size = int.from_bytes(header[:4], "big")
            box_type = header[4:8].decode("latin1", errors="replace")

            if size == 1:
                # 64-bit extended size
                ext_size = f.read(8)
                size = int.from_bytes(ext_size, "big")
                f.seek(offset + size)
            elif size == 0:
                # Extends to end of file
                boxes.append((box_type, file_size - offset, offset))
                break
            else:
                f.seek(offset + size)

            boxes.append((box_type, size, offset))
            offset += size

    return boxes


def scan_source_files_for_banned_strings(search_dir: Path | str) -> list[dict]:
    """Scan all Python and script files in a directory for forbidden slate/counter strings."""
    root = Path(search_dir)
    violations = []
    if not root.exists():
        return violations

    for p in root.rglob("*"):
        if p.is_file() and p.suffix in [".py", ".js", ".json", ".txt"]:
            # Skip test files and caches
            if "tests" in p.parts or "__pycache__" in p.parts:
                continue
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                for banned in BANNED_LEGACY_STRINGS:
                    if banned in content:
                        lines = content.splitlines()
                        for line_idx, line in enumerate(lines, 1):
                            if banned in line:
                                violations.append({
                                    "file": str(p),
                                    "line": line_idx,
                                    "banned": banned,
                                    "text": line.strip(),
                                })
            except Exception as e:
                pass

    return violations


def resolve_audio_file() -> Path:
    """Find the production audio_clean_30s.wav, or fall back to explorer reference audio."""
    prod_path = TARGET_REPO / "audio_clean_30s.wav"
    if prod_path.exists():
        return prod_path
    if EXPLORER_AUDIO.exists():
        return EXPLORER_AUDIO
    raise FileNotFoundError(
        f"Neither production audio ({prod_path}) nor explorer reference audio ({EXPLORER_AUDIO}) found."
    )


def resolve_video_file() -> Path | None:
    """Find the production output/audiobook_summary_30s.mp4 if rendered."""
    prod_path = TARGET_REPO / "output" / "audiobook_summary_30s.mp4"
    if prod_path.exists():
        return prod_path
    alt_path = TARGET_REPO / "audiobook_summary_30s.mp4"
    if alt_path.exists():
        return alt_path
    return None
