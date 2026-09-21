# Video 1 — Source Research Prompts

> **Purpose:** Find the best sources, reference YouTube videos, and fresh angles for "The Most Terrifying Weapons Ever Banned" BEFORE writing the script.
> **Created:** Aug 21, 2026
> **Status:** Ready to execute

---

## How to Use This File

1. **Prompt B (vidIQ) → Execute FIRST.** Paste into vidIQ web app. Get vidIQ's source and video recommendations.
2. **Prompt A (New Conversation) → Execute SECOND.** Open a new Antigravity conversation with Claude Opus 4.6 (Thinking). Paste Prompt A. When the agent asks, paste vidIQ's answers from Prompt B.

---

## PROMPT B — For vidIQ Website (Paste This First)

> **Where:** vidIQ web app chat
> **Cost:** ~5 credits
> **What you get back:** Specific YouTube videos to study + source angles that avoid recycled content

```
I'm making a YouTube video titled "The Most Terrifying Weapons Ever Banned" — a 12-minute stickman animation explainer in the "Every X Explained" catalog format.

I need your help finding the BEST source videos and unique angles. Please answer all 5 parts:

**PART 1 — REFERENCE VIDEOS TO STUDY**
Find me 8-12 YouTube videos I should watch before scripting. I need TWO types:
- Type A: Competitor videos in dark history / military explainer niche (channels like Serious History, ExplainTory, Infographics Show, Brofessor Stein, Simple History, The Paint Explainer, Armory Professor). Find their best-performing videos about banned weapons, war crimes, Geneva Convention, or weapons history.
- Type B: Non-competitor educational videos about banned weapons, chemical weapons, Geneva Convention, international law of war — from history professors, military experts, documentary channels, or legal explainers. These give me facts and angles the competitor channels missed.

For each video, tell me: title, channel, views, and WHY I should watch it (what angle or fact I can learn from it).

**PART 2 — OVERUSED ANGLES TO AVOID**
Which angles and talking points about banned weapons are ALREADY done to death on YouTube? I want to know what every other video already says so I can SKIP those obvious takes and find something fresh. What facts does every single banned weapons video repeat?

**PART 3 — FRESH ANGLES NOBODY IS COVERING**
Based on what's currently trending and what's missing in the banned weapons content space on YouTube right now — what angle would make my video feel like a HUMAN made it, not a mass-produced AI explainer? What's the non-obvious story or paradox that no channel is covering?

**PART 4 — PRIMARY SOURCES**
What are the actual legal documents, treaties, or historical accounts I should reference to give my video credibility that competitors don't have? (Example: Bernal Diaz's firsthand account of the macuahuitl, the actual text of the Hague Convention, the CCW Protocol on Blinding Lasers, etc.)

**PART 5 — WHAT'S HAPPENING RIGHT NOW (Aug 2026)**
Any current events or recent news about weapons bans, arms treaties, or weapons debates that I could reference to make my video feel timely? (Note: I CANNOT mention active military conflicts like Turkey, Sudan, Russia-Ukraine by name — demonetization risk. But I can reference treaties, laws, and policy debates.)
```

---

## PROMPT A — For New AI Conversation (Paste This Second)

> **Where:** New Antigravity IDE conversation → Claude Opus 4.6 (Thinking)
> **What you get back:** A complete `research_notes.md` file saved to `projects/01_banned_weapons/`

