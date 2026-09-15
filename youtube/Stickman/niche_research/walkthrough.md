# Walkthrough: ai-writing-gaps Skill Build

## What Was Built

The `ai-writing-gaps` skill — a structural YouTube script QA system that catches the 15 deep AI writing failures that `/humanizer` can't detect.

**Installed at:** `C:\Users\renu5\.gemini\config\skills\ai-writing-gaps\`

---

## Phase Summary

### Phase 1: Topic Research (Complete)
- **Part 1:** Deep analysis of Topics 1-10 → [phase1_part1_topics_1_to_10.md](file:///C:/Users/renu5/.gemini/antigravity/brain/4066a897-2bf3-4059-a041-ff0d7ca88866/phase1_part1_topics_1_to_10.md)
- **Part 2:** Deep analysis of Topics 11-20 → [phase1_part2_topics_11_to_20.md](file:///C:/Users/renu5/.gemini/antigravity/brain/4066a897-2bf3-4059-a041-ff0d7ca88866/phase1_part2_topics_11_to_20.md)

### Phase 2: Pattern Extraction (Complete)
- 15 mechanisms extracted with operational HOW instructions → [phase2_pattern_extraction.md](file:///C:/Users/renu5/.gemini/antigravity/brain/4066a897-2bf3-4059-a041-ff0d7ca88866/phase2_pattern_extraction.md)
- Source corpus: 9 videos, 24,035 words, 4 channels, ~2.5 hours

### Phase 3: Skill Build (Complete)
5 files created via parallel subagents:

| File | Size | Purpose |
|------|------|---------|
| [SKILL.md](file:///C:/Users/renu5/.gemini/config/skills/ai-writing-gaps/SKILL.md) | 6.8 KB | Main instructions, 3 modes, trigger phrases |
| [pattern_library.md](file:///C:/Users/renu5/.gemini/config/skills/ai-writing-gaps/pattern_library.md) | 18.3 KB | 15 universal patterns + 4 channel blueprints |
| [qa_checklist.md](file:///C:/Users/renu5/.gemini/config/skills/ai-writing-gaps/qa_checklist.md) | 7.9 KB | Two-pass QA system with scoring |
| [learned_patterns.md](file:///C:/Users/renu5/.gemini/config/skills/ai-writing-gaps/learned_patterns.md) | 1.2 KB | Empty template (grows with each transcript) |
| [benchmarks.md](file:///C:/Users/renu5/.gemini/config/skills/ai-writing-gaps/benchmarks.md) | 5.4 KB | Quantitative competitor reference card |

---

## Skill Features

### 3 Operating Modes
1. **Audit Mode** — Submit your script → get a Human Score %, 15-dimension scorecard, flagged lines with specific rewrites, top 3 priority fixes
2. **Learn Mode** — Upload competitor transcript → skill extracts new patterns, filters for quality, appends to learned_patterns.md
3. **Blueprint Mode** — Say "write in Brofessor Stein style" → applies channel-specific patterns

### 15 Structural Patterns
1. Wrong Detail (Tier-3 forensic micro-details)
2. Emotional Whiplash (tonal gear-shifts after intensity peaks)
3. Source as Story (dramatic citation, not bibliography)
4. Modern Language Collision (strategic register mismatch)
5. One-Word Drop (standalone topic name openings)
6. Narrator Has a Body (sarcasm, fourth-wall breaks, "you")
7. Causal Transitions (no "Next up" or "Moving on")
8. Courage in Voice (zero hedging)
9. Oral Rhythm (breath points, fragments, short punches)
10. Pop Culture Anchoring (audience-world comparisons)
11. Editorial Selectivity (A/B/C weighting, not equal time)
12. Zero-Latency Cold Open (0.10s to topic)
13. Abrupt Mic-Drop Outro (sub-5 seconds, zero CTA)
14. Tactile Sensory Grounding (physical objects, not abstract adjectives)
15. 90-Second Micro-Loop (Setup → Complication → Payoff)

### 4 Channel Blueprints
- **Esoteric Catalog** (Brofessor Stein) — artifact listicles, $62 RPM
- **Diagnostic Armor** (EverythingProfessor) — psychology/science, second-person
- **Retribution Anthology** (Serious History) — 3-story narratives, 6.35M views
- **Pop-Culture Autopsy** (The Analyst) — systems analysis, sardonic comparisons

### Learning Loop
- Grows with every competitor transcript uploaded
- Quality gate: only novel, reproducible patterns pass
- Topic-specific patterns extracted alongside general ones
- `learned_patterns.md` accumulates over time

### Two-Pass Integration
- Pass 1: `/humanizer` (33 surface AI tells)
- Pass 2: `ai-writing-gaps` (15 structural failures)
- Combined: scripts structurally indistinguishable from top competitors

---

## How to Use

```
"audit my script"           → Runs Audit Mode
"learn from this transcript" → Runs Learn Mode  
"write in Serious History style" → Applies Blueprint
"structural pass"           → Runs Audit Mode
"script DNA check"          → Runs Audit Mode
"pass 2"                    → Runs Audit Mode
```

---

## Verified
- ✅ All 5 files created and installed
- ✅ YAML frontmatter valid with pushy description
- ✅ 15 patterns with detect/fix/benchmark for each
- ✅ 4 channel blueprints with verbal tics and segment architecture
- ✅ QA checklist with scoring system and execution order
- ✅ Learning loop template ready for first transcript
- ✅ Benchmarks from 9-video forensic corpus
