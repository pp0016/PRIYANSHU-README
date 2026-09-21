Title: Live Content

Description: Fetched live

Source: https://raw.githubusercontent.com/sudoax0n/gemini-watch/main/README.md

---

<p align="center">
  <img src="public/assets/banner.png" width="100%" alt="Gemini Watch Banner" />
</p>

# Gemini Watch 👁️

**Gemini Watch** is a native, multimodal extension for the [Gemini CLI](https://github.com/google-gemini/gemini-cli) that gives the agent "eyes" to watch videos from YouTube, Vimeo, TikTok, or local files.

Instead of relying on heavy MCP servers or complex setups, `gemini-watch` provides a highly optimized pipeline that downloads videos with `yt-dlp`, extracts frames with `ffmpeg`, and transcribes audio natively using Gemini's multimodal capabilities. The Gemini CLI then natively loads these visual and audio cues directly into its multimodal context window to answer any question about the video.

## ✨ Features
* **Multimodal Visual & Audio Inputs:** Automatically extracts auto-scaled video frames and native audio tracks. It uses the CLI's `read_file` tool to feed both visuals and audio into Gemini's massive multimodal context window.
* **Multi-Platform Support:** Works flawlessly with YouTube, Vimeo, TikTok, Twitter/X, Twitch, and most `yt-dlp` compatible websites, as well as local video files (`.mp4`, `.mov`, `.mkv`, etc.).
* **Smart Native Fallback:** Automatically pulls native or auto-generated captions first. If unavailable, it extracts the audio track for Gemini to "hear" and transcribe natively—**no external API keys (Whisper/Groq) required.**
* **Denser Focused Zoom:** Supports focusing on specific timestamps (e.g. `--start 01:00 --end 01:30`) to extract frames at a higher density for detailed analysis of brief moments.
* **Pure Python Standard Library:** Requires **zero** external Python packages (no pip installs needed outside standard tools).
* **Setup Wizard:** Includes a built-in preflight checker (`setup.py`) to detect missing binaries in one command.

## 🛠️ Prerequisites

To use this extension, you must have **Python 3**, **FFmpeg**, and **yt-dlp** installed on your system.

### Install Dependencies:
* **macOS:**
  ```bash
  brew install ffmpeg yt-dlp
  ```
* **Windows (via Winget):**
  ```bash
  winget install Gyan.FFmpeg
  winget install yt-dlp.yt-dlp
  ```
* **Linux:**
  ```bash
  sudo apt install ffmpeg
  ```
  (And install `yt-dlp` via your package manager or pipx)

## 📦 Installati

