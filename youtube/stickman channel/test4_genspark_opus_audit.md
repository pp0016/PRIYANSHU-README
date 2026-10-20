# Test 4 Audit: Genspark Opus 5.5 One-Shot vs vidIQ Step B

## Verdict

As delivered, the Opus one-shot is **not better** than the vidIQ Step B script. It has **better raw material**, though. Its facts are more accurate, the dark turn is stronger, and it busts a myth that Step B left alone. It failed the length test badly, and it misreported its own length. Cut by about 30%, it would probably become the best script we have.

One caveat changes how to read this test. The 13-beat skeleton in your prompt **was vidIQ's Step B structure**. So Opus did not design anything here. It executed a design vidIQ made. This test measured Opus as a writer, not as a structure designer. Test 3 (MCP pipeline) is still the only test where Opus does both.

---

## 1. Word count: did it hit 2,000+?

It overshot. Measured with a script on the file, not estimated:

| | Words |
|---|---|
| **Spoken narration (actual)** | **3,560** |
| What Opus claimed at the end | "about 2,500" ❌ |
| Your target | 2,000–2,400 |
| Step B (vidIQ) | ~2,360 |

- It wrote about **48% more than the maximum**. At a typical TTS pace of ~150–165 wpm that's **21–24 minutes**, not 15.
- **The self-report was off by ~1,000 words.** Lesson: never trust a model's word count about its own output. Always measure.
- It didn't stop halfway, and it didn't hallucinate content to pad the length. The extra words are real material spread across every beat (see the cut plan below).

### Per-beat length (measured)

| Beat | Words | Budget for 15 min | Over by |
|---|---|---|---|
| Hook | 329 | 220 | +109 |
| Job 1 Fire | 300 | 200 | +100 |
| Job 2 Tools | 301 | 200 | +101 |
| Job 3 Clothing | 344 | 240 | +104 |
| Midpoint re-hook | 184 | 120 | +64 |
| Job 4 Shelter | 416 | 280 | +136 |
| Job 5 Hunt/Store | 285 | 200 | +85 |
| Job 6 Together | 200 | 150 | +50 |
| Dark turn | 181 | 160 | +21 |
| Humor | 185 | 140 | +45 |
| Goggles | 242 | 150 | +92 |
| Yaghan | 217 | 180 | +37 |
| Payoff (Spain) | 179 | 160 | +19 |
| Close | 203 | 150 | +53 |

---

## 2. Framework compliance

### Problem-door bridges: ✅ followed, ⚠️ too literally

Every section ends by naming a flaw that opens the next one. Fire doesn't move → tools. A blade can't keep you warm → clothing. A house doesn't feed you → hunting. Food runs out → who eats. The structure is not a chronological listicle. It's a real deficit chain.

**The problem:** the word "flaw" appears **7 times**, and "fatal flaw" 4 times. Your prompt said "name the fatal flaw," and Opus used that exact phrase as a spoken template. By Job 3 a viewer can hear the machinery: *"But X has a fatal flaw."* A formula only works while the audience can't see it. Step B varied its bridges ("Warmth solved, as long as you never leave. Which is a problem, because you have to leave."), and that's better craft.

### Delayed payoff loop: ✅ executed cleanly

- **Loop 1 (hibernation):** planted early with an explicit promise ("you'll have an answer, and it's stranger than yes or no"). Paid off in the last ~2 minutes with the lemur torpor twist. The promise is delivered, which is the part most scripts fail.
- **Loop 2 (doorway):** planted at the midpoint ("where would you put the door?") and paid off in the next section. It says "Hold that answer" instead of Step B's "Put your answer in the comments." That's the better choice. A mid-video comment prompt hands the viewer an exit to leave the video.

### Re-hooks: ✅ frequent, varied enough

Hard-stop lines carry them: "That's not a campfire. That's controlled heat." "It wasn't panic. It was a calendar." The **Solutré myth-bust** ("It's a great image. It's also probably wrong.") is the best single re-hook in any of our scripts. Step B didn't have it.

