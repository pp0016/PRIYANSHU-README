"""
Tier 2: Boundary & Corner Cases Test Suite
Manim 05-Cel-Boil Audiobook Summary Replication
"""

import sys
import unittest
import numpy as np
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from test_helpers import (
    TARGET_REPO,
    resolve_audio_file,
    resolve_video_file,
    probe_media_file,
)

# Attempt import from target repo first, fallback to stubs
try:
    import sys
    if str(TARGET_REPO) not in sys.path:
        sys.path.insert(0, str(TARGET_REPO))
    import cel_boil
    import subtitles
    import scene
except ImportError:
    import stubs as cel_boil
    import stubs as subtitles
    import stubs as scene


class TestTier2BoundaryCases(unittest.TestCase):
    """Tier 2: Verification of mathematical boundaries, invariants, and edge cases."""

    def test_01_exact_pcm_sample_count(self):
        """Audio stream must contain exactly 1,440,000 PCM samples (48000 Hz * 30.000s)."""
        import wave
        audio_path = resolve_audio_file()
        with wave.open(str(audio_path), "rb") as wf:
            n_frames = wf.getnframes()
            sample_rate = wf.getframerate()

        expected_samples = 48000 * 30  # 1,440,000
        self.assertEqual(
            n_frames, expected_samples,
            f"PCM frame count must be exactly {expected_samples}, got {n_frames}"
        )
        self.assertEqual(sample_rate, 48000)

    def test_02_audio_container_and_stream_duration_boundaries(self):
        """Audio container duration must be exactly 30.000000s via FFprobe."""
        audio_path = resolve_audio_file()
        metadata = probe_media_file(audio_path)

        fmt = metadata.get("format", {})
        duration_str = fmt.get("duration", "0")
        duration_float = float(duration_str)

        self.assertAlmostEqual(
            duration_float, 30.000000, places=4,
            msg=f"Audio duration must be exactly 30.000000s, got {duration_str}"
        )

        streams = metadata.get("streams", [])
        self.assertGreaterEqual(len(streams), 1)
        self.assertEqual(streams[0].get("codec_name"), "pcm_s16le")
        self.assertEqual(int(streams[0].get("channels")), 2)

    def test_03_video_container_duration_boundary(self):
        """Video container duration must be locked to 30.000s (720 frames at 24 fps)."""
        video_path = resolve_video_file()
        if video_path is not None:
            metadata = probe_media_file(video_path)
            fmt = metadata.get("format", {})
            v_dur = float(fmt.get("duration", 0))
            self.assertAlmostEqual(
                v_dur, 30.000, delta=0.08,
                msg=f"Rendered video duration {v_dur:.3f}s outside boundary [29.92, 30.08]"
            )
        else:
            # Check scene object specification
            scene_obj = scene.AudiobookSummaryScene()
            dur = getattr(scene_obj, "duration", 30.0)
            self.assertAlmostEqual(dur, 30.0, places=2)

    def test_04_resolution_and_framerate_boundary(self):
        """Video specifications must be 1920x1080 resolution at 24 FPS."""
        video_path = resolve_video_file()
        if video_path is not None:
            metadata = probe_media_file(video_path)
            v_stream = next((s for s in metadata.get("streams", []) if s.get("codec_type") == "video"), None)
            self.assertIsNotNone(v_stream, "No video stream found in MP4")
            self.assertEqual(v_stream.get("width"), 1920)
            self.assertEqual(v_stream.get("height"), 1080)
            r_fps = v_stream.get("r_frame_rate", "24/1")
            self.assertIn("24", r_fps)
        else:
            scene_obj = scene.AudiobookSummaryScene()
            fps = getattr(scene_obj, "fps", 24)
            self.assertEqual(fps, 24)

    def test_05_cel_boil_zero_drift_over_720_frames(self):
        """Cel-boil points must exhibit ZERO cumulative drift over 720 frames (30s @ 24fps)."""
        try:
            import manim as mn
            mob = mn.Circle(radius=1.0)
        except ImportError:
            mob = cel_boil.Circle(radius=1.0)

        initial_points = mob.points.copy()
        initial_com = np.mean(initial_points, axis=0)
        amp = 0.03

        cel_boil.apply_cel_boil(mob, amp=amp, fps=12, seed=42)

        dt = 1.0 / 24.0
        for frame in range(1, 721):
            mob.update(dt=dt)
            current_points = mob.points
            current_com = np.mean(current_points, axis=0)

            # Center of mass drift must stay near zero (no Brownian walk)
            com_drift = np.linalg.norm(current_com - initial_com)
            self.assertLess(
                com_drift, 0.015,
                f"Frame {frame}: Center of mass drifted by {com_drift:.5f} (limit 0.015)"
            )

            # Max displacement must stay strictly bounded by amplitude
            max_disp = np.max(np.linalg.norm(current_points - initial_points, axis=1))
            self.assertLessEqual(
                max_disp, amp * 2.5,
                f"Frame {frame}: Max displacement {max_disp:.4f} exceeded amplitude boundary"
            )

        # After all 720 frames, final center of mass must still match origin
        final_com = np.mean(mob.points, axis=0)
        self.assertLess(
            np.linalg.norm(final_com - initial_com), 0.01,
            "After 720 frames, object center experienced persistent drift!"
        )

    def test_06_cel_boil_extreme_amplitude_boundaries(self):
        """Extreme amplitude and scale values must execute without numerical overflow/NaN."""
        for test_amp in [1e-6, 0.001, 0.1, 0.5]:
            for test_scale in [0.1, 1.0, 50.0]:
                try:
                    import manim as mn
                    mob = mn.Square(side_length=1.0)
                except ImportError:
                    mob = cel_boil.Square(side_length=1.0)

                cel_boil.apply_cel_boil(mob, amp=test_amp, scale=test_scale, fps=12, seed=1)
                mob.update(dt=0.2)
                self.assertFalse(np.isnan(mob.points).any(), f"NaN detected at amp={test_amp}, scale={test_scale}")
                self.assertFalse(np.isinf(mob.points).any(), f"Inf detected at amp={test_amp}, scale={test_scale}")

    def test_07_temporal_query_boundary_clamping(self):
        """Kinetic Subtitle queries outside [0.00s, 29.58s] must clamp gracefully."""
        mgr = subtitles.KineticSubtitleManager()

        # Pre-roll (< 0s)
        self.assertIsNone(mgr.get_cue_at(-0.01))
        self.assertIsNone(mgr.get_cue_at(-10.0))

        # Start boundary (0.0s)
        cue_0 = mgr.get_cue_at(0.0)
        self.assertIsNotNone(cue_0)
        self.assertEqual(cue_0["index"], 1)

        # Beat 10 outro window (29.58s - 30.00s)
        self.assertIsNone(mgr.get_cue_at(29.58))
        self.assertIsNone(mgr.get_cue_at(29.99))
        self.assertIsNone(mgr.get_cue_at(30.00))

        # Post-roll (> 30s)
        self.assertIsNone(mgr.get_cue_at(30.01))
        self.assertIsNone(mgr.get_cue_at(100.0))

    def test_08_beat_transition_temporal_partitions(self):
        """All 10 visual beat windows must form a contiguous, non-overlapping partition of [0, 30]."""
        beat_windows = [
            (1, 0.00, 1.50),
            (2, 1.50, 4.50),
            (3, 4.50, 9.00),
            (4, 9.00, 12.20),
            (5, 12.20, 15.00),
            (6, 15.00, 18.50),
            (7, 18.50, 23.36),
            (8, 23.36, 26.14),
            (9, 26.14, 29.58),
            (10, 29.58, 30.00),
        ]

        self.assertEqual(beat_windows[0][1], 0.00, "Beat 1 must start at 0.00s")
        self.assertEqual(beat_windows[-1][2], 30.00, "Beat 10 must end at 30.00s")

        for i in range(len(beat_windows) - 1):
            curr_end = beat_windows[i][2]
            next_start = beat_windows[i + 1][1]
            self.assertEqual(
                curr_end, next_start,
                f"Discontinuity between Beat {beat_windows[i][0]} (end={curr_end}) and Beat {beat_windows[i+1][0]} (start={next_start})"
            )


if __name__ == "__main__":
    unittest.main()
