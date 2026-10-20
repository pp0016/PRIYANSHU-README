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

## new find 2026-10-07: `google-genai` (Python SDK)

**What it is:** The official Python SDK for Google's Gemini models. Unlike standard web interfaces, this is a programmatic "factory engine" that allows AI agents to build multi-step, autonomous content pipelines, bypass manual copy-pasting, and avoid web app crashes.

### 🧠 Core Capabilities
1. **Data Synthesis (Structured Outputs):** Uses Pydantic schemas (`response_schema`) to force the AI to return strict JSON data instead of conversational text. Perfect for converting messy research outputs into clean data variables.
2. **Function Calling (Tool Binding):** Connects to existing CLI commands. The AI can decide *when* to trigger research scripts based on the context of the prompt.
3. **Orchestration Dependency:** The SDK is just the brain client. True multi-agent pipelines require wrapping these SDK calls inside an external framework like `ruflo`.

---

### 🚀 Content Creator Automation Pipelines (Use Cases)

#### 1. The Headless "Stickman" Video Orchestrator
Instead of chatting to generate a script, the SDK acts as an end-to-end compiler for the Stickman pipeline.
* **The Pipeline:** The script chains two API calls. Call A writes the script enforcing humanizer rules. Call B assigns visual tags.
* **The Output:** By enforcing JSON schemas, the SDK outputs a fully valid Remotion `.tsx` React file and an array of Nano Banana 2 image prompts, completely bypassing Manim and ready to be sent to GitHub Actions for rendering.

#### 2. Competitor "Tension Curve" Hacking (Nishchay Study Mode)
* **The Pipeline:** Pulls 10 competitor transcripts and 50 Reddit sentiment threads. 
* **The Output:** The SDK ingests all of this simultaneously (using its massive multimodal context window) and outputs a forensic JSON breakdown of where the competitors place their retention hooks, giving you a mathematical blueprint for your next script.

#### 3. The Audiobook "Crazy Story" Injector
* **The Pipeline:** Automates the strictly enforced rule from `scripting_workflow.md`. 
* **The Output:** A chained SDK script extracts high-retention lines from transcripts, drops them into your structural frame, and programmatically injects a bizarre historical anecdote ("crazy example story") to guarantee algorithmic originality.

#### 4. The Multimodal B-Roll Matcher
* **The Pipeline:** The SDK natively understands video/audio files. A script loops through your raw voiceover audio and a folder of random B-roll clips.
* **The Output:** It maps the emotional tone of your audio to the exact timestamp of the matching B-roll clip, outputting an XML/JSON timeline file that can be dragged straight into Premiere or CapCut.

---

