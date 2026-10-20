# Test Infrastructure: Manim 05-Cel-Boil Audiobook Summary Replication

## 1. Overview & Architectural Philosophy
The testing framework for the Manim 05-Cel-Boil Audiobook Summary Replication implements an **opaque-box 4-tier verification architecture**. Tests are strictly decoupled from implementation internals and independently evaluate interface contracts, mathematical invariants, spectral audio fingerprints, vector point stability, binary container signatures, and video metadata without facades, dummy mocks, or hardcoded results.

```
                                      [run_all_tests.py]
                                              │
              ┌───────────────────────┬───────┴───────┬───────────────────────┐
              ▼                       ▼               ▼                       ▼
      [Tier 1: Features]      [Tier 2: Boundary] [Tier 3: Integration]  [Tier 4: Acceptance]
      - Audio 30.0s / 48kHz   - Exact 1,440,000   - A/V Muxing Sync      - Headless Render
      - Siren Omission (FFT)    PCM Samples       - Subtitle Coverage    - MP4 Atom Integrity
      - Cel-Boil Updaters     - 30.000s Duration    [0.00s - 29.58s]       (ftyp, moov, mdat)
      - 10 Visual Beats       - 1920x1080 @ 24fps - Differential Jitter  - FFprobe Metadata
      - 12 Hinglish Subtitles - Zero Drift over     Bézier Continuity    - Zero Exit Errors
      - Warm Cream #f4e9d0      720 Frames        - 15 SFX Beat Mapping
      - Clean Slate Omission  - Temporal Clamping - Layering Hierarchy
```

---

## 2. Directory Layout & Module Inventory

The test suite is structured into modular tiers supported by low-level verification helpers and mathematical oracles:

```
c:\Users\renu5\Downloads\priyanshu readme\tests_cel_boil\
├── __init__.py                          # Package initializer
├── test_helpers.py                      # Discovery, FFprobe parser, FFT siren oracle, atom inspector
├── stubs.py                             # Contract stubs & reference specification implementations
├── test_tier1_feature_coverage.py       # Tier 1: 11 feature coverage tests
├── test_tier2_boundary_cases.py         # Tier 2: 8 boundary and corner case tests
├── test_tier3_integration.py           # Tier 3: 5 cross-feature integration tests
├── test_tier4_acceptance.py             # Tier 4: 4 real-world execution & acceptance tests
└── run_all_tests.py                     # Central test runner with ANSI table & JSON export
```

---

## 3. Tier-by-Tier Specification & Assertion Coverage

### Tier 1: Opaque-Box Feature Coverage (`test_tier1_feature_coverage.py`)
- **Audio Duration & Format (`test_01`)**: Validates that `audio_clean_30s.wav` is exactly 30.000s duration, 48,000 Hz sample rate, 2 channels (stereo), 16-bit PCM (`pcm_s16le`), with non-silent RMS signal ($> 0.01$).
- **Siren Omission Spectral Check (`test_02`)**: Analyzes the audio window $t \in [8.16\text{s}, 9.56\text{s}]$ using normalized cross-correlation against the reference 850±260 Hz police siren FM chirp. Confirms cosine similarity is $< 0.10$ (clean audio is $0.0027$) and verifies oracle sensitivity against an adversarial dirty signal ($r > 0.95$).
- **Cel-Boil Updater Presence (`test_03`)**: Verifies that calling `apply_cel_boil(vmob)` registers an updater function in `vmob.updaters` and perturbs points relative to cached base points on `.update(dt)`.
- **Cel-Boil Zero Displacement at Amp 0 (`test_04`)**: Evaluates `apply_cel_boil(vmob, amp=0.0)`, confirming points remain strictly identical to initial base geometry after update steps.
- **Visual Beats Presence (`test_05`)**: Evaluates `get_beat_group(beat_idx)` for all 10 visual beats ($1 \le b \le 10$), asserting each returns a non-empty `VGroup` with valid sub-mobjects.
- **Color Palette Compliance (`test_06`)**: Verifies that all sub-mobjects across all 10 beats utilize colors conforming strictly to the project cel palette (`PAL.cream` `#f4e9d0`, `PAL.ink` `#1c1613`, `PAL.red` `#e5402b`, `PAL.yel` `#ffc425`, `PAL.hi` `#fff6e2`, `PAL.pencil` `#d9573f`).
- **Kinetic Hinglish Subtitles Presence (`test_07`)**: Verifies `KineticSubtitleManager` contains exactly 12 structured kinetic banners with kicker, bold hero, and sub lines.
- **Pill Container Backing Structure (`test_08`)**: Confirms subtitle banners construct a 3-layer pill backing (drop shadow, body fill, inked contour) with spring pop entrance animation.
- **Warm Cream Background (`test_09`)**: Confirms `AudiobookSummaryScene` configures `camera.background_color = "#f4e9d0"`.
- **Clean Slate Source Code Omission (`test_10`)**: Recursively scans all project files in target repository using AST/text scanning to guarantee zero occurrences of banned legacy strings: `"SC. 05"`, `"AUDIOBOOK SUMMARY"`, `"No. 074"`, `"CEL BOIL ANIMATION"`, `"on 2s"`, `"drawPencil"`, `"peg_hole"`.
- **Clean Slate Mobject Inspection (`test_11`)**: Inspects all instantiated text mobjects in beats 1-10 to ensure no slate or exposure counter text is drawn.

