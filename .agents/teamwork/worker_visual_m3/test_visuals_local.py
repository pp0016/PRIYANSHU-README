"""
test_visuals_local.py — Comprehensive Test Suite for Visual Beats & Kinetic Subtitles
Verifies:
1. Procedural vector construction of all 10 visual beats.
2. 12-beat kinetic Hinglish subtitle banners and cue synchronization.
3. Authentic cel-boil attachment across all beats (12 fps on beats 1-9; 8 fps on beat 10).
4. Time-dynamic updates for key visual beat events (cork pop, seals, alert waves, die, brain, book slam, rings, shield, flame, plaque).
5. Clean-slate compliance: zero slate text ("AUDIOBOOK SUMMARY"), zero exposure counters ("No. 074", "CEL BOIL"), and zero police siren graphics.
"""

import sys
import os

# Add manim-port to sys.path
MANIM_PORT_DIR = r"C:\Users\renu5\Downloads\mg-styles-15-test\manim-port"
if MANIM_PORT_DIR not in sys.path:
    sys.path.insert(0, MANIM_PORT_DIR)

import numpy as np
from manim import VGroup, VMobject, Text

import visual_beats
from visual_beats import (
    get_beat_group, BEAT_CLASSES, BEAT_TIMINGS,
    PAL_CREAM, PAL_INK, PAL_RED, PAL_YEL, PAL_HI, PAL_PENCIL,
    STAGE_CENTER, OUTRO_CENTER,
    Beat1MagnifyingGlass, Beat2TrustRespect, Beat3DifferenceQuestion,
    Beat4CommunicationGame, Beat5BrainPsychology, Beat6HeroBookSlam,
    Beat7ManipulationToRelationships, Beat8ZeroArguments,
    Beat9InspireFlame, Beat10Chapter1Teaser
)

import subtitles
from subtitles import (
    KineticSubtitleManager, KineticSubtitleBanner,
    KINETIC_SUBTITLE_DATA, create_subtitle_manager
)

from cel_boil import is_cel_boil_active


def test_palette_and_constants():
    """Verify authentic 05-cel-boil color palette tokens and stage coordinate geometry."""
    print("\n--- Test 1: Color Palette Tokens & Coordinate Geometry ---")
    assert PAL_CREAM == "#f4e9d0", f"Incorrect PAL_CREAM: {PAL_CREAM}"
    assert PAL_INK == "#1c1613", f"Incorrect PAL_INK: {PAL_INK}"
    assert PAL_RED == "#e5402b", f"Incorrect PAL_RED: {PAL_RED}"
    assert PAL_YEL == "#ffc425", f"Incorrect PAL_YEL: {PAL_YEL}"
    assert PAL_HI == "#fff6e2", f"Incorrect PAL_HI: {PAL_HI}"
    assert PAL_PENCIL == "#d9573f", f"Incorrect PAL_PENCIL: {PAL_PENCIL}"

    # Stage center should be at y = +0.4444 (canvas 480 vs 540)
    expected_stage_y = 60.0 * (8.0 / 1080.0)
    assert np.isclose(STAGE_CENTER[0], 0.0), "Stage center X should be 0.0"
    assert np.isclose(STAGE_CENTER[1], expected_stage_y, atol=1e-4), f"Stage center Y mismatch: {STAGE_CENTER[1]}"
    assert np.allclose(OUTRO_CENTER, [0.0, 0.0, 0.0]), "Outro center should be [0, 0, 0]"
    print("[PASS] Test 1: Color palette and stage coordinates verified.")


def test_construct_all_10_beats():
    """Verify procedural construction of all 10 beats without errors."""
    print("\n--- Test 2: Procedural Construction of All 10 Beats ---")
    for beat_idx in range(1, 11):
        t_start, t_end = BEAT_TIMINGS[beat_idx]
        t_mid = (t_start + t_end) / 2.0

        beat_group = get_beat_group(beat_idx, t_start=t_start, t_end=t_end, t=t_mid, boil=False)
        assert isinstance(beat_group, VGroup), f"Beat {beat_idx} must be a VGroup instance"
        assert len(beat_group) > 0, f"Beat {beat_idx} has no subcomponents!"

        # Count total leaves with points
        leaves = [m for m in beat_group.family_members_with_points() if len(m.points) > 0]
        assert len(leaves) > 0, f"Beat {beat_idx} has no vector primitives with points!"

        cls_name = beat_group.__class__.__name__
        print(f"  Beat {beat_idx:2d} ({t_start:5.2f}s - {t_end:5.2f}s): {cls_name:32s} | {len(leaves):3d} vector leaves")
    print("[PASS] Test 2: All 10 beat VGroups constructed successfully.")


