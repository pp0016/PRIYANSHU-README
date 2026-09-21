# Teamwork Project Prompt — Draft

> Status: LAUNCHED — teamwork agents active (conversation 059b3680)
> Goal: Craft prompt → get user approval → delegate to teamwork_preview

Extract the "Human Script DNA" from 9 top-performing YouTube competitor videos by transcribing their audio via Groq Whisper API, running deep structural analysis across 8 dimensions, and compiling findings into a reusable script template for Priyanshu's faceless YouTube channel.

Working directory: C:\Users\renu5\Downloads\priyanshu readme\niche_research\human_script_dna
Integrity mode: development

## Requirements

### R1. Transcribe All 9 Audio Files

Transcribe every MP3 file in `audio/` using the Groq Whisper API (`whisper-large-v3-turbo` model). Use `verbose_json` response format with `segment` and `word` timestamp granularities. Save each result as:
- `transcripts/[channel_snake_case]_[short_title_snake_case].json` (full Whisper response with timestamps)
- `transcripts/[channel_snake_case]_[short_title_snake_case].txt` (plain text transcript for reading)

The Groq API key is: `[REDACTED_GROQ]`

All 9 files are under 25MB and need no chunking. The files are:

1. `Brofessor Stein_Every Mystical Artifact Explained in 17 Minutes.mp3` (8.5 MB)
2. `Brofessor Stein_The Most Censored Symbols Explained in 16 Minutes.mp3` (15.7 MB)
3. `Brofessor Stein_The Most Disturbing Books You Shouldn t Read.mp3` (18.7 MB)
4. `EverythingProfessor_Every Manipulation Technique How To Combat It Explained.mp3` (12.2 MB)
5. `EverythingProfessor_Every Rare Drug Its Effects Explained in 21 Minutes.mp3` (20.4 MB)
6. `Serious History_Extreme Vigilante Justice in History.mp3` (14.1 MB)
7. `Serious History_When Nice People Snapped in History.mp3` (16.1 MB)
8. `The Analyst_Every BANNED Book Explained in 15 Minutes.mp3` (14.7 MB)
9. `The Analyst_Every Government Form Explained in 12 Minutes.mp3` (12.3 MB)

Python 3.11.9 is available. Install the `groq` package via pip before running.

### R2. Analyze Each Transcript Across 8 Dimensions

For each of the 9 transcripts, produce a DNA analysis file saved to `analysis/[channel]_[short_title]_dna.md`. Each analysis must cover ALL 8 dimensions below. Use the Whisper timestamp data where relevant.

**Dimension A — Hook Analysis (First 30 Seconds)**
- The exact first sentence and what device it uses (pattern interrupt, question, shocking stat, cold open story snippet)
- What promise is made to the viewer, if any
- Seconds before the main topic is introduced
- Whether there's a cold open before any intro/branding

**Dimension B — Source Citation Patterns**
- Count every named source (author name, book title, study, year, institution)
- How each source is introduced (e.g. "According to..." vs "In 1923, Dr. X at Harvard found..." vs woven into narrative)
- Source density: sources per 1,000 words
- Obscurity assessment: are these first-page-of-Google sources or deep research?

**Dimension C — Narrative Bridge Patterns**
- Every transition phrase used between segments (verbatim quotes from the transcript)
- Whether callbacks to earlier segments exist (and examples)
- Whether there's a connecting thread/throughline across the video or if it's a pure list format

**Dimension D — Emotional Pacing (Using Timestamps)**
- Map energy levels across the video timeline (1 = calm exposition, 5 = intense/shocking content)
- Identify "breather" moments: where does the narrator pull back after intense content?
- Estimate pace changes using word-per-minute density across segments (Whisper word timestamps)
- Identify pauses between segments (gaps in the timestamp data)

**Dimension E — Anti-Slop Markers**
- Specific, weird details that only a human researcher would find (not surface-level Wikipedia facts)
- Personal opinions stated as opinions (not "many people believe")
- Humor type: self-deprecating, dark, observational, none
- Imperfect phrasing that sounds natural (not grammatically perfect but sounds right when spoken)
- Narrator persona/character: what attitude or voice do they project?

**Dimension F — Segment Architecture** *(beyond original README)*
- Average segment length in seconds and words
- Segment count per video
- Ratio of "story/narrative" segments to "explanation/factual" segments
- Whether segments follow a consistent internal structure (setup → details → payoff) or vary

