# Stikaman YouTube Project — Full Audit

> **Date:** Aug 13, 2026 | **This is Conversation 5** (new session)
> **Previous conversations:** `ec84b8ec` (Convo 1) → `f78e1ae0` (Convo 2, DELETED) → `9eb8538f` (Convo 3-4, most recent)
> **Model:** Claude Opus 4.6 (Thinking)

---

## Decisions Already Made

| # | Decision | Source | Confidence |
|---|----------|--------|------------|
| 1 | **Channel: Stikaman** — English, faceless, stickman/motion graphics educational explainer. Tier 1 countries (US/UK/AU/CA). 10-15 min videos. | README + context-rule | ✅ LOCKED |
| 2 | **Niche: "Every X Explained" format** — Topic-first, niche-later approach. First 5 videos test different topics (mythology, weapons, psychology, dark books, ancient empires). | `final_analysis_and_launch_plan.md` §5 | ✅ LOCKED |
| 3 | **Production stack:** Remotion (code-based animation) + Nano Banana 2 (AI images) + ElevenLabs (voiceover) + FFmpeg + CapCut (captions). GitHub Actions for cloud rendering. | README + context-rule | ✅ LOCKED |
| 4 | **Target output:** 2 videos/week at medium quality. | `final_analysis_and_launch_plan.md` §6 | ✅ LOCKED |
| 5 | **Anti-sycophancy always active.** Blunt, honest feedback. Mentor/manager tone. | context-rule §Communication | ✅ LOCKED |
| 6 | **Primary model channel:** Brofessor Stein ($22.4K/mo from 361K subs, $62 RPM/1K subs). Dark history, 19min avg, 2/week, motion graphics. | `final_analysis_and_launch_plan.md` §2 | ✅ LOCKED |
| 7 | **Title DNA formula:** `Every [X] & [Impact/Effect] Explained in [N] Minutes` + dark/forbidden knowledge hooks + personal framing ("How YOU'D die"). | `final_analysis_and_launch_plan.md` §3 | ✅ LOCKED |
| 8 | **5-video starter pack confirmed** (see Video 1 section below for full list). | `final_analysis_and_launch_plan.md` §5 | ✅ LOCKED |
| 9 | **Second channel: Nishchay Stories** (Hindi dramatic entertainment, IAS/IPS/Police themes). 100% competitor-driven. Lower priority — side-by-side study. | README + context-rule | ✅ LOCKED |
| 10 | **Script philosophy:** AI as edge, not crutch. Competitor research → user's angle → AI assists structure → user's final voice. /humanizer pass mandatory. | context-rule §Scripting | ✅ LOCKED |
| 11 | **Weekly schedule:** Mon-Sat production. Thu = college + rest. 20+ hours/week. | `final_analysis_and_launch_plan.md` §6 | ✅ LOCKED |

---

## Work Already Completed

### Research Phase (Complete — 4 conversations, ~250 vidIQ credits spent)

- [x] **72+ competitor channels** organized across 5+ categories
- [x] **vidIQ deep stats** on 12+ channels (subs, views, growth, earnings)
- [x] **5 keyword research pulls** (history, psychology, science, stickman, bedtime)
- [x] **5 outlier searches** (100 videos analyzed)
- [x] **3 trending searches** + **3 channel video analyses** (Serious History, A Talking Hat, Bluntly Explained)
- [x] **Live browser scrapes** on 5 key channels (Paint Explainer, Brofessor Stein, EverythingProfessor, Qxir, Serious History) — 0 API credits
- [x] **AI slop risk ranking** per niche (Psychology = EXTREME, History = HIGH, Bedtime = LOW)
- [x] **Trust score strategy** (5-point plan for new channels)
- [x] **Time to $1K/month estimates** per niche
- [x] **Hallucination audit:** All 5 key channel stats verified against live data
- [x] **Competitor title DNA extraction** — breakout formulas for EP, Paint Explainer, Brofessor Stein
- [x] **RPM per 1K subs analysis** — Brofessor Stein 3-8x higher than all others
- [x] **Dead/stagnant channel analysis** (A Talking Hat = quit, Qxir = stagnant, someunfilteredguy = dead)

### Deliverables Produced

| File | Location | What It Is |
|------|----------|------------|
| `final_analysis_and_launch_plan.md` | niche_research/ + artifacts | **THE MASTER DOC** — verified competitive landscape, title DNA, 5-video starter pack, weekly schedule, production prompt |
| `strategy_audit_and_course_correction.md` | niche_research/ + artifacts | Deep strategy audit with course corrections |
| `competitor_forensic_report.md` | artifacts (9eb8538f) | Forensic competitor breakdown |
| `niche_analysis_final.md` | convo f78e1ae0 artifacts | 7-niche ranking with Demand/Supply scores |
| `top_3_channel_picks.md` | convo f78e1ae0 artifacts | 3 channel pick analysis (EP, Paint Explainer, 20 Min Professor) |
| `top_5_options_vidiq.md` | convo ec84b8ec artifacts | Original 5 options with vidIQ data |
| `live_channel_data_*.md` (5 files) | niche_research/ | Live scraped channel data |
| `key_channels_analysis.md` | niche_research/ | Deep analysis of 18 key channels |
| `channels org opus4.6.md` | niche_research/ | 72+ channels organized |
| `youtube-data-extractor` skill | Created during convo 9eb8538f | Skill for bulk live data extraction |

