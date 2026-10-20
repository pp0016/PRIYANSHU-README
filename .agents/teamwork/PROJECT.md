# Project: Manim 05-Cel-Boil Audiobook Summary Replication

## Architecture
- **Engine**: Python Manim Community Edition (v0.21.0) with custom VMobject point perturbation updaters.
- **Audio Pipeline**: Procedural DSP SFX generation via `mgaudio` and sample-accurate 30.000000s audio mix (TTS voiceover + 15 SFX with police siren removed).
- **Video Specifications**: 1920x1080 (16:9), 24 FPS master, exactly 30.000s (720 frames), background `#f4e9d0`.
- **Styling**: Warm cream paper texture, hand-drawn vector art, Simplex/Value noise vector cel-boil on twos (12 fps) and threes (8 fps), 12 kinetic Hinglish subtitle banners.
- **Clean Slate**: 100% removal of top-left slate ("AUDIOBOOK SUMMARY"), bottom-right exposure counters ("No. 074", "CEL BOIL"), and top peg bar holes.
- **Audio Sync**: Muxing master WAV with rendered MP4 via WinGet Gyan FFmpeg 8.0.1 (`-c:v copy -t 30.000000`).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Audio Master Pipeline | Trim TTS to 30.000s, generate 15 procedural SFX via `mgaudio`, remove police siren at 8.16s, mix into 30.000000s 48kHz stereo WAV | M1 | Survey (Explorer 2) |
| 2 | Cel-Boil Vector Engine | Manim VMobject vector perturbation updater with 2D/3D noise field, 12/8 fps stepping, differential jitter to prevent drift & Bézier cracking | M2 | Survey (Explorer 1 & 3) |
| 3 | Kinetic Hinglish Subtitle Engine | 12 structured 3-line kinetic banners (kicker, hero, sub) with pill backing, spring pop entrance, and living boil jitter synced to audio cues | M3 | Survey (Explorer 1) |
| 4 | 10-Beat Visual Timeline | Procedural Manim vector scenes for all 10 visual beats (Magnifying Glass, Trust/Respect Seals, Question Mark, Speech Balloons/Die, Brain, Book Slam, Slash/Friendship, Zero Arguments, Flame Spirit, Outro Plaque) | M3 | Survey (Explorer 1) |
| 5 | Clean Slate & Frame Styling | `#f4e9d0` background, triple frame border, paper flecks, zero slate text, zero exposure counters | M4 | Survey (Explorer 1 & 3) |
| 6 | Scene Assembly & 30.00s Render | Full `AudiobookSummaryScene(Scene)` rendering 720 frames (30.00s) and muxing clean audio with zero siren | M4 | Survey (Explorer 1, 2, 3) |
| 7 | Opaque-Box E2E Test Suite | 4-tier test suite verifying exact duration, siren absence, cel-boil updater presence, clean slate, and render execution | E2E | Survey (All) |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| E2E | E2E Test Track | Comprehensive test suite & runner verifying all requirements | Survey | IN_PROGRESS |
| M1 | Clean Audio Master Pipeline | `audio_pipeline.py` producing `audio_clean_30s.wav` (no siren, exact 30.000s) | Survey | PLANNED |
| M2 | Manim Cel-Boil Vector Engine | `cel_boil.py` custom Manim Mobject perturbation updaters | Survey | PLANNED |
| M3 | 10-Beat Visual Timeline & Subtitles | `visual_beats.py` (all 10 beats) and `subtitles.py` (kinetic Hinglish banners) | M2 | PLANNED |
| M4 | Scene Assembly & Master Render | `scene.py` and `render.py` assembling full 30.00s scene, clean slate, video-audio mux | M1, M2, M3 | PLANNED |
| M5 | E2E Validation & Verification Gate | Full execution against E2E test suite, Reviewers, Challengers, and Forensic Auditor | M4, E2E | PLANNED |

## Interface Contracts
### `audio_pipeline.py` ↔ `render.py`
- Output: `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\audio_clean_30s.wav`
- Format: 48,000 Hz, 16-bit stereo PCM, exactly 1,440,000 samples (30.000000s duration).
- Content: Trimmed TTS voiceover + 15 procedural SFX; police siren frequency sweep at 8.16s completely omitted.

### `cel_boil.py` ↔ `visual_beats.py` / `subtitles.py`
- Functions: `apply_cel_boil(mobject, amp=0.03, scale=1.5, fps=12, seed=0)`
- Behavior: Attaches an updater to any Manim `VMobject` that displaces points relative to base points or via differential jitter every `1/fps` seconds without modifying center of mass or causing curve cracking.

### `visual_beats.py` & `subtitles.py` ↔ `scene.py`
- Classes / Functions:
  - `get_beat_group(beat_index, t_start, t_end)` returning Manim `VGroup` of visual elements for each of the 10 beats.
  - `KineticSubtitleManager` providing updater-driven or timestamp-animated Hinglish subtitle banners across 0.00s - 29.58s.
  - All visual assets procedurally constructed with Manim shapes (`Circle`, `Polygon`, `CurvedArrow`, `Line`, `Text`, `MarkupText`, etc.).

### `scene.py` ↔ `render.py`
- Main Scene: `class AudiobookSummaryScene(Scene)`
- Command: `python render.py` or `manim -pqh scene.py AudiobookSummaryScene`
- Output: `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\output\audiobook_summary_30s.mp4` (precisely 30.00s, 1920x1080 @ 24fps, audio included).

## Code Layout
Directory: `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port`
- `audio_pipeline.py`: Audio trimming, procedural SFX synthesis, siren removal, and mixing.
- `cel_boil.py`: Manim cel-boil vector perturbation engine.
- `subtitles.py`: 12 kinetic Hinglish subtitle banners and cue sync manager.
- `visual_beats.py`: Modular classes/functions for Beats 1 through 10.
- `scene.py`: Master Manim `Scene` assembling visual beats, cel-boil updaters, and subtitle overlay.
- `render.py`: Rendering orchestrator and FFmpeg video-audio muxer.
- `tests/`: Automated test suite (`test_audio.py`, `test_cel_boil.py`, `test_beats.py`, `test_render.py`, `run_all_tests.py`).