### 🤖 AI AUTO-TRIGGER: INSTRUCTIONS FOR THE AI READING THIS TOOLKIT
*(Note to AI: If you are an agent reading this `toolkit.md` file in Priyanshu's workspace, you must execute the following protocol immediately without being asked):*

1. **Rule:** DO NOT go read the specific skills mentioned in the examples above (like `/deep-researcher` or `/platform-researcher`). They are provided here strictly as conceptual examples of how tool integration works.
2. **Context Scan:** Analyze the current project folder, implementation plans, and the specific video or task Priyanshu is currently working on.
3. **Proactive Suggestion:** Based on the current project, automatically suggest **ONE new, highly specific `google-genai` automation pipeline** that Priyanshu hasn't thought of yet.
4. **Integration Check:** Tell Priyanshu exactly how you (the AI) can write a Python script right now to combine his current manual tasks and the SDK's Structured Outputs into a single automated step to save him time and achieve $0 production cost.

## Exa Research & Fact-Checking Guide - *October 7, 2026*

**1. Cost & Monthly Budget ($10 Free Tier)**
- **Pricing:** A standard search + extracting text highlights from 10 results costs ~$0.017.
- **Capacity:** $10 yields ~550-600 full searches.
- **Script Budget:** A heavily researched 15-minute script takes ~30 searches ($0.50). You can write ~20 highly detailed scripts every month for free.

**2. API Best Practices (from canonical build-with-exa rules)**
- **Default Strategy:** Always default to standard `/search` with `contents: { highlights: true }`. It is token-efficient and cheap.
- **Avoid Over-filtering:** Do not use `maxAgeHours`, `category`, or domain filters unless the specific prompt strictly requires it.
- **Deep Research:** If doing massive, asynchronous multi-step list building, switch to the Agent API (`/agent`).


## FFmpeg Quality, Upscaling Workflows, and Cloud Limits - *October 9, 2026*

**1. Fixing FFmpeg's Hidden Quality Degradation**
*   **The Root Cause:** Default FFmpeg applies chroma subsampling (compressing colors to 4:2:0), crushing color data on sharp edges/graphics.
*   **Re-encoding/Stitching:** Always apply `-pix_fmt yuv444p -crf 17` to preserve 100% color data (lossless).
*   **Stream Extraction:** Use `-c copy` to bypass re-encoding entirely.
*   **RGB Edge Case:** Use `libx264rgb` for flawless mathematical RGB preservation.

**2. WinGet FFmpeg Path & The Global Rule**
*   **Primary Path Mandate:** Exclusively use: `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe`
*   **Global Rule:** Generic `ffmpeg` alias is banned. The absolute WinGet path and zero-degradation flags are permanently hardcoded globally via `GEMINI.md`.

**3. AI Upscaling Tools**
*   **Anime/Graphics:** Video2X (using Real-ESRGAN) is superior for line art and flat colors.
*   **Live-Action:** SUPIR generates hyper-realistic textures (pores/hair). Real-ESRGAN ruins real people (plastic mannequins). SUPIR demands massive VRAM.
*   **Fast/Lightweight:** The `libplacebo` filter (with `ewa_lanczos`) is best for fast FFmpeg native enhancements.

**4. Cloud Upscaling Infrastructure**
*   **Fal.ai:** Best for instant, free, watermark-less image upscaling.
*   **Hugging Face Spaces:** Free cloud option for AI video upscaling (open-source models on huge GPUs), but has server queues.
*   **CapCut Online:** Reliable zero-setup fallback for video upscaling up to 4K.

**5. Google Colab Limits & Faceless Strategy**
*   **The 12-Hour Colab Myth:** Realistically provides 2 to 4 hours before preemption.
*   **The 90-Minute Timeout:** Silent kill if the browser tab is idle.
*   **The 15GB Drive Trap:** Saving rendered video to free Google Drive quota causes "Disk Full" crashes.
*   **OOM on SUPIR:** Free-tier T4 GPUs (15GB VRAM) crash on SUPIR. Needs Colab Pro A100.
*   **Faceless Channel Strategy:** Use Colab to upscale low-quality B-Roll, generate free voiceovers, generate thumbnails via SDXL/Flux, and act as a remote render farm to free up local laptops.

---

## 🎬 Documentary Style Tools Required

> Added: 2026-10-13 | Purpose: Programmatic documentary/commentary-style video editing
> These tools enable keyframe animation, word-synced text, color grading, film grain, and cinematic transitions — all controlled from terminal via Remotion. No manual editing required.

### NPM Packages (Remotion Ecosystem)

| Package | Install | Purpose |
|---|---|---|
| `@remotion/effects` | `npm install @remotion/effects` | Color grading (3D LUTs, sepia, desaturation), film grain overlay, cinematic vignette, paper texture shader |
| `@remotion/transitions` | `npm install @remotion/transitions` | Hard cuts, crossfade/dissolve, slide/wipe, glitch flash transitions between shots |
| `@remotion/captions` | `npm install @remotion/captions` | Word-level text sync from ElevenLabs timestamps — triggers text popups on spoken keywords |

### Font

| Font | Source | Purpose |
|---|---|---|
| **Montserrat** (Black, Bold, ExtraBold) | [fonts.google.com/specimen/Montserrat](https://fonts.google.com/specimen/Montserrat) | Bold geometric sans-serif for keyword text, stat callouts, date stamps, title cards |

### Project Location

| Item | Path |
|---|---|
| Remotion Project | `C:\Users\renu5\.gemini\antigravity\scratch\documentary-style\documentary-template` |
| Template Compositions | Inside the Remotion project `src/` folder |

### What Each Tool Does in the Documentary Pipeline

- **@remotion/effects**: Applies the two-LUT color grading system (warm sepia for historical → cool blue-grey for crisis moments), adds procedural film grain that flickers per-frame (so AI images look like archival footage), adds soft vignette (darkened edges) to direct focus, and provides a paper texture shader for newspaper/document overlays.
- **@remotion/transitions**: Handles all scene-to-scene transitions. Hard cuts are default. Crossfades (0.25-0.4s) reserved for era/tone changes. Slide/wipe for graphic-to-graphic moves. Glitch flashes for dramatic keyword reveals.
- **@remotion/captions**: Takes the word-level timestamps from ElevenLabs' `with-timestamps` API and connects them to Remotion's `useCurrentFrame()` — so bold yellow text pops onto screen with a spring bounce animation at the exact millisecond the narrator speaks each keyword.
- **Montserrat**: The font family used for all on-screen text. Yellow for emphasis keywords, white for neutral labels, red for failure/negative, cyan-on-black for end cards.

### Key Remotion Component Libraries (Optional Installs)

| Library | GitHub | Stars | Purpose |
|---|---|---|---|
| Remocn | [Remocn/remocn](https://github.com/Remocn/remocn) | ~1,600 | Copy-paste animated components — Typewriter, RGB Glitch Text, Kinetic Type, VHS filter |
| remotion-bits | [av/remotion-bits](https://github.com/av/remotion-bits) | ~480 | Modular animation bits — Ken Burns presets, text effects |
| @remotion/rough-notation | Official Remotion | Built-in | Hand-drawn highlight markers on documents/text (circle, underline, box) |