---

## 3. Voice: premium documentary or AI slop?

**Premium documentary, not slop.** It has none of the usual slop vocabulary (no "delve," "tapestry," "testament to," "in today's world"). Sentences are short, concrete and specific. A Tier-1 viewer would hear a competent narrator.

Three tics hold it back:

1. **Prompt echo.** Your prompt contained example phrases, and Opus used them word for word: "It's not settled" appears **3 times**, plus "You are the proof" and "They are the reason you do." This is the biggest lesson from this test. **Any example phrase you put in a prompt will appear verbatim in the output.** Describe the effect you want, not the words.
2. **One-word reveal paragraphs, overused.** "Hibernation." "The eyed needle." "Skull cups." "The cow." Each one works. Six of them become a pattern.
3. **Reference echo in the close.** "You turn up the thermostat" brings back the exact concept we removed from Step A because the reference video uses it. "You are the proof" is near-verbatim from the reference ("You're the proof"). Partly your prompt's fault, since it asked for that close.

---

## 4. Accuracy: where Opus clearly wins

This matters more than it sounds. Tier-1 history audiences fact-check in the comments, and one wrong claim at the top of the comments costs trust.

| Claim | Step B (vidIQ) | Opus | Better |
|---|---|---|---|
| Solutré | "Drive a herd against ground it can't climb" | Says the cliff-drive story is probably wrong: the bones sit at the slope's foot, which points to seasonal ambush | **Opus** |
| Fire site | "Ukraine fire pits" | Names **Korman' 9**, Dniester valley, three hearths with different functions | **Opus** |
| Bear skinning | "Northern Europe" | Names **Schöningen, Germany**, explains why paw cut marks mean skinning (no meat on toes) | **Opus** |
| Cold-trap door at Mezhyrich | Presented as fact | Says the evidence is fragmentary and the design is proven for Inuit houses | **Opus** (honest) |
| Volgu points | Hunting implication | "Nobody hunts with that": display pieces, "they were showing off" | **Opus** |
| Calorie math | "One reindeer is three days of calories for one family": unsourced, and likely wrong (a reindeer's meat feeds a family for closer to a week) | 100 W per human, 10 people = 1 kW: sound physics | **Opus** |

The trade-off: honest hedging softens a payoff. The doorway answer lands less hard because Opus admits the Mezhyrich evidence is thin. For a channel that wants to last, that's the right trade.

---

## 5. Correction: Step B was not a 9.5

Your friend's Claude scored Step B at 6.5, and I re-checked my own score against it rather than defending it. **My 9.5 was inflated.** I graded Step B relative to Test 1 and Step A, not against an absolute standard. Problems I let slide:

- Mid-video "put your answer in the comments" (an exit ramp)
- An unsourced, likely wrong calorie claim (reindeer = 3 days)
- Mezhyrich cold-trap door stated as fact when the evidence is thin
- "Job one / Job two…" is an announced numbered roadmap. Both scripts share this, because the skeleton demanded it.

**Re-derived Step B: 8.5/10.** I can't explain the gap down to 6.5 without seeing your friend's reasoning. If you paste its critique, I'll go through it point by point and tell you which points hold.

---

## 6. Scorecard (same scale throughout)

**Scale:** 10 = would beat the reference video's retention with a Tier-1 audience. 7 = competitive in the niche. 5 = watchable but forgettable. 3 = generic AI.

| Category | Step B (re-derived) | Opus one-shot |
|---|---|---|
| Hook | 9 | 8.5 (strong, but ~2 min long) |
| Structure design | 9 (vidIQ designed it) | n/a (inherited) |
| Problem-door bridges | 9 (varied) | 7 (template visible) |
| Delayed payoff loops | 8.5 (comment exit ramp) | 9 |
| Re-hooks | 8.5 | 9 (Solutré myth-bust) |
| Voice | 8.5 | 7.5 (prompt echo, reveal tic) |
| Humor beat | 8.5 ("Holstein") | 8 ("Another cow." "Underfloor heating that moos.") |
| Dark turn | 8.5 | 9 (zigzag engraving, ritual reading, "Your species. Same brain.") |
| Accuracy / hedging | 7 | 9.5 |
| Length discipline | 9 | 3 (+48%, misreported) |
| Reference-echo avoidance | 8.5 | 7.5 |
| **Overall** | **8.5** | **8.0 as delivered → ~9 after the cut** |

---

## 7. Cut plan (3,560 → ~2,450 words)

Cut, don't rewrite. The material is good.

- **Hook (−110):** shorten the cave-navigation sentence (Cueva Mayor, squeezing through passages). Merge the "tropical machine" paragraph into one line.
- **Job 1 (−100):** keep the 600°C figure, the hearths built for different jobs, and "a dead mammoth was firewood." Cut the burned-bone debate paragraph.
- **Job 2 (−100):** drop the heat-treatment aside. Keep Volgu and "they were showing off." That's the gold in this section.
- **Job 3 (−100):** compress the tallow paragraph to two sentences.
- **Job 4 (−135):** cut the 1965 farmer and the room dimensions. Keep the 429-year reuse and the cold-trap physics.
- **Goggles (−90):** keep the 80% UV reflection figure, cut the soot and "sharpens vision" details.
- **Close (−50):** keep two of the three callbacks (needle → seams, fire → heat). Drop the thermostat line.
- **Global:** keep 2 of the 7 "flaw" bridges and rephrase the other 5. Keep 1 "It's not settled." Keep at most 3 one-word reveals.

---

## 8. Prompt fixes for the next Genspark run

1. **Per-beat word budgets** (like the table above) instead of one total. Models hit section budgets far better than global ones.
2. **No example phrases.** Replace "use second-person ownership ('You are the proof')" with "make the viewer feel they are the evidence of the story, phrased differently each time."
3. **Banned phrases:** "fatal flaw," "It's not settled" (hedge with varied wording), "thermostat," "You are the proof," "put your answer in the comments."
4. **Bridge variety rule:** "Each bridge must use a different sentence structure. Never repeat a bridge phrase."
5. **Accuracy rule (keep what worked):** "If evidence for a claim is thin at a specific site, say so in one clause and move on."

---

## 9. How to split the work (vidIQ / Genspark / this chat)

| Step | Tool | Why |
|---|---|---|
| Forensic analysis + 13-beat skeleton | **vidIQ AI Coach** (Step B P1 + skeleton half of P2) | You have ~1,500 credits, and vidIQ's analysis was its strongest output (9/10) |
| Full script, one shot | **Genspark Opus** (scarce, so use it once) | It held 3,500 words in one go without stopping, so the first-half/second-half split isn't needed. Spend the limited uses only on the step where writing quality matters most |
| Audit + cut list | **This chat** | Measure word count, check bridges/loops/echo, produce the cut |
| Fix pass | Genspark (1 call) or this chat | Only if the audit fails |

The runner-up was vidIQ multi-step for everything. It lost because vidIQ's facts were weaker (Solutré, calorie math), and accuracy is the one thing you can't easily check yourself.

---

## Status

- Part 1: done (Test 1, Step A, Step A fix, Step B)
- **Test 4 (Genspark Opus one-shot): this audit**
- Part 2 (SRT upload to vidIQ): pending
- Test 3 (MCP pipeline, Opus designs + writes): pending
- Handoff: after Part 2 and Test 3

**Not checked:** I didn't web-verify Korman' 9's hearth temperatures, the Volgu discovery year (Opus says 1873, Step B says 1874; sources differ), the "cow ≈ 1 kW" figure, or Step B's Watanabe 2021 citation. Check these before you record.
