# Audio Pipeline & Reference Asset Survey Analysis

**Date:** 2026-10-10  
**Investigator:** Explorer Survey 2 (`teamwork_preview_explorer`)  
**Workspace:** `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary`  
**Reference Audio File:** `C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3`  

---

## Executive Summary

1. **TTS Voiceover File:** The speech track originates from `C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3` (93.762s mono 44.1 kHz MP3, 128 kbps). Trimming to exactly 30.00 seconds preserves the complete 10-beat narrative script up to `"inspire karein"` (ending at 29.58s) plus a 0.42s clean tail hold.
2. **Sound Effects (SFX):** 16 distinct sound effects were mapped in `audio.py`. There are **no external sample audio files**—every SFX is procedurally synthesized via DSP code using the local library `mgaudio` (`C:\Users\renu5\Downloads\mg-styles-15-test\1st\lib\audio\mgaudio`).
3. **Police Siren Removal:** Defined at lines 15–22 of `audio.py` as `police_siren(dur=1.4)` and mapped at line 68 as `m.sfx(police_siren(1.4), at=8.16)`. Removing line 68 completely removes the 1.4-second siren wobble without touching the preceding tension riser (`at=6.80`) or any other synchronized cue.
4. **Mixing Pipeline:** Clean audio generation consists of generating the 15 non-siren SFX into a 30.00s WAV via `mgaudio`, then mixing with the 30.00s trimmed TTS via FFmpeg using `-filter_complex "[0:a]volume=1.0[a0];[1:a]volume=0.9[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=0:normalize=0,volume=1.1[outa]"` exported as `pcm_s16le` 48 kHz stereo WAV (exactly 1,440,000 samples). This was verified live with zero errors.
5. **System Tools:** FFmpeg 8.0.1 full build is confirmed at the mandatory WinGet path, and Python 3.11 with `numpy` 1.26.4, `scipy` 1.17.1, `soundfile` 0.13.1, and a virtualenv containing Manim 0.21.0 are verified and available.

---

## 1. TTS Voiceover Track Inspection

### 1.1 Technical Profile (FFprobe Verified)
- **Path:** `C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3`
- **Container / Codec:** MP3 (`mp3float` decoder, MPEG audio layer 3)
- **Total Duration:** 93.762177 seconds (1 minute 33.76 seconds)
- **Sample Rate:** 44,100 Hz (44.1 kHz)
- **Channels:** 1 (mono)
- **Sample Format:** `fltp` (32-bit floating point)
- **Bitrate:** 128 kb/s CBR (`bit_rate`: 128,000 bps)
- **File Size:** 1,501,353 bytes
- **Encoder Tag:** Lavf60.16.101
- **Stream Offset:** `start_time` = 0.025057s (typical MP3 priming/padding delay)

### 1.2 Dialogue Script & Timestamp Alignment
According to `transcription.json` and `cues.js`, the first 30 seconds covers:
- **0.00s – 1.08s:** "Kya aapne kabhi notice kiya"
- **1.08s – 4.02s:** "hai ki kuch log bina force kiye hi dusron ka trust aur respect gain kar lete hain?"
- **4.56s – 8.16s:** "Jabki kuch log sahi baat keh kar bhi logon ko convince nahi kar paate hain. Aakhir..."
- **8.16s – 8.78s:** "difference kya hai?"
- **9.22s – 12.20s:** "Kya logon ko influence karna sirf achi communication skills ka game hai?"
- **12.20s – 14.76s:** "Ya iske peeche human psychology ko samajhne ka ek deeper science hai?"
- **15.16s – 18.08s:** "Dale Carnegie ki legendary book How to Win Friends and Influence People"
- **18.66s – 23.36s:** "aapko logon ko manipulate karna nahi balki unhe genuinely samajhna aur better relationships build karna sikhati hai."
- **23.36s – 26.66s:** "Is wonderful book mein hum jaanenge ki bina argument ke apni baat kaise rakhein,"
- **27.26s – 29.58s:** "criticism ke bina dusron ko improve karne ke liye kaise inspire karein."
- **29.58s – 30.00s:** Room decay / visual outro hold.

