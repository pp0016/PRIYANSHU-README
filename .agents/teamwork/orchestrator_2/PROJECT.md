# Project: Automated 3D Motion Graphics Pipeline & Cloud Render Farm

## Architecture
The system delivers an automated, high-end 3D motion graphics pipeline built on Blender's Python API (`bpy`) and a parallel cloud render farm running on GitHub Actions.

- **Procedural 3D Typography Engine (`blender/scene_generator.py`)**:
  - Headless procedural scene builder utilizing `bpy`.
  - Multi-tier typography hierarchy (Gold Metallic text, Neon Cyan Glowing Rim text) with bevel, extrusion, and eased keyframed animation (overshoot easing).
  - Reflective obsidian ground plane and floating glowing geometric accent particles with rotational drift.
  - 4-point studio lighting rig (Area Key, Area Fill, Cyan Rim Kicker, moving Keyframed Glint Light).
  - Cinematic 75mm camera rig with Track-To constraints, Depth of Field (DoF f/2.2), and dynamic dolly push-in animation.
  - Cycles CPU engine with OpenImageDenoise (OIDN), adaptive sampling threshold (0.05), and clamped light bounces.
  - CLI argument support for frame ranges (`-s <start> -e <end>`), output naming (`-o <pattern>`), and headless execution.

- **Parallel Cloud Render Farm Workflow (`.github/workflows/blender_render.yml`)**:
  - Preflight matrix planner job dividing total animation frames (e.g. 120 frames) into parallel runner chunks (e.g. 30 frames per chunk).
  - Parallel matrix render workers on `ubuntu-latest`:
    - Direct download and extraction of portable Blender 4.2+ LTS tarball (~12s setup).
    - Installation of minimal system libraries (`libxi6`, `libglu1-mesa`, `libgl1-mesa-dri`).
    - Headless Cycles CPU rendering outputting numbered lossless PNG image sequences (`frame_#####.png`).
    - Upload of per-chunk PNG artifacts using `actions/upload-artifact@v4`.
  - FFmpeg Stitcher Job:
    - Downloads all chunks using `actions/download-artifact@v4` with `pattern: frames-chunk-*` and `merge-multiple: true`.
    - Validates downloaded frame count against expected total frames.
    - Concatenates the unified image sequence into a final broadcast-quality `.mp4` video (`yuv420p`, `-crf 18`, `libx264`, `+faststart`).
    - Uploads final video artifact.

- **E2E Test Suite & Automated Verification (`tests/` & `tests_manim_blender/`)**:
  - Comprehensive 4-tier test suite covering CLI parsing, headless bpy execution, PBR materials, matrix chunk math, GitHub Actions workflow YAML parsing, and FFmpeg video validation.
  - Unified test runner `tests_manim_blender/run_all_tests.py` providing structured reporting.

- **Non-Destructive Integration**:
  - Completely preserves existing Manim project (`main.py`, `.github/workflows/render.yml`).
  - Isolated in `blender/` directory, `.github/workflows/blender_render.yml`, and `tests/`.

---

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F1 | Open-Source Quality Calibration & Baseline Specs | Establish professional motion graphics standards, shader graphs, lighting rigs, and kinetic typography easing curves based on top-tier open-source Blender templates (`blender/baseline_spec.md`). | M1 | ORIGINAL_REQUEST R3 |
| F2 | Procedural 3D Typography Creation | Procedural generation of 3D text curves with extrusion, bevel depth, and resolution via `bpy` (`blender/scene_generator.py`). | M2 | ORIGINAL_REQUEST R1 |
| F3 | Advanced Shaders & Materials | Procedural Principled BSDF shaders: Gold Metallic, Neon Cyan Emission/Glow with AgX/Filmic color management, and reflective obsidian floor. | M2 | ORIGINAL_REQUEST R1 |
| F4 | Cinematic Lighting & Camera Rig | 4-point studio lighting setup (Key, Fill, Rim, animated Glint) + 75mm camera rig with DoF bokeh and dolly push-in. | M2 | ORIGINAL_REQUEST R1 |
| F5 | Eased Keyframing & Kinetic Particle Accents | Overshoot scale entry animations for text lines + floating animated diamond particles. | M2 | ORIGINAL_REQUEST R1 |
| F6 | Headless CLI & Engine Optimization | Automated Cycles CPU configuration with OIDN, adaptive sampling, clamped bounces, persistent data, and CLI override compatibility. | M2 | ORIGINAL_REQUEST R1 |
| F7 | Parallel Matrix Render Workflow | GitHub Actions workflow downloading portable Blender, executing parallel matrix runners across 30-frame chunks (`.github/workflows/blender_render.yml`). | M3 | ORIGINAL_REQUEST R2 |
| F8 | Frame Artifact Upload & Consolidation | Per-chunk PNG sequence upload with `actions/upload-artifact@v4` and unified download via `download-artifact@v4` with `merge-multiple: true`. | M3 | ORIGINAL_REQUEST R2 |
| F9 | Frame Validation & FFmpeg Video Stitching | Total frame integrity check and FFmpeg single-pass compilation to smooth, non-stuttering MP4. | M3 | ORIGINAL_REQUEST R2 |
| F10 | Comprehensive E2E Testing Suite | Multi-tier test suite verifying headless execution, frame counts, video duration, codec validity, and render farm outputs. | M4 | ORIGINAL_REQUEST Criteria |

