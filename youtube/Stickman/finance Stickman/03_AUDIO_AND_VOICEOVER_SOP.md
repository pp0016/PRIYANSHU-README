# 🎙️ SOP 03: Audio, Voiceover & 4-Act Soundscape (Quiet Money POV)

> **Purpose:** Generate clean, engaging ElevenLabs v3 narration with millisecond timestamps and a dynamic 4-act sound design architecture to prevent audio fatigue across a 20–25 minute video.

---

## 1. TTS Generation & Voice Tuning (ElevenLabs v3)

* **Engine:** ElevenLabs v3 (`eleven_v3`) via API or web studio.
* **Voice Profile:** Confident, analytical, conversational explainer voice (e.g., *Adam*, *George*, or *Marcus*).
* **Voice Parameters:**
  - **Stability:** `Natural` (0.45 – 0.55) to maintain vocal warmth and prevent robotic monotony.
  - **Similarity Boost:** `High` (0.75 – 0.85) to preserve voice identity across episodes.
  - **Speed & Pacing:** Conversational, intimate yet driving pace (~180–195 WPM) delivering 3,800–4,700 words across 20.0 to 25.0 minutes.
* **Emotion & Pacing Tags in v3 (Act Pivot Injection):**
  - Insert tags strategically at emotional pivots:
    - `[thoughtfully]` for complex financial and behavioral trade-offs.
    - `[skeptically]` or `[curious]` when introducing societal status traps and coworker justifications.
    - `[firmly]` or `[whispers]` right before revealing a quiet compound milestone or a hidden tax reality.
    - `[warmly]` in the resolution when delivering permission and affirmation statements.

---

## 2. Word-Level Timestamp Extraction

* **Endpoint:** Use ElevenLabs `POST /v1/text-to-speech/{voice_id}/with-timestamps`.
* **Output:** Extracts start and end timestamps for every spoken word and punctuation mark.
* **Data Processing & Director Hand-off:**
  - Save as `cut_durations.json` inside `projects/[NN]_[topic]/audio/`.
  - Format: List of hold durations matched to each of the 550–700 image files for the FFmpeg concat demuxer:
    ```json
    [
      {"file": "images/img_001.png", "duration": 0.95},
      {"file": "images/img_002.png", "duration": 1.10},
      ...
      {"file": "images/img_650.png", "duration": 2.25}
    ]
    ```
  - **Director Bridge:** `cut_durations.json` is fed directly into [`screenplay_director_manifest-part-of-4-or-screenplay-writing-.md`](file:///c:/Users/renu5/Downloads/priyanshu%20readme/youtube/Stickman/finance%20Stickman/screenplay_director_manifest-part-of-4-or-screenplay-writing-.md) to lock scene boundaries `[SCENE NN | Start - End]` and align transitions and SFX cues with millisecond accuracy.

---

## 3. The 4-Act Dynamic Soundscape (Preventing Audio Fatigue)

In a 20–25 minute video, a single repeating background loop causes viewer tuning-out by minute 8. We transition across **4 distinct musical beds** aligned to the story's 4 acts:

| Narrative Act | Runtime Window | Musical Bed Character | Volume / Mix | Sound Design Highlights |
|---|:---:|---|---|---|
| **Act 1: The Quiet Decision** | 0:00 – 5:30 | Subtle acoustic pulse / curious minimalist lo-fi beat | Ducked -16 dB | High-cadence SFX in first 30s hook (cash count, key clink, subtle boom every 1–2s). |
| **Act 2: The Social Friction** | 5:30 – 11:30 | Low atmospheric friction drone / muted pulsing bass | Ducked -16 dB | Subtle office ambiance, car engine idle, distant murmurs during coworker interactions. |
| **Act 3: The System Reveal** | 11:30 – 17:30 | Investigative synth pulse / driving clockwork rhythm | Ducked -16 dB | Digital UI blips, spreadsheet paper flips, metallic impact at institutional revelations. |
| **Act 4 & Resolution** | 17:30 – 25:00 | Warm, expansive reflective acoustic / gentle piano chords | Ducked -16 dB (surges at final 60s) | Sub-bass grounding, deep emotional silence during final permission statement. |

---

## 4. SFX Library & Sound Placement Cadence

* **Governing Catalog:** 31 verified broadcast assets detailed in [`screenplay_director_manifest-part-of-4-or-screenplay-writing-.md`](file:///c:/Users/renu5/Downloads/priyanshu%20readme/youtube/Stickman/finance%20Stickman/screenplay_director_manifest-part-of-4-or-screenplay-writing-.md) (Location: `assets/sfx/<name>.wav`, 48kHz Stereo, -18 LUFS normalized).
* **Placement Cadence:**
  - **First 30–45s Hook:** 1 Sound Effect every **1.0 to 1.5 seconds** (synced with the 0.8s–1.2s hyper-cuts).
  - **Remaining Narrative:** 1 Sound Effect every **3.0 to 5.0 seconds** at key conceptual pivots.
* **Non-Negotiable Pre-Roll Offset Rule:**
  - Always cue whooshes and whip sounds **1 to 2 frames (33ms to 60ms) before the video cut** (`offset: -60ms`) so the audio crest lands exactly on the visual contact frame.
* **Core SFX Palette (Sample from 31 Assets):**
  | Sound Asset | File Name | Acoustic Character | Typical Placement |
  |---|---|---|---|
  | **Modern Shutter** | `shutter-modern.wav` | Crisp DSLR camera snap | Freeze-frame evidence holds, screenshot citations |
  | **Whoosh** | `whoosh.wav` | Fast air displacement | Push-in zooms, quick cuts, text badges |
  | **Whip Pan** | `whip.wav` | High-velocity snap | Fast camera pan, topic shifts, chapter cards |
  | **Sub Bass Boom** | `vine-boom.wav` | Heavy 808 sub-drop | Instant pattern interrupts, shocking revelations |
  | **Trailer Braam** | `dramatic-boomer.wav` | Cinematic trailer braam | Existential threats, cliffhangers at act pivots |
  | **Record Scratch** | `record-scratch.wav` | Vinyl needle drag stop | Abrupt silence, debunking statements, reality checks |
  | **Paper Turn** | `page-turn.wav` | Tactile paper rustle | Leaked bank statements, IRS filings, car titles |
  | **Mechanical Switch** | `switch.wav` | Snappy toggle click | Contrasting "What they claimed" vs "What actually happened" |

---

## 5. Background Music Ducking & Mastering

* **Multi-Stream Audio Mixing (Zero Voice Drop):**
  - In FFmpeg, naive mixing drops narrator volume whenever SFX trigger. The production mixing filter keeps voice volume constant:
    ```bash
    amix=inputs=3:duration=first:dropout_transition=0:normalize=0,alimiter=limit=0.95
    ```
* **Production Sidechain Ducking:**
  - Background music automatically drops by **-16 dB** whenever speech narration is active and swells during pauses:
    ```bash
    [bgm][voice]sidechaincompress=threshold=0.08:ratio=6:attack=100:release=350[ducked_bgm]
    ```
* **Master Normalization (YouTube Broadcast Spec):**
  - Integrated Loudness: **-14.0 LUFS** ($\pm 0.5$ LUFS).
  - True Peak: **$\le -1.0$ dBTP** (prevents YouTube audio compression distortion).
  - Sample Format: **48,000 Hz, 16-bit Stereo PCM (`pcm_s16le`)**.