### 1.3 How to Cut Exactly to 30.00 Seconds
- **Direct MP3 trimming limitation:** MP3 frames contain 1,152 samples (~26.12 ms). Slicing MP3 bitstreams directly causes frame quantization jitter (e.g. `out/tts_trimmed.mp3` has a duration of 30.027755s).
- **Exact PCM WAV approach:** Trimming and resampling directly into uncompressed PCM WAV via FFmpeg (`-t 30.000000 -c:a pcm_s16le -ar 48000 -ac 2`) yields exactly **1,440,000 audio samples** ($48,000 \text{ samples/sec} \times 30.000000 \text{ sec}$), achieving microsecond synchronization accuracy.

---

## 2. Sound Effects (SFX) Inventory & Mapping

In `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\audio.py`, audio effects are arranged using `mgaudio.mix.Mix(duration=30.0, bpm=120)`.

There are **zero external audio files** in `assets/` or `audio/`. Every effect is generated procedurally via NumPy DSP routines from `mgaudio`.

### 2.1 Complete SFX Mapping Table
| Timestamp | Dialogue / Visual Event | Function / Generator | DSP Description | Status |
|:---:|:---|:---|:---|:---:|
| **0.05s** | Intro paper slate entrance | `sfx.paper('slide', dur=0.35)` | Bandpass filtered noise slide | **Keep** |
| **1.08s** | "Notice kiya?" curiosity pop | `sfx.pop('cork', 1.0)` | Resonant exponential decay pop | **Keep** |
| **3.12s** | "Trust aur Respect" warm chime | `sfx.ding(note=72)` | Pure sine ring modulated chime (C5) | **Keep** |
| **6.80s** | "Aakhir..." tension riser | `rising_sweep(1.35)` | Logarithmic pitch riser sweep | **Keep** |
| **8.16s** | "Aakhir difference kya hai?" | `police_siren(1.4)` | Sine modulated 850±260 Hz FM wobble | ❌ **REMOVE** |
| **11.20s** | "atchi communication skills" | `mechanical_tick()` | `sfx.tick('hi')` + `sfx.click('wood')` | **Keep** |
| **14.18s** | "Deeper science" subtle blip | `sfx.blip(note=67)` | Clean UI notification blip (G4) | **Keep** |
| **16.04s** | "Dale Carnegie..." Book Slam | `book_slam()` | `sfx.paper('flip')` + `sfx.impact('punch')` + `sfx.boom(0.8, 48)` | **Keep** |
| **19.34s** | "manipulate karna nahi" Gunshot | `gunshot(0.7)` | `sfx.impact('punch')` + `sfx.pop('cork')` + sub boom | **Keep** |
| **21.86s** | "better relationships build" | `sfx.sparkle(dur=0.55)` | Multi-oscillator high sparkle cascade | **Keep** |
| **23.36s** | "Is wonderful book mein" | `page_turn_spread()` | Paper flip (0.32s) + paper rustle (0.35s) | **Keep** |
| **24.20s** | "bina argument ke" Badge 1 | `sfx.sticker_slap(seed=11)` | Tactile adhesive snap | **Keep** |
| **25.00s** | "apne baat kaise rakhein" gesture | `sfx.whoosh(0.35, 'heavy')` | Directional low-air whoosh | **Keep** |
| **26.20s** | "criticism..." Badge 2 | `sfx.sticker_slap(seed=22)` | Punchy slap transient | **Keep** |
| **28.20s** | "dusron ko improve..." Badge 3 | `sfx.shimmer_hit('G5')` | Harmonic shimmer bloom | **Keep** |
| **28.74s** | "se inspire karna" hero bell | `sfx.ding(note=79)` | High flourish bell chime (G5) | **Keep** |

---

## 3. Police Siren Removal Analysis

