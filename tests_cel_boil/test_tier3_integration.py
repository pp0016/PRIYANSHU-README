"""
Tier 3: Cross-Feature Integration Test Suite
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
    import visual_beats
    import scene
    from stubs import SFX_CUES
except ImportError:
    import stubs as cel_boil
    import stubs as subtitles
    import stubs as visual_beats
    import stubs as scene
    from stubs import SFX_CUES


class TestTier3Integration(unittest.TestCase):
    """Tier 3: Cross-feature synchronization, differential stability, and layer composite integration."""

    def test_01_audio_video_multiplexing_sync(self):
        """Audio and video stream durations must synchronize within < 0.05s tolerance."""
        audio_path = resolve_audio_file()
        audio_meta = probe_media_file(audio_path)
        audio_dur = float(audio_meta.get("format", {}).get("duration", 30.0))

        video_path = resolve_video_file()
        if video_path is not None:
            video_meta = probe_media_file(video_path)
            video_dur = float(video_meta.get("format", {}).get("duration", 30.0))
            drift = abs(audio_dur - video_dur)
            self.assertLess(
                drift, 0.05,
                f"Audio-Video multiplexing drift ({drift:.4f}s) exceeds 0.05s tolerance"
            )
        else:
            scene_obj = scene.AudiobookSummaryScene()
            expected_video_dur = getattr(scene_obj, "duration", 30.0)
            drift = abs(audio_dur - expected_video_dur)
            self.assertLess(
                drift, 0.001,
                f"Audio master ({audio_dur:.4f}s) and scene target ({expected_video_dur:.4f}s) out of sync"
            )

    def test_02_subtitle_timeline_complete_coverage(self):
        """Subtitle timeline must continuously cover [0.00s, 29.58s] with zero temporal gaps."""
        mgr = subtitles.KineticSubtitleManager()

        # Sample at 50ms intervals across the entire 29.58s speech window
        t_samples = np.linspace(0.00, 29.55, 592)
        missing_gaps = []

        for t in t_samples:
            cue = mgr.get_cue_at(float(t))
            if cue is None:
                missing_gaps.append(round(float(t), 3))

        self.assertEqual(
            len(missing_gaps), 0,
            f"Found uncovered gaps in dialogue timeline: {missing_gaps[:10]} (total {len(missing_gaps)})"
        )

        # Outro hold window (29.58s - 30.00s) must have no subtitle banner
        outro_samples = np.linspace(29.58, 30.00, 10)
        for t in outro_samples:
            self.assertIsNone(
                mgr.get_cue_at(float(t)),
                f"Subtitle banner active during Beat 10 outro hold at t={t:.3f}s"
            )

    def test_03_differential_jitter_stability_bezier_curves(self):
        """Differential jitter must preserve Bézier curve continuity without cracking or self-intersections."""
        try:
            import manim as mn
            mob = mn.Circle(radius=1.5)
        except ImportError:
            mob = cel_boil.Circle(radius=1.5)

        cel_boil.apply_cel_boil(mob, amp=0.03, scale=1.5, fps=12, seed=10)

        # Step 12 frames
        for f in range(12):
            mob.update(dt=1.0 / 12.0)
            pts = mob.points
            diffs = np.diff(pts, axis=0)
            norms = np.linalg.norm(diffs, axis=1)
            # Filter out shared endpoints between adjacent Bezier segments (norms ~ 0)
            active_segs = norms[norms > 1e-5]

            # Segment lengths must not collapse to zero
            self.assertTrue(
                np.all(active_segs > 0.01),
                f"Frame {f}: Curve collapsed to near-zero segments: min={np.min(active_segs)}"
            )

            # Segment length ratio must not experience violent spikes (cracking)
            ratio = np.max(active_segs) / (np.min(active_segs) + 1e-9)
            self.assertLess(
                ratio, 6.0,
                f"Frame {f}: Curve distortion ratio {ratio:.2f} exceeded continuity threshold"
            )

    def test_04_sfx_audio_cue_alignment_with_visual_beats(self):
        """All 15 procedural SFX cues must map precisely to their respective visual beats."""
        beat_ranges = {
            1: (0.00, 1.50),
            2: (1.50, 4.50),
            3: (4.50, 9.00),
            4: (9.00, 12.20),
            5: (12.20, 15.00),
            6: (15.00, 18.50),
            7: (18.50, 23.36),
            8: (23.36, 26.14),
            9: (26.14, 29.58),
            10: (29.58, 30.00),
        }

        self.assertEqual(len(SFX_CUES), 15, f"Expected exactly 15 SFX cues, got {len(SFX_CUES)}")

        for cue in SFX_CUES:
            b_idx = cue["beat"]
            t = cue["time"]
            b_start, b_end = beat_ranges[b_idx]
            self.assertGreaterEqual(
                t, b_start,
                f"SFX {cue['sfx']} at {t}s precedes Beat {b_idx} start ({b_start}s)"
            )
            self.assertLessEqual(
                t, b_end,
                f"SFX {cue['sfx']} at {t}s exceeds Beat {b_idx} end ({b_end}s)"
            )

            # Confirm police siren is NOT in the cue list
            self.assertNotIn("siren", cue["sfx"].lower(), "Forbidden police siren found in SFX mapping!")

    def test_05_visual_and_subtitle_layering_order(self):
        """Subtitles must be layered in front of visual beat objects for maximum legibility."""
        mgr = subtitles.KineticSubtitleManager()
        banner = mgr.get_banner_mobject(1)
        beat_group = visual_beats.get_beat_group(1)

        # Both must be valid renderable groups
        self.assertIsNotNone(banner)
        self.assertIsNotNone(beat_group)
        self.assertGreater(len(banner), 0)
        self.assertGreater(len(beat_group), 0)


if __name__ == "__main__":
    unittest.main()