### Tier 2: Boundary and Corner Cases (`test_tier2_boundary_cases.py`)
- **Exact PCM Sample Count (`test_01`)**: Enforces an exact sample count of $1,440,000$ audio samples ($48000 \times 30.000000$). Fails on $\pm 1$ sample jitter.
- **Audio Stream Duration Boundary (`test_02`)**: Evaluates FFprobe metadata, asserting format duration is exactly $30.000000$s and codec is `pcm_s16le`.
- **Video Container Duration Boundary (`test_03`)**: Asserts video container duration is locked to $30.000$s within $\pm 0.08$s boundary (720 frames at 24 fps).
- **Resolution and Framerate (`test_04`)**: Validates $1920 \times 1080$ resolution and exactly 24 FPS (`r_frame_rate == "24/1"`).
- **Zero Drift over 720 Frames (`test_05`)**: Simulates 720 frames (30 seconds @ 24 fps) of cel-boil updates. Mathematically proves:
  1. Center of mass drift $\|\text{CoM}(t) - \text{CoM}(0)\| < 0.015$ across all frames.
  2. Maximum displacement is bounded: $\max_i \|\mathbf{p}_i(t) - \mathbf{p}_i(0)\| \le 2.5 \times \text{amp}$.
  3. Final center of mass at frame 720 matches initial origin within $< 0.01$ (zero cumulative Brownian walk).
- **Extreme Amplitude Boundaries (`test_06`)**: Evaluates micro-jitter (`amp=1e-6`) and macro-boil (`amp=0.5`), scale extremes ($0.1$ to $50.0$), confirming zero NaN or Inf values.
- **Temporal Query Clamping (`test_07`)**: Verifies `get_cue_at(t)` handles $t < 0$, $t = 0$, $t = 29.58$, and $t > 30$ cleanly without out-of-bounds exceptions.
- **Beat Transition Partitions (`test_08`)**: Asserts that all 10 beat time windows form a contiguous mathematical partition of $[0.00\text{s}, 30.00\text{s}]$ with zero temporal gaps and zero overlaps.

### Tier 3: Cross-Feature Integration (`test_tier3_integration.py`)
- **Audio-Video Multiplexing Sync (`test_01`)**: Enforces that audio duration and video duration differ by $< 0.05$ seconds.
- **Subtitle Timeline Continuous Coverage (`test_02`)**: Samples the entire dialogue timeline at 50ms intervals across $[0.00\text{s}, 29.55\text{s}]$ (592 samples), verifying zero gaps in speech subtitle coverage, while confirming banners are cleanly suppressed during the Beat 10 outro hold ($29.58\text{s} - 30.00\text{s}$).
- **Differential Jitter Bézier Stability (`test_03`)**: Analyzes segment lengths between consecutive Bézier curve vertices over 12 frames. Asserts no segments collapse to zero ($> 0.01$) and distortion ratio remains bounded ($< 6.0$), preventing curve cracking or self-intersections.
- **SFX Cue Audio Alignment (`test_04`)**: Validates that all 15 procedural SFX timestamps map strictly within their designated visual beat windows, and confirms the 8.16s police siren is excluded from the mapping.
- **Layering Order Hierarchy (`test_05`)**: Verifies that subtitle banners and visual beat elements assemble cleanly in the composite hierarchy.

### Tier 4: Real-World Execution & Acceptance (`test_tier4_acceptance.py`)
- **Headless Render Verification (`test_01`)**: Verifies that `AudiobookSummaryScene` instantiates and executes `construct()` headlessly without GUI dependencies, missing fonts, or crashes.
- **Output File Integrity (`test_02`)**: Inspects the rendered MP4 file binary headers, verifying file size $> 100\text{ KB}$ and presence of top-level `ftyp`, `moov`, and `mdat` atom boxes.
- **FFprobe Media Metadata (`test_03`)**: Uses WinGet Gyan FFprobe 8.0.1 to validate container format, H.264 video stream (1920x1080 @ 24fps), and stereo audio stream (48kHz).
- **Absence of Render Error Codes (`test_04`)**: Compiles all production Python modules with `py_compile`, asserting zero syntax errors, missing imports, or unhandled exceptions.

---

## 4. Execution Commands

### Run Full Test Suite (Recommended)
```powershell
& "C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe" tests_cel_boil/run_all_tests.py
```
Or via standard Python:
```powershell
python tests_cel_boil/run_all_tests.py
```

### Run Individual Tiers
```powershell
# Tier 1: Feature Coverage
& "C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe" -m unittest tests_cel_boil.test_tier1_feature_coverage

# Tier 2: Boundary & Corner Cases
& "C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe" -m unittest tests_cel_boil.test_tier2_boundary_cases

# Tier 3: Cross-Feature Integration
& "C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe" -m unittest tests_cel_boil.test_tier3_integration

# Tier 4: Acceptance / Real-World
& "C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe" -m unittest tests_cel_boil.test_tier4_acceptance
```

---

## 5. Environment Calibration & Tool Paths
- **Python Runtime**: Python 3.11.9
- **Virtual Environment**: `C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe`
- **Manim Engine**: Manim Community Edition v0.21.0
- **FFmpeg Binary**: `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe`
- **FFprobe Binary**: `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffprobe.exe`
- **Reference Audio**: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\explorer_survey_2\test_audio_clean_30s.wav` (48kHz 16-bit stereo PCM, 1,440,000 samples, zero siren)
- **Target Repository**: `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\`
