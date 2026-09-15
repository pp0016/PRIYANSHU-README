# Execution Plan v3 — Updated Aug 18, 2026

> All previous versions had wrong assumptions. This one aligns with your actual corrections.

---

## What Changed From v2

| v2 (Wrong) | v3 (Fixed) |
|---|---|
| Both channels from Day 1 | **Stickman scripts FIRST**, Nishchay study parallel, Nishchay production later |
| Whop = find clients, cold DMs | Whop = community marketplace. Join, pick up RPM deals, clip, upload. |
| Filled in niche details | **No niche plans given yet.** Plan waits for your input. |
| 30-day monetization math | Removed. Don't bring up unless asked. |
| Voice cloning recommendation | Deleted. |
| 20-step daily plans | ADHD-friendly: next 1-2 actions only. |

---

## The Sequence (Your Decision — Don't Rearrange)

```
PHASE 1 (NOW):     Stickman → ideas, competitor study, scripts
PHASE 1b (PARALLEL): Nishchay → READ competitor scripts (study only, no production)
PHASE 2 (AFTER):   Nishchay → production begins once study phase improves your scripting
ONGOING:           Clipping (Whop + Vyro) → see clipping/ folder for details
```

**Split: 60% Stickman / 40% Nishchay**

---

## Production Pipeline (Per Video — End to End)

### Step-by-Step Workflow

```
Step 1: TOPIC VALIDATION
    → Check project_brief.md in youtube/Stickman/projects/[NN]_[name]/
    → vidIQ keyword validation (check competition score)
    → vidIQ title scoring (aim for 85+, front-load emotion words)
    → Confirm topic from phase1 deep research rankings

Step 2: RESEARCH (Day 1)
    → Read phase1_part1 or part2 for topic's deep research
    → Watch 2-3 competitor reference videos
    → Compile facts and sources into research_notes.md

Step 3: SCRIPT (Day 1-2)
    → Use /prompt-forge to write a tight scripting prompt for the AI
    → Write hook (first 30 seconds — pattern interrupt)
    → Full draft (~1,800 words for 12 min)
    → While writing: activate /humanizer + /ai-writing-gaps + /stop-slop
      (these run DURING writing, not as separate passes)
    → /humanizer: kills surface AI tells (vocabulary, em dashes, rule-of-three)
    → /ai-writing-gaps: fixes structural problems (pacing, sources, contrast)
    → /stop-slop: removes predictable AI patterns from prose
    → Save as script_v1.md in project folder

Step 4: VOICEOVER (Day 2)
    → ElevenLabs generation with emotional tags
    → Save voiceover_notes.md

Step 5: VISUALS (Day 2-3)
    → Nano Banana 2 image generation per scene
    → Google Omni video clips where needed
    → Visual plan saved as visual_plan.md

Step 6: ASSEMBLY (Day 3)
    → Remotion/FFmpeg composition
    → Captions added
    → 4K export (local or GitHub Actions)

Step 7: POLISH & PUBLISH (Day 3)
    → Thumbnail designed (3 concepts, pick best)
    → Title + description + tags finalized (vidIQ scored)
    → vidIQ tag optimization (use volume-proven tags, avoid 0-vol keywords)
    → vidIQ description template with timestamps
    → Upload to YouTube
    → Update project_brief.md checklist
```

## Updated Video Priority Order (Phase 1 Deep Research — Aug 17, 2026)

| Priority | Topic | Composite Score | Project Folder |
|----------|-------|:-:|----------------|
| **Video 1** | The Most Terrifying Weapons Ever Banned | 94 (title: 93) | `projects/01_banned_weapons/` |
| **Video 2** | Every Banned Book in History Explained | 83 | `projects/02_banned_books/` |
| **Video 3** | Dumb War Tactics That Actually Worked | 74 | `projects/03_dumb_war_tactics/` |
| **Video 4** | Every Monster from Greek Mythology Explained | 89 | `projects/04_greek_mythology_monsters/` |
| **Video 5** | Every Type of Bullet Explained | 91 | `projects/05_bullet_types/` |

> [!NOTE]
> Full deep-dive research for each topic: `niche_research/phase1_part1_topics_1_to_10.md` and `phase1_part2_topics_11_to_20.md`
> Project briefs with production checklists: `projects/[NN]_[name]/project_brief.md`

---

## Tool Stack

### Research & Scripting
| Tool | Use |
|------|-----|
| NotebookLM | Upload competitor videos, extract insights, gym audio |
| Gemini (web app) | Native video + audio analysis |
| Antigravity IDE | Script writing, research, commands |
| vidIQ (Web App) | Script Writer, Title Generator, Daily Ideas, Learn ONLY |
| vidIQ MCP | Keyword research, outliers, channel stats (5 free accounts) |

### Voice & Music
| Tool | Use |
|------|-----|
| ElevenLabs | AI voiceover with emotional tags |
| Google Lyria 3 | Background music matched to scene mood |

### Visuals & Assembly
| Tool | Use |
|------|-----|
| Nano Banana 2 | AI image generation |
| Google Omni | AI video clips (2-10 sec) |
| FFmpeg | Local video assembly, audio mixing, 4K export |
| Remotion | React-based programmatic video editing + animated captions |
| GitHub Actions | Free cloud rendering (2,000 min/month) |

### Polish
| Tool | Use |
|------|-----|
| CapCut | Captions + color grading |
| Agent Reach | Web scraping for live data |