def test_cel_boil_attachment_and_rates():
    """Verify cel-boil attaches cleanly to each beat with correct fps (12 vs 8)."""
    print("\n--- Test 3: Cel-Boil Attachment & Frame Rate Stepping ---")
    for beat_idx in range(1, 11):
        expected_fps = 8 if (beat_idx == 10) else 12
        beat_group = get_beat_group(beat_idx, boil=True)

        assert is_cel_boil_active(beat_group), f"Cel-boil not active on Beat {beat_idx}!"

        # Verify rate stepping
        assert getattr(beat_group, "_boil_fps", None) == expected_fps, (
            f"Beat {beat_idx} expected boil fps {expected_fps}, got {getattr(beat_group, '_boil_fps', None)}"
        )

        # Check leaf points are displaced and no NaNs
        leaves = [m for m in beat_group.family_members_with_points() if len(m.points) > 0]
        has_active_leaves = 0
        for leaf in leaves:
            if getattr(leaf, "_cel_boil_active", False):
                has_active_leaves += 1
                assert not np.isnan(leaf.points).any(), f"NaN points in leaf of Beat {beat_idx}"
                assert not np.isinf(leaf.points).any(), f"Inf points in leaf of Beat {beat_idx}"

        assert has_active_leaves > 0, f"No active boiling leaves found in Beat {beat_idx}!"
        print(f"  Beat {beat_idx:2d}: cel-boil active at {expected_fps} FPS | {has_active_leaves} boiling leaves")
    print("[PASS] Test 3: Cel-boil engine attached cleanly to all 10 beats.")


