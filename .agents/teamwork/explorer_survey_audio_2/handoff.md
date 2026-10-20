# Handoff Report — Audio & SFX Explorer (explorer_survey_audio_2)

**Mission**: Survey Requirement R1 (Audio Trimming) and R3 (Unique Sound Effects) for the 30-Second Pure `05-cel-boil` Native Audiobook Summary Video.  
**Target Directory**: `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary`  
**Handoff Type**: Hard (Investigation & Survey Complete)  

---

## 1. Observation

### 1.1 Source TTS Audio Verification (Requirement R1)
- **Path**: `C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3`
- **File Existence**: Verified present on disk.
- **Probe Command**:
  ```powershell
  & "C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffprobe.exe" -v error -show_entries format=duration,bit_rate,format_name -show_entries stream=codec_name,sample_rate,channels "C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3"
  ```
- **Output**:
  ```
  [STREAM]
  codec_name=mp3
  sample_rate=44100
  channels=1
  [/STREAM]
  [FORMAT]
  format_name=mp3
  duration=93.762177
  bit_rate=128098
  [/FORMAT]
  ```
- **Stream Attributes**: Mono MP3, 44,100 Hz sample rate, 128 kbps constant bitrate, total duration 93.762177 seconds (~1m 33.76s).

### 1.2 Trimming Mechanics & Verification
- **Stream-Copy Trimming Test Command**:
  ```powershell
  & "C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe" -y -ss 00:00:00.000 -t 00:00:30.000 -i "C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3" -c copy "out/tts_trimmed.mp3"
  ```
- **Observed Result**: Due to MP3 packet framing (~26.12 ms/frame at 44.1 kHz), stream copying cuts at packet boundary: `duration=30.027755`.
- **Integrated PCM Mixing in `audio.py`**:
  ```python
  subprocess.run([
      FFMPEG, "-y",
      "-t", "30", "-i", TTS_MP3,
      "-t", "30", "-i", SFX_WAV,
      "-filter_complex", "[0:a]volume=1.0[a0];[1:a]volume=0.9[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=0,volume=1.1[outa]",
      "-map", "[outa]",
      "-t", "30",
      "-ar", "48000",
      "-ac", "2",
      OUT_WAV
  ], check=True)
  ```
- **Observed Result for `out/audio.wav`**:
  ```
  [STREAM]
  codec_name=pcm_s16le
  sample_rate=48000
  channels=2
  [/STREAM]
  [FORMAT]
  duration=30.000000
  bit_rate=1536020
  [/FORMAT]
  ```
  Duration is sample-accurate to exactly `30.000000` seconds (1,440,000 samples @ 48 kHz).

### 1.3 `audio.py` Structure & Loop Identification (Requirement R3)
- **Path**: `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\audio.py` (93 lines).
- **Core Architecture**:
  - Uses `mgaudio.Mix(duration=30.0, bpm=120)`.
  - Defines custom procedural synthesizers:
    - `police_siren(dur=1.4)` (lines 15–22): FM sinusoidal synthesis at 48 kHz.
    - `gunshot(dur=0.7)` (lines 24–28): Multi-layer impact + cork pop + sub boom.
    - `book_slam()` (lines 30–35): Multi-layer paper flip + punch impact + sub boom.
  - Placed SFX events:
    - `0.05`: `sfx.paper('slide', dur=0.4)`
    - `1.08`: `sfx.pop('cork', 1.0)`
    - `3.12`: `sfx.ding(note=72)`
    - `8.16`: `police_siren(1.4)`
    - `14.18`: `sfx.blip(note=67)`
    - `16.04`: `book_slam()`
    - `19.34`: `gunshot(0.7)`
    - `21.86`: `sfx.sparkle(dur=0.5)`
    - `23.36`: `book_slam()` (Duplicate!)
    - `25.00`: `sfx.whoosh(0.35, 'heavy')`
    - `28.74`: `sfx.ding(note=79)` (Duplicate chime category)
- **Execution Run Observation**:
  Running `python audio.py` yields:
  ```
  [mgaudio] C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\out\sfx.wav: 30.000s LUFS -14.02 TP -1.22 dBTP  WARN: silence gap 4.25s
  30-second audio mixed successfully without loops.
  ```
  - `WARN: silence gap 4.25s`: An audible dead zone exists between `3.12s` and `8.16s` (5.04s gap), and between `9.56s` and `14.18s` (4.62s gap).
  - Repetition: `book_slam()` is used identically twice (16.04s and 23.36s). At 23.36s, the on-screen visual is an open book spread, not a slam.
  - Missing Animation Sync: In `scene.js`, three distinct principle badges animate into screen at `24.2s` (Badge 1: "1. NO ARGUMENT"), `26.2s` (Badge 2: "2. NO CRITICISM"), and `28.2s` (Badge 3: "3. INSPIRE OTHERS"). In `audio.py`, timestamps `24.2s` and `26.2s` have zero sound effects.