### Script Quality Skills
| Skill | When |
|-------|------|
| `/prompt-forge` | Before writing — creates a rigid, optimized prompt for the AI |
| `/humanizer` | During writing — kills 33 surface AI tells |
| `/ai-writing-gaps` | During writing — fixes 17 structural problems |
| `/stop-slop` | During writing — removes predictable AI prose patterns |

### Tool Rules
- Do NOT call vidIQ MCP without permission
- Always mention credit costs before suggesting vidIQ operations
- vidIQ web app: Script Writer, Title Generator, Learn, Daily Ideas ONLY
- Full tool details + setup: `_toolkit/toolkit.md`

## vidIQ Integration (What vidIQ Does Better)

| Pipeline Step | Use vidIQ For | Use Antigravity For |
|---------------|---------------|--------------------|
| Topic validation | Keyword volume + competition scores | Deep topic research + rabbit holes |
| Title | Title scoring (0-100), aim for 85+ | Hook architecture + paradox structure |
| Thumbnail | Scoring + niche benchmarks | Concept design + image generation |
| Tags | Character-counted tag lists with volume data | — |
| Description | Template with timestamps + hashtags | — |
| Post-publish | Retention curves, drop-off analysis, traffic sources | Strategic interpretation of the data |
| Competitor analysis | Live engagement %, VPH, breakout ratios | Forensic analysis of why things work |

### Key vidIQ Findings (Aug 19, 2026)
- "banned weapons explained" = 0 search vol. Use CTR titles, search-optimized tags.
- "dark history explained" = best comp-to-volume ratio (29.1 comp, 13.8K vol)
- "stickman animation" = 1.5M monthly volume (huge discovery potential)
- Serious History (819K) = direct stickman competitor, 3.9% engagement
- **⚠️ Feb 1, 2027: Monetization threshold doubles (4K → 8K watch hours)**
- Full vidIQ data: `niche_research/vidiq_data_aug19.md`

## Multi-Agent Mode (When Ready)

Using `/teamwork-preview` in Antigravity, run parallel agents:
- Agent 1: Analyze top 10 channels in your niche via vidIQ
- Agent 2: Research trending keywords
- Agent 3: Build a content calendar
- Agent 4: Clipping research (see clipping/ folder)

All running simultaneously. Use this AFTER your first video is published, not before.

## Daily Schedule Blocks

| Block | Time | Hours | Use |
|---|---|---|---|
| 🏠 Home Work | ~9-11 AM | 1-2h | Light tasks, planning, prep for library |
| 🚶 Travel | ~11-12 PM | — | To library |
| 📚 Library (Deep Work) | 12-6:45 PM | ~7h | Main work block — laptop + unlimited 5G. Scripting, Remotion, research, production |
| 🏋️ Gym (Passive) | 7-10 PM | 3h | NotebookLM audio + voice notes to WhatsApp "Capture" group between sets |
| 🟢 Light Work | 10 PM-12 AM | 1-2h | Progress check, leftover tasks, 3 bullets in WhatsApp "Daily Log" at 11:50 PM |
| 🛏️ Sleep | 12 AM | — | Hard cutoff — phone away |

Total: ~9-10.5h active + 3h passive. 6 working days/week. Thursday = college + REST (library closed).

> **Current 7-day checklist**: See `7day_checklist_aug11-17.md` for Notion-ready daily tasks.

---

## Phase 1: Stickman — Production Mode

**Niche research = COMPLETE.** Deep research for all 20 topics done. Video order decided.

**Current task:** Produce Video #1 (Every Banned Weapon in History Explained)
1. Open `projects/01_banned_weapons/project_brief.md`
2. Follow the production checklist
3. Use `/prompt-forge` to write the scripting prompt
4. Deep research already done: `niche_research/phase1_part1_topics_1_to_10.md` → Topic 1

---

## Phase 1b (Parallel): Nishchay — Study Mode

**Goal**: Absorb competitor scripting patterns before producing anything.

**What needs to happen:**
1. Build a Nishchay competitor database (5-10 channels doing IAS/IPS/DM dramatic content)
2. Read/analyze their top-performing scripts — dramatic structure, hooks, tension curves
3. Note what patterns repeat across winning videos

**This is study time, not production time.** You're sharpening your scripting before you produce.

**Tools for this:**
- `vidiq_video_transcript` (5 credits) — pull competitor scripts directly
- `vidiq_outliers` (5 credits) — find which videos are outperforming their channel average
- NotebookLM — feed competitor transcripts, generate audio summaries for gym
- Gemini web app — paste video URLs, ask for dramatic structure analysis

---

## Clipping (Moved to clipping/ folder)

All clipping details (Whop + Vyro) now live in `clipping/` folder. See:
- `clipping/clipping_overview.md` — overview and TODO
- `clipping/whop/whop_guide.md` — Whop marketplace details
- `clipping/vyro/campaigns.md` — Vyro campaigns and rates

---

## ADHD Rules (Non-Negotiable)

1. **Production before consumption.** No YouTube, no tutorials, no research until the day's production block is done.
2. **One thing at a time.** Don't start video #2 until video #1 script is done.
3. **Phone in another room** during deep work.
4. **If you've been "planning" for more than 30 minutes, you're procrastinating.** Start writing.
5. **No new OneTab saves.** If you find a video, write the title on paper. Review weekly.

---

## Your Next Action

**Open `projects/01_banned_weapons/project_brief.md` and start the production checklist.**
