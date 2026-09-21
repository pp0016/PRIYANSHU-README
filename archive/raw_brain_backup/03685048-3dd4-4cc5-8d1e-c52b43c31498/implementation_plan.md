# Implementation Plan — Absorbing Human Script DNA Into a Production Prompt

---

## The Problem

You built an incredible system across another conversation. The output is **massive**:

| File | Size | Lines |
|------|------|-------|
| `script_dna_template.md` | 50.5 KB | 771 lines |
| `cross_channel_convergence.md` | 60.8 KB | 647 lines |
| `vidiq_comparison.md` | 52.2 KB | 578 lines |
| `ai_writing_gaps.md` | 23.7 KB | 360 lines |
| 9 individual DNA analyses | ~205 KB total | ~2,000+ lines |
| 9 transcripts (.txt) | ~157 KB total | raw competitor scripts |
| **TOTAL** | **~549 KB** | **~4,300+ lines** |

**549 KB of dense analysis.** If I dump all of this into a new conversation prompt, it will:
1. Blow through the context window
2. Dilute the actionable instructions with background evidence
3. Cost you massively on tokens every single conversation

**The goal:** Compress 549 KB into a ~15-20 KB production prompt that captures 100% of the actionable rules and 0% of the background proof.

---

## How I'll Do It (3 Phases)

### Phase 1: Digest & Compress (This Conversation)

I read every file and extract ONLY the actionable rules — not the evidence, not the examples, not the methodology. Just the "when writing a script, do THIS."

**What gets extracted:**
- 6 universal DNA patterns (from `cross_channel_convergence.md`)
- 4 channel blueprints / fill-in-the-blank templates (from `script_dna_template.md`)
- 12 anti-slop verification gates (from `script_dna_template.md` Dimension 8)
- 11 structural AI failure checks (from `ai_writing_gaps.md`)
- Humanizer integration matrix (from `script_dna_template.md` Dimension 9)
- Hook formulas with fill-in-the-blank slots (from `script_dna_template.md` Dimension 1)
- Key benchmarks: 149.8 WPM, 10.23 sources/1K words, Grade 9.6, 0.10s time-to-topic
- vidIQ verdict: "Skip for drafting, maximize for packaging"
- ElevenLabs pacing tags mapped to emotional arc

**What gets DROPPED:**
- All 9 individual analysis reports (evidence, not instructions)
- All 9 raw transcripts (source material, already distilled)
- All methodology explanations (how the system was built)
- All verbatim competitor quotes longer than 1 sentence (keep 1 example per pattern)
- The vidIQ comparison scoring matrix (verdict already captured)
- Python scripts (audit tools, not production tools)

**Output:** `script_dna_cheatsheet.md` — ~15 KB, everything a new conversation needs

---

### Phase 2: Build the Production Prompt (This Conversation)

Combine the cheatsheet with:
- Your topic choice (from the Top 20 list)
- Production stack context (Remotion + Nano Banana 2 + ElevenLabs + stickman)
- Visual storyboard framework (what to generate per scene)
- Thumbnail/title/SEO instructions
- The two-pass QA system (Humanizer surface pass → DNA structural pass)

**Output:** A single copy-paste prompt block you drop into a new conversation to get a complete production-ready script

---

### Phase 3: Save as a Skill (Optional, Recommended)

Turn the cheatsheet + production prompt into a proper `/skill` so ANY future conversation automatically has the DNA system loaded.

**Output:** `C:\Users\renu5\.gemini\config\skills\stikaman-script-dna\SKILL.md`

This means you never paste the prompt again — every new conversation already knows how to write scripts the Stikaman way.

---

## Work Division

| Task | Who Does It | How Long |
|------|-------------|----------|
| Read all 6 major .md files | **Me (subagents, parallel)** | ~5 min |
| Compress into cheatsheet | **Me** | ~10 min |
| Build production prompt | **Me + your topic pick** | ~5 min |
| Save as skill (optional) | **Me** | ~5 min |
| **Total** | | **~25 min** |

> [!IMPORTANT]
> **I will NOT start scripting Video 1 in this step.** This phase is purely about building the tool. Once the prompt/skill is ready, you paste it into a new conversation (or use it here) and THAT's when scripting starts.

---

## End Goal

**Before this plan:**
- 549 KB of files that no conversation can fully absorb
- No way to write a script without re-explaining the DNA system every time

**After this plan:**
- A ~15 KB cheatsheet that fits in any conversation context
- A copy-paste production prompt with everything baked in
- (Optional) A permanent skill that every conversation inherits automatically

---

## Open Questions

1. **Do you want the skill (Phase 3)?** — It means every future conversation automatically knows the DNA system. Recommended, but adds ~5 min.
2. **Have you picked your first topic from the Top 20 list?** — I need this to build the production prompt in Phase 2. If you haven't picked yet, I'll build a generic prompt and you fill in the topic.
3. **Anything from the DNA conversation that you feel I should NOT compress out?** — For example, if you want ALL the verbatim competitor quotes preserved, the cheatsheet will be bigger.
