# Priyanshu's YouTube Creator Toolkit

> Common execution tools extracted from all workflows. Organized by category.
> Each tool includes type, access location, and a short summary of how/where to use it.

---

## 🤖 AI Models & LLMs

| Tool | Type | Location / Access |
|---|---|---|
| Gemini (3.1 Pro, 3.5 Flash) | Cloud AI | [aistudio.google.com](https://aistudio.google.com) or Antigravity IDE — API key |
| Claude / Claude Opus | Cloud AI | [claude.ai](https://claude.ai) or Antigravity IDE — API key |
| ChatGPT | Cloud AI | [chatgpt.com](https://chatgpt.com) — browser or API |
| Groq API | Cloud API | [console.groq.com](https://console.groq.com) — API key (`gsk_...`) in `.env` file |
| Google Flow / Gemini Omni Flash | Cloud AI | [flow.google.com](https://flow.google.com) — browser-based video/image generation |

- **Gemini**: Primary AI for scripting, research, video analysis via `google-genai` API. Use Gemini 3.1 Pro for deep reasoning, 3.5 Flash for speed tasks.
- **Claude Opus**: Script chairman in multi-model council workflows. Strong at long-form narrative structure and critical editing.
- **ChatGPT**: Third voice in 3-model council research. Also used for quick ideation when other models are rate-limited.
- **Groq API**: Runs Llama 3.x at 500–1000 tokens/sec. Use for bulk transcript processing, rapid script rewrites, and batch content repurposing. Free tier has rate limits.
- **Google Flow**: Browser-based batch image/video generation using Omni Flash. Use for quick visual concept testing and B-roll clip generation.

---

## 🎙️ Transcription & Speech-to-Text

| Tool | Type | Location / Access |
|---|---|---|
| Groq Whisper | Cloud API (NOT a download) | Same Groq API key, endpoint `api.groq.com/openai/v1/audio/transcriptions` |
| WhisperX | Local Python tool | `pip install whisperx` — runs on your GPU |

- **Groq Whisper**: Transcribes 1-hour audio in 3–5 seconds via cloud. 25MB file upload limit — compress with `ffmpeg` first. Same `whisper-large-v3` model as OpenAI. Use when speed matters and you're online.
- **WhisperX**: Local GPU-based transcription with word-level timestamps and speaker diarization. Use when you need offline processing, no file size caps, or privacy. Slower but free after setup.

---

## 🎬 Video Generation & Editing

| Tool | Type | Location / Access |
|---|---|---|
| Google Veo 3.1 | Cloud AI | Google AI Studio or Google Flow — browser |
| Remotion / Remotion Studio | Local framework | `npm install remotion` — React-based video assembly |
| CapCut | Desktop app | [capcut.com](https://capcut.com) — download desktop version |
| FFMPEG | CLI tool | `winget install Gyan.FFmpeg` |
| ffprobe | CLI tool (bundled with FFmpeg) | Installed with FFmpeg |

- **Veo 3.1**: AI video clip generation. Use for B-roll segments, establishing shots, and visual transitions that would be expensive to film.
- **Remotion**: Programmatic video assembly using React/TypeScript. Use for animated captions, motion graphics, lower thirds, and templated video builds. Renders via CLI.
- **CapCut**: Color grading, animated word-by-word captions, and final polish. Desktop version is free and powerful for quick edits.
- **FFMPEG**: The backbone CLI tool. Audio mixing, video assembly, format conversion, frame extraction, silence generation, loudness normalization (-14 LUFS).
- **ffprobe**: Audio forensics — loudness detection, silence detection, stream metadata inspection. Use before FFMPEG processing to analyze source files.

---

## 🖼️ Image Generation & Graphics

| Tool | Type | Location / Access |
|---|---|---|
| Nano Banana 2 | Cloud AI | Google AI Studio — Gemini 3 Pro Image model |
| ImageFX | Cloud AI | [aitestkitchen.withgoogle.com/tools/image-fx](https://aitestkitchen.withgoogle.com/tools/image-fx) |

- **Nano Banana 2**: AI stick figure / stylized image generation via Gemini. Use for custom illustration-style thumbnails and explainer visuals that look hand-drawn.
- **ImageFX**: Google's image generation playground. Quick concept art, thumbnail backgrounds, and visual brainstorming without API setup.

---

## 📊 Graphics, Slide Decks & Diagrams (NotebookLM)

| Tool | Type | Location / Access |
|---|---|---|
| NotebookLM (Gemini Notebook) | Cloud app | [notebooklm.google.com](https://notebooklm.google.com) — browser |

- **Primary use — Research**: Upload scripts, articles, PDFs, YouTube links as sources. NotebookLM synthesizes them into summaries, Q&A, and audio podcast overviews. Use during pre-production to absorb research material fast.
- **Secondary use — Slide Deck Images**: Feed your script or source material into NotebookLM → use the slide deck feature → it generates styled images/slides based on the content. These can be used as visual assets in your videos — graphics that maintain a consistent aesthetic tied to your source material. Not full motion graphics, but static graphics and diagrams that AI image generators struggle to match for informational accuracy.

---

## 🔊 Audio & Voiceover

| Tool | Type | Location / Access |
|---|---|---|
| ElevenLabs (v3) | Cloud API + web app | [elevenlabs.io](https://elevenlabs.io) — API key or browser |
| Google Lyria 3 | Cloud AI | Google AI Studio / MusicFX — browser |
| Suno | Cloud AI | [suno.com](https://suno.com) — browser |

- **ElevenLabs**: AI voiceover generation. Use v3 for audio tags, pacing control, and punctuation-driven delivery. Clone your voice or use preset voices. Primary voiceover tool for narration.
- **Lyria 3 / MusicFX**: Google's AI music generation. Use for custom background tracks when stock music doesn't fit the mood. Free via AI Studio.
- **Suno**: AI music generation with vocals. Use when you need a full song with lyrics (intros, outros, themed segments). Complements Lyria for different use cases.

---

## 🎵 Music Libraries (Free)

| Tool | Type | Location / Access |
|---|---|---|
| YouTube Audio Library | Website | YouTube Studio → Audio Library |
| Mixkit | Website | [mixkit.co](https://mixkit.co) — direct download, no account |
| Pixabay / Pixabay Music | Website | [pixabay.com/music](https://pixabay.com/music) |
| Unminus | Website | [unminus.com](https://unminus.com) — download MP3/WAV |
| Freesound | Website | [freesound.org](https://freesound.org) — requires free account |
| Mixkit (SFX) | Website | [mixkit.co/free-sound-effects](https://mixkit.co/free-sound-effects/) |
| BBC Sound Effects | Website | [sound-effects.bbcrewind.co.uk](https://sound-effects.bbcrewind.co.uk) |

- **YouTube Audio Library**: Safest option — zero Content ID risk since it's YouTube's own library. Limited variety but guaranteed clean.
- **Mixkit**: Higher quality curation than Pixabay. Also offers video templates for Premiere/DaVinci. No account needed.
- **Pixabay Music**: Massive catalog, inconsistent quality. Good for background ambient tracks.
- **Unminus**: Small indie catalog (lo-fi, chill, ambient). Occasional Content ID false positives — keep download receipts.
- **Freesound**: Community-uploaded SFX. Check individual licenses (some require attribution). Best for specific foley sounds.
- **BBC Sound Effects**: High-quality archival sounds. Personal/educational/research use — check license for commercial YouTube use.

---

## 🎵 Music Libraries (Paid)

| Tool | Type | Location / Access |
|---|---|---|
| Epidemic Sound | Subscription | [epidemicsound.com](https://epidemicsound.com) — $15/mo |
| Artlist | Subscription | [artlist.io](https://artlist.io) — $10–17/mo |

- **Epidemic Sound**: 40,000+ tracks with stems, direct YouTube Content ID whitelisting, AI mood matching. Industry standard for mid-to-large creators.
- **Artlist**: Similar to Epidemic. Includes SFX bundle. Some creators prefer its catalog style. Both eliminate Content ID issues entirely.

---

## 🔍 Research & Data Scraping

| Tool | Type | Location / Access |
|---|---|---|
| Supadata | Cloud API | [supadata.ai](https://supadata.ai) — API key, 100 free requests/mo |
| youtube-transcript-api | Python package | `pip install youtube-transcript-api` |
| yt-dlp | CLI tool | `winget install yt-dlp` or `pip install yt-dlp` |
| scrapetube | Python package | `pip install scrapetube` |

- **Supadata**: Reliable transcript + metadata extraction API. Handles proxy rotation so it works from cloud servers where `youtube-transcript-api` fails. Auto-generates transcripts via Whisper for videos with no captions.
- **youtube-transcript-api**: Local Python transcript extraction. Works great on your own machine. Breaks on cloud servers (YouTube blocks data center IPs). Use for local scripts only.
- **yt-dlp**: Download video/audio from YouTube. Use for backing up your channel, grabbing competitor videos for research, extracting audio for Whisper. Requires `ffmpeg` installed. Violates YouTube ToS but the tool itself is legal.
- **scrapetube**: Gets all video IDs from any YouTube channel without API quota. Feed results into `yt-dlp` or `youtube-transcript-api` for bulk processing.

---

## 📈 Analytics & SEO

| Tool | Type | Location / Access |
|---|---|---|
| YouTube Analytics MCP | Local MCP server | Python package + OAuth setup (see tool_guide.md) |
| vidIQ | Chrome extension + web | [vidiq.com](https://vidiq.com) — free tier + paid |
| TubeBuddy | Chrome extension | [tubebuddy.com](https://tubebuddy.com) — free tier is limited |
| Social Blade | Website | [socialblade.com](https://socialblade.com) — browser |
| Spotter Studio | Web app | [spotter.com](https://spotter.com) — $49/mo |

- **YouTube Analytics MCP**: Pipes your channel's views, CTR, retention, revenue, and audience data directly into Antigravity IDE. Ask your AI agent questions about your channel performance in natural language. Requires Google Cloud OAuth setup.
- **vidIQ**: Keyword research, competitor keyword tracking, search volume scores. Free tier is usable. Best for post-idea SEO validation — "will people search for this?"
- **TubeBuddy**: Main remaining value is bulk catalog management (mass-edit descriptions/links across 100+ videos). Tag optimization is outdated. Free tier is a demo.
- **Social Blade**: Quick channel growth comparison. Check competitor subscriber/view trends over time. Free browser tool, no setup.
- **Spotter Studio**: AI-powered ideation based on your channel's outlier videos. Best for established channels with 50+ videos. Expensive at $49/mo. Not useful for new channels.

---

## 📤 Publishing & Distribution

| Tool | Type | Location / Access |
|---|---|---|
| YouTube Studio | Web app | [studio.youtube.com](https://studio.youtube.com) |
| TikTok | Web/mobile | [tiktok.com](https://tiktok.com) |
| Instagram Reels | Mobile app | Instagram app |
| Facebook Reels | Web/mobile | Facebook app or creator studio |

- **YouTube Studio**: Upload, SEO metadata, scheduling, thumbnail upload, AI content disclosure, community posts, native A/B thumbnail testing (Test & Compare).
- **TikTok / Instagram Reels / Facebook Reels**: Short-form repurposing destinations. Crop long-form 16:9 to 9:16 using Python (mediapipe + opencv) or CapCut.

---

## 🛠️ CLI & System Tools

| Tool | Type | Location / Access |
|---|---|---|
| Python (3.10+) | Local runtime | Installed on your machine |
| FFMPEG | CLI tool | `winget install Gyan.FFmpeg` |
| ffprobe | CLI tool | Bundled with FFmpeg |
| PowerShell | System shell | Built into Windows |
| pip | Python package manager | Bundled with Python |

- **Python**: The backbone connecting every other tool. Scripts for automation, API calls, video processing, analytics, and content repurposing.
- **FFMPEG/ffprobe**: Audio/video processing CLI. Every video workflow eventually runs through these.
- **PowerShell**: Windows automation — batch file operations, scheduled tasks, environment setup.

---

## 🐍 Python Libraries (Key Ones)

| Library | Install | Use Case |
|---|---|---|
| `google-genai` | `pip install google-genai` | Gemini API access for video analysis, script generation |
| `groq` | `pip install groq` | Groq API client for fast LLM inference + Whisper |
| `Pillow` (PIL) | `pip install Pillow` | Image compositing, thumbnail text overlays |
| `opencv-python` | `pip install opencv-python` | Frame extraction, face detection, video analysis |
| `pydub` | `pip install pydub` | Audio manipulation, silence stripping, normalization |
| `requests` | `pip install requests` | HTTP API calls to any service |
| `google-api-python-client` | `pip install google-api-python-client` | YouTube Data API v3 — upload, metadata, analytics |

---

## 🤖 Antigravity Agent Skills & MCP

| Tool | Type | Location / Access |
|---|---|---|
| Antigravity IDE | Desktop IDE | Local installation |
| Humanizer | Agent Skill | `C:\Users\renu5\.gemini\config\skills\humanizer` |
| Anti-Sycophancy | Agent Skill | `C:\Users\renu5\.gemini\config\skills\anti-sycophancy` |
| Voiceover Enhancer | Agent Skill | `C:\Users\renu5\.gemini\config\skills\voiceover-enhancer-skill` |
| Ruflo | Agent Platform | Multi-agent orchestration for AI coding agents |
| GitHub Actions | CI/CD | [github.com](https://github.com) — workflow YAML files |

- **Antigravity IDE**: Your primary AI coding environment. Runs agents, skills, MCP servers. Everything connects through here.
- **Humanizer**: Strips AI writing patterns from scripts before recording. Removes "delve," "landscape," em-dash abuse, and other AI tells.
- **Anti-Sycophancy**: Forces critical thinking in AI responses. Prevents yes-man behavior when reviewing your scripts, strategies, and ideas.
- **Voiceover Enhancer**: Prepares scripts for ElevenLabs TTS — strips non-narration elements, adds pacing markers, normalizes text.
- **Ruflo**: Multi-agent orchestration. Coordinates multiple AI agents for complex pipeline tasks (research → script → voiceover → assembly).
- **GitHub Actions**: Automate repetitive workflows — scheduled scraping, batch processing, deployment pipelines.

---

---

# 🔧 Extended Toolkit — Stickman Studio Unique Tools

> Tools unique to the "Stickman Studio - Copy Before doing any change by Rook" workflow.
> Kept separate since they serve specialized research and forensic analysis purposes.

## 🔬 Academic Research Tools

| Tool | Type | Location / Access |
|---|---|---|
| Google Scholar | Website | [scholar.google.com](https://scholar.google.com) |
| PubMed | Website | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov) |
| JSTOR | Website | [jstor.org](https://jstor.org) — some free, most require institutional access |
| ResearchGate | Website | [researchgate.net](https://researchgate.net) — free account |

- **Google Scholar**: Find peer-reviewed papers, citation counts, and related work for fact-based scripts. Use when making claims that need academic backing.
- **PubMed**: Medical/health/biology research database. Use for health-related content to cite real studies instead of blog posts.
- **JSTOR**: Academic journal archive. Many papers behind paywall — check for open-access versions.
- **ResearchGate**: Researcher profiles and paper downloads. Often has free PDFs that JSTOR gates.

## 🖼️ Image Processing & Visual Forensics

| Tool | Type | Location / Access |
|---|---|---|
| ImageMagick / magick | CLI tool | `winget install ImageMagick` or [imagemagick.org](https://imagemagick.org) |
| opencv-python | Python library | `pip install opencv-python` |
| librosa | Python library | `pip install librosa` |
| MS Paint | Desktop app | Built into Windows |

- **ImageMagick**: CLI image manipulation — overlays, transparent backgrounds, batch resizing, Red X overlays, watermarks. Use when Pillow isn't enough or you need batch shell processing.
- **opencv-python**: Advanced frame analysis, face detection for thumbnail selection, sharpness scoring, and video-to-image extraction.
- **librosa**: Audio analysis — pitch detection, tempo extraction, energy contour mapping. Use for syncing visuals to audio beats or analyzing voice characteristics.
- **MS Paint**: Crude illustration reference. Used in stickman/ink style for intentionally rough, hand-drawn aesthetic — the "anti-polish" look.

## 📊 Competitor Intelligence

| Tool | Type | Location / Access |
|---|---|---|
| spy_competitor.py | Custom Python script | In your Stickman Studio workflow folder |
| Grok | Cloud AI | [grok.com](https://grok.com) — X/Twitter AI |
| google-genai | Python library | `pip install google-genai` |

- **spy_competitor.py**: Your custom script for YouTube competitor analysis — channel tracking, outlier detection, keyword gap analysis. Check if it still runs; dependencies and API keys may need refreshing.
- **Grok**: X/Twitter's AI. Used in 3-model council for script generation as a third opinion alongside Gemini and Claude.
- **google-genai**: Gemini Python API. Direct video analysis, transcript processing, and programmatic AI calls from scripts.
