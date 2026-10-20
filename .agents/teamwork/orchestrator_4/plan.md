# Project Plan — Manim "Cel-Boil" Audiobook Summary Replication

## Goal
Replicate the 30-second "05-cel-boil" audiobook summary visual style using the Python Manim engine. Deliver a rendered 30.00-second MP4 with hand-drawn cel-boil vector perturbation on `#f4e9d0` background, 10 visual beats synced to audio, kinetic Hinglish subtitles, clean slate (no slates or exposure counters), and audio without police sirens.

## Architecture & Milestones
- **Phase 0: Survey & Specification Mining**
  - Explorer 1 / Spec Miner 1: Analyze JS reference implementation (`C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\scene.js`, etc.) for visual beats, timing, typography, and canvas boil algorithm.
  - Explorer 2: Analyze audio assets, sound effect mappings, police siren timestamp/removal method, and 30-second audio composition.
  - Explorer 3 / Spec Miner 2: Analyze Manim engine capabilities, point-jittering updaters (`add_updater`), custom Mobject / VMobject point perturbation, performance, and `#f4e9d0` background configuration.

- **Phase 1: Dual Track Decomposition**
  - **E2E Testing Track**: Build automated test harness, verification scripts for video duration (30.00s), audio inspection (siren absent), slate removal inspection, and Cel-Boil updater code review. Publishes `TEST_READY.md`.
  - **Implementation Track**:
    - Milestone 1: Custom Manim Cel-Boil Engine (VMobject vector perturbation updater, seed/noise logic, boil rate).
    - Milestone 2: Audio Engineering & Audio Composition (30.00s TTS + SFX minus siren).
    - Milestone 3: 10-Beat Visual Timeline & Kinetic Hinglish Subtitle System.
    - Milestone 4: Scene Assembly, Clean Slate Integration, and Video Rendering.
    - Milestone 5: E2E Test Suite Validation & Verification Gate (Reviewer, Challenger, Auditor).

## Gate & Integrity Policy
- Strict AND pass criteria: Tests pass, Reviewer APPROVE, Challenger confirms correctness, Auditor CLEAN.
- Zero tolerance for integrity violations or hardcoded facades.
