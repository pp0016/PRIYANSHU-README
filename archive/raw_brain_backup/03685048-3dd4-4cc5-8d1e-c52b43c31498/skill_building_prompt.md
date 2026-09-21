# Skill-Building Conversation Prompt

> **Copy-paste everything below into a new conversation.**
> **Model:** Opus 4.6 (Thinking) for ALL phases. Do not switch models.
> **Confirmed decisions from /grill-me session (Aug 17, 2026):**
> - Skill name: `ai-writing-gaps` ✅
> - Top 20 topic list: FINAL, no changes ✅
> - Pattern library: Universal patterns + channel-specific blueprints + learning loop ✅
> - Learning loop: Auto-append, but FILTER — only add truly exceptional patterns, not everything ✅
> - Transcript source: Competitor videos on the SAME TOPIC the user is currently making a video about ✅
> - Self-audit: YES — the skill should also audit the user's own scripts and flag AI-sounding lines with specific fix suggestions ✅

---

## Your Mission

You are building a skill called `ai-writing-gaps`. This skill fixes the structural problems in AI-generated YouTube scripts that `/humanizer` cannot catch. Humanizer handles surface tells (em dashes, "vibrant tapestry", rule-of-three). This skill handles the deeper architecture: pacing, source integration, emotional contrast, narrative bridges, and the specific choices that make human-written scripts retain viewers.

**Before you do ANYTHING, read this skill:**
```
C:\Users\renu5\.gemini\config\skills\skill-creator\SKILL.md
```

You will use `/skill-creator` in Phase 3 to build the actual skill. Learn its format and requirements now.

---

## Source Files (Read These As Instructed Per Phase)

### The 20-Topic List (Phase 1)
```
C:\Users\renu5\Downloads\priyanshu readme\niche_research\top_20_video_topics.md
```

