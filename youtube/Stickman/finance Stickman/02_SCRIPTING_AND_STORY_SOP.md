# ✍️ SOP 02: Scripting Operational Harness & Story Engine (Quiet Money POV)

> **Purpose:** Operational Standard Operating Procedure (SOP) governing the complete end-to-end scriptwriting pipeline for Quiet Money POV. This document connects topic intake to pre-scripting vidIQ outlier intelligence, turnkey Claude Opus screenplay generation, post-script metadata packaging, and two-tier quality gating.
>
> ⚠️ **Core Architecture Law:** All narrative craft, the 22 Kill Rules, the POV Finance Level Architecture, character laws, and anti-AI-voice caps live inside [`/wealth-psychology-scriptwriter-2`](file:///C:/Users/renu5/.gemini/config/skills/wealth-psychology-scriptwriter-2/SKILL.md). This SOP operates as the permanent production harness that feeds, deploys, packages, and verifies every script.

---

> ### 📌 Alternate Script Style Available: POV Finance Style
>
> We have reverse-engineered and cloned the exact script writing format used by **@POVFinanceUS** (25K+ subs, 4.47M views, 14 transcripts forensically analysed). This is an **alternate script writing style** — not our default.
>
> **When to use it:** When Priyanshu explicitly says "write in POV Finance style" or "use the POV Finance format." This style uses timestamped cold opens, "Level one / two / three" chapter cards, a recurring foil named Daniel, a mentor aphorism planted at 15% and decoded at 95%, the crossover beat, a cost chapter, and exact coda reprises. It runs at ~150 WPM for 22–35 minute scripts.
>
> **Style file:** [`POV_FINANCE_SCRIPT_WRITING_STYLE.md`](file:///c:/Users/renu5/Downloads/priyanshu%20readme/youtube/Stickman/finance%20Stickman/POV_FINANCE_SCRIPT_WRITING_STYLE.md)

---

## 1. Production Parameters & Runtime Scaling (20–25 Minutes)

* **Target Runtime:** **20.0 – 25.0 minutes** (1,200 – 1,500 seconds).
* **Speaking Pacing:** **180–195 WPM** (measured via ElevenLabs `eleven_v3` with channel voice).
* **Word Budget:** **3,800 – 4,700 words total** ($\pm 5\%$), calculated dynamically:
  $$\text{Word Budget} = \text{Target Runtime (min)} \times 185\text{ WPM}$$
  - *20.0 Min:* ~3,800 words (range: 3,600 – 4,000 words)
  - *22.5 Min:* ~4,200 words (range: 4,000 – 4,400 words)
  - *25.0 Min:* ~4,700 words (range: 4,500 – 4,900 words)
* **Hook Word Cap:** Strictly **50 words maximum** (for 20–25 minute runtime: 15–20 seconds spoken).

---

## 1.1 Audience Psychology & Comment Forensics Mandates

Derived directly from forensic comment analysis of top-performing videos across 70+ channels:

### 1. Permission and Affirmation, Not Instruction
The top-liked comments on viral POV finance videos are never *"thanks for the tips."* They are:
- *"I needed to hear this today."*
- *"This is my exact life right now."*
- *"Finally someone said it out loud."*
**Scripting Rule:** The audience is not looking for a lecture; they are looking for validation that their quiet financial choices, frugality, or refusal to keep up with the Joneses are legitimate.

### 2. Emotional Resonance Over Financial Accuracy
Top comments discuss friendship loss, isolation, embarrassing silence at dinners, and family judgment—not compound interest formulas.
**Scripting Rule:** Every script must lead with an emotional/social anchor in the first 60 seconds (a relatable human dilemma, office friction, or family pressure). Mathematical formulas and balance deltas must only be introduced after the emotional stakes are firmly locked.

### 3. Absolute Mathematical Integrity (Zero Inflated Math)
Audiences actively police return calculations. Comments with 100+ likes ruthlessly mock scripts using unrealistic 10%–12% compounding or fantasy dividend yields.
**Scripting Rule:** 
- Every calculation must use real inflation-adjusted historical baselines (6.7% to 7.2% real S&P 500 CAGR).
- Never round up to make numbers look prettier.
- Show formulas on screen and cite data sources (Bureau of Labor Statistics, Federal Reserve, S&P historical averages).

### 4. Second-Person POV Format Superiority
Competitive analysis proved third-person explainers (*"In 2008, the market crashed..."*) suffer from flat subscriber conversion and high drop-off. Second-person immersive framing (*"You took the trade. Your brother took the degree..."*) triggers intense viewer self-identification. All scripts must remain 100% in second-person POV.

---

## 2. Phase 1: Pre-Scripting Intelligence & Intake (THE MANDATORY STARTING POINT)

Whenever we start a script, we **always** begin with this step. We feed the topic and premise into vidIQ AI Coach to harvest verified outlier benchmarks and high-impact dialogue lines before drafting.

### 2.0 PROMPT 1.5: The 5-Video Outlier Benchmark, High-Impact Line & Story-Format Architecture Harvester

> **Where to paste:** `app.vidiq.com` → AI Coach (Enable **Deep Thinking**)  
> **Cost:** 25 Credits (Deep Thinking Mode)  
> **Frequency:** Run per topic before writing any new script.  
> **Core Principle:** **vidIQ does NOT write the script.** AI Coach in **Deep Thinking (25 Credits)** processes all 5 outlier transcripts in full in one single pass. This guarantees **zero hallucinations**, extracts the top 5 benchmark videos (50x+ breakout), and harvests:
> 1. Their most visceral, memorable, and high-impact lines video-by-video with psychological placement guidance.
> 2. **The Exact Narrative Format & Story Arc of each video** broken down like an expert scriptwriter (Hooks, Story Beats, Pacing Mechanisms, Conflict Points, Math Turning Points, and Payoffs).
>
> These harvested lines AND architectural format breakdowns are then fed into Claude Opus (`/wealth-psychology-scriptwriter-2`). This allows Claude Opus to understand precisely how each video was engineered, distill the winning narrative flows, and synthesize the ultimate custom script tailored to our topic.

```text
Act as a Master Script Analyst, YouTube Forensic Transcript & Virality Researcher.

[EXECUTION MODE: 25 CREDITS DEEP THINKING — PROCESS ALL 5 TRANSCRIPTS IN FULL WITH ZERO HALLUCINATIONS]

I am preparing to write an original, high-retention 20–25 minute second-person POV script for our faceless wealth psychology channel @quietmoneypov.
Our Video Topic & Title: [INSERT TOPIC / TITLE e.g., "POV: You Kept the Same Car for 20 Years — Here's What It Built"]
Core Premise: [INSERT 1-2 SENTENCE PREMISE e.g., "Driving a modest paid-off car for 20 years instead of paying $765/mo auto notes, investing the difference into S&P 500, and building $383,800 liquid freedom while coworkers drown in debt."]

Your task is to analyze YouTube for the TOP 5 OUTLIER & SIMILAR VIDEOS on this exact topic or closely related financial themes (from both small breakout channels and established finance creators). Read their transcripts in depth.

Do NOT write a script. Instead, deliver the forensic intelligence in these 6 structured sections:

### 1. THE 5 BENCHMARK OUTLIER VIDEOS:
Identify 5 specific high-performing or outlier videos on this topic. For each:
- Video Title & Channel Name
- View Count & Outlier Breakout Ratio (Target: 50x+ channel average, e.g., 50x to 100x+ breakout)
- Core Angle: What was this video's unique angle or emotional entry point?

### 2. THE BEAT MAPS OF NARRATIVE STRUCTURE & SCENE VIGNETTES (Video by Video — 1 through 5):
Act as an elite script doctor. Break down the EXACT beat maps of narrative structure and storytelling engine used by EACH of the 5 videos so our AI scriptwriter (Claude Opus 4.6) can understand how each narrative was built:
For EACH of the 5 reference videos, provide:
- Video Title & Format Archetype: (e.g., 'Two-Character Parallel Timeline', 'Chronological Life-Phase Ladder', 'First-Person Confessional into 30-Year Mathematical Audit', etc.)
- Opening Hook Anatomy & Summary: How does the hook open? What is the opening tension, first line, and cognitive contract? Summarize the hook structure concisely in the exact tone of the script.
- Beat Map of Narrative Structure & Scene Vignettes:
  Because the raw transcripts are massive, distill the entire narrative into its sequential beats. For EVERY chronological beat (e.g., Beat 1: Initial purchase & status disparity -> Beat 2: The dealership financing trap -> Beat 3: The 5-year social friction test -> Beat 4: Compounding crossover -> Beat 5: Retirement divergence):
  * Beat Label & Core Conflict: What happens in this specific beat.
  * Beat Scene Vignette: A 2–3 sentence dramatized summary of this beat written as an active scene (using second-person POV, concrete physical objects, and the original transcript's blunt, unpolished sentence cadence).
- Pacing & Retention Mechanics: How does this specific video keep viewers watching? (e.g., frequent scoreboard cards, recurring character foil, sensory vignettes, dramatic dialogue intercuts).
- Climax & Emotional Resolution: How does the video conclude its argument, and what makes the final payoff feel earned?

### 3. ALL HIGH-IMPACT LINES BY REFERENCE SCRIPT (Comprehensive & Unlimited Harvest — Video by Video):
Do NOT limit yourself to 10 lines. Extract ALL usable, high-impact, and unforgettable lines from EACH of the 5 reference video scripts that created massive viewer resonance or retention.
Organize the harvest video-by-video (Video 1 through Video 5):

For EACH of the 5 Videos, provide:
- Video Title & Channel Name
- Harvested Impact Lines & Recommended Placement:
  For EVERY single line extracted, tell us:
  * The Exact Line / Quote: (The punchy, memorable line).
  * Where to Use It in Our Script & Why: (Based on viewer psychology, tell us where this line can be used most effectively in our script—whether in the opening hook, during a confrontation, to build tension, at a mathematical turning point, or as an emotional ending payoff—to impress the viewer and keep them hooked).

### 4. THE 3 RETENTION DROPS & CLICHE TRAPS TO AVOID:
- Where did these reference videos get boring, lecture-heavy, or repetitive?
- Which generic financial clichés must our script strictly avoid?
- What pacing mistakes caused viewers to drop off?

### 5. THE 40% KNOWLEDGE & EMOTIONAL GAP:
- What did all 5 videos fail to address? (e.g., the psychological awkwardness in office garages, family guilt, the quiet triumph of sovereign cash).
- What is the single biggest unsaid truth our 20-minute POV script can exploit that NONE of these 5 videos said?

### 6. TOP 5 HIGH-CTR TITLE ALTERNATIVES WITH THUMBNAIL PAIRING:
Generate 5 high-CTR, curiosity-driven title alternatives under 70 characters with paired thumbnail concepts suitable for a faceless 2D stickman channel.
```

---

### 2.1 Live Fact-Checking & Mathematical Ground Truth (via Exa MCP)

* **The Ground Truth Law:** **Data is gathered AFTER research, NEVER assumed beforehand.** If numbers are written before research, they risk hallucination and instant viewer backlash.
* **Exa MCP Integration (`web_search_exa`):** Use Exa MCP directly in the workspace to retrieve verified, real-world primary economic data:
  1. *Debt & Payment Realities:* Exact current auto loan debt, average monthly note, and loan durations from Experian / LendingTree (e.g., $765/mo new, $542/mo used, 69.5 month average term, $1.713T total auto debt).
  2. *Inflation-Adjusted Returns:* Verified historical real S&P 500 CAGR from official sources (Investopedia: 6.69% real CAGR since 1957; 6.81% since 1928).
  3. *Wage Baselines for Unit Conversions:* Official median full-time weekly earnings from the U.S. Bureau of Labor Statistics (BLS median full-time earnings) to ground time-conversion formulas ($765/mo = ~24.5 hours of work).
* **Assembly Rule:** Combine vidIQ's harvested lines with Exa's real-time verified data into `dossier/script_intake.md` before writing begins.

---

### 2.2 Standard Intake Template (`dossier/script_intake.md`)

```markdown
# Script Intake Dossier: [Episode Title]

## 1. Topic Authorization Answers (Mandatory 1-Sentence Rules)
- Whose unspoken struggle is this?: [e.g., The 24-year-old making $45k who feels behind because coworkers are leasing $60k trucks.]
- What is the journey from → to?: [From feeling ashamed of driving a dented 2008 Honda to realizing silent liquidity bought 8 years of life autonomy.]
- What does the viewer suspect that we confirm?: [That everyone financing luxury status is one missed paycheck away from total collapse.]

## 2. The 40% Competitor Gap Map, Beat Maps & Scene Vignettes (from vidIQ Prompt 1.5)
- Top 5 Benchmark Reference Videos (50x+ Outliers):
  - Ref Video 1: [Title & Channel Name | Outlier Breakout Ratio e.g. 78x]
    - Format Archetype: [e.g., Two-Character Parallel Timeline / Chronological Life-Phase Ladder]
    - Hook Anatomy & Tone: [Opening tension, first line, cognitive contract, summarized in original voice]
    - Beat Map of Narrative Structure & Scene Vignettes:
      - Beat 1 [Label]: [Dramatized 2–3 sentence micro-scene preserving the transcript's raw second-person POV, sensory anchors, and psychological tension]
      - Beat 2 [Label]: [Dramatized 2–3 sentence micro-scene...]
      - Beat 3 [Label]: [Dramatized 2–3 sentence micro-scene...]
      - Beat 4 [Label]: [Dramatized 2–3 sentence micro-scene...]
      - Beat 5 [Label]: [Dramatized 2–3 sentence micro-scene...]
    - Line: "[Quote / Impactful line]" -> Recommended Placement: [Where in script to use it & why, as recommended by vidIQ]
    - Line: "[Quote / Impactful line]" -> Recommended Placement: [Where in script to use it & why, as recommended by vidIQ]
  - Ref Video 2: [Title & Channel Name | Breakout Ratio]
    - Format Archetype: [...]
    - Hook Anatomy & Tone: [...]
    - Beat Map & Scene Vignettes: [...]
    - Line: "[Quote...]" -> Recommended Placement: [Where in script to use it & why]
  - Ref Videos 3–5: [Harvested beat maps, scene vignettes, and impact lines organized by video...]
- Saturated Competitor Points (Skip / Max 1 line): [e.g., "Compound interest is magic", "Save 20% of your paycheck"]
- Knowledge & Emotional Gaps (Must form >=40% of narrative): [e.g., The awkward silence when peers realize you have no debt; the dealer finance office kickback scam.]

## 3. Real-Rate Mathematical Model (7–8% Real S&P 500)
- Asset / Contribution: [$100 initial + $200/month recurring]
- Real Inflation-Adjusted Return Rate: [7.2% annualized]
- Milestone 1 (Year 3): [$7,980 liquid — equivalent to 3.5 months of total emergency survival]
- Milestone 2 (Year 7): [$23,400 liquid — equivalent to the entire sticker price of the coworker's depreciated SUV]
- Milestone 3 (Year 15): [$74,800 liquid — compounding accelerates past annual salary contributions]
- Source / Citation: [Historical S&P 500 Real CAGR 1970–2025, Bureau of Labor Statistics]

## 4. Pre-Calculated Unit Conversions (Dollars → Time / Silence)
- $389/month truck payment = 11 days of work every single month just to sit in traffic
- $10,000 liquid buffer = 6 months of being able to tell a toxic boss "no" without blinking
- $100 invested on a Tuesday = buying back 4 hours of your future Friday afternoons

## 5. Topic-Driven Protagonist Wardrobe Requirement (Immutable Character Law)
- Setting / Social Role: [e.g., Corporate office / Blue-collar trade / Bank meeting / Domestic saver]
- Protagonist Wardrobe Specification: [Define episode costume tailored to topic: e.g., 'Sky-blue oxford shirt with rolled sleeves and slate chinos' OR 'Rugged canvas work jacket and boots' OR 'Default oatmeal sweater fallback']
- Core Facial Identity Reminder: Consistent 2D cel-shaded face across all videos (side-swept dark brown hair, calm observant eyes, 100% neutral/peaceful stoic expression ALWAYS).
```

---

## 3. Phase 2: Turnkey Skill Invocation Prompt (Claude Opus Scriptwriting)

Once `dossier/script_intake.md` is populated with the vidIQ harvested lines and verified numbers, paste or send this master prompt into Antigravity chat to trigger the `/wealth-psychology-scriptwriter-2` skill:

```text
/wealth-psychology-scriptwriter-2

Write a full-length, masterclass second-person POV script for Quiet Money POV following every locked rule in your skill.

EPISODE PARAMETERS:
- Title: [INSERT TOPIC/TITLE e.g., POV: You Kept the Same Car for 20 Years — Here's What It Built]
- Target Runtime: 20–25 Minutes (Word Budget: 3,800–4,700 words at 185 WPM)
- Hook Cap: 50 words maximum (fast 0:00–0:40 hyper-hook)

20–25 MINUTE SCALING ARCHITECTURE:
- Beat Map Format: POV Finance Level Architecture (Cold Open -> Thesis Negation -> Level 1 Mentor Plant -> Levels 2-5 -> Crossover Beat -> Cost Chapter -> Aphorism Decoded -> Coda Reprise -> Narrative CTA)
- Mentor Aphorism: Plant at ~15% in Level 1; decode at ~90%.
- Recurring Mundane Object: Appears in first 30s, appears 3+ times, appears in Coda reprise.
- Character Escalation: Minimum 3 named characters (e.g., Daniel as the foil, Christopher as the mentor, Jessica as the partner).
- Three-Part Number Weld: Weld every number to a physical body/moment and execute at least 2 unit conversions (Dollars -> Time/Silence).
- Crossover Math: Must use real verifiable arithmetic (take-home pay vs portfolio growth).
- Harvested Line & Beat Map Synthesis: Synthesize the harvested Beat Maps of Narrative Structure from the 5 outlier videos into our custom story arc, and integrate ALL high-impact lines (listed in Section 2 of the Input Dossier) into the narrative at the exact psychological moments recommended by vidIQ (hook, confrontation, math shock, emotional payoff).

INPUT DOSSIER:
[PASTE CONTENTS OF dossier/script_intake.md HERE]

OUTPUT DELIVERABLE REQUIREMENT:
Deliver BOTH mandatory copies in full without truncation:
1. Copy 1: Main Script with visual tags [V: ...] at every paragraph, ending with the complete Script Report.
2. Copy 2: Clean TTS Script for ElevenLabs (visual tags stripped, numbers spelled as words, phonetic pronunciation, breath breaks).
```

---

## 4. Phase 3: Post-Script Packaging & Virality Pre-Flight (via vidIQ AI Coach)

Once Claude Opus drafts the script, we run these two prompts in `app.vidiq.com` → AI Coach to lock packaging and ensure virality.

### 4.1 PROMPT 2: Script-First Title & Full SEO Suite (Minus Thumbnail)

> **Where to paste:** `app.vidiq.com` → AI Coach  
> **Cost:** 10 Credits  
> **Frequency:** Run per video after your script draft is written.

```text
Act as a YouTube Packaging & Metadata Expert.

Here is my finalized script for a faceless finance/wealth video:

SCRIPT:
[PASTE FINISHED SCRIPT HERE]

Based strictly on the core conflict, emotional payoff, and central paradox of this script, generate the complete packaging and SEO suite (excluding the thumbnail):

### 1. TEN CATCHY TITLE CANDIDATES (Ranked with vidIQ Predicted Scores)
Generate 10 high-CTR title variations designed for Tier-1 audience (18–35) across these 3 psychological categories:
- Category A: The Stealth Paradox / Social Friction (3 titles) (e.g., "POV: You Quietly...")
- Category B: The Broken System / Hidden Trap (4 titles) (e.g., "The Math Trap Keeping...")
- Category C: The Unspoken Mistake / Late Realization (3 titles) (e.g., "The $100k Mistake...")

For each title:
- Provide predicted vidIQ Title Score (0–100). Target: >= 80.
- State why it creates high curiosity without feeling like cheap clickbait.
- Highlight your single #1 recommended title.

### 2. FULL CONVERSATIONAL SEO DESCRIPTION
- Write a 2-paragraph description in second-person POV.
- Naturally integrate high-volume search intent keywords without keyword stuffing.
- Include 4 to 6 curiosity-inducing timestamp chapter labels mapping the 20–25 minute video turning points.

### 3. TAGS & KEYWORD CLUSTERS
- 15 targeted YouTube tags (mix of broad niche tags and specific long-tail search queries).
- 3 primary keyword clusters to target in video metadata.
```

---

### 4.2 PROMPT 3: Daily Pre-Flight Virality & Retention Audit

> **Where to paste:** `app.vidiq.com` → AI Coach  
> **Cost:** 10 Credits  
> **Frequency:** Run per video before sending script to voiceover.

```text
Act as a ruthless YouTube Retention Auditor & Algorithm Simulator.

I am preparing to send this script to voiceover and visual assembly. Before I spend production resources, audit whether this script can succeed on YouTube.

TITLE: [INSERT SELECTED TITLE FROM PROMPT 2]

SCRIPT:
[PASTE DRAFT SCRIPT HERE]

Answer these 4 diagnostic questions with zero sugarcoating:

### 1. VIRALITY POTENTIAL SCORE (0–100)
- Score this script's virality potential purely on narrative strength, emotional resonance, and retention pacing.
- Does this script have the power to break out on a small channel (<10k subscribers)? Why or why not?

### 2. RETENTION & ENGAGEMENT AUDIT (Sentence-by-Sentence Drag Check)
- Will this script maintain >50% Average Percentage Viewed (APV)?
- Quote any specific lines, paragraphs, or transitions that drag, sound like generic textbook advice, or create viewer fatigue.
- How can those specific lines be rewritten to restore momentum?

### 3. TITLE-SCRIPT ALIGNMENT CHECK
- Does the opening 45 seconds immediately honor the emotional promise of the title?
- Does the viewer get hooked on the central question before any dry data or spreadsheet numbers appear?

### 4. FINAL PRODUCTION VERDICT
- State definitively: 
  [PASS FOR PRODUCTION] — Ready for voiceover synthesis.
  OR
  [REVISE BEFORE PRODUCTION] — List the exact 2 or 3 edits needed to pass.
```

---

## 5. Phase 4: Two-Copy Pipeline Output Routing

When `/wealth-psychology-scriptwriter-2` generates the output, save the components into their dedicated pipeline locations inside `projects/[NN]_[topic]/`:

| Output Component | Destination File | Consumer Pipeline Stage |
|---|---|---|
| **Copy 1: Visual Script** | `projects/[NN]_[topic]/script_v1.md` | Ingested by the **Screenplay Director Manifest** (`screenplay_director_manifest-part-of-4-or-screenplay-writing-.md`) to construct `screenplay.md` with transitions, SFX, and kinetic typography. |
| **Copy 2: Clean TTS Script** | `projects/[NN]_[topic]/audio/voiceover_clean.txt` | Directly feeds **SOP 03** (ElevenLabs v3 narration generation & timestamp extraction). |
| **Script Report & Math Log** | `projects/[NN]_[topic]/dossier/script_audit.md` | Permanent archive for YouTube Partner Program appeal defense and mathematical verification. |

---

## 6. Phase 5: Two-Tier Quality Verification Gate & Model Specialization

> [!IMPORTANT]
> ### 🤖 MODEL ARCHITECTURE & ROLE ASSIGNMENT:
> 1. **Claude Opus (The Script Creator):**
>    - Uses `/wealth-psychology-scriptwriter-2` to craft the master 20–25 minute script.
>    - **STRICT OPUS FORBIDDEN RULE:** Claude Opus MUST NEVER read or execute `UNIFIED_SCRIPTWRITING_QUALITY_GATE.md`. At 72 KB (~20,000+ tokens), loading this massive gate file into Opus burns excessive context tokens and risks token exhaustion. Opus only validates its own internal Skill Report metrics (Tier 1).
> 2. **Gemini 3.8 Flash / Gemini 3.1 Pro (The Forensic Quality Gate Auditor):**
>    - With its massive 1M+ token context window and lightning speed, **Gemini 3.8 Flash is exclusively assigned to audit the finished script against `UNIFIED_SCRIPTWRITING_QUALITY_GATE.md`**.
>    - Gemini executes all 7 stages (Stages 0–7) independently to ensure complete objective rigor (an author model should never grade its own work).

### Tier 1: Skill Report Metrics Audit (Checked by Scriptwriter / Opus)
Check the appended report at the bottom of the script:
- [ ] **Word Count:** Within 3,800 – 4,700 words ($\pm 5\%$).
- [ ] **Hook Words:** Under the 50-word cap.
- [ ] **Visual Completeness:** Exactly zero `[V: NONE]` tags in Copy 1.
- [ ] **Character Count:** At least 3 distinct named characters with quoted dialogue.
- [ ] **Unit Conversions:** At least 2 verified conversions of dollars into time/silence/distance.
- [ ] **Crossover Math:** Confirmed realistic arithmetic where portfolio growth outpaces take-home pay.

### Tier 2: The Full 7-Stage Quality Gate Audit (Checked by Gemini 3.8 Flash ONLY)

Use this **Turnkey Gemini Quality Gate Audit Prompt** whenever running on Gemini 3.8 Flash / Gemini 3.1 Pro:

```text
Act as the Master YouTube Script Quality Auditor for Quiet Money POV.

Execute an exhaustive forensic audit of our draft script against UNIFIED_SCRIPTWRITING_QUALITY_GATE.md. 

INPUT FILES:
- Draft Script: projects/[NN]_[topic_slug]/script_v1.md
- Master Quality Gate: UNIFIED_SCRIPTWRITING_QUALITY_GATE.md

AUDIT PROTOCOL — EXECUTE ALL 7 STAGES IN ORDER:
1. Stage 0: Topic Authorization (7 Binary Tests: Mechanism, Ladder, Invisible-Cost, Second-Person, Send, Secret, Stranger)
2. Stage 1: Instant Disqualification (Check all 22 Kill Triggers: autobiography, "Picture this", announced numbering, act-percentage scaffolding, moralizing endings, CTA stacks. Any single hit = immediate REJECT)
3. Stage 2: Must-Pass Binary Criteria (20 checks: physical opening within 3 sentences, named emotion in 10s, cognitive contract in 60s, three-part number welds, 3 named characters, escalating non-monetary costs)
4. Stage 3: Scored 100-Point Rubric (Detailed scoring across 10 categories. Must score >= 85/100 to pass)
5. Stage 4: Adversarial Re-Read (Hostile forensics pass hunting for boring sections, unearned progress, or flat dialogue)
6. Stage 5: Banned Patterns Sweep (Ctrl+F scan for forbidden buzzwords: "delve", "tapestry", "in today's world", "That's not X, that's Y", etc.)
7. Stage 6: Production Pass (Visual tags [V:] completeness, ElevenLabs TTS readiness)
8. Stage 7: Formal Sign-Off Verdict (Issue strictly: PASS, REJECT — PREMISE, or REJECT — DRAFT)

OUTPUT DELIVERABLE:
Write the complete audit report to: projects/[NN]_[topic_slug]/dossier/quality_gate_audit.md.
If REJECTED, cite the exact line numbers and provide concrete rewrite instructions.
```

### Hand-off Action:
Once Gemini issues a formal `PASS` verdict:
1. Update `projects/[NN]_[topic]/README.md` checklist: `[x] Scripted`.
2. Proceed immediately to **SOP 03 (ElevenLabs Audio & Timestamps)** to generate `voiceover.wav` and extract `cut_durations.json`.
3. Ingest `script_v1.md` and `cut_durations.json` into the **Screenplay Director Manifest** ([`screenplay_director_manifest-part-of-4-or-screenplay-writing-.md`](file:///c:/Users/renu5/Downloads/priyanshu%20readme/youtube/Stickman/finance%20Stickman/screenplay_director_manifest-part-of-4-or-screenplay-writing-.md)) to compile the machine-parseable `screenplay.md`. **Mandatory First Step:** The Director locks the protagonist's topic-adaptive wardrobe (preserving the 100% consistent neutral face across videos) before tagging the 58 xfade transitions, 31 Remotion SFX cues (-60ms pre-roll), and 6 Void Canvas typography archetypes.
4. Hand off `screenplay.md` to **SOP 04 (Screenplay-Driven Visuals)** and **SOP 05 (FFmpeg Assembly)**.