### 3.1 Code Location
- **Definition:** Lines 15–22 of `audio.py`:
  ```python
  def police_siren(dur=1.4):
      sr = 48000
      t = np.linspace(0, dur, int(sr * dur), False)
      f = 850 + 260 * np.sin(2 * np.pi * 1.5 * t)
      phase = 2 * np.pi * np.cumsum(f) / sr
      sig = 0.45 * np.sin(phase) + 0.2 * np.sin(2 * phase)
      env = np.minimum(t / 0.08, 1.0) * np.minimum((dur - t) / 0.15, 1.0)
      return mg.core.Sound((sig * env).astype(np.float32))
  ```
- **Invocation / Placement:** Line 68 of `audio.py`:
  ```python
  # 8.16: "Aakhir difference kya hai?" - Police Siren frequency sweep
  m.sfx(police_siren(1.4), at=8.16)
  ```
- **Visual Association in Canvas Reference:** In `scene.js` (lines 289–308), the siren triggers concentric warning rings and flashing alert beacons at `t >= 8.16`. In the new Manim replication, R3 explicitly requires this siren to be eliminated.

### 3.2 Surgical Removal Method
- **Source-Level Deletion:** In the Python audio generation script, simply delete or omit line 68 (`m.sfx(police_siren(1.4), at=8.16)`).
- **Preservation of Context:** 
  - Line 65 (`m.sfx(rising_sweep(1.35), at=6.80)`) ends cleanly at $6.80 + 1.35 = 8.15\text{s}$, creating an energetic riser up to the question.
  - The dialogue `"difference kya hai?"` (8.16s – 8.78s) now plays with complete vocal clarity without the overpowering siren alarm over it.
  - No post-mix filtering (e.g. notch filters or spectral subtraction) should ever be used, as that would degrade the speech quality. Procedural removal at synthesis guarantees 100% loss-free vocal fidelity.

---

## 4. Mixing Pipeline & Exact Reproduction Code

### 4.1 Standalone Clean Python Generation Script
The following complete script builds the clean, siren-free 30.00-second audio track. It has been tested and verified locally.

```python
import sys, os, subprocess
import numpy as np

MGAUDIO_PATH = r"C:\Users\renu5\Downloads\mg-styles-15-test\1st\lib\audio"
sys.path.insert(0, MGAUDIO_PATH)
import mgaudio as mg
from mgaudio import sfx

# 1. Initialize 30.0-second timeline
m = mg.Mix(duration=30.0, bpm=120)

# 2. Composite SFX definitions
def gunshot(dur=0.7):
    crack = sfx.impact('punch', 1.4)
    pop = sfx.pop('cork', 1.8)
    boom = sfx.boom(dur, 65)
    return mg.layer([(crack, 0, 3, 0), (pop, 0, 2, 0), (boom, 0, 0, 0)])

def book_slam():
    return mg.layer([
        (sfx.paper('flip', dur=0.2), 0, 2, 0),
        (sfx.impact('punch', 1.3), 0.04, 3, 0),
        (sfx.boom(0.8, 48), 0.04, 1, 0)
    ])

def rising_sweep(dur=1.35):
    sw = sfx.riser(dur=dur, kind='sweep')
    sw.sync = 0.0
    return sw

def mechanical_tick():
    return mg.layer([
        (sfx.tick('hi'), 0, 0, 0),
        (sfx.click('wood'), 0.005, -2, 0)
    ])

def page_turn_spread():
    return mg.layer([
        (sfx.paper('flip', dur=0.32), 0, 1.5, 0),
        (sfx.paper('rustle', dur=0.35), 0.04, -2, 0)
    ])

# 3. Synchronized cues (15 sound effects, SIREN OMITTED)
m.sfx(sfx.paper('slide', dur=0.35), at=0.05)
m.sfx(sfx.pop('cork', 1.0), at=1.08)
m.sfx(sfx.ding(note=72), at=3.12)
m.sfx(rising_sweep(1.35), at=6.80)
# (8.16s police_siren omitted here)
m.sfx(mechanical_tick(), at=11.20)
m.sfx(sfx.blip(note=67), at=14.18)
m.sfx(book_slam(), at=16.04)
m.sfx(gunshot(0.7), at=19.34)
m.sfx(sfx.sparkle(dur=0.55), at=21.86)
m.sfx(page_turn_spread(), at=23.36)
m.sfx(sfx.sticker_slap(seed=11), at=24.20)
m.sfx(sfx.whoosh(0.35, 'heavy'), at=25.00)
m.sfx(sfx.sticker_slap(seed=22), at=26.20)
m.sfx(sfx.shimmer_hit('G5'), at=28.20)
m.sfx(sfx.ding(note=79), at=28.74)

# 4. Render clean SFX WAV
sfx_wav_path = "clean_sfx.wav"
m.export(sfx_wav_path)

# 5. Mix with TTS voiceover via FFmpeg
tts_mp3 = r"C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3"
ffmpeg_bin = r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"
out_wav = "audio_clean_30s.wav"

cmd = [
    ffmpeg_bin, "-y",
    "-t", "30.000000", "-i", tts_mp3,
    "-t", "30.000000", "-i", sfx_wav_path,
    "-filter_complex", "[0:a]volume=1.0[a0];[1:a]volume=0.9[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=0:normalize=0,volume=1.1[outa]",
    "-map", "[outa]",
    "-t", "30.000000",
    "-c:a", "pcm_s16le",
    "-ar", "48000",
    "-ac", "2",
    out_wav
]
subprocess.run(cmd, check=True)
print("Generated clean 30.00s audio track:", out_wav)
```