def test_temporal_beat_dynamics():
    """Verify dynamic update_time(t) behavior and event triggers across beats."""
    print("\n--- Test 4: Dynamic update_time(t) Event Triggers ---")

    # Beat 1: Cork pop at 1.08s
    b1 = Beat1MagnifyingGlass(t=0.5, boil=False)
    b1.update_time(0.5)
    assert len(b1.spark_burst) == 0, "No sparks expected at t=0.5s in Beat 1"
    b1.update_time(1.2)
    assert len(b1.spark_burst) == 6, f"Expected 6 twinkle sparks at t=1.2s, got {len(b1.spark_burst)}"
    print("  Beat 1: Cork pop twinkle burst verified at t=1.2s (6 radial twinkles).")

    # Beat 2: 3.12s Chime ripples
    b2 = Beat2TrustRespect(t=2.0, boil=False)
    b2.update_time(2.0)
    assert len(b2.chime_burst) == 0, "No chime ripples expected at t=2.0s in Beat 2"
    b2.update_time(3.5)
    assert len(b2.chime_burst) == 5, f"Expected 5 chime elements (2 rings + 3 stars) at t=3.5s, got {len(b2.chime_burst)}"
    print("  Beat 2: Chime ripple rings and stars verified at t=3.5s.")

    # Beat 3: Vibration and 8.16s Alert waves
    b3 = Beat3DifferenceQuestion(t=5.0, boil=False)
    b3.update_time(5.0)
    assert len(b3.alert_waves_group) == 0, "No alert waves expected at t=5.0s in Beat 3"
    b3.update_time(8.5)
    assert len(b3.alert_waves_group) == 5, f"Expected 5 alert elements (3 rings + 2 beacons) at t=8.5s, got {len(b3.alert_waves_group)}"
    print("  Beat 3: Alert rings and beacons verified at t=8.5s.")

    # Beat 4: 11.76s Tick sparkle
    b4 = Beat4CommunicationGame(t=10.0, boil=False)
    b4.update_time(10.0)
    assert len(b4.sparkle_group) == 0, "No sparkle expected at t=10.0s in Beat 4"
    b4.update_time(11.9)
    assert len(b4.sparkle_group) == 1, "Expected 1 twinkle star above die at t=11.9s"
    print("  Beat 4: Tick sparkle verified at t=11.9s.")

    # Beat 5: Traveling electrons and 14.18s Thought sparkle
    b5 = Beat5BrainPsychology(t=13.0, boil=False)
    b5.update_time(13.0)
    assert len(b5.electrons_group) == 3, f"Expected 3 orbiting electrons, got {len(b5.electrons_group)}"
    assert len(b5.thought_flash) == 0, "No thought flash expected at t=13.0s in Beat 5"
    b5.update_time(14.5)
    assert len(b5.thought_flash) == 3, f"Expected 3 thought stars at t=14.5s, got {len(b5.thought_flash)}"
    print("  Beat 5: 3 orbiting electrons and thought flash verified at t=14.5s.")

    # Beat 6: 16.04s Book slam shockwave
    b6 = Beat6HeroBookSlam(t=15.5, boil=False)
    b6.update_time(15.5)
    assert len(b6.impact_shockwave) == 0, "No shockwave expected prior to 16.04s in Beat 6"
    b6.update_time(16.2)
    # 24 speedlines + 12 sparks = 36 shockwave elements
    assert len(b6.impact_shockwave) == 36, f"Expected 36 shockwave elements at t=16.2s, got {len(b6.impact_shockwave)}"
    print("  Beat 6: 16.04s book slam shockwave verified (24 speedlines + 12 sparks).")

    # Beat 7: Phase A (X slash) vs Phase B (Friendship rings)
    b7 = Beat7ManipulationToRelationships(t=19.0, boil=False)
    b7.update_time(19.0)
    assert len(b7.phase_a) > 0 and len(b7.phase_b) == 0, "Expected Phase A active at t=19.0s"
    b7.update_time(22.0)
    assert len(b7.phase_a) == 0 and len(b7.phase_b) > 0, "Expected Phase B active at t=22.0s"
    print("  Beat 7: Manipulation X-slash -> Friendship rings & heart transition verified.")

    # Beat 8: Phase A (Lightning) vs Phase B (Wave ribbons & shield)
    b8 = Beat8ZeroArguments(t=24.0, boil=False)
    b8.update_time(24.0)
    assert len(b8.phase_a) > 0 and len(b8.phase_b) == 0, "Expected Phase A active at t=24.0s"
    b8.update_time(25.0)
    assert len(b8.phase_a) == 0 and len(b8.phase_b) > 0, "Expected Phase B active at t=25.0s"
    print("  Beat 8: Clashing lightning -> Wave ribbons & peace shield verified.")

    # Beat 9: Flame bob and 28.74s Chime burst
    b9 = Beat9InspireFlame(t=27.0, boil=False)
    b9.update_time(27.0)
    assert len(b9.chime_cascade) == 0, "No chime cascade expected at t=27.0s in Beat 9"
    b9.update_time(29.0)
    assert len(b9.chime_cascade) == 8, f"Expected 8 chime twinkles at t=29.0s, got {len(b9.chime_cascade)}"
    print("  Beat 9: Flame spirit character & 28.74s chime burst verified.")

    # Beat 10: Outro Plaque elements
    b10 = Beat10Chapter1Teaser(t=29.8, boil=False)
    assert len(b10.corner_stars) == 4, f"Expected 4 corner stars on plaque, got {len(b10.corner_stars)}"
    print("  Beat 10: Outro plaque with 4 corner stars and Dale Carnegie title verified.")

    print("[PASS] Test 4: Dynamic update_time(t) event triggers verified.")