```
<task_brief>

## Objective
Research and compile the best sources, reference videos, and fresh content angles for a YouTube video titled "The Most Terrifying Weapons Ever Banned" — a 12-minute stickman animation explainer. Save everything to `projects/01_banned_weapons/research_notes.md`.

## Context
<context>
Read these files IN THIS ORDER before doing anything:
1. `c:\Users\renu5\Downloads\priyanshu readme\priyanshu-agent.md` — who I am, workspace rules, communication style
2. `c:\Users\renu5\Downloads\priyanshu readme\youtube\Stickman\implementation_plan.md` — production pipeline, tool stack, video order
3. `c:\Users\renu5\Downloads\priyanshu readme\youtube\Stickman\projects\01_banned_weapons\project_brief.md` — Video 1 details: hook, retention template, tags, description
4. `c:\Users\renu5\Downloads\priyanshu readme\youtube\Stickman\niche_research\phase1_part1_topics_1_to_10.md` — read ONLY Topic 1 (banned weapons) section for existing deep research

After reading these files, you will have full context on:
- The channel (Stikaman — dark history stickman animation)
- The video format ("Every X Explained" catalog, 12 min, ~1,800 words)
- The hook (Character-first: Aztec macuahuitl + Bernal Diaz)
- The retention template (minute-by-minute structure with pattern interrupts)
- The competitive landscape (Serious History, ExplainTory, Infographics Show)
- The keywords ("dark history explained" = best ratio, "stickman animation" = discovery)
- The paradox angle (nukes are legal, expanding bullets are banned)

EXISTING RESEARCH ALREADY DONE (don't redo this):
- Niche research for all 20 topics = COMPLETE
- Competitor analysis (Serious History, ExplainTory) = COMPLETE
- vidIQ keyword data = COMPLETE
- Title scoring (93/100) = DONE
- Thumbnail concepts (5 concepts with prompts) = DONE
- Hook decision (Option 1 — character-first) = LOCKED
- Video order (Weapons → Books → War Tactics → Greek Myths → Bullets) = LOCKED

WHAT'S MISSING (this is your job):
- Which specific YouTube videos should I study before scripting?
- What are the best primary and secondary sources for each weapon?
- Which weapons should be in the final video (12-15 max from 30+ candidates)?
- What's the fresh angle that makes this feel human-made, not AI-generated?
- What facts/stories does every competitor already cover (so I can SKIP them)?
</context>

## Instructions
Think carefully before starting. This is source research, NOT script writing.

<instructions>
1. Read the 4 files listed above. Confirm you've read them by listing 3 key facts from each file.

2. Search the web for: "banned weapons history", "Geneva Convention weapons banned", "weapons too cruel for war", "Hague Convention prohibited weapons", "weapons of war international law", "strangest banned weapons". Find factual sources — academic, legal, historical. NOT other YouTube scripts.

3. Search the web for: YouTube videos about banned weapons, weapons history explainers, Geneva Convention explainers, dark history weapons. Find 8-12 specific videos I should WATCH before scripting. For each video, note:
   - Title, channel name, view count
   - What unique angle or fact this video covers
   - What I can LEARN from it (not copy — learn structure, pacing, or a specific fact)

4. I will paste vidIQ's recommendations when you ask. vidIQ will give me competitor videos, overused angles, fresh angles, and primary sources. Cross-check vidIQ's recommendations against your own research. Flag disagreements.

5. Compile a WEAPON LONGLIST — every weapon that has been banned, restricted, or debated in international law. Organize by era:
   - Ancient (pre-1500)
   - Early Modern (1500-1800)
   - Industrial/WWI (1800-1918)
   - WWII era (1918-1945)
   - Modern/Cold War (1945-2000)
   - Contemporary (2000-present)
   - Currently debated (autonomous weapons, cyber weapons, etc.)

   For each weapon, note: name, what it does, when banned, by which treaty, and the ONE surprising fact that makes it interesting for video.

6. From the longlist, recommend 12-15 weapons for the final video. Selection criteria:
   - Visual variety (each weapon should look different in stickman animation)
   - Escalation (should feel like the weapons get more terrifying)
   - At least 3 paradoxes (legal vs banned contradictions)
   - Mix of eras (don't cluster all weapons in one time period)
   - At least 2 weapons nobody else covers

7. Identify OVERUSED FACTS — things every banned weapons video already says. I want to know these so the script can either SKIP them or present them with a twist. List at least 5 overused talking points.

8. Identify 3-5 FRESH ANGLES — stories, paradoxes, or perspectives that NO competitor video covers. These are the differentiators that make my video feel original.

9. Save everything to: `c:\Users\renu5\Downloads\priyanshu readme\youtube\Stickman\projects\01_banned_weapons\research_notes.md`
</instructions>

## Constraints
<constraints>
- Do NOT write the script. This is research ONLY.
- Do NOT call vidIQ MCP tools — I will paste vidIQ data manually when you ask.
- Do NOT modify any existing files except creating/writing `research_notes.md`.
- Do NOT touch `priyanshu-agent.md` — it's lightweight by design, don't add to it.
- Do NOT re-do niche research. Topic validation, competitor analysis, keyword data are DONE.
- Do NOT mention active military conflicts (Turkey, Sudan, Russia-Ukraine) by name — demonetization risk. You CAN reference treaties and policy debates.
- Do NOT duplicate data that already exists in `project_brief.md` or `phase1_part1_topics_1_to_10.md`.
- STOP and ask me before making any decision not covered by these instructions.
</constraints>

## Output Format
<output_format>
Save a single file: `projects/01_banned_weapons/research_notes.md` with this structure:

```markdown
# Research Notes — The Most Terrifying Weapons Ever Banned
## Last Updated: [date]

## Reference Videos to Watch
[Table: Title | Channel | Views | What to Learn From It]
(8-12 videos, mix of competitors and non-competitors)

## Primary Sources
[Table: Source | Type | What It Covers | Why It Matters]
(Legal documents, historical accounts, treaties)

## Weapon Longlist (All Candidates)
### Ancient (pre-1500)
[weapon name — what it does — banned by — surprising fact]
### Early Modern (1500-1800)
...
### Industrial/WWI
...
### WWII Era
...
### Modern/Cold War
...
### Contemporary
...
### Currently Debated
...

## Recommended 12-15 Weapons for Final Video
[Table: # | Weapon | Era | Why Include | Paradox? | Visual Description for Animation]

## Overused Facts to Skip or Twist
[Numbered list of 5+ talking points every competitor already covers]

## Fresh Angles (Our Differentiators)
[3-5 unique angles, stories, or paradoxes nobody else is covering]

## vidIQ Cross-Check
[Agent's analysis of vidIQ recommendations — agreements and disagreements]

## Sources Cited
[All URLs and documents referenced]
```
</output_format>

## Success Criteria
- research_notes.md exists in `projects/01_banned_weapons/`
- Contains 8-12 reference videos with specific reasons to watch each
- Contains a weapon longlist of 25+ weapons across all eras
- Contains a curated shortlist of 12-15 weapons with selection rationale
- Contains 5+ overused facts and 3-5 fresh angles
- Zero overlap with data already in project_brief.md or phase1 research
- No script content — research only

</task_brief>
```

---

## What Happens After Both Prompts Are Done

Once you have:
- ✅ vidIQ's source recommendations (from Prompt B)
- ✅ `research_notes.md` saved by the new AI conversation (from Prompt A)

**Come back to me.** I'll create the next prompt: the actual script-writing prompt that uses the research notes as input.

The sequence is:
1. ~~Source Research~~ ← **YOU ARE HERE**
2. Script Writing (next prompt — I'll build it after research is done)
3. Script Quality Pass (/humanizer + /ai-writing-gaps + /stop-slop)
4. Voiceover Prep (/voiceover-enhancer-skill)
5. Everything else (animation, thumbnails, upload)

---

*Created by the project manager. Execute in order. Don't skip steps.*
