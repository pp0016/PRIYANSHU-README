# 📁 audio/ — Voiceover Synthesis & Pacing Architecture

## 🎯 Purpose
Hosts the master ElevenLabs v3 narration, word-level timestamps, and SFX/background music assets.

## ✅ What is REQUIRED Here
1. **`voiceover.wav`**:
   - Master narration generated via ElevenLabs v3 (`eleven_v3`).
   - Profile: Confident, conversational, analytical explainer voice (Adam/George/Marcus).
   - Parameters: Stability 0.45–0.55, Similarity 0.75–0.85, Pacing ~200 WPM.
   - Format: 48,000 Hz, 16-bit Stereo PCM (`pcm_s16le`), normalized to -14.0 LUFS.
2. **`cut_durations.json`**:
   - Generated from `POST /v1/text-to-speech/{voice_id}/with-timestamps`.
   - Maps each sentence/scene cut to exact milliseconds for FFmpeg timeline stitching.
   - Format: `[{"file": "img_001.png", "duration": 2.75}, ...]`
3. **`music_bed.wav`** (Optional if mixed externally):
   - Ambient, subtle corporate/investigative score sidechain-ducked -16 dB during speech.

## ❌ What is NOT REQUIRED / FORBIDDEN
- Do NOT keep flawed audio takes, robotic monologues, or broken takes.
- Do NOT use uncompressed multi-gigabyte DAW sessions here.