### 1.4 SFX Asset Inventory in `lib/audio`
- **Location**: `C:\Users\renu5\Downloads\mg-styles-15-test\1st\lib\audio`
- **Procedural Synthesizers (`mgaudio.sfx`)**:
  - Impacts & Hits: `impact` ('punch', 'cinematic', 'metal', 'trailer', 'thud', 'glitch'), `boom`, `sub_drop`.
  - Transients & UI: `pop` ('cork', 'mouth', 'bubble'), `blip`, `click` ('wood', 'hard', 'switch'), `tick` ('hi'), `ui`, `ding`, `chime`.
  - Motion: `whoosh` ('air', 'swoosh', 'swish', 'heavy', 'sci', 'cloth', 'fire'), `swish`, `riser`, `downlifter`.
  - Tactile Foley: `paper` ('flip', 'slide', 'rustle', 'tear'), `sticker_slap`, `sticker_peel`, `tape_rip`, `stamp`, `pen`.
  - Visual Accents: `sparkle`, `shimmer_hit`, `magic`, `glitch`, `stutter`.
- **Acoustic Samples (`lib/audio/samples`)**:
  - `slapstick` (`slapstick_rr1.flac`, `slapstick_rr2.flac`, `slapstick_rr3.flac`) — high-impact wooden slap.
  - `woodblock` (`wood_click_f_rr1.flac`, `wood_click_ff.flac`, `wood_click2_mp.flac`) — crisp tactile ticks.
  - `glock`, `marimba`, `vibraphone`, `timpani`, `crash`, `wineglass`.

---

## 2. Logic Chain

1. **Premise**: Requirement R1 mandates cutting the main TTS audio down to exactly the first 30 seconds, and Requirement R3 mandates strictly synced, unique, non-repeating sound effects aligned to on-screen kinetic cues.
2. **Analysis of Trimming (R1)**:
   - Source MP3 is 93.76s long. 30.00s corresponds to timestamp 0:30.00, which terminates directly after "se inspire karna" (spoken at 29.08s–29.58s in `cues.js`), before "logon ko genuinely" begins at 30.08s. This provides a natural, clean sentence boundary.
   - Using FFmpeg `-t 30` with `-ar 48000 -ac 2` decodes and resamples the stream into exactly `duration=30.000000` s without packet truncation or pitch distortion.
3. **Analysis of Loop Elimination & SFX Uniqueness (R3)**:
   - While `audio.py` has removed generic rhythmic timer loops, it reuses the exact same composite asset `book_slam()` at 23.36s that was used at 16.04s.
   - At 16.04s, "Dale Carnegie ki legendary book" enters as a heavy hero 3D hardbound book landing with an impact burst (`speedLinesRadial` + 12 sparks). A heavy `book_slam()` is acoustically appropriate.
   - At 23.36s, the visual transitions to an open spread ("Is wonderful book mein..."). Reusing `book_slam()` is redundant. Replacing it with `book_open()` / `page_turn()` (`sfx.paper('flip', dur=0.28)` layered with a subtle wooden tap) provides distinct tactile foley.
   - The 4.25s+ silence warning in `mgaudio` occurs because no kinetic feedback bridges the 3.12s–8.16s and 8.16s–14.18s sections. Adding a rising tension whoosh (`sfx.riser('sweep')`) at 6.80s matches the alert burst in `scene.js`, and adding a clockwork tick at 11.20s mirrors the psychology gears rotating.
4. **Analysis of Principle Badges Alignment**:
   - `scene.js` lines 366–381 explicitly pop three badges using `E.outBack`:
     - 24.2s: "1. NO ARGUMENT"
     - 26.2s: "2. NO CRITICISM"
     - 28.2s: "3. INSPIRE OTHERS"
   - In `audio.py`, these badges lack synchronous hits. Placing `sfx.sticker_slap()` or tactile wood clicks at 24.2s and 26.2s, followed by a bright celebration chime at 28.2s, locks the audio to the native visual animation.

---

## 3. Caveats

1. **MP3 Container vs. PCM WAV Duration**: If cutting the MP3 as a standalone file using `-c copy`, the duration will be `30.027755` seconds due to MP3 packet size constraints. The production pipeline must use the PCM WAV export (`-t 30 -ar 48000 -ac 2 out/audio.wav`), which is mathematically guaranteed to be exactly 30.000000 seconds.
2. **Mixing Gain & Peak Ceilings**: In `audio.py`, mixing the TTS voiceover with loud procedural SFX must keep peaks below 0 dBFS to prevent digital clipping. The existing volume weights (`[0:a]volume=1.0`, `[1:a]volume=0.9`, combined `volume=1.1`) reach True Peak around -1.22 dBTP, which is within the broadcast standard (<= -1.0 dBTP).
3. **No External Sourcing Required**: All required sound effects (book slam, siren, gunshot, page turn, badge slaps, chimes) can be procedurally generated via `mgaudio.sfx` and `numpy`. No external web assets or third-party downloads are needed.

