# Overnight Video Compression Plan

The goal is to deeply compress all video files in your `Camera imports` folder while retaining almost identical visual quality, following the exact `video-compressor` skill guidelines.

## Current State
* **Source Folder:** `C:\Users\renu5\OneDrive\Pictures\Camera imports`
* **Total Videos Found:** 185 files (`.mp4`, `.mov`, etc.)
* **Total Starting Size:** ~5.36 GB

## User Review Required

> [!IMPORTANT]
> Since this is a long-running overnight `/goal`, please review this plan and click **Proceed** if you are ready for me to begin. Once started, I will not stop until every single video is compressed.

## Proposed Changes

I will execute a PowerShell script that does the following:

1. Create a brand new destination folder: `C:\Users\renu5\OneDrive\Pictures\Camera imports compressed`
2. Mirror your exact folder structure inside this new directory so everything stays perfectly organized.
3. Compress every single video using FFmpeg with the precise skill settings:
   * **Codec:** H.264 (`libx264`) for universal Windows compatibility (avoids the `0xc00d5212` missing codec error).
   * **Compression:** `-crf 28` (Standard ~15% visual quality drop, huge file size reduction).
   * **Speed:** `-preset fast`
   * **Audio:** AAC at 128k bitrate.
4. Safely skip any non-video files (photos will remain untouched in the original folder).
5. At the very end, I will calculate and report the exact amount of storage space saved.

### [Data Safety]
Your original videos will **NOT** be deleted or modified. The compressed versions will be created in the brand new folder.

## Verification Plan

### Automated Checks
* The script will verify that `ffmpeg` successfully produces an output file for each input video.
* Once the script finishes, I will automatically calculate the total file size of the new directory and compare it against the original 5.36 GB to determine the final compression ratio.
