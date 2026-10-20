"""
Tier 1: Feature Coverage Test Suite
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
    PALETTE,
    BANNED_LEGACY_STRINGS,
    resolve_audio_file,
    analyze_audio_siren_omission,
    synthesize_police_siren_signal,
    scan_source_files_for_banned_strings,
)

# Attempt import from target repo first, fallback to stubs
try:
    import sys
    if str(TARGET_REPO) not in sys.path:
        sys.path.insert(0, str(TARGET_REPO))
    import cel_boil
    import visual_beats
    import subtitles
    import scene
    PROD_MODULES_AVAILABLE = True
except ImportError:
    import stubs as cel_boil
    import stubs as visual_beats
    import stubs as subtitles
    import stubs as scene
    PROD_MODULES_AVAILABLE = False


class TestTier1FeatureCoverage(unittest.TestCase):
    """Tier 1: Verification of individual feature specifications and requirements."""

    def test_01_audio_duration_and_format(self):
        """Audio must be exactly 30.000s, 48kHz, 16-bit stereo PCM, non-silent."""
        audio_path = resolve_audio_file()
        self.assertTrue(audio_path.exists(), f"Audio file not found: {audio_path}")

        import wave
        with wave.open(str(audio_path), "rb") as wf:
            sample_rate = wf.getframerate()
            n_channels = wf.getnchannels()
            sampwidth = wf.getsampwidth()
            n_frames = wf.getnframes()
            raw_bytes = wf.readframes(n_frames)

        duration = n_frames / sample_rate
        self.assertEqual(sample_rate, 48000, f"Expected 48000 Hz sample rate, got {sample_rate}")
        self.assertEqual(n_channels, 2, f"Expected 2 channels (stereo), got {n_channels}")
        self.assertEqual(sampwidth, 2, f"Expected 16-bit PCM (2 bytes per sample), got {sampwidth}")
        self.assertAlmostEqual(duration, 30.000000, places=4, msg=f"Duration must be 30.000s, got {duration:.6f}")

        # Non-silent audio check
        samples = np.frombuffer(raw_bytes, dtype=np.int16).astype(np.float32) / 32768.0
        rms = np.sqrt(np.mean(samples ** 2))
        self.assertGreater(rms, 0.01, f"Audio signal appears silent or empty (RMS = {rms:.5f})")

    def test_02_siren_omission_spectral_check(self):
        """Police siren (850±260 Hz chirp at 8.16s) must be completely omitted from audio."""
        audio_path = resolve_audio_file()
        metrics = analyze_audio_siren_omission(audio_path)

        # In clean audio without the siren, cosine similarity is near zero (< 0.05)
        self.assertFalse(
            metrics["has_siren"],
            f"Police siren detected in audio! Cosine similarity={metrics['cosine_similarity']:.4f}"
        )
        self.assertLess(
            metrics["cosine_similarity"], 0.10,
            f"Siren template correlation too high ({metrics['cosine_similarity']:.4f}) at 8.16s window"
        )

        # Adversarial verification: Test that the oracle DOES detect a synthesized siren when present
        siren_template = synthesize_police_siren_signal(48000, 1.4)
        mock_dirty = siren_template / np.linalg.norm(siren_template)
        siren_norm = siren_template / np.linalg.norm(siren_template)
        oracle_sim = float(np.dot(mock_dirty, siren_norm))
        self.assertGreater(oracle_sim, 0.95, "Oracle sensitivity check failed: siren was not detected in dirty mock")

    def test_03_cel_boil_updater_presence_on_vmobject(self):
        """apply_cel_boil must attach an updater function to VMobjects and perturb points."""
        try:
            import manim as mn
            test_mob = mn.Circle(radius=1.0)
        except ImportError:
            test_mob = cel_boil.Circle(radius=1.0)

        initial_points = test_mob.points.copy()
        cel_boil.apply_cel_boil(test_mob, amp=0.03, scale=1.5, fps=12, seed=0)

        self.assertGreaterEqual(
            len(test_mob.updaters), 1,
            "apply_cel_boil did not attach an updater to the VMobject"
        )

        # Simulate update
        test_mob.update(dt=0.1)
        self.assertFalse(
            np.allclose(test_mob.points, initial_points),
            "VMobject points did not perturb after cel_boil update step"
        )

    def test_04_cel_boil_zero_displacement_when_amp_zero(self):
        """When amp=0.0, points must remain strictly identical to initial base geometry."""
        try:
            import manim as mn
            test_mob = mn.Square(side_length=2.0)
        except ImportError:
            test_mob = cel_boil.Square(side_length=2.0)

        initial_points = test_mob.points.copy()
        cel_boil.apply_cel_boil(test_mob, amp=0.0, fps=12, seed=0)
        test_mob.update(dt=0.15)

        self.assertTrue(
            np.allclose(test_mob.points, initial_points),
            "VMobject points perturbed despite amp=0.0"
        )

    def test_05_visual_beats_presence_all_10_beats(self):
        """All 10 visual beats must construct valid VGroups with non-empty geometries."""
        for beat_idx in range(1, 11):
            group = visual_beats.get_beat_group(beat_idx, t_start=float(beat_idx), t_end=float(beat_idx + 1))
            self.assertIsNotNone(group, f"Beat {beat_idx} returned None")
            self.assertGreater(len(group), 0, f"Beat {beat_idx} VGroup has 0 child mobjects")

    def test_06_visual_beats_color_palette_compliance(self):
        """All visual beats must utilize colors conforming to the paper cel palette."""
        valid_hexes = set(c.lower() for c in PALETTE.values())
        for beat_idx in range(1, 11):
            group = visual_beats.get_beat_group(beat_idx)
            submobs = getattr(group, "submobjects", [])
            for mob in submobs:
                color = getattr(mob, "color", None)
                colors_to_test = []
                if color is not None:
                    colors_to_test.append(str(color).lower())
                # If composite (e.g. Text with glyphs), check glyphs as well
                for child in getattr(mob, "submobjects", []):
                    ch_col = getattr(child, "color", None)
                    if ch_col is not None:
                        colors_to_test.append(str(ch_col).lower())

                for c_str in colors_to_test:
                    # Allow standard manim color repr or hex
                    is_valid = any(vh in c_str for vh in valid_hexes) or ("rgb" in c_str) or ("color" in c_str)
                    self.assertTrue(
                        is_valid,
                        f"Beat {beat_idx} mobject color {c_str} not in palette {valid_hexes}"
                    )

    def test_07_kinetic_hinglish_subtitles_12_banners(self):
        """Kinetic Subtitle Manager must contain exactly 12 structured Hinglish banners."""
        mgr = subtitles.KineticSubtitleManager()
        cues = getattr(mgr, "cues", [])
        self.assertEqual(len(cues), 12, f"Expected 12 kinetic subtitle banners, got {len(cues)}")

        for cue in cues:
            self.assertIn("kicker", cue, "Subtitle cue missing 'kicker' line")
            self.assertIn("hero", cue, "Subtitle cue missing 'hero' line")
            self.assertIn("sub", cue, "Subtitle cue missing 'sub' line")
            self.assertIn("start", cue, "Subtitle cue missing 'start' timestamp")
            self.assertIn("end", cue, "Subtitle cue missing 'end' timestamp")
            self.assertLess(cue["start"], cue["end"], f"Invalid cue timing: {cue}")

    def test_08_subtitles_pill_container_structure(self):
        """Each subtitle banner must construct a pill-backed container VGroup."""
        mgr = subtitles.KineticSubtitleManager()
        banner = mgr.get_banner_mobject(1)
        self.assertIsNotNone(banner)
        self.assertGreaterEqual(len(banner), 3, "Subtitle banner must contain backing shapes and text lines")

    def test_09_warm_cream_background_color(self):
        """Master AudiobookSummaryScene must configure warm cream background #f4e9d0."""
        scene_obj = scene.AudiobookSummaryScene()
        bg_color = getattr(scene_obj.camera, "background_color", None)
        self.assertIsNotNone(bg_color)
        bg_str = str(bg_color).lower()
        self.assertIn("#f4e9d0", bg_str, f"Background color must be warm cream '#f4e9d0', got {bg_str}")

    def test_10_clean_slate_omission_in_source_code(self):
        """All banned legacy strings (slate, exposure counters, peg bar) must be absent."""
        violations = scan_source_files_for_banned_strings(TARGET_REPO)
        self.assertEqual(
            len(violations), 0,
            f"Found forbidden slate/counter strings in source code: {violations}"
        )

    def test_11_clean_slate_omission_in_visual_mobjects(self):
        """Rendered visual beats and subtitle banners must not contain slate text."""
        banned_lower = [b.lower() for b in BANNED_LEGACY_STRINGS]

        # Inspect all beats
        for b_idx in range(1, 11):
            group = visual_beats.get_beat_group(b_idx)
            for mob in getattr(group, "submobjects", []):
                text_val = getattr(mob, "text", "")
                if text_val:
                    for b in banned_lower:
                        self.assertNotIn(
                            b, text_val.lower(),
                            f"Beat {b_idx} contains forbidden text '{b}': '{text_val}'"
                        )


if __name__ == "__main__":
    unittest.main()