**Dimension G — Vocabulary Fingerprint** *(beyond original README)*
- Estimated reading level (Flesch-Kincaid or equivalent assessment)
- Does the narrator use jargon then explain it, or avoid jargon entirely?
- Identify 10-15 signature phrases or verbal tics unique to this channel
- Sentence length distribution: are sentences mostly short and punchy, long and flowing, or mixed?

**Dimension H — Retention & Open Loop Mechanics** *(beyond original README)*
- Where are open loops planted? (promises of "we'll get to that" or "but first" or "that's not even the craziest part")
- How many unanswered questions are stacked before payoff?
- Are there "preview hooks" (brief mentions of upcoming content to keep the viewer watching)?
- End-of-video structure: does it end abruptly, loop back, tease next video, or summarize?

### R3. Cross-Channel Convergence Analysis

After analyzing all 9 videos individually, produce `cross_channel_convergence.md` that separates:

- **Universal Human Script DNA**: Patterns that ALL 4 channels share. These are the non-negotiable elements that make scripts sound human regardless of style.
- **Channel-Specific Style**: Patterns unique to one channel (Brofessor Stein's humor, The Analyst's clinical tone, etc.). These are optional style choices, not DNA.
- **Surprising Findings**: Patterns that contradict common YouTube scripting advice or that appeared in the highest-performing videos but NOT in others.

### R4. Build the Reusable Script DNA Template

Compile all findings into `script_dna_template.md` — a practical, fill-in-the-blank template that Priyanshu can hand to any AI scripting tool or use manually. It must include:

- Hook formula with 3+ proven patterns and real examples from the transcripts
- Source density target (sources per 1,000 words) with citation style examples
- Transition toolkit: list of transition patterns with verbatim examples
- Emotional arc template: typical energy curve with timestamp markers
- Segment architecture guide: recommended segment length, count, and internal structure
- Anti-slop checklist: every checkbox must be concrete and verifiable (not "make it sound human" — instead "include at least X named sources per 1,000 words")
- Vocabulary guidelines: reading level target, jargon handling rules, sentence length guidance
- Retention mechanics: where to plant open loops, how many to stack, payoff timing
- A section titled "Humanizer Integration" mapping which anti-slop rules overlap with the existing /humanizer skill and which are new discoveries from this analysis

### R5. vidIQ Comparison Assessment

Produce `vidiq_comparison.md` that answers: does vidIQ's Script Writer feature add value as a starting point before applying the DNA template, or should it be skipped entirely? This can be a reasoned assessment based on the DNA findings — it does not require actually running vidIQ Script Writer.

## Acceptance Criteria

### Transcription Completeness
- [ ] All 9 JSON transcript files exist in `transcripts/` and each contains valid JSON with `segments` and `words` arrays
- [ ] All 9 TXT transcript files exist and each contains at least 1,000 words of transcript text
- [ ] Transcripts are correctly named using the convention `[channel]_[short_title].[ext]`

### Analysis Depth
- [ ] All 9 DNA analysis files exist in `analysis/` and each covers all 8 dimensions (A through H)
- [ ] Each analysis cites specific verbatim quotes from the transcript as evidence (not paraphrased summaries)
- [ ] Source citation counts include actual numbers (e.g., "14 named sources in 3,200 words = 4.4 per 1K words")
- [ ] Emotional pacing maps reference actual timestamps from the Whisper data
- [ ] Vocabulary fingerprints include the 10-15 signature phrases per channel

### Cross-Channel Analysis
- [ ] `cross_channel_convergence.md` exists and explicitly separates universal patterns from channel-specific style
- [ ] At least 5 universal DNA patterns are identified with evidence from 3+ channels each
- [ ] At least 3 "surprising findings" are documented

### Template Usability
- [ ] `script_dna_template.md` exists and contains fill-in-the-blank sections a human can actually use
- [ ] Anti-slop checklist has at least 10 concrete, verifiable checkboxes
- [ ] Every recommendation in the template cites which competitor video(s) demonstrated the pattern
- [ ] Humanizer integration section exists and maps overlaps

### vidIQ Assessment
- [ ] `vidiq_comparison.md` exists and gives a clear recommendation (use as starting point, skip, or use selectively)

---
*Next: when approved → delegate via invoke_subagent (see Delegation Protocol)*