---

## Work Remaining

### ⚠️ CRITICAL — Blocks First Video

| # | Item | Status | What's Needed |
|---|------|--------|---------------|
| 1 | **Write Video 1 script** ("Every Monster from Greek Mythology Explained in 12 Minutes") | NOT STARTED | Full ~1,800 word script with hook, 8-12 monsters, sources, /humanizer pass |
| 2 | **Visual storyboard for Video 1** | NOT STARTED | Scene-by-scene plan: what Nano Banana generates, what Remotion animates, stickman placement |
| 3 | **Thumbnail concepts for Video 1** | NOT STARTED | 3 concepts with text overlay + monster imagery + color scheme |
| 4 | **Title + description + tags for Video 1** | NOT STARTED | SEO-optimized for low-competition keywords |
| 5 | **Remotion project setup** | NOT STARTED | Initialize codebase, design system, animation templates |
| 6 | **ElevenLabs voice selection/testing** | NOT STARTED | Pick voice, test tone for dark/dramatic delivery |

### 🟡 IMPORTANT — Needed Soon

| # | Item | Status |
|---|------|--------|
| 7 | **Channel name finalized** — Options: "Stikaman Explains", "Simply Explained", "[Word] Explained". Not yet picked. | UNRESOLVED |
| 8 | **Channel branding** — Logo, banner, channel description, avatar | NOT STARTED |
| 9 | **Production pipeline test** — End-to-end: script → images → animation → voiceover → render → export | NOT STARTED |
| 10 | **Nishchay Stories competitor study** — Saved tabs in `nishchay_chrome_tabs_saved.md` but no study started | NOT STARTED |

### 🟢 LATER — Can Wait

| # | Item | Status |
|---|------|--------|
| 11 | **"Human Script DNA" extraction system** — Phase 3 from the big prompt. Extracting what makes human-written scripts feel human. | NOT STARTED (was planned but never executed) |
| 12 | **Gap analysis** (Phase 4 from big prompt) | NOT STARTED |
| 13 | **Remaining vidIQ credits budget** — ~45-95 credits left (conflicting counts, resets Aug 20) | UNCLEAR |

---

## First Video — Current Status

### What's Decided

**Video 1:** "Every Monster from Greek Mythology Explained in 12 Minutes"

| Attribute | Decision |
|-----------|----------|
| **Topic** | Greek Mythology monsters — intersection of history + dark + mainstream appeal |
| **Evidence** | Mythological Man (3.6K subs) → 325K views, 140x breakout, 289 VPH. Paint Explainer's Greek myths → 509K views, 5.9K VPH (trending) |
| **Length** | 10-12 minutes (~1,800 words script) |
| **Tone** | Dark, dramatic |
| **Visual approach** | Nano Banana monster illustrations + Remotion kinetic typography/reveal animations + stickman for scale comparisons |
| **Title formula** | "Every [Monster/Creature] from [Mythology] Explained in [N] Minutes" |

### What's NOT Done (Very Next Action)

> **The very next action is: Write the Video 1 script.**
>
> Specifically: A full ~1,800 word script with:
> 1. Hook (first 30 seconds — pattern interrupt, shocking fact)
> 2. 8-12 monsters, ordered from least to most terrifying
> 3. Specific historical sources cited (not generic "ancient Greeks believed")
> 4. Narrative bridges between segments (not just a list)
> 5. /humanizer pass — no AI slop

The production prompt is already written in [final_analysis_and_launch_plan.md §8](file:///C:/Users/renu5/Downloads/priyanshu%20readme/niche_research/final_analysis_and_launch_plan.md).

---

## Full 5-Video Starter Pack (For Reference)

| # | Title | Key Evidence |
|---|-------|--------------|
| 1 | **Every Monster from Greek Mythology Explained in 12 Minutes** | 325K views from 3.6K sub channel, Paint Explainer trending on Greek myths |
| 2 | **Every Banned Weapon in History Explained** | "weapons explained" = 25.3/100 competition (LOW), Armory Professor 567K from 3.3K subs |
| 3 | **Every Type of Depression Explained in 15 Minutes** | Mindfo 248K from 4.9K subs (301x breakout), tests psychology angle |
| 4 | **The Most Disturbing Books You Should Never Read** | Brofessor Stein 525K, 444 VPH — currently trending |
| 5 | **How You'd Die in Every Ancient Empire** | Paint Explainer's proven formula, 242K views, 88 VPH |

---

## Ambiguities / Unresolved Items

1. **vidIQ credit balance unclear** — Last confirmed balance was 95 credits (Aug 11), but more may have been spent during the browser scraping session. Resets Aug 20.
2. **Channel name not finalized** — "Stikaman" or "Stikaman Explains" or something new?
3. **"Human Script DNA" system** — Was requested (Phase 3 of the big prompt) but never built. Is this still wanted, or skip it and learn by doing?
4. **Audio question unanswered** — "Do you actually need audio, or is transcript-only sufficient for script DNA extraction?" — was asked but convo ended before answer.