### The Human Script DNA Corpus (Phase 2)
All files are in: `C:\Users\renu5\Downloads\priyanshu readme\niche_research\human_script_dna\`

**Key synthesis files (READ ALL in Phase 2):**
| File | Size | What It Contains |
|------|------|-----------------|
| `ai_writing_gaps.md` | 23.7 KB | **THE CORE** — 11 structural AI failures with real transcript evidence. This is the soul of the skill. |
| `cross_channel_convergence.md` | 60.8 KB | 6 universal DNA patterns, 4 channel styles, 5 counter-intuitive findings, full quantitative matrix |
| `script_dna_template.md` | 50.5 KB | 10-dimension production template with fill-in-the-blank blueprints, 12 anti-slop gates, humanizer integration matrix |
| `vidiq_comparison.md` | 52.2 KB | Verdict: "Skip vidIQ for drafting, maximize for packaging." Full 8-dimension comparison. |
| `walkthrough of md files present here.md` | 5 KB | Summary of all deliverables |

**Individual DNA analyses (SKIM in Phase 2, read 2-3 deeply):**
9 files in `analysis/` folder — one per competitor video. ~205 KB total. Each has 8 dimensions: Hook, Sources, Bridges, Pacing, Anti-Slop, Architecture, Vocabulary, Retention.

**Channels analyzed:** Brofessor Stein (3 videos), EverythingProfessor (2), Serious History (2), The Analyst (2).

**Raw transcripts (DO NOT read all — reference only if needed):**
9 `.txt` + 9 `.json` files in `transcripts/` folder. ~3.7 MB total. These are the Whisper transcriptions from Groq API.

---

## Phase Structure — STOP After Each Phase

### Phase 1 Part 1: Deep Topic Research (Topics 1-10)

**Read:** `top_20_video_topics.md`

For topics 1 through 10, go deep. For each topic:
- What makes this topic work for a faceless animated explainer channel?
- What's the specific hook angle that would drive clicks?
- What research rabbit holes would a HUMAN writer fall into that AI wouldn't find?
- What's the "wrong detail" (the weird, footnote-level fact that makes viewers stop scrolling)?
- How would this topic be structured — catalog format? Narrative anthology? Diagnostic breakdown?

**Output:** A deep analysis of topics 1-10 with structural recommendations for each.

> [!IMPORTANT]
> **STOP HERE.** Create an implementation plan for Part 2. Wait for my approval before continuing.

---

### Phase 1 Part 2: Deep Topic Research (Topics 11-20)

Same depth as Part 1, for topics 11 through 20.

**Output:** Deep analysis of topics 11-20.

> [!IMPORTANT]
> **STOP HERE.** Create an implementation plan for Phase 2. Wait for my approval before continuing.

---

### Phase 2: Pattern Extraction — The HOW, Not the WHAT

**Read ALL synthesis files listed above.** Then skim the 9 individual DNA analyses.

**Critical instruction:** I don't want quotes or famous writers' lines. I want HOW they write. The patterns, rhythms, and choices that AI cannot replicate even after running `/humanizer`.

For each of the 11 items in `ai_writing_gaps.md` (and any new patterns you discover in the other files):

Extract the MECHANISM. Not "Serious History uses emotional whiplash." Instead:
- **What triggers it:** After every section describing violence or death
- **What it looks like:** A modern slang phrase dropped into a historical context ("Bro could have really used a prenup" about a 19th-century gold rush millionaire)
- **Why AI can't do it:** AI maintains a consistent register. It won't risk breaking tone because its training optimizes for coherence, not contrast.
- **How to detect its absence:** If reading a script aloud, you never laugh or exhale between dark sections, the whiplash is missing.
- **How to implement it:** After every intense section (death, violence, betrayal), insert ONE sentence that shifts register — modern slang, dark humor, or a narrator reaction that breaks the fourth wall.

Do this for EVERY pattern. The output should be a complete "HOW to write like this" manual, not a "WHAT they write" summary.

**This skill works ALONGSIDE `/humanizer`, not replacing it:**
- Humanizer = surface pass (catches 33 mechanical AI tells)
- This skill = structural pass (catches the 11+ deeper failures that survive humanizer)

**Output:** Complete pattern extraction document with mechanisms, detection methods, and implementation instructions for each pattern.

> [!IMPORTANT]
> **STOP HERE.** Create an implementation plan for Phase 3. Wait for my approval before continuing.

---

### Phase 3: Build the Skill Using /skill-creator

Use the `/skill-creator` skill (which you read at the start) to build the actual `ai-writing-gaps` skill.

**Skill requirements:**

1. **Name:** `ai-writing-gaps`
2. **Location:** `C:\Users\renu5\.gemini\config\skills\ai-writing-gaps\`
3. **Trigger phrases:** "fix my script", "check for AI patterns", "structural pass", "script DNA", "writing gaps", "deep script check", "why does this sound like AI", "make this sound human", "retention check", "anti-slop audit", "script QA", "pass 2"
4. **Must NOT trigger on:** surface humanizer tasks (those go to /humanizer)
5. **Works with:** `/humanizer` (surface pass first, then this skill for structural pass)

**The skill MUST contain:**

**A. The Pattern Library (Universal + Channel Blueprints)**
Two sections:

**Section 1: Universal Patterns** — things ALL 4 channels do. Each pattern needs:
- Name
- What it is (1 sentence)
- How to detect its absence in a script
- How to fix it (specific instruction, not vague advice)
- Benchmark from competitor data (e.g., "10.23 sources per 1,000 words")

**Section 2: Channel-Specific Blueprints** — selectable writing styles:
- Esoteric Catalog (Brofessor Stein model) — relic/artifact/symbol listicles, dense archival sourcing
- Diagnostic Armor (EverythingProfessor model) — psychological/scientific explainers, staccato rhythm
- Retribution Anthology (Serious History model) — 3-story deep narratives, dark comedic juxtaposition
- Pop-Culture Autopsy (The Analyst model) — system/concept explainers, pop culture analogies

The user should be able to say "write in Brofessor Stein style" and the skill applies that blueprint's specific patterns.

**B. The Two-Pass QA Checklist**
A step-by-step checklist that runs AFTER `/humanizer`:
1. Run humanizer (surface pass — 33 checks)
2. Run ai-writing-gaps (structural pass — 11+ checks)
3. Score the script on each dimension
4. Flag specific lines that fail each check
5. Suggest specific rewrites for flagged lines

**C. The Learning Loop (MANDATORY)**

This is the most important feature. Every time I upload a new transcript (competitor video, my own script, or any reference material), the skill should:

1. **SCAN** the transcript for good human writing patterns that AI + humanizer still can't produce
2. **CATCH** those patterns — identify exactly what the pattern is, why it works, and why AI wouldn't generate it
3. **FILTER** — only keep truly exceptional, novel patterns. Not everything is worth adding. The agent must be selective and only append patterns that are genuinely different from what's already in the library.
4. **ADD** the filtered patterns to `learned_patterns.md` inside the skill folder
5. **TELL ME** exactly what got added — pattern name, example from the transcript, and why it matters

**IMPORTANT context for the learning loop:** The transcripts the user uploads will be competitor videos on the SAME TOPIC they're currently making a video about. So the skill should also extract topic-specific patterns (how competitors handle THIS specific subject), not just general writing patterns.

The skill gets better after every script I feed it. The learned_patterns.md file grows over time.

**Implementation of the learning loop:**
```
C:\Users\renu5\.gemini\config\skills\ai-writing-gaps\
├── SKILL.md              # Main skill instructions
├── pattern_library.md    # Base patterns from Phase 2
├── learned_patterns.md   # Grows with every transcript upload
├── qa_checklist.md       # Two-pass QA system
└── benchmarks.md         # Competitor benchmarks (WPM, source density, etc.)
```

When the skill detects a new pattern from an uploaded transcript, it should:
```
## New Pattern Detected: [PATTERN_NAME]
- **Source:** [transcript filename]
- **Topic relevance:** [how this pattern relates to the specific topic being researched]
- **Example:** [exact quote from transcript]
- **What makes it human:** [why AI wouldn't generate this]
- **Detection:** [how to check if a script is missing this]
- **Fix:** [how to add this pattern to a script]
- **Quality gate:** [why this pattern passed the filter — what makes it exceptional]
- **Added to:** learned_patterns.md on [date]
```

**E. Self-Audit Mode (For User's Own Scripts)**
When the user runs the skill on their OWN script (not a competitor transcript), the skill should:
1. Run through all patterns in the library (base + learned)
2. Flag specific lines/paragraphs that fail each check
3. For each flagged line, provide a SPECIFIC rewrite suggestion (not "make it more vivid" — show the actual rewritten line)
4. Score the script on each dimension (1-10)
5. Give an overall "human score" percentage
6. List the top 3 most impactful fixes that would improve the script the most

**D. The Benchmark Reference Card**
Quick-reference numbers from the DNA analysis:
- Average speech rate: 149.8 WPM
- Source density: 10.23 named sources per 1,000 words
- Reading level: Grade 9.6 (Flesch-Kincaid)
- Time to topic: 0.10 seconds (zero throat-clearing)
- Average segment count: 10 per video
- Average segment duration: 164.3 seconds
- Hook architecture: Category anchor (0-8s) → Paradox/discord (8-18s) → Macro promise (18-30s)

**Output:** The complete skill, installed at the path above, with all 4 components (A-D).

> [!IMPORTANT]
> **STOP HERE.** Show me the skill structure and ask for final approval before finishing.

---

## Rules for This Conversation

1. **After each phase, STOP.** Make an implementation plan for the next phase. Wait for my "go."
2. **Don't skip any point.** Every item in this prompt must be addressed.
3. **Don't summarize the DNA files.** Extract HOW they write, not WHAT they write.
4. **The skill must work alongside `/humanizer`.** It's Pass 2, not a replacement for Pass 1.
5. **The learning loop is non-negotiable.** The skill MUST get smarter with every transcript.
6. **Use `/skill-creator`** to build the skill in Phase 3. Read its SKILL.md first.
7. **Be blunt.** Use the anti-sycophancy mindset — if something in the DNA analysis is weak, say so. If a pattern is redundant with humanizer, drop it. Quality over quantity.
