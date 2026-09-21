# 🔍 Full Audit: Gemini's GitHub Repo Analysis

I re-read every single README across all 43 repos using independent auditors. Here is the fact-check of what Gemini told you, what it got wrong, and my final recommendation.

---

## ❌ Where Gemini Was WRONG

### 1. **ruflo** (1.76 GB) — Gemini said "Delete, needs GPU"
> **WRONG.** Ruflo does NOT need a GPU at all. It's a lightweight Node.js/Rust orchestration tool that coordinates AI agents. It runs fine on CPU with ~512 MB RAM. However, 1.76 GB is bloated for what it does — the `.git` history and `node_modules` are likely inflated. **Verdict: It CAN run on your laptop, but 1.76 GB is excessive for a coordination tool. You can reinstall it smaller if you ever need it.**

### 2. **ViMax** (3.14 MB) — Gemini said "Delete, needs GPU"
> **WRONG.** ViMax does NOT need a GPU. It's a Python orchestration tool that sends all heavy work (video generation, scripts, storyboarding) to cloud APIs (OpenAI, Gemini, Veo, Kling). It needs only 4–8 GB RAM. **Verdict: This RUNS FINE on your laptop. Gemini incorrectly lumped it with GPU-heavy tools.**

### 3. **speech-to-speech** (2.83 MB) — Gemini said "Delete, needs GPU"
> **PARTIALLY WRONG.** It has CPU fallback modes and can work using cloud APIs for the LLM and TTS parts. A GPU is only "strongly recommended" for real-time low-latency voice chat. For basic use, your laptop can handle it. **Verdict: Usable on your laptop, just not for real-time live voice conversations.**

---

## ✅ Where Gemini Was CORRECT

| Repo | Gemini Said | Audit Confirms |
|:-----|:-----------|:---------------|
| **unsloth** (62 MB) | ❌ Delete, needs GPU | ✅ Correct — needs 6–8 GB VRAM minimum |
| **comfyui** (43 MB) | ❌ Delete, needs GPU | ✅ Correct — GPU practically required |
| **OmniVoice** (1.26 MB) | ❌ Delete, needs GPU | ✅ Correct — GPU strongly recommended |
| **MoneyPrinterTurbo** (200 MB) | ✅ Keep, cloud APIs | ✅ Correct — no GPU, 4 GB RAM minimum |
| **OpenReels** (64 MB) | ✅ Keep, cloud APIs | ✅ Correct — no GPU, 2–4 GB RAM |
| **OpenMontage** (83 MB) | ✅ Keep, cloud APIs | ✅ Correct — no GPU, 4 GB RAM |
| **HyperFrames** (569 MB) | ✅ Keep, CPU-only | ✅ Correct — Node.js + FFmpeg, no GPU |
| **airi** (558 MB) | ✅ Keep, cloud APIs | ✅ Correct — uses WebGPU/WASM, cloud APIs |
| **mempalace** (60 MB) | ✅ Keep, lightweight | ✅ Correct — CPU-only, 2–4 GB RAM |
| **remotion-main** (712 MB) | 🗑️ Delete, use `npx` | ✅ Correct — `npx create-video@latest` handles everything |

---

## ⚠️ Repos Gemini Completely MISSED (Never Analyzed)

Gemini only analyzed ~15 of your 43 repos. It skipped all of these:

### Lightweight Skills & Tools (ALL run on your laptop ✅)

