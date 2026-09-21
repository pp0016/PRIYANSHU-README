# Human Script DNA — Project Folder

> **Purpose:** Extract what makes top competitor scripts feel HUMAN — specific sources, narrative structure, emotional pacing, anti-AI-slop patterns — so Priyanshu can replicate it in his own scripts.
> **Run this in:** A separate conversation from the main production workflow.
> **Model:** Start with Gemini 3.1 Pro for data collection, switch to Opus 4.6 for analysis.

---

## The Idea (From Priyanshu)

Most AI-generated YouTube scripts sound like AI. The /humanizer skill catches surface-level AI tells ("delve into", "tapestry of", etc.), but it doesn't teach you the STRUCTURE of a human-written script:
- How do human writers cite sources? (Not "researchers say" — they name the researcher, the year, the institution)
- What narrative devices do they use between segments? (Not "next, let's look at" — they use story bridges, callbacks, questions)
- How do they pace emotional shifts? (Where do they speed up? Where do they pause?)
- What makes the hook work? (First 30 seconds — what pattern interrupt, what promise?)

This system extracts that DNA from real competitor videos.

---

## Workflow

### Step 1: Select Target Videos (5-8 videos)

Pick from these proven breakout videos (already identified in research):

**Brofessor Stein (highest RPM, $62/1K subs):**
- "Every Mystical Artifact Explained in 17 Minutes" — 1.5M views
- "The Most Disturbing Books You Shouldn't Read" — 525K, 444 VPH
- "The Most Censored Symbols Explained in 16 Minutes" — 1.1M views

**Serious History (816K subs, $7.2K/mo):**
- "Extreme Vigilante Justice in History" — 6.35M views, 362 VPH
- "When Nice People Snapped in History" — 3.55M views

**EverythingProfessor (596K subs, fastest growing):**
- "Every Drug & Its Effect Explained in 17 Minutes" — 5.1M views
- "Every Manipulation Technique & How To Combat It" — 2.6M views

**The Analyst (601K subs, DEAD — study their best before they disappeared):**
- "Every Government Form Explained" — 4.36M views
- "Every BANNED Book Explained" — 3.4M views

### Step 2: Transcribe with Groq + Whisper

**Why Groq/Whisper, not YouTube auto-captions:**
- YouTube auto-captions miss punctuation, speaker intent, and pacing cues
- Whisper captures actual speech patterns, pauses, emphasis shifts
- Groq's API is fast and Priyanshu has API keys

**How to do it:**
1. Download video audio (use yt-dlp: `yt-dlp -x --audio-format mp3 "VIDEO_URL"`)
2. Send to Groq Whisper API for transcription
3. Save raw transcript as `transcripts/[channel]_[short_title].txt`

**Groq Whisper API call (Python):**
```python
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

with open("audio_file.mp3", "rb") as file:
    transcription = client.audio.transcriptions.create(
        file=("audio_file.mp3", file.read()),
        model="whisper-large-v3-turbo",
        response_format="verbose_json",  # Includes timestamps
        timestamp_granularities=["segment", "word"]
    )

# Save with timestamps for pacing analysis
with open("transcript_output.json", "w") as f:
    import json
    json.dump(transcription.model_dump(), f, indent=2)
```

### Step 3: Extract Script DNA (Opus 4.6 Analysis)

**Switch to Opus 4.6 for this step.** Feed each transcript and extract:

#### A. Hook Analysis (First 30 Seconds)
- What's the FIRST sentence? (Pattern interrupt? Question? Shocking stat?)
- Does it make a promise? What promise?
- How many seconds before the topic is introduced?
- Is there a "cold open" (story snippet) before the intro?

#### B. Source Citation Patterns
- Count every specific source mentioned (author name, book title, study, year, institution)
- How are sources introduced? ("According to..." vs "In 1923, Dr. X at Harvard found..." vs woven into narrative)
- How many sources per 1,000 words?
- Do they cite OBSCURE sources (not Wikipedia-first-result)?

#### C. Narrative Bridge Patterns
- How does the script transition between segments?
- List every transition phrase used
- Are there callbacks to earlier segments?
- Is there a "thread" that connects all segments (not just a list)?

#### D. Emotional Pacing (Requires Whisper Timestamps)
- Map energy levels across the video timeline (1 = calm, 5 = intense)
- Where are the "breather" moments? (After intense content, before the next section)
- How long are pauses between segments?
- Does the voice speed up or slow down at key moments?

#### E. Anti-Slop Markers (What Makes It NOT Sound Like AI)
- Specific, weird details that only a human researcher would find
- Personal opinions stated as opinions (not "many people believe")
- Humor (if any) — what type? Self-deprecating? Dark? Observational?
- Imperfect phrasing that feels natural (not grammatically perfect but sounds right)
- Does the narrator have a "character" or persona?

### Step 4: Build the Script DNA Template

Compile all findings into a reusable template:

```markdown
# Script DNA Template — [Channel Name] Style

## Hook Formula
[Extracted pattern]

## Source Density
[X sources per 1,000 words. Types: ___]

## Transition Toolkit
[List of transition patterns, with examples]

## Emotional Arc
[Typical energy curve: start → build → peak → breathe → build → peak → conclusion]

## Anti-Slop Checklist
- [ ] At least [X] named sources per 1,000 words
- [ ] At least [X] "weird specific detail" that can't be found on first Google result
- [ ] No generic transitions ("Now let's look at...", "Moving on to...")
- [ ] At least [X] callback to earlier segment
- [ ] [Other patterns found]

## /humanizer Integration
[Which humanizer rules overlap with the DNA findings, which are new]
```

### Step 5: Test Against vidIQ Script Writer (Optional)

After building the DNA system:
1. Write a test script using the DNA template
2. Write the same script using vidIQ's Script Writer feature
3. Compare both using the Anti-Slop Checklist
4. Score: Does the DNA system improve over vidIQ, or does vidIQ actually add value?

This determines whether to use vidIQ Script Writer as a STARTING POINT (then DNA-pass) or to skip it entirely.

---

## Prompt for the New Conversation

Copy-paste this into a new conversation:

```
Read the Human Script DNA project file:
C:\Users\renu5\Downloads\priyanshu readme\niche_research\human_script_dna\README.md

I have audio files from 5-8 top YouTube competitor videos ready to transcribe.
My Groq API key is set up for Whisper transcription.

Execute the workflow:
1. Help me transcribe each audio file using Groq Whisper API
2. Analyze each transcript for Script DNA (hooks, sources, transitions, pacing, anti-slop markers)
3. Build the reusable Script DNA Template
4. Test it against vidIQ Script Writer output

Use Gemini 3.1 Pro for transcription work, then tell me to switch to Opus 4.6 for analysis.
Use /humanizer skill — the DNA system should work WITH humanizer, not replace it.

DO NOT start production or scripting — this conversation is ONLY for building the DNA extraction system.
```

---

## Files to Prepare Before Starting

1. **Audio files** — Download from 5-8 videos using: `yt-dlp -x --audio-format mp3 "VIDEO_URL"`
2. **Groq API key** — Set as environment variable `GROQ_API_KEY`
3. **This README** — The new conversation reads this as its instruction set

---

## Expected Output

After this conversation completes, you'll have:
- `transcripts/` folder with timestamped transcripts of 5-8 competitor videos
- `analysis/` folder with DNA extraction for each video
- `script_dna_template.md` — the reusable template for all future scripts
- `vidiq_comparison.md` — whether vidIQ Script Writer helps or hurts
- A clear /humanizer integration guide

Hand the `script_dna_template.md` back to the main production conversation to use when scripting Video 1.