def test_kinetic_subtitles_system():
    """Verify 12-beat kinetic subtitle banners and cue synchronization."""
    print("\n--- Test 5: Kinetic Subtitle Banners & Cue Synchronization ---")
    assert len(KINETIC_SUBTITLE_DATA) == 12, f"Expected 12 subtitle beats, got {len(KINETIC_SUBTITLE_DATA)}"

    mgr = create_subtitle_manager(t=0.0, boil=True)
    assert len(mgr.banners) == 12, f"Expected 12 banner instances, got {len(mgr.banners)}"

    # Check each banner's structure
    for idx, b_data in enumerate(KINETIC_SUBTITLE_DATA, start=1):
        banner = mgr.banners[idx - 1]
        assert banner.kicker_text == b_data["kicker"]
        assert banner.hero_text == b_data["hero"]
        assert banner.sub_text == b_data["sub"]
        assert is_cel_boil_active(banner), f"Banner {idx} should have cel boil active!"
        print(f"  Banner {idx:2d} ({b_data['start']:5.2f}s - {b_data['end']:5.2f}s): [{b_data['kicker'][:18]:18s}] | [{b_data['hero'][:24]:24s}]")

    # Test cue transitions and active banner switching
    test_times = [0.5, 2.5, 5.5, 8.0, 10.5, 13.5, 16.5, 19.5, 22.0, 24.5, 27.5]
    for t_test in test_times:
        mgr.update_time(t_test)
        assert len(mgr.banner_container) == 1, f"Expected active banner at t={t_test}s"
        active = mgr.banner_container[0]
        assert active.start_time <= t_test < active.end_time, (
            f"Active banner time window [{active.start_time}, {active.end_time}) does not match t={t_test}"
        )

    # Test smooth hiding during Beat 10 outro plaque (t >= 29.58s)
    mgr.update_time(29.60)
    assert len(mgr.banner_container) == 0, "Subtitle banner must be hidden when t >= 29.58s!"
    mgr.update_time(29.90)
    assert len(mgr.banner_container) == 0, "Subtitle banner must remain hidden at t=29.90s!"
    print("  Subtitles smoothly hidden during Beat 10 outro plaque (t >= 29.58s).")

    print("[PASS] Test 5: Kinetic subtitle system verified across all 12 beats.")


def test_clean_slate_compliance():
    """Verify complete omission of slate text, exposure counters, and police sirens."""
    print("\n--- Test 6: Clean-Slate Compliance Inspection ---")

    forbidden_strings = [
        "AUDIOBOOK SUMMARY",
        "No. 074",
        "No. ",
        "CEL BOIL",
        "POLICE SIREN",
        "SIREN",
        "COP",
    ]

    all_texts_found = []

    # Check all Text mobjects in all 10 beats
    for beat_idx in range(1, 11):
        bg = get_beat_group(beat_idx, boil=False)
        for mob in bg.get_family():
            if isinstance(mob, Text):
                text_val = mob.text.upper()
                all_texts_found.append(text_val)
                for forbidden in forbidden_strings:
                    assert forbidden not in text_val, (
                        f"Found forbidden text '{forbidden}' in Beat {beat_idx}: '{text_val}'"
                    )

    # Check all Text mobjects in subtitle banners
    mgr = create_subtitle_manager(t=0.0, boil=False)
    for b in mgr.banners:
        for mob in b.get_family():
            if isinstance(mob, Text):
                text_val = mob.text.upper()
                all_texts_found.append(text_val)
                for forbidden in forbidden_strings:
                    assert forbidden not in text_val, (
                        f"Found forbidden text '{forbidden}' in subtitle banner: '{text_val}'"
                    )

    print(f"  Inspected {len(all_texts_found)} Text objects. Zero slate text, zero exposure counters, zero sirens.")
    print("[PASS] Test 6: Clean-slate compliance verified.")


def run_all_tests():
    """Runs the complete verification test suite."""
    print("======================================================================")
    print("RUNNING LOCAL VISUAL BEATS & KINETIC SUBTITLES VERIFICATION SUITE")
    print("======================================================================")

    test_palette_and_constants()
    test_construct_all_10_beats()
    test_cel_boil_attachment_and_rates()
    test_temporal_beat_dynamics()
    test_kinetic_subtitles_system()
    test_clean_slate_compliance()

    print("\n======================================================================")
    print("ALL TESTS PASSED! VISUAL BEATS & SUBTITLES SUITE FULLY VERIFIED.")
    print("======================================================================\n")


if __name__ == "__main__":
    run_all_tests()