### 4.2 Muxing into Final Manim Render
When Manim finishes rendering the 30-second video (`video_rendered.mp4`), the final output MP4 can be combined without re-encoding the visual stream using:
```powershell
& "C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe" -y `
  -i video_rendered.mp4 `
  -i audio_clean_30s.wav `
  -c:v copy `
  -c:a aac -b:a 192k `
  -t 30.000000 `
  final_audiobook_summary.mp4
```
If re-encoding video for Windows Media Player compatibility (R4 in original request):
```powershell
& "C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe" -y `
  -i video_rendered.mp4 `
  -i audio_clean_30s.wav `
  -c:v libx264 -pix_fmt yuv420p -crf 17 `
  -c:a aac -b:a 192k `
  -t 30.000000 `
  final_audiobook_summary.mp4
```

---

## 5. System Audio Tools & Environment Assessment

1. **FFmpeg & FFprobe Executables:**
   - Path: `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe`
   - Version: FFmpeg 8.0.1 full build (built with GCC 15.2.0, supports full filter complex, high-res audio resampling, x264, aac, etc.).
   - Path: `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffprobe.exe` (verified operational).
2. **Python Environment & Audio Libraries:**
   - Python: 3.11.9 (64-bit AMD64)
   - `numpy`: 1.26.4 (Installed)
   - `scipy`: 1.17.1 (Installed)
   - `pydub`: Installed
   - `soundfile`: 0.13.1 (Installed)
   - `wave`: Standard library (Installed)
3. **Manim Environment:**
   - `manim`: Version 0.21.0 installed in virtual environment `C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe`.
4. **mgaudio DSP Engine:**
   - Located at `C:\Users\renu5\Downloads\mg-styles-15-test\1st\lib\audio\mgaudio`. Fully working and capable of generating all required motion-graphics sound design assets offline without internet or external APIs.

---

## 6. Pre-Generated Verification Artifacts
- Script: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\explorer_survey_2\test_audio_pipeline.py`
- Clean SFX Track: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\explorer_survey_2\test_sfx_no_siren.wav` (30.000s, 48kHz 24-bit stereo)
- Clean Master Mixed Audio: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\explorer_survey_2\test_audio_clean_30s.wav` (30.000000s, 1,440,000 samples, 48kHz 16-bit stereo PCM, exact size: 5,760,078 bytes)
