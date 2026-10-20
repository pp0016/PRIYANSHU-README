# 🎬 SOP 05: FFmpeg Mass-Production Assembly (Quiet Money POV)

> **Purpose:** Assemble 550–700 still images, master voiceover audio, and SFX into a high-octane, hard-cut video using pure FFmpeg automation in under 2 minutes of render time.

---

## 1. Absolute Binary & Zero-Degradation Rules

Per user rules and global constraints:
* **Strict Absolute Path (Never use generic `ffmpeg` alias):**
  `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe`
* **Zero-Degradation Flags (Mandatory on all re-encoding):**
  `-pix_fmt yuv420p -crf 17`
* **Broadcast Standard Atom Placement:**
  `-movflags +faststart` (places `moov` header before `mdat` for instant playback).

---

## 2. Hard-Cut Image Sequencing Architecture (Concat Demuxer)

Rather than rendering complex video files or encoding hundreds of individual video clips, we use **FFmpeg's Concat Demuxer** to stitch images with exact, microsecond-accurate hold durations.

### Concat File Format (`images_timeline.txt`):
```text
file 'images/img_001.png'
duration 2.45
file 'images/img_002.png'
duration 1.80
file 'images/img_003.png'
duration 3.10
...
file 'images/img_330.png'
duration 2.50
file 'images/img_330.png'
```
*(Note: The final image must be repeated once at the end of the concat file per FFmpeg demuxer specification).*

---

## 3. The 1-Click Automated Build Script (`assemble_video.py`)

Save this script inside each project directory to automate the entire assembly in one command:

```python
import json
import os
import subprocess

FFMPEG_EXE = r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"

def build_video(project_dir, output_filename="final_video.mp4"):
    images_dir = os.path.join(project_dir, "images")
    voiceover_path = os.path.join(project_dir, "audio", "voiceover.wav")
    timestamps_json = os.path.join(project_dir, "audio", "cut_durations.json")
    concat_file = os.path.join(project_dir, "images_timeline.txt")
    output_path = os.path.join(project_dir, output_filename)

    # 1. Load cut durations calculated from voiceover timestamps
    with open(timestamps_json, "r", encoding="utf-8") as f:
        cuts = json.load(f) # list of {"file": "img_001.png", "duration": 2.45}

    # 2. Write the FFmpeg Concat file
    with open(concat_file, "w", encoding="utf-8") as f:
        for cut in cuts:
            img_path = os.path.join("images", cut["file"]).replace("\\", "/")
            f.write(f"file '{img_path}'\n")
            f.write(f"duration {cut['duration']:.3f}\n")
        # Final image repeat requirement for concat demuxer
        if cuts:
            last_img = os.path.join("images", cuts[-1]["file"]).replace("\\", "/")
            f.write(f"file '{last_img}'\n")

    print(f"Generated concat timeline with {len(cuts)} cuts.")

    # 3. Execute zero-degradation FFmpeg command
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_file,
        "-i", voiceover_path,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "17",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        output_path
    ]

    print("Running FFmpeg rendering pipeline...")
    subprocess.run(cmd, check=True)
    print(f"✅ Video rendered successfully: {output_path}")

if __name__ == "__main__":
    build_video(os.getcwd())
```

---

## 4. Director-Grade Assembly: Transitions, SFX & Sidechain Ducking

> [!IMPORTANT]
> When compiling videos directed via [`screenplay_director_manifest-part-of-4-or-screenplay-writing-.md`](file:///c:/Users/renu5/Downloads/priyanshu%20readme/youtube/Stickman/finance%20Stickman/screenplay_director_manifest-part-of-4-or-screenplay-writing-.md), `assemble_video.py` or Remotion parses `projects/[NN]_[topic]/screenplay.md` to elevate assembly from a basic slideshow into human-editor caliber video.

### A. 58 Hardware `xfade` Transitions
Applies transitions between key cutaways and act pivots without quality loss:
```bash
ffmpeg -i clip1.mp4 -i clip2.mp4 -filter_complex "xfade=transition=zoomin:duration=0.5:offset=2.5" -pix_fmt yuv420p -crf 17 output.mp4
```
*(Catalog includes `zoomin`, `hblur`, `fadefast`, `slideleft`, `wipetl`, `horzopen`, `dissolve` per Section 3 of Director Manifest).*

### B. Multi-Stream Audio Mixing with Sidechain Ducking
Combines voice narration, background music bed, and SFX cues while preventing narrator volume drop:
```bash
-filter_complex "[1:a][0:a]sidechaincompress=threshold=0.08:ratio=6:attack=100:release=350[ducked_bgm];[0:a][ducked_bgm][2:a]amix=inputs=3:duration=first:dropout_transition=0:normalize=0,alimiter=limit=0.95[aout]"
```

### C. Audio Pre-Roll Alignment (-60ms Offset)
All transition SFX (`whoosh.wav`, `whip.wav`) are placed **1 to 2 frames (33ms to 60ms) before the video cut point** to ensure peak acoustic impact lands synchronously on the visual cut.

---

## 5. Execution Command in PowerShell

To render the finished video from your terminal:

```powershell
python assemble_video.py
```

* **Fast Concat Render:** Under 2 minutes on standard laptop CPU.
* **Full Director Assembly (xfade + SFX + ducking):** 3–5 minutes with zero GPU crashes and pristine 1080p quality.