---

## 4. Conclusion

1. **Requirement R1 is fully solvable**: The source TTS at `C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3` is healthy and cleanly cuts to 30.00s using the verified WinGet FFmpeg command.
2. **Requirement R3 recommendations**:
   - Delete the duplicate `book_slam()` at 23.36s and replace it with a unique `page_turn_spread()`.
   - Eliminate the 4.25s silence gap by adding a tension riser at 6.80s (synced with the question alert burst) and a gear tick at 11.20s.
   - Sync tactile badge hits at 24.2s, 26.2s, and 28.2s to match the `scene.js` `E.outBack` badge animations.
3. **Complete 30-Second Unique Kinetic Cue Sheet**:

| Timestamp (s) | Frame (24 fps) | Spoken Narration (`cues.js`) | Visual Cue (`scene.js`) | Sound Effect / Generator Recipe | Acoustic Character |
|---|---|---|---|---|---|
| **0.05** | f1 | "کیا آپ نے" | Intro pencil slate / frame setup | `sfx.paper('slide', dur=0.35)` | Crisp paper slide |
| **1.08** | f26 | "Notice kiya?" | Idea bulb appears & turns on | `sfx.pop('cork', pitch=1.1)` | Inquisitive tactile pop |
| **3.12** | f75 | "Trust aur Respect" | Lightbulb filament glows & rays expand | `sfx.ding(note=72)` | Warm melodic chime (C5) |
| **6.80** | f163 | "Aakhir..." | Radial speed lines alert burst | `sfx.riser(dur=1.35, kind='sweep')` | Rising tension sweep |
| **8.16** | f196 | "difference kya hai?" | Act 2 Gear transition (Red & Yellow) | `police_siren(dur=1.4)` | FM Siren frequency sweep |
| **11.20** | f269 | "atchi communication skills" | Interlocking gear rotation | `sfx.tick('hi')` + `sfx.click('wood')` | Mechanical gear tooth tick |
| **14.18** | f340 | "deeper science hai" | Central thought sparkle atom lights up | `sfx.blip(note=67)` | Clean tonal bell (G4) |
| **16.04** | f385 | "Dale Carnegie ki book" | Hero 3D Book slam & impact burst | `book_slam()` (`paper('flip')` + `impact('punch')` + `boom(0.8, 48)`) | Heavy cinematic hero thud |
| **19.34** | f464 | "manipulate karna nahi" | Warning accent / dancing flame entrance | `gunshot(dur=0.7)` (`punch` + `cork` + `boom`) | Sharp transient gunshot crack |
| **21.86** | f525 | "better relationships" | Floating celebration hearts & twinkles | `sfx.sparkle(dur=0.55)` | Shimmering magic sparkle |
| **23.36** | f561 | "Is wonderful book mein" | Act 4 Open Book Spread transition | `page_turn_spread()` (`paper('flip', 0.28)` + `paper('rustle', 0.3)`) | Tactile parchment page turn |
| **24.20** | f581 | "bina argument ke" | Badge 1: '1. NO ARGUMENT' pops in | `sfx.sticker_slap(seed=11)` | Crisp slapstick hit |
| **25.00** | f600 | "apne baat kaise rakhein" | Swift directional gesture | `sfx.whoosh(0.35, 'heavy')` | Low-end air pass-by |
| **26.20** | f629 | "criticism..." | Badge 2: '2. NO CRITICISM' pops in | `sfx.sticker_slap(seed=22)` | Punchy tactile slap |
| **28.20** | f677 | "dusron ko improve..." | Badge 3: '3. INSPIRE OTHERS' hero pop | `sfx.shimmer_hit(dur=0.6)` | Uplifting metallic hit |
| **28.74** | f690 | "inspire karna" | Hero star flourishes & twinkles | `sfx.ding(note=79)` | High bell chime (G5) |

---

## 5. Verification Method

### 5.1 Independent TTS Trimming Test
Run the exact Gyan WinGet FFmpeg command to verify that the trimmed output is generated and matches 30 seconds:
```powershell
& "C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe" -y -t 30 -i "C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3" -ar 48000 -ac 2 "C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\out\test_tts_30s.wav"
```
Check duration using ffprobe:
```powershell
& "C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffprobe.exe" -v error -show_entries format=duration "C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\out\test_tts_30s.wav"
```
*Expected Result*: `duration=30.000000`.

### 5.2 Audio Mix Execution Verification
From `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary`, run:
```powershell
python audio.py
```
*Expected Result*:
- Zero unhandled exceptions.
- Generation of `out/sfx.wav` and `out/audio.wav`.
- Duration confirmed at 30.000000s.

### 5.3 Invalidation Conditions
- If the source MP3 file at `C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3` is moved or deleted.
- If FFmpeg produces an output duration other than 30.00s.
- If `audio.py` introduces a repeating looping loop timer (`for t in range(...)`) rather than explicit kinetic timestamp mappings.
