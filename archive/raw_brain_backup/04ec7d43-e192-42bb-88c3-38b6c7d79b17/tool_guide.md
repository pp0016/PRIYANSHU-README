# Execution Tools — Honest Reference Guide for Long-Form YouTube Creators

> [!IMPORTANT]
> This document covers **where each tool lives, what it actually does, where it breaks, and how you use it** as a long-form content creator. No marketing language. Where a tool is overrated or redundant, that's stated plainly.

---

## 1. Groq API

| Detail | Answer |
|---|---|
| **What** | Cloud-hosted LLM inference on custom LPU chips. Runs open-source models (Llama 3.x, Mixtral, Gemma, Whisper) at 500–1,000+ tokens/second. |
| **Where to get it** | [console.groq.com](https://console.groq.com) → sign up → generate API key (`gsk_...`) |
| **It is NOT** | A desktop app. You cannot "open Groq." It is a developer API you connect to from Python scripts, n8n, Make.com, or TypingMind. |
| **Pricing** | Free tier with daily rate limits. Pay-as-you-go: Llama 3.1 8B ~$0.05/1M input tokens. Llama 3.3 70B ~$0.59/1M input. Whisper ~$0.04–$0.11/hour of audio. |

**How you actually use it as a creator:**
1. Feed a video transcript to Llama 3.3 70B → get 5 Short/Reel scripts, chapter timestamps, newsletter summary, and social posts in 2–3 seconds.
2. Bulk-process 50 video transcripts to find content gaps across your channel history in under a minute.
3. Rapid script iteration — rewrite hooks, intros, CTAs at high speed without waiting 10–30s per response like slower APIs.

**Real limitations:**
- No GPT-4o, Claude, or Gemini Pro — only open-weight models.
- Strict rate limits (TPM/RPM) on free tier. Multi-agent workflows hit walls fast.
- Max output ~8K tokens per request.
- Requires a frontend/glue layer — non-coders need n8n or Make.com to use it.

---

## 2. Groq Whisper

| Detail | Answer |
|---|---|
| **What** | Cloud API for speech-to-text running `whisper-large-v3` on Groq LPUs |
| **Where is it downloaded?** | **It is NOT downloaded.** It is a cloud API at `api.groq.com/openai/v1/audio/transcriptions`. You access it via `pip install groq` in Python or HTTP requests. |
| **Speed** | ~200x real-time. A 1-hour audio file transcribes in **3–5 seconds**. Local Whisper on RTX 4090 takes 30s–2min; on CPU, 10+ minutes. |
| **Quality** | Identical to OpenAI Whisper large-v3 (same weights). 95%+ accuracy for English. |
| **File limit** | 25 MB per request. Compress audio to FLAC/MP3 mono or chunk with `ffmpeg` before uploading. |

**Where to "organize" it:**
There is nothing to organize on disk. Your Groq API key (`gsk_...`) is the only thing you store. Put it in a `.env` file or your secrets manager. The Python package (`groq`) is installed in your virtual environment via pip. That's it.

**Honest comparison to local Whisper:**
- Groq Whisper: fast, zero GPU needed, costs money, uploads audio to US servers, 25MB file cap.
- Local Whisper (`faster-whisper`): free, fully offline/private, needs 6–10GB VRAM, no file size cap, slower.
- Both hallucinate repeated phrases ("Thank you for watching") during silence. Use VAD trimming before uploading.

---

## 3. Python

**Python is the glue that connects everything in your workflow.** Here is where it fits in each production stage:

| Stage | What Python Does | Libraries |
|---|---|---|
| **Research & scraping** | Pull competitor video titles, transcripts, metadata | `yt-dlp`, `youtube-transcript-api`, `google-api-python-client` |
| **Scripting & AI** | Generate script structures, estimate spoken length, run through LLMs | `google-genai`, `openai`, `groq` |
| **Audio processing** | Local speech-to-text, subtitle SRT generation, audio normalization to -14 LUFS | `faster-whisper`, `pydub`, `soundfile` |
| **Video editing automation** | Silence removal, rough cuts, code animations | `ffmpeg-python`, `MoviePy`, `Manim` |
| **Thumbnail creation** | Frame extraction, background removal, text overlay compositing | `opencv-python`, `rembg`, `Pillow` |
| **Publishing** | Batch video upload, thumbnail assignment, chapter formatting via YouTube Data API | `google-api-python-client` |
| **Repurposing (Shorts)** | Auto-crop 16:9 → 9:16 with face tracking, burn animated captions | `mediapipe`, `MoviePy`, `opencv-python` |
| **Analytics** | Custom retention curves, RPM trackers, subscriber models | `pandas`, `plotly`, `matplotlib` |

> [!WARNING]
> You have scripts scattered across multiple workflow folders. The risk: you forget which script does what, dependencies rot, and nothing runs 6 months later. Consider consolidating your Python tools into a single repo with a `requirements.txt` and clear folder structure.

---

## 4. Mixkit (mixkit.co)

| Detail | Answer |
|---|---|
| **What** | Curated stock video, music, SFX, and video templates. Owned by Envato. |
| **Actually free?** | Yes — all assets on Mixkit itself are free. No account needed. But search results promote paid Envato Elements items (upsell funnel). |
| **License for YouTube** | Commercial use allowed on monetized videos. No attribution required. Cannot resell raw tracks. |
| **Content ID risk** | Occasional false-positive Content ID claims if a third party improperly registers a Mixkit track. Keep download receipts. |

**vs. Pixabay/Pexels:** Mixkit has a smaller, tighter catalog with higher average quality (better color grading, video-first composition). Pexels/Pixabay have massive catalogs but wildly inconsistent quality. Mixkit's unique advantage: **video editing templates** for Premiere/DaVinci/After Effects that Pexels and Pixabay don't offer.

---

## 5. Supadata (supadata.ai)

| Detail | Answer |
|---|---|
| **What** | REST API for scraping transcripts and metadata from YouTube, TikTok, Instagram, X. |
| **Why it exists** | `youtube-transcript-api` fails on cloud servers because YouTube blocks data center IPs. Supadata handles proxy rotation and CAPTCHAs server-side. |
| **Key feature** | If a video has NO captions, Supadata auto-routes audio through Whisper to generate a transcript anyway. |
| **It is NOT** | A browser extension or YouTube sidebar plugin. It is an API (`api.supadata.ai/v1`) + MCP server + n8n/Make integrations. |
| **Pricing** | Free: 100 requests/month. Paid: ~$10/month or ~$0.99/1,000 requests. |

**When to use it vs. `youtube-transcript-api`:** Use `youtube-transcript-api` for local scripts on your own machine. Use Supadata when deploying to cloud, when you need transcripts from videos with no captions, or when you need reliability at scale.

---

## 6. TubeBuddy

| Detail | Answer |
|---|---|
| **What** | Chrome extension that adds SEO tools, tag analysis, bulk processing, and thumbnail A/B testing to YouTube Studio. |
| **Free tier** | Basically a demo. Keyword Explorer capped at 3 results, tag suggestions capped at 3, A/B testing locked, bulk tools locked. |
| **Paid** | Pro $3–9/mo, Star/Legend $20–50+/mo. |

**What it does that YouTube Studio doesn't:**
1. Bulk-update descriptions, affiliate links, cards, and end screens across hundreds of videos.
2. Show competitor video tags on watch pages.
3. Keyword search volume/competition scores.

**Honest problems:**
- **Tags are mostly irrelevant now.** YouTube's own docs say tags play a minimal role in discovery. TubeBuddy's heavy tag optimization push is outdated.
- **Browser lag.** It injects UI elements into YouTube Studio and slows Chrome down.
- **Aggressive upsell popups.** Constant nudges to upgrade tiers.
- **Increasing redundancy.** YouTube Studio now has native search insights, analytics improvements, and thumbnail A/B testing ("Test & Compare"), which was TubeBuddy's main differentiator.

> [!NOTE]
> The one thing TubeBuddy still does well that nothing else replicates easily: **bulk catalog management** (mass-editing descriptions, swapping links across 200+ videos). If you don't need that, vidIQ or free YouTube Studio features cover the rest.

---

## 7. Unminus (unminus.com)

| Detail | Answer |
|---|---|
| **What** | Free royalty-free music platform ("Unsplash for Music"). Independent project by musician Wowa. |
| **Still active?** | Yes — overhauled to Unminus v2 with redesigned frontend and B2B API. |
| **License** | CC0-style: free for commercial and non-commercial use, no attribution required. |
| **Catalog size** | Small — hundreds of tracks (mostly lo-fi, chill, electronic, ambient). |

**vs. Epidemic Sound / Artlist:** Unminus cannot compete. Epidemic/Artlist have 40,000+ tracks, stems (separated vocal/drum/bass), AI matching, and direct YouTube Content ID whitelisting. Unminus tracks occasionally get flagged by YouTube's algorithm and require manual dispute.

**When Unminus makes sense:** Zero-budget projects, quick background music for drafts/internal videos, or when you specifically want that indie lo-fi aesthetic and don't want to pay $15/mo for Epidemic.

---

## 8. YouTube Analytics MCP

| Detail | Answer |
|---|---|
| **What** | A Model Context Protocol server that connects AI agents (Antigravity, Claude Code, Cursor) directly to YouTube Analytics API and YouTube Data API v3. |
| **What it exposes** | Views, watch time, CTR, impressions, revenue (RPM/CPM), subscriber gain/loss, traffic sources, device types, audience demographics, retention data — all queryable by your AI agent via natural language. |

**Setup (5 steps):**
1. Create a Google Cloud Project at [console.cloud.google.com](https://console.cloud.google.com)
2. Enable YouTube Data API v3 + YouTube Analytics API
3. Create OAuth 2.0 credentials (Desktop App) → download `client_secret.json`
4. Run the MCP server locally once → authenticate via browser → generates `token.json`
5. Register in Antigravity's `mcp_config.json`:
```json
{
  "mcpServers": {
    "youtube-analytics": {
      "command": "python",
      "args": ["-m", "youtube_studio_mcp"],
      "env": {
        "YOUTUBE_CLIENT_SECRET_FILE": "C:/path/to/client_secret.json",
        "YOUTUBE_CHANNEL_ID": "UCxxxxxxxxxxxxxxxxxxxxxx"
      }
    }
  }
}
```

**Real use cases in Antigravity:**
- "Check my video performance over the last 14 days. Flag any video where CTR is below 4.5%."
- "Compare CTR before and after I changed the thumbnail on video XYZ 48 hours ago."
- "Look at retention curves of my last 3 tutorials and tell me where viewers drop off."

**Notable implementations on GitHub:**
- `pauling-ai/youtube-mcp-server` — ~40 tools, Python/FastMCP, covers analytics + publishing + transcripts.
- `i1s-abhishek/youtube-studio-mcp` — installable via `pip install youtube-studio-mcp`, includes video metadata editing + comment management.

---

## 9. youtube-transcript-api (Python)

| Detail | Answer |
|---|---|
| **What** | Unofficial Python library that extracts captions/transcripts from YouTube videos without an API key. |
| **Install** | `pip install youtube-transcript-api` |
| **CLI** | `youtube_transcript_api <video_id>` |

```python
from youtube_transcript_api import YouTubeTranscriptApi
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
```

**When it fails (and it will):**
1. **Cloud IP blocking** — YouTube blocks AWS/GCP/Azure/Hetzner IPs. Works fine locally, breaks on servers.
2. **Rate limiting (429)** — Rapid sequential requests get throttled. Need `time.sleep()` or proxy rotation.
3. **Auto-generated captions** lack punctuation, have phonetic misspellings, no speaker diarization.
4. **Disabled captions** — if the uploader turned off captions, there's nothing to fetch.
5. **Age-restricted videos** — requires exporting browser cookies, which is fragile.

**When to use it:** Local scripts for pulling transcripts of your own or competitor videos. For production/cloud deployment, use Supadata instead.

---

## 10. yt-dlp

| Detail | Answer |
|---|---|
| **What** | The leading open-source CLI video/audio downloader. Active fork of `youtube-dl` with speed fixes, multi-threading, SponsorBlock integration. |
| **Install on Windows** | `winget install yt-dlp` (recommended) or `pip install yt-dlp` or download `yt-dlp.exe` from GitHub Releases. |
| **Prerequisite** | Install `ffmpeg` (`winget install Gyan.FFmpeg`) so yt-dlp can merge video+audio streams into single MP4 files. |

**Legal situation:**
- The software itself is legal (confirmed by EFF after 2020 DMCA battle).
- Using it violates YouTube's Terms of Service (Section 5) — civil breach, not criminal.
- Downloading copyrighted content for re-upload is infringement. Downloading for fair use (commentary, criticism, education) is legally protected, but Content ID will still flag re-used clips.

**Your actual use cases as a creator:**
- Backup your own uploaded channel catalog locally.
- Grab competitor videos for offline research and transcript extraction.
- Extract clean audio streams → feed to Whisper for transcription.
- Download reference footage for video essays.

---

## 11. spy_competitor.py

| Detail | Answer |
|---|---|
| **What** | **Not a standard open-source tool.** It is a custom Python script name commonly used for ad-hoc YouTube competitor analysis. |
| **Where is it?** | It exists in your `"Stickman Studio - Copy Before doing any change by Rook"` workflow folder. It is YOUR script (or a script from the Rook project). |
| **Do not confuse with** | `py-spy` (a Python profiler — completely unrelated). |

**What such a script typically does:**
1. Takes competitor channel URLs/IDs
2. Fetches subscriber count, video count, total views, upload frequency via YouTube Data API
3. Calculates "outlier" videos (3x–10x above channel average)
4. Extracts titles, tags, descriptions for keyword/topic gap analysis
5. Exports to CSV or Pandas dataframe

> [!TIP]
> Since this is a custom script, check whether it still runs. Dependencies may have rotted. Open it, read the imports, verify the API keys it needs are still valid.

---

## 12. Spotter Studio

| Detail | Answer |
|---|---|
| **What** | AI-powered pre-production and ideation suite by Spotter (backed by MrBeast, Dude Perfect, Colin & Samir). |
| **Price** | $49/month or $299/year. |
| **How it differs from vidIQ/TubeBuddy** | vidIQ = SEO and keyword research (post-idea validation). TubeBuddy = workflow automation and bulk edits (in-studio logistics). Spotter Studio = **creative ideation before filming** — analyzes your channel history to find outlier patterns and generates video concepts, titles, thumbnail ideas, and hooks. |

**When it's useful:** You have an established channel, you're stuck on what to make next, and you want data-driven concept generation based on what already worked for you.

**When it's NOT useful:** New channels with no video history (it needs data to analyze). If you already know what to make and just need SEO optimization, vidIQ does that cheaper.

**Real complaints:** $49/mo is steep for smaller creators. Lacks post-upload SEO/analytics. Requires an established public catalog to function.

---

## Quick-Reference: Where Everything Lives

| Tool | Type | Location / Access |
|---|---|---|
| Groq API | Cloud API | [console.groq.com](https://console.groq.com) — API key in `.env` file |
| Groq Whisper | Cloud API (NOT a download) | Same Groq API key, endpoint `api.groq.com/openai/v1/audio/transcriptions` |
| Python | Local runtime | Installed on your machine, scripts in your project folders |
| Mixkit | Website | [mixkit.co](https://mixkit.co) — download assets directly |
| Supadata | Cloud API | [supadata.ai](https://supadata.ai) — API key |
| TubeBuddy | Chrome extension | [tubebuddy.com](https://tubebuddy.com) — install in Chrome |
| Unminus | Website | [unminus.com](https://unminus.com) — download MP3/WAV |
| YouTube Analytics MCP | Local MCP server | Python package + OAuth setup (see Section 8 above) |
| youtube-transcript-api | Python package | `pip install youtube-transcript-api` |
| yt-dlp | CLI tool | `winget install yt-dlp` or `pip install yt-dlp` |
| spy_competitor.py | Custom script | In your Stickman Studio workflow folder |
| Spotter Studio | Web app | [spotter.com](https://spotter.com) — $49/mo subscription |
