# Human Script DNA — Extraction Pipeline

Extract what makes top competitor scripts sound HUMAN by transcribing 9 competitor videos via Groq Whisper, analyzing each transcript for script DNA patterns, and building a reusable template for Priyanshu's channel.

## Current State

**9 audio files ready** in `audio/` directory:

| # | Channel | Video | Size |
|---|---------|-------|------|
| 1 | Brofessor Stein | Every Mystical Artifact Explained in 17 Minutes | 41.5 MB |
| 2 | Brofessor Stein | The Most Censored Symbols Explained in 16 Minutes | 15.7 MB |
| 3 | Brofessor Stein | The Most Disturbing Books You Shouldn't Read | 18.7 MB |
| 4 | EverythingProfessor | Every Manipulation Technique & How To Combat It | 12.2 MB |
| 5 | EverythingProfessor | Every Rare Drug & Its Effects Explained in 21 Minutes | 20.4 MB |
| 6 | Serious History | Extreme Vigilante Justice in History | 28.1 MB |
| 7 | Serious History | When Nice People Snapped in History | 16.1 MB |
| 8 | The Analyst | Every BANNED Book Explained in 15 Minutes | 14.7 MB |
| 9 | The Analyst | Every Government Form Explained in 12 Minutes | 12.3 MB |

**Groq API key provided** — will use `whisper-large-v3-turbo` model.

---

## Proposed Execution

### Phase 1: Transcription (Python + Groq Whisper API)

1. **Create a Python script** that:
   - Reads each MP3 from `audio/`
   - Sends to Groq Whisper API (`whisper-large-v3-turbo`, `verbose_json` format with segment + word timestamps)
   - Saves JSON transcripts to `transcripts/` folder
   - Saves plain-text versions alongside for easy reading
   - Handles Groq's **25MB file size limit** — the two files over 25MB (Brofessor Stein Mystical Artifacts at 41.5MB and Serious History Vigilante Justice at 28.1MB) will need to be **split into chunks** using FFmpeg, transcribed separately, and stitched back together

2. **Install dependencies**: `groq` Python package (via pip in a venv)

3. **Run transcription** — 9 files, estimated ~5-10 minutes total

> [!IMPORTANT]
> **Groq API has a 25MB file upload limit.** Two files exceed this:
> - `Brofessor Stein_Every Mystical Artifact Explained in 17 Minutes.mp3` (41.5 MB)
> - `Serious History_Extreme Vigilante Justice in History.mp3` (28.1 MB)
> 
> These will be split into ~20MB chunks via FFmpeg, transcribed separately, and merged.

### Phase 2: Script DNA Analysis (Opus 4.6)

For each of the 9 transcripts, analyze:

- **A. Hook Analysis** — First 30 seconds: pattern interrupt type, promise made, cold open presence
- **B. Source Citation Patterns** — Named sources, introduction style, density per 1K words, obscurity level
- **C. Narrative Bridge Patterns** — Transition phrases, callbacks, connecting threads
- **D. Emotional Pacing** — Energy mapping across timeline using Whisper timestamps, breather moments, pace shifts
- **E. Anti-Slop Markers** — Weird specific details, personal opinions, humor type, imperfect phrasing, narrator persona

Each analysis saved to `analysis/[channel]_[short_title]_dna.md`

### Phase 3: Build Reusable Template

Compile cross-video patterns into:
- `script_dna_template.md` — The master template with formulas, checklists, and examples
- `/humanizer` integration notes — How DNA findings work with the existing humanizer skill

### Phase 4: vidIQ Comparison (Optional)

- Compare DNA-system output vs vidIQ Script Writer
- Save results to `vidiq_comparison.md`

---

## Output Files

```
human_script_dna/
├── README.md (existing)
├── audio/ (existing, 9 MP3s)
├── transcripts/
│   ├── brofessor_stein_mystical_artifacts.json
│   ├── brofessor_stein_mystical_artifacts.txt
│   ├── ... (9 pairs)
├── analysis/
│   ├── brofessor_stein_mystical_artifacts_dna.md
│   ├── ... (9 files)
├── script_dna_template.md
├── vidiq_comparison.md
└── humanizer_integration.md
```

## Verification Plan

### Automated
- Confirm all 9 transcripts are generated and non-empty
- Confirm all 9 analysis files are generated

### Manual
- Priyanshu reviews the `script_dna_template.md` and confirms it captures patterns he recognizes from watching these channels
- Template is handed back to the main production conversation for Video 1 scripting
