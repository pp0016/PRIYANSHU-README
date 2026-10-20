# Project: 30-Second Audiobook Summary Cel-Boil Pure Native Rebuild

## Architecture
- **Harness & Render Engine**: Node.js Puppeteer harness (`harness/render.mjs`) driving headless Chrome on Windows, capturing canvas frames, stitching via WinGet FFmpeg (`ffmpeg-8.0.1-full_build`).
- **Visual Scene**: Native HTML5 Canvas 2D scene (`demos/audiobook-summary/js/scene.js`) powered by procedural cel-boil engine (`demos/audiobook-summary/js/engine.js`). Cream background (`#f4e9d0`), hand-inked line boils on twos, pure procedural vectors (magnifying glass, seals, question marks, brain orbits, book slam, sparks, badges).
- **Audio & SFX**: Python audio pipeline (`demos/audiobook-summary/audio.py`) leveraging `lib/audio/mgaudio.py`. Decodes and trims source TTS (`C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3`) to exactly 30.000s, synthesizes 16 unique kinetic sound effects (book slam, siren, gunshot, page turn, badge slaps, chimes), and mixes down to `out/audio.wav` (48kHz stereo PCM, 30.000000s).
- **Muxing & Windows Playability**: FFmpeg encodes video with `-pix_fmt yuv420p` and `-profile:v high` to ensure 100% native playback on Windows Media Player without errors.

## Code Layout & Write Boundaries
- `demos/audiobook-summary/audio.py`: Owned exclusively by Milestone 1 Worker.
- `demos/audiobook-summary/js/scene.js`: Owned exclusively by Milestone 2 Worker.
- `harness/render.mjs`: Owned exclusively by Milestone 3 Worker.
- `.agents/teamwork/*`: Coordination metadata only.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | R1: Audio Trimming | Cut source TTS MP3 down to exactly 30.000000s PCM WAV (48kHz stereo) | M1 (DONE) | ORIGINAL_REQUEST.md § R1 |
| 2 | R3: Unique SFX & Loop Purge | Purge duplicate book slams, silence gaps; add distinct synced SFX (book slam, siren, gunshot, page turn, slaps) | M1 (DONE) | ORIGINAL_REQUEST.md § R3 |
| 3 | R2: Purge Raster Images | Remove all .png/.jpg references, preloading logic, and drawImage calls from scene.js | M2 (DONE) | ORIGINAL_REQUEST.md § R2 |
| 4 | R2: Pure Native Cel-Boil Visuals | Build 10-beat Hinglish kinetic text & procedural cel-boil vector doodles synced to voiceover cues | M2 (DONE) | ORIGINAL_REQUEST.md § R2 |
| 5 | R4: Windows-Compatible FFmpeg | Force -pix_fmt yuv420p, high profile, forward-slash concat list, and log [ffmpeg] commands | M3 (IN_PROGRESS) | ORIGINAL_REQUEST.md § R4 |
| 6 | R4: 30-Second Video Render | Render 720 frames (30s @ 24fps), mux audio.wav, generate out/video.mp4 | M3 (IN_PROGRESS) | ORIGINAL_REQUEST.md § R4 |
| 7 | Acceptance & Integrity Verification | Verify ffprobe duration=30.0s, yuv420p, zero image imports, forensic audit CLEAN | M4 (PLANNED) | ORIGINAL_REQUEST.md Acceptance Criteria |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Audio Trimming & SFX Pipeline | Update audio.py: trim TTS to 30.000s, implement 16 unique SFX cues, run python audio.py | none | DONE |
| M2 | Pure Native Cel-Boil Visuals | Rebuild scene.js: remove all images, implement 10-beat cel-boil Hinglish kinetic scene | none | DONE |
| M3 | Render Harness & Video Render | Patch render.mjs (yuv420p, concat fix, logging) and execute full 30s video render | M1, M2 | IN_PROGRESS |
| M4 | Gate Verification & Audit | Multi-agent review (Reviewers, Challengers, Forensic Auditor) and acceptance verification | M3 | PLANNED |

## Interface Contracts
### audio.py ↔ render.mjs
- File: `demos/audiobook-summary/out/audio.wav`
- Format: PCM 16-bit stereo (`pcm_s16le`), 48,000 Hz sample rate.
- Duration: Exactly 30.000000 seconds (1,440,000 samples).
- Peak: <= -1.0 dBTP (no digital clipping).

### scene.js ↔ render.mjs
- File: `demos/audiobook-summary/js/scene.js`
- Exports: `init()`, `render(ctx, f, t)`, `W = 1920`, `H = 1080`, `FPS = 24`.
- Duration: 30.00 seconds (720 frames from frame 0 to 719).
- Background: `#f4e9d0` (`PAL.cream`).
- Asset Dependencies: ZERO external `.png` or `.jpg` files.

### render.mjs ↔ Windows OS
- Output: `demos/audiobook-summary/out/video.mp4`
- Video Stream: H.264 (High profile, Level 4.1 or 4.0), `-pix_fmt yuv420p`, 1920x1080, 24 fps, duration exactly 30.00 seconds.
- Audio Stream: AAC-LC, 48000 Hz, stereo.
- Compatibility: Plays natively in Windows Media Player.