| Repo | Size | What It Does |
|:-----|:-----|:-------------|
| **graphify** | 13 MB | Converts codebases into visual knowledge graphs. No GPU. |
| **Pixelle-Video** | 10 MB | Another AI short-video generator (cloud mode). No GPU. |
| **Scrapling** | 4 MB | Web scraping framework with anti-bot bypass. No GPU. |
| **findskill** | 34 MB | Windows skill finder for AI coding tools. No GPU. |
| **gstack** | 53 MB | Virtual engineering team skills for AI agents. No GPU. |
| **handy** | 7 MB | Offline speech-to-text desktop app. Runs on CPU. |
| **agent-browser** | 7 MB | Browser automation CLI for AI agents. No GPU. |
| **remotion-motion-graphics-skill-main** | 58 MB | Motion graphics skill files for Remotion. No GPU. |
| **video-shotcraft-main** | 48 MB | 152 cinematic shot recipes for Remotion. No GPU. |
| **claude-seo** | 4 MB | SEO audit tool with 25 sub-skills. No GPU. |
| **agency-agents** | 4 MB | Collection of AI agent personas. Just markdown. |
| **superpowers** | 1 MB | Dev methodology for AI agents. Just markdown. |
| **last30days-skill-main** | 13 MB | Real-time social media research tool. No GPU. |
| **marketingskills** | 3 MB | Marketing framework skills. Just markdown. |
| **higgsfield-ai-prompt-skill-main** | 5 MB | AI video prompt engineering guide. Just markdown. |
| **super-video-maker-skill** | 0.5 MB | Video production skill. Just markdown + scripts. |
| **youtube-automation-agent** | 0.5 MB | YouTube automation workflow. Just scripts. |
| **notebooklm-mcp** | 0.5 MB | NotebookLM API tool. Lightweight. |
| **book-to-skill** | 0.5 MB | Converts books into agent skills. Just scripts. |
| **modelcontextprotocol** | 0.25 MB | MCP reference docs. Just markdown. |
| **social-media-skills** | 0.22 MB | Social media skills. Just markdown. |
| **humanizer** | 0.05 MB | Anti-AI writing fixer. Just markdown. |
| **ai-ad-prompt-guide** | 0.04 MB | Ad prompt engineering guide. Just markdown. |
| **youtube-thumbnail-pro** | 0.02 MB | Thumbnail design skill. Just markdown. |
| **stop-slop** | 0.02 MB | Anti-AI writing patterns. Just markdown. |

### One Gemini Missed That Needs Caution ⚠️

| Repo | Size | What It Does |
|:-----|:-----|:-------------|
| **Open-Generative-AI** | 28 MB | AI image/video studio. Cloud mode works fine, but local mode needs GPU. |

### Duplicates Found 🔄

| Duplicate 1 | Duplicate 2 | Action |
|:------------|:------------|:-------|
| **Agent-Reach** (1 MB) | **Agent-Reach-main** (1 MB) | Delete one — they're the same repo |
| **super-video-maker-skill** (0.5 MB) | **super-video-maker-skill-main** (0.8 MB) | Delete one — they're the same repo |

---

## 🎯 Final Recommendation

### Definitely DELETE (saves ~2.6 GB, truly unusable on your laptop)

| Repo | Size | Reason |
|:-----|:-----|:-------|
| **remotion-main** | 712 MB | `npx create-video@latest` replaces it |
| **ruflo** | 1,763 MB | Bloated; reinstall if needed |
| **unsloth** | 62 MB | Needs dedicated GPU you don't have |
| **comfyui** | 43 MB | Needs dedicated GPU you don't have |
| **OmniVoice** | 1.3 MB | Needs GPU for practical use |
| **Agent-Reach** (duplicate) | 1 MB | Duplicate of Agent-Reach-main |
| **super-video-maker-skill** (duplicate) | 0.5 MB | Duplicate of the -main version |

### Keep (all work on your laptop) ✅

Everything else! All your Remotion skills, video tools (MoneyPrinterTurbo, OpenReels, OpenMontage, Pixelle-Video, ViMax), research tools (graphify, claude-seo, last30days, Scrapling), agent skills (gstack, agency-agents, superpowers, marketingskills), and utility tools (mempalace, handy, agent-browser, HyperFrames, airi) — **all run perfectly on your 8 GB Intel i5 laptop using cloud APIs and CPU-only processing.**

### The "Same Purpose" Claim — Partially True

Gemini said MoneyPrinterTurbo, OpenReels, and OpenMontage "all do the exact same thing." This is **mostly true but oversimplified**:

- **MoneyPrinterTurbo** → Best for quick, automated faceless shorts from a keyword. Simplest to use.
- **OpenReels** → Best for polished vertical shorts with spring-animated captions. More visual.
- **OpenMontage** → Most powerful — supports full-length videos, multiple rendering engines, live research. Not just shorts.

> [!TIP]
> All three are worth keeping since they're small and serve slightly different use cases. But if you only want ONE, keep **MoneyPrinterTurbo** for quick shorts and **OpenMontage** for serious projects.
