# Takeout Video Compression — Full Context & Prompt

## How the Plan Evolved

### Original Idea
- Compress ALL videos AND images from Google Takeout (22.63 GB)
- Create a separate `Takeout C` folder with mirrored structure
- Target 80%+ compression on everything
- Use subagents for parallel processing

### What Changed & Why

| Decision | Original | Changed To | Reason |
|---|---|---|---|
| **Images** | Compress all 17,099 images | ❌ **Dropped entirely** | Already JPEG-compressed. Only 20-35% savings realistic. Not worth it. |
| **Output location** | Separate `Takeout C` folder | ✅ **Same folder, " C" suffix** | Simpler. No folder duplication. Compress in-place. |
| **Which videos** | All 689 videos | ✅ **Only ≥20 MB (171 files)** | 171 files = 77.2% of video storage. The other 518 tiny clips = only 2.6 GB, not worth CPU time. |
| **Cleanup** | Keep originals forever | ✅ **Delete list → batch delete at end** | Compressed file replaces original. Log originals for bulk delete after review. |
| **Subagents** | 10-20 subagents | ✅ **Single script** | One script = one approval click. Subagents = many approval clicks. Script is better. |
| **Permissions** | Approve every command | ✅ **Open Takeout as workspace** | Opening the folder as a project/workspace eliminates folder access permission popups. |

### Final Numbers

| What | Count | Size | Action |
|---|---|---|---|
| Videos ≥ 20 MB | 171 files | 10.3 GB (77.2%) | ✅ Compress with FFmpeg |
| Videos < 20 MB | 518 files | 2.6 GB (22.8%) | ❌ Skip |
| Images | 17,099 files | 9.6 GB | ❌ Skip |
| JSON metadata | 17,793 files | 12.6 MB | ❌ Skip |
| **Expected result** | 171 compressed | ~2-3 GB saved space | ~7-8 GB freed |

---

## Step-by-Step: What To Do

### Step 1: Open Takeout as Workspace
1. In Antigravity IDE, press `Ctrl+K Ctrl+O` (or **File → Open Folder**)
2. Navigate to `C:\Users\renu5\Downloads\Takeout`
3. Select it and open
4. This makes Takeout your workspace — no more folder permission popups

### Step 2: Start a New Conversation
1. Open a new chat in Antigravity
2. Paste the prompt below (Section: **THE PROMPT**)
3. Hit send

### Step 3: Approve Once
- The agent will write a single `.ps1` script and ask to run it
- Click **Allow** once
- It runs in the background, compresses all 171 videos

### Step 4: Review & Delete Originals
- When done, the agent will show you the results (before/after sizes)
- It will show the delete list
- You approve one delete command to remove the originals

---

## THE PROMPT

Copy everything below this line and paste it into the new conversation:

---

```
Read the video-compressor skill at C:\Users\renu5\.gemini\config\skills\video-compressor\SKILL.md first.

I have a Google Takeout backup at the current workspace folder. It's 22.63 GB total but I only want to compress VIDEOS. No images, no JSON metadata, nothing else.

Here's the exact plan — follow it precisely:

**WHAT TO COMPRESS:**
- Only .mp4 files that are 20 MB or larger
- There are approximately 171 such files totaling ~10.3 GB
- SKIP all videos under 20 MB (not worth the CPU time)
- SKIP all images, JSON files, and everything else

**FFmpeg SETTINGS (mandatory, no exceptions):**
- Codec: H.264 (libx264) — do NOT use H.265/HEVC
- Quality: CRF 28
- Preset: fast
- Audio: AAC at 128k bitrate
- Command pattern: ffmpeg -y -i "input.mp4" -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 128k "output.mp4"

**FILE NAMING & LOCATION:**
- Save compressed video in the SAME folder as the original
- Naming: add " C" before the extension. Example: VID20251210165836.mp4 → VID20251210165836 C.mp4
- Do NOT create a separate output folder

**WORKFLOW:**
1. Write a SINGLE PowerShell script (.ps1 file) that does EVERYTHING — do not run individual FFmpeg commands
2. The script must:
   a. Recursively find all .mp4 files ≥ 20 MB in the Takeout folder
   b. Skip any file that already has " C" in the name (already compressed / avoid re-processing)
   c. Skip if the compressed version already exists (resume capability)
   d. Compress each video with the FFmpeg settings above
   e. After each successful compression, log the ORIGINAL file's full path to a file called "delete_list.txt" in the Takeout root folder
   f. Also log: original size, compressed size, and percentage saved — both to console and to a "compression_log.txt" file
   g. At the end, print a summary: total files processed, total original size, total compressed size, total percentage saved
3. Run the script as a single command (one approval from me)
4. After the script finishes, show me the summary results
5. Do NOT delete any original files automatically — just build the delete_list.txt. I will review and approve deletion separately.

**IMPORTANT RULES:**
- Do NOT ask me questions. Just build the script and run it.
- Do NOT process images. Videos only.
- Do NOT create subagents. One script, one run.
- If a video fails to compress, log the error and continue to the next video. Do not stop.
- Report file sizes in MB for individual files, GB for totals.

START IMMEDIATELY. Write the script and run it.
```

---

## What This Prompt Does

1. **Reads the skill** so the agent knows H.264/CRF 28 rules
2. **Gives exact specs** — no ambiguity, no questions, no back-and-forth
3. **Single script approach** — one approval click from you
4. **Resume-capable** — if interrupted, re-running skips already-compressed files
5. **Delete list** — originals tracked but NOT deleted until you say so
6. **Error handling** — failed videos get logged, script keeps going

After it finishes, you'll have:
- `compression_log.txt` — full report of every video (before/after sizes)
- `delete_list.txt` — list of originals safe to delete
- All compressed videos sitting next to their originals with " C" in the name