---

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Open-Source Quality Calibration & Baseline Specs | Baseline specification `blender/baseline_spec.md` detailing professional typography, lighting, shader, and motion parameters. | none | DONE |
| M2 | Procedural 3D Typography bpy Engine | Implementation of `blender/scene_generator.py` with full procedural scene generation, materials, lighting, camera, keyframing, and CLI options. | M1 | DONE |
| M3 | Parallel Cloud Render Farm Workflow | Implementation of `.github/workflows/blender_render.yml` and `.gitignore` for parallel matrix rendering and FFmpeg stitching. | M2 | DONE |
| M4 | E2E Testing Track & Final Verification | Comprehensive 4-Tier test suite in `tests/`, test runner `run_all_tests.py`, multi-agent review, challenger validation, and forensic audit. | M3 | DONE |

---

## Interface Contracts

### CLI Contract: `blender/scene_generator.py`
- Invocation:
  `blender -b -P blender/scene_generator.py -- [OPTIONS]`
  or with standard Blender flags:
  `blender -b -P blender/scene_generator.py -o "<output_dir>/frame_#####" -s <start> -e <end> -a`
- Options:
  - `--start <int>`: Start frame (default: 1)
  - `--end <int>`: End frame (default: 60)
  - `--output <path>`: Output frame template (default: `//output/frame_#####`)
  - `--samples <int>`: Cycles render samples (default: 16-32)
  - `--text1 <str>`: Primary hook line (default: "KABHI NOTICE KIYA?")
  - `--text2 <str>`: Secondary hook highlight (default: "TRUST & RESPECT")
- Exit Code: 0 on success, non-zero on failure.
- Output Format: 8-bit PNG RGBA image sequence `frame_00001.png`, etc.

### Workflow Contract: `.github/workflows/blender_render.yml`
- Trigger: `push` to `main`, `workflow_dispatch` (with `total_frames`, `chunk_size` inputs).
- Runners: `ubuntu-latest`.
- Matrix outputs: `frames-chunk-<chunk_id>` artifacts.
- Final artifact: `Final_3D_Typography_Hook` containing `Final_3D_Typography_Hook.mp4`.
- Video specification: H.264, 1920x1080 @ 30fps, `yuv420p`, CRF 18, `faststart`.

---

## Code Layout
```
c:\Users\renu5\Downloads\manim_video_repo\
├── .github\
│   └── workflows\
│       ├── render.yml                 # Existing Manim workflow (preserved)
│       └── blender_render.yml         # Parallel Blender Cloud Render Farm
├── blender\
│   ├── baseline_spec.md               # Quality calibration baseline specification
│   ├── scene_generator.py             # Main procedural 3D typography bpy engine
│   └── __init__.py
├── tests\
│   ├── __init__.py
│   ├── test_helpers.py                # Discovery & validation helpers
│   ├── test_tier1_feature_coverage.py # Headless execution, CLI flags, materials, lighting
│   └── test_tier2_boundary_cases.py   # Edge cases, 1-frame, extreme text, sampling
├── .gitignore                         # Output and cache exclusions
├── main.py                            # Existing Manim scene
└── requirements.txt                   # Dependencies
```
