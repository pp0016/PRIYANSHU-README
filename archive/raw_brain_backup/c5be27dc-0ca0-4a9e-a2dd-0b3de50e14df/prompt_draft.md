# Teamwork Project Prompt

> Status: Launched
> Goal: Execute pipeline to cut videos and generate Groq Whisper subtitles

Write a Python script that uses FFmpeg to automatically cut 7 specific video clips based on provided timestamps, generates fast-paced SRT subtitle files (maximum 3 words per line) using the Groq Whisper API, and delivers the final cut videos alongside their SRT files.

Working directory: `C:\Users\renu5\Downloads\cliping first video\viral_pipeline`
Integrity mode: development

## Requirements

### R1. Video Clipping
The script must take a list of 7 timestamps (start and end) and an input video file, and use FFmpeg to extract these segments into individual MP4 files.

### R2. Subtitle Generation via Groq API
The script must generate transcripts for each of the 7 clips exclusively using the **Groq Whisper API** (cloud-based, not local). The script should extract the audio from the clips, send it to the Groq API, and retrieve the word-level timestamp data. The Groq API key is located in the environment (e.g., `.env` file).

### R3. Fast-Paced Subtitle Formatting
The script must process the word-level transcript data from Groq and output standard SRT files where **no single subtitle block contains more than 3 words**. The timing of each block must be accurately mapped to those specific words.

### R4. Final Output
The script must output both the 7 clipped `.mp4` video files and the 7 corresponding formatted `.srt` files into an easily accessible output folder.

## Acceptance Criteria

### Video Extraction
- [ ] Running the script successfully outputs 7 distinct `.mp4` video files.
- [ ] The duration of each output video file matches the calculated duration from the provided timestamps (± 1 second).

### Subtitle Formatting
- [ ] Running the script successfully outputs 7 distinct `.srt` files (one for each clip).
- [ ] A programmatic check of the generated `.srt` files confirms that 0% of the subtitle blocks contain more than 3 words.
- [ ] The timestamps in the SRT files align chronologically and do not overlap.
