# DISPATCH — Worker M1: Clean Audio Master Pipeline (teamwork_preview_worker)
- Working Directory: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\worker_audio_m1`
- Original Request: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\ORIGINAL_REQUEST.md`
- Project Document: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\orchestrator_4\PROJECT.md`
- Mission: Implement `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\audio_pipeline.py` and generate `audio_clean_30s.wav` (exactly 30.000000s, 1,440,000 samples @ 48kHz stereo, siren completely omitted).

## 2026-10-10T18:18:52Z
You are Worker M1: Clean Audio Master Pipeline (teamwork_preview_worker).
Your working directory is: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\worker_audio_m1`
MANDATORY: Read `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\ORIGINAL_REQUEST.md` before starting work.
Also read `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\orchestrator_4\PROJECT.md`.
Reference the analysis in `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\explorer_survey_2\analysis.md` and `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\audio.py`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your exclusive write ownership:
- `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\audio_pipeline.py`
- Produces `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\audio_clean_30s.wav`

Tasks:
1. Implement `audio_pipeline.py` in `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\`:
   - Imports/uses `mgaudio` from `C:\Users\renu5\Downloads\mg-styles-15-test\1st\lib\audio\mgaudio` (or reuses procedural SFX algorithms directly).
   - Generates all 15 procedural sound effects mapped in `audio.py` (cork pop at 1.08s, ding at 3.12s, rising sweep at 6.80s, mechanical tick at 11.20s, blip at 14.18s, book slam at 16.04s, gunshot at 19.34s, sparkle at 21.86s, page turn at 23.36s, sticker slap at 24.20s, whoosh at 25.00s, sticker slap at 26.20s, shimmer at 28.20s, ding at 28.74s, paper slide at 0.05s).
   - COMPLETELY OMITS the police siren sound effect (`police_siren(1.4)` at 8.16s).
   - Trims source TTS MP3 `C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3` to precisely 30.000000s.
   - Mixes TTS and 15 SFX using WinGet FFmpeg (`C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe`) with `amix=inputs=2:duration=first:dropout_transition=0:normalize=0,volume=1.1`.
   - Exports master `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\audio_clean_30s.wav` as 48kHz, 16-bit stereo PCM with exactly 1,440,000 samples (precisely 30.000000s).
2. Execute `python audio_pipeline.py` using `C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe` and verify:
   - Output file exists and is exactly 30.000000s.
   - Run verification script to confirm zero siren energy in [8.16s - 9.56s].
3. Write `handoff.md` with complete verification command outputs and send a message.
