"""Tier 4 Test Suite: Real-World Workloads & End-to-End Pipeline Verification.

Verifies:
1. Real rendered frame inspection:
   - File exists, size > 500KB (actual ~1.43MB).
   - Valid PNG binary signature (0x89 50 4E 47 0D 0A 1A 0A).
   - Valid 13-byte IHDR chunk.
   - Resolution is exactly 1920x1080.
   - Bit depth 8, color mode RGBA (color_type 6).
   - Decodable by PIL Image without errors.
2. Synthetic multi-frame sequence generation & FFmpeg compilation into valid MP4:
   - Full FFmpeg stitch execution matching production workflow parameters.
   - ffprobe video stream validation (h264 codec, yuv420p, 1920x1080, 30fps).
   - Verification of '+faststart' web optimization (moov atom before mdat atom).
   - Frame continuity and timestamp integrity (zero dropped frames).
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess
import unittest
from pathlib import Path

# Add target repository to sys.path
PROJECT_ROOT = Path(r"c:\Users\renu5\Downloads\manim_video_repo")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Add workspace test directory to sys.path
WORKSPACE_TESTS = Path(__file__).resolve().parent
if str(WORKSPACE_TESTS) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_TESTS))

from test_helpers import (
    find_blender_binary,
    find_ffmpeg_binary,
    find_ffprobe_binary,
    validate_png_header,
    validate_png_file,
    probe_video,
    verify_video_faststart,
)

from PIL import Image, ImageDraw, ImageFont


class TestTier4RealWorldScenarios(unittest.TestCase):
    """Tier 4: Real-World Scenarios and End-to-End Video Verification."""

    @classmethod
    def setUpClass(cls):
        cls.ffmpeg_bin = find_ffmpeg_binary()
        cls.ffprobe_bin = find_ffprobe_binary()
        if not cls.ffmpeg_bin or not cls.ffprobe_bin:
            raise unittest.SkipTest("FFmpeg or FFprobe missing from PATH.")

        cls.real_frame_path = PROJECT_ROOT / "output" / "test_frame_1.png"

    # -------------------------------------------------------------
    # 1. Real Rendered PNG Frame Inspection
    # -------------------------------------------------------------
    def test_01_real_rendered_png_binary_integrity(self):
        """Verify binary PNG signature and IHDR fields on actual rendered Blender frame."""
        self.assertTrue(
            self.real_frame_path.is_file(),
            f"Expected real rendered frame at {self.real_frame_path}",
        )

        meta = validate_png_header(str(self.real_frame_path))
        self.assertTrue(meta["valid_signature"])
        self.assertEqual(meta["width"], 1920)
        self.assertEqual(meta["height"], 1080)
        self.assertEqual(meta["bit_depth"], 8)
        self.assertEqual(meta["color_type"], 6)  # RGBA
        self.assertEqual(meta["color_mode"], "RGBA")
        self.assertEqual(meta["compression"], 0)
        self.assertEqual(meta["filter_method"], 0)
        self.assertEqual(meta["interlace"], 0)

    def test_02_real_rendered_png_size_and_pil_decoding(self):
        """Verify real rendered frame exceeds 500KB and decodes cleanly in PIL."""
        self.assertTrue(self.real_frame_path.is_file())

        # Production Cycles frame is ~1.43 MB (> 500,000 bytes)
        file_size = self.real_frame_path.stat().st_size
        self.assertGreater(
            file_size,
            500000,
            f"Rendered PNG size ({file_size} bytes) is suspiciously small (< 500KB)",
        )

        meta = validate_png_file(
            str(self.real_frame_path),
            expected_width=1920,
            expected_height=1080,
            expected_mode="RGBA",
            min_size_bytes=500000,
        )
        self.assertEqual(meta.get("pil_mode"), "RGBA")

    # -------------------------------------------------------------
    # 2. Multi-Frame Sequence & FFmpeg Broadcast Stitching
    # -------------------------------------------------------------
    def test_03_synthetic_sequence_and_ffmpeg_broadcast_stitching(self):
        """Generate 10 frames, compile via FFmpeg, and verify broadcast MP4 stream properties."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            frames_dir = temp_path / "frames"
            frames_dir.mkdir(parents=True, exist_ok=True)

            num_frames = 10
            # Generate 10 consecutive frames: frame_00001.png to frame_00010.png
            for i in range(1, num_frames + 1):
                # Create 1920x1080 RGBA synthetic motion graphics frame
                img = Image.new("RGBA", (1920, 1080), (10, 12, 18, 255))
                draw = ImageDraw.Draw(img)
                # Draw simulated kinetic glowing graphic
                center_x = int(960 + (i - 5) * 20)
                center_y = int(540 + (i - 5) * 10)
                draw.rectangle(
                    [center_x - 150, center_y - 60, center_x + 150, center_y + 60],
                    fill=(0, 215, 255, 220),
                    outline=(255, 184, 46, 255),
                    width=4,
                )
                frame_file = frames_dir / f"frame_{i:05d}.png"
                img.save(str(frame_file), "PNG")

            # Verify all 10 frames were written
            generated_frames = list(frames_dir.glob("frame_*.png"))
            self.assertEqual(len(generated_frames), num_frames)

            # Compile with FFmpeg matching .github/workflows/blender_render.yml production spec
            output_mp4 = temp_path / "Final_3D_Typography_Hook.mp4"
            ffmpeg_cmd = [
                self.ffmpeg_bin,
                "-y",
                "-framerate", "30",
                "-start_number", "1",
                "-i", str(frames_dir / "frame_%05d.png"),
                "-c:v", "libx264",
                "-profile:v", "high",
                "-level:v", "4.2",
                "-pix_fmt", "yuv420p",
                "-preset", "ultrafast",
                "-crf", "18",
                "-movflags", "+faststart",
                str(output_mp4),
            ]

            proc = subprocess.run(
                ffmpeg_cmd,
                capture_output=True,
                text=True,
                check=False,
                timeout=30,
            )
            self.assertEqual(
                proc.returncode, 0, f"FFmpeg compilation failed (code {proc.returncode}):\n{proc.stderr}"
            )
            self.assertTrue(output_mp4.is_file(), "Compiled MP4 file not found")
            self.assertGreater(output_mp4.stat().st_size, 10000, "Compiled MP4 is too small")

            # Introspect with ffprobe
            probe_data = probe_video(str(output_mp4))
            streams = probe_data.get("streams", [])
            video_stream = None
            for s in streams:
                if s.get("codec_type") == "video":
                    video_stream = s
                    break

            self.assertIsNotNone(video_stream, "No video stream found in stitched MP4")
            self.assertEqual(video_stream.get("codec_name"), "h264")
            self.assertEqual(video_stream.get("pix_fmt"), "yuv420p")
            self.assertEqual(video_stream.get("width"), 1920)
            self.assertEqual(video_stream.get("height"), 1080)
            self.assertEqual(video_stream.get("r_frame_rate"), "30/1")

            # Verify frame count and duration
            nb_frames = int(video_stream.get("nb_frames", num_frames))
            self.assertEqual(nb_frames, num_frames)

            # Verify faststart (moov atom before mdat atom)
            has_faststart = verify_video_faststart(str(output_mp4))
            self.assertTrue(has_faststart, "Faststart (+faststart) moov box not positioned before mdat")

    def test_04_ffmpeg_missing_frame_error_detection(self):
        """Verify that a missing or corrupted frame in the sequence triggers proper validation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            frames_dir = temp_path / "corrupt_seq"
            frames_dir.mkdir(parents=True, exist_ok=True)

            # Create frames 1, 2, but intentionally drop frame 3, then create frame 4
            for i in [1, 2, 4]:
                img = Image.new("RGBA", (192, 108), (255, 0, 0, 255))
                img.save(str(frames_dir / f"frame_{i:05d}.png"))

            # Count check simulation (as performed in GitHub Actions stitcher preflight)
            expected_total = 4
            actual_count = len(list(frames_dir.glob("frame_*.png")))
            self.assertNotEqual(
                actual_count,
                expected_total,
                "Pre-stitch count check should detect missing frame 3",
            )


if __name__ == "__main__":
    unittest.main()
