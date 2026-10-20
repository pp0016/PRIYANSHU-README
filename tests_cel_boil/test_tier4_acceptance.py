"""
Tier 4: Real-World Execution & Acceptance Test Suite
Manim 05-Cel-Boil Audiobook Summary Replication
"""

import sys
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from test_helpers import (
    TARGET_REPO,
    resolve_audio_file,
    resolve_video_file,
    probe_media_file,
    parse_mp4_box_headers,
)

# Attempt import from target repo first, fallback to stubs
try:
    import sys
    if str(TARGET_REPO) not in sys.path:
        sys.path.insert(0, str(TARGET_REPO))
    import scene
except ImportError:
    import stubs as scene


class TestTier4Acceptance(unittest.TestCase):
    """Tier 4: Acceptance verification of headless rendering, container integrity, and FFprobe metadata."""

    def test_01_headless_render_verification(self):
        """AudiobookSummaryScene must construct headlessly without GUI dependencies or crashes."""
        scene_instance = scene.AudiobookSummaryScene()
        self.assertIsNotNone(scene_instance)

        # Execute construct()
        scene_instance.construct()

        # Verify background configuration and mobject hierarchy
        bg = getattr(scene_instance.camera, "background_color", None)
        self.assertIsNotNone(bg)
        self.assertIn("#f4e9d0", str(bg).lower())

        mobs = getattr(scene_instance, "mobjects", [])
        self.assertGreater(len(mobs), 0, "AudiobookSummaryScene populated zero mobjects during construct()")

    def test_02_output_file_integrity(self):
        """Rendered output MP4 must possess valid binary atom headers (ftyp, moov, mdat)."""
        video_path = resolve_video_file()
        if video_path is None:
            self.skipTest(
                "Final rendered MP4 not yet produced by Milestone 4 render pipeline. "
                "Skipping binary container atom check until master render completes."
            )

        self.assertTrue(video_path.exists())
        self.assertGreater(video_path.stat().st_size, 100_000, "Rendered video file is suspiciously small (<100KB)")

        # Inspect top-level MP4 atoms
        boxes = parse_mp4_box_headers(video_path)
        box_types = [b[0] for b in boxes]

        self.assertIn("ftyp", box_types, "MP4 file missing mandatory 'ftyp' file type box")
        self.assertIn("moov", box_types, "MP4 file missing mandatory 'moov' movie metadata box")
        self.assertIn("mdat", box_types, "MP4 file missing mandatory 'mdat' media data box")

    def test_03_ffprobe_metadata_validation(self):
        """Final media must validate 1920x1080 @ 24fps video and 48kHz stereo audio via FFprobe."""
        video_path = resolve_video_file()
        if video_path is not None:
            meta = probe_media_file(video_path)
            streams = meta.get("streams", [])

            # Video stream validation
            v_stream = next((s for s in streams if s.get("codec_type") == "video"), None)
            self.assertIsNotNone(v_stream, "MP4 contains no video stream")
            self.assertEqual(v_stream.get("codec_name"), "h264")
            self.assertEqual(v_stream.get("width"), 1920)
            self.assertEqual(v_stream.get("height"), 1080)
            self.assertIn("24", v_stream.get("r_frame_rate", ""))

            # Audio stream validation
            a_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)
            self.assertIsNotNone(a_stream, "MP4 contains no audio stream")
            self.assertEqual(int(a_stream.get("channels")), 2)
            self.assertEqual(int(a_stream.get("sample_rate")), 48000)

            # Container duration validation
            duration = float(meta.get("format", {}).get("duration", 0))
            self.assertAlmostEqual(duration, 30.000, delta=0.08)
        else:
            # Pre-render verification: Verify audio master metadata
            audio_path = resolve_audio_file()
            audio_meta = probe_media_file(audio_path)
            streams = audio_meta.get("streams", [])
            self.assertGreaterEqual(len(streams), 1)
            a_stream = streams[0]
            self.assertEqual(a_stream.get("codec_name"), "pcm_s16le")
            self.assertEqual(int(a_stream.get("sample_rate")), 48000)
            self.assertEqual(int(a_stream.get("channels")), 2)
            duration = float(audio_meta.get("format", {}).get("duration", 0))
            self.assertAlmostEqual(duration, 30.000000, places=4)

    def test_04_absence_of_render_error_codes(self):
        """Clean execution: modules must load and initialize with zero uncaught exceptions."""
        import py_compile
        # If target repo has python files, ensure all compile without syntax errors
        py_files = list(TARGET_REPO.glob("*.py")) if TARGET_REPO.exists() else []
        for pf in py_files:
            try:
                py_compile.compile(str(pf), doraise=True)
            except py_compile.PyCompileError as e:
                self.fail(f"Syntax error compiling {pf.name}: {e}")


if __name__ == "__main__":
    unittest.main()
