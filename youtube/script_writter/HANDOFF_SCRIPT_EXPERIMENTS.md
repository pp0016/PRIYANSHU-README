# Handoff: vidIQ Scriptwriting Experiments

Read this first in any new conversation about scriptwriting. Fill in the blank rows as tests get done.

**Owner:** Priyanshu. Runs faceless YouTube channels. Can't easily judge English script quality for Tier 1 audiences, and doesn't like re-reading long drafts. **Needs a final script plus a pass/fail sheet, not drafts to review.**

**Credits:** about 150 vidIQ web credits per Gmail per month, across 10+ active accounts (1,500+ total). Credits aren't a constraint. The goal is to test every approach properly once.

---

## 1. Goal

Find the most reliable way to produce exceptional, human-sounding, original, monetizable scripts. Then turn it into a repeatable pipeline that ideally runs from Opus and the vidIQ MCP, without hand-holding.

---

## 2. Key files

| File | What it is |
|---|---|
| `workflow/SCRIPT_WRITING_TEMPLATE.md` | **Use this when writing any script.** Rules + checklist, no examples |
| `workflow/SCRIPT_WRITING_LEARNINGS.md` | Detailed learnings **with** examples from the test topic (reference only, don't feed to a writer) |
| `C:\Users\renu5\Downloads\script writting idea\` | All raw test outputs, organized by test |
| ↳ `vidiq script writter result\` | Test 1 output + screenshot |
| ↳ `single prompt result\` | Test 2 Step A one-shot + fix prompt result |
| ↳ `multi step prompt result\` | Test 2 Step B prompts 1, 2, 3 results |
| ↳ `testing_map all promtps.md` | Exact prompts used for Step A and Step B |
| ↳ `test2_part1_audit.md` | Earlier audit (scores later corrected, see §4) |

Test topic used for every test so far: "Ice Age Survival: The Brutal Inventions That Saved Humanity," 15 min target. Reference video: `wt_7Hp7d7I8` ("How Did Ancient Humans Survive Deadly Winters?", 10:24, ~929K views). A second candidate reference, `tpfo9tRWQy4`, has **not** been used in any test.

---

## 3. Test log

Scale: 10 = publish as-is, beats the reference · 7 = publish after a focused edit · 5 = needs a structural rewrite · 3 = derivative, unusable.

| Test | Method | Status | Score | Why |
|---|---|---|---|---|
| **Test 1** | vidIQ Scriptwriter, 15 min, "Match Reference Video" (1 video), picked concept 2 of 3 | ✅ Done | **3.5** | Reworded copy of the reference. Same hook, order, examples. Dropped its best moments. Generic CTA. The tool has no instruction field. |
| **Test 2 · Part 1 · Step A** | AI Coach, one engineered prompt (analyze + map + write), 1 video attached | ✅ Done | **5** | New hook and order, but our "mandatory content" list was taken from the reference, so it re-ordered the reference's facts. Several near-copied sentences. Script ran ~10 min at the reference's pace, not 15. |
| **Test 2 · Part 1 · Step A fix** | Same chat, prompt fixing 4 paragraphs (humor, closer, cannibalism detail, Yaghan detail) | ✅ Done | **5.5** | Fixes landed. It added a distorted Darwin quote and an unsourced metabolism claim. |
| **Test 2 · Part 1 · Step B** | AI Coach, 3 prompts: analysis only → skeleton + first half → second half | ✅ Done | **7 (best so far)** | Researched new sources, double open loop, real tone shift after a dark turn. Flaws: the counting frame ends 5 min early, a disclaimer in the hook, a mid-video "comment your guess" ask, "reading this" slip, overused "not X, it's Y" lines, honesty tic, misread Mezhyrich date range, runtime short. |
| **Test 2 · Part 2 · Step A** | AI Coach, attach **SRT/text transcripts of 2 videos**, one-shot | ⬜ NOT DONE | — | — |
| **Test 2 · Part 2 · Step B** | Same input, 3-prompt multi-step | ⬜ NOT DONE | — | — |
| **Test 2 · Part 3** | Same as Part 2 but **audio files** instead of transcripts (only if the upload accepts audio) | ⬜ NOT DONE | — | — |
| **Test 3** | Opus writes it from vidIQ MCP data: 2–3 transcripts + top comments (+ optional "Most replayed" data), following the template | ⬜ NOT DONE | — | — |
| **Final comparison** | Best of Test 2 vs Test 3, decide the pipeline | ⬜ NOT DONE | — | — |

**How to run the pending tests**
- **Part 2:** download SRT/transcripts for both reference videos, attach both in a new AI Coach chat (Attach image or file), and reuse the Step A, then Step B prompts from `testing_map all promtps.md`. **But remove the "mandatory content" list taken from the reference** and ask it to research its own material instead. Save outputs to a new folder and score them on the same scale.
- **Test 3:** follow section 7 of `SCRIPT_WRITING_LEARNINGS.md` and Part G of the template.

---

## 4. Conclusions so far, and why

1. **The Scriptwriter tool is out** for reference-based work. Matching is all it does, and it can't take instructions.
2. **The AI Coach multi-step method is the best vidIQ method.** Separate analysis, then halves, then research room.
3. **Prompt quality caused most of the improvement.** Same tool, same reference, much better output once failures were named and good vs. bad voice was described.
4. **Our own prompt made the model copy.** Listing reference facts as "mandatory" turned it into a reorder. Never do that again.
5. **AI-cited sources still need checking.** Errors found: a Mezhyrich 0–429 year uncertainty range presented as "400 years of use," the Solutré cliff-drive myth, overstating the eyed needle (bone awls came 30–40k years earlier), and a distorted Darwin quote.
6. **Earlier audits in this project were too generous** (they gave 6 / 8 / 8.5 / 9.5). The scores above are the corrected ones.
7. **Length must be set in words at the measured narrator pace**, not in minutes.

---

## 5. Facts about the tools

**vidIQ web**
- Scriptwriter: topic, Long/Short, duration, Tone (preset / custom / Match Reference Video, one video). Asks one clarifying question, offers 3 concepts, has a Refine box. About 1 credit per minute.
- AI Coach: one YouTube attachment per chat. Pasted links aren't read. Has "Attach a video" and "Attach image or file," and Regular / Deep Thinking modes. About 10 credits per message. It can research outside sources.

**vidIQ MCP**
- `vidiq_video_transcript` (param `videoId`, 5 cr)
- `vidiq_video_comments` (5 cr/page, sort by relevance, filter by min likes)
- `vidiq_comment_insights` (5 cr, niche-level questions and complaints)
- `vidiq_video_watch` (25 cr, visual scene breakdown)
- `vidiq_video_stats` (5 cr, views/likes/VPH over time)
- `vidiq_generate_script` (1 cr/min)
- **No MCP tool returns audience retention.**

**Other**
- yt-dlp may read the "Most replayed" graph (`heatmap` field). Not tested. It measures rewatches, not retention.
- Exa MCP's API key isn't configured (401). Priyanshu plans to use Exa for fact-checking while scripting.

**YouTube policy**
- July 15, 2025: "repetitious content" was renamed "inauthentic content." AI help is allowed. Template-like or mass-produced content with little variation or author input can be demonetized. Realistic synthetic media must be disclosed.

---

## 6. Open items (not started)

| Item | Status | Notes |
|---|---|---|
| Test 2 Part 2 (SRT, 2 videos) | ⬜ Not done | See §3 |
| Test 2 Part 3 (audio) | ⬜ Not done | Check first that audio upload is accepted |
| Test 3 (MCP + Opus) | ⬜ Not done | The real candidate for the pipeline |
| Final comparison + pipeline decision | ⬜ Not done | |
| Build our own scriptwriter pipeline | ⬜ Not done | Only after Test 3. MCP pull → analysis → skeleton → two halves → audit against template → fix → final + pass/fail sheet |
| Measure the TTS narrator's real words per minute | ⬜ Not done | Needed to set word counts |
| yt-dlp "Most replayed" check | ⬜ Not done | Run once on the reference to see if the field exists |
| Signature opening sound + "premium channel small details" list | ⬜ Not done | Prompt written earlier in the original conversation. Run it in vidIQ AI Coach and in a fresh Opus chat, then compare |
| Test the second reference `tpfo9tRWQy4` | ⬜ Not done | Needed for 2-reference tests |

---

## 7. Learnings added after this handoff

_(Add new findings here with date, test name, and what changed.)_

| Date | Test | Learning |
|---|---|---|
| | | |
| | | |
