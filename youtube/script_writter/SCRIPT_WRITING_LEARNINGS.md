# Script Writing Learnings

What we learned from testing vidIQ's scriptwriting on one topic ("Ice Age Survival"), written so it applies to any niche. Read this before writing any script, by hand, with vidIQ, or with the vidIQ MCP.

Reference video used in every test: "How Did Ancient Humans Survive Deadly Winters?" (`wt_7Hp7d7I8`, 10:24, ~929K views, ~2,390 words).

---

## 1. What we tested, in order

| # | Method | What happened | Re-audited score |
|---|---|---|---|
| Test 1 | vidIQ **Scriptwriter** (topic + 15 min + "Match Reference Video") | Rewrote the reference with new words. Same hook, same section order, same examples. Dropped the reference's best moments. Generic "like and subscribe" ending. | **3.5 / 10** |
| Test 2, Step A | vidIQ **AI Coach**, one long prompt (analyze + map + write) | Different hook and section order. But almost every fact still came from the reference, and several sentences are near-copies. | **5 / 10** |
| Test 2, Step A + fix | Same chat, one "fix these 4 paragraphs" prompt | Fixes landed (humor, closer, cannibalism detail, Yaghan detail). The fix also introduced a new factual distortion. | **5.5 / 10** |
| Test 2, Step B | AI Coach, three prompts: (1) analysis only, (2) skeleton + first half, (3) second half | Best result. New sources the reference never used, real open loops, real humor beat. Still has structural and factual problems listed below. | **7 / 10** |

Scale: 10 = publish as-is and beats the reference. 7 = publish after a focused edit. 5 = needs a structural rewrite. 3 = derivative, don't use.

Still not done: Test 2 Part 2 (upload transcripts/audio of two videos to AI Coach) and Test 3 (build the script ourselves from vidIQ MCP data).

---

## 2. Corrections to the earlier audits

The earlier reports in this project scored too generously. These are the fixes.

**The one-shot was scored 8/10 for originality. It's closer to 5.** We forced it to copy. Our "mandatory content" list (bone goggles, cold-trap door, tallow, Yaghan, hibernation, needle, Mezhyrich) was taken straight from the reference transcript. So the script re-ordered the reference's fact list instead of researching its own. Near-copied lines:

| Reference | One-shot |
|---|---|
| "People made homes out of giants." | "People made homes out of giants." (identical) |
| "It's so small it sounds silly." | "It's so small it almost sounds like a joke." |
| "One scientist called it maybe the most important invention in human history, and he's got a point." | "One researcher called it maybe the most important invention in human history. For your survival, he's got a point." |
| "They figured that out tens of thousands of years before anyone wrote down how it works." | "They figured out how air moves tens of thousands of years before anyone wrote the physics down." |
| "Simple, a little gross, and it worked." | "It's a little gross..." |
| "...stacking mammoth bones into a house to tapping a button for heat." | "...stacking mammoth bones into a shelter to pressing a button for heat." |

**Step B was scored 9.5/10. It's a 7.** Problems the earlier audit missed:

1. **The counting frame breaks.** The hook promises "six jobs." Job six ends around 9:40. The last five minutes (dark turn, humor, goggles, Yaghan, payoff) sit outside the frame. A viewer counting to six feels the video is over at job six, which makes that a likely drop-off point. If you promise a count, everything has to live inside it, or the count has to be the setup for a bigger final item.
2. **The hook undercuts itself.** Within 40 seconds it says the hibernation idea is disputed and "I'm not going to pretend this is settled." Honesty is good, but it belongs at the payoff, not before the viewer has a reason to stay.
3. **It tells viewers to go to the comments mid-video** ("Put your answer in the comments, then keep watching"). Sending people to the comments at 5:15 sends them away from the video. Ask the question, don't send them anywhere.
4. **A medium slip:** "the reason there's a person reading this." It's a video.
5. **A narrator habit that turns into a tic:** "I'm not going to pretend," "I want to be straight," "here's the honest note," "I'm not going to tell you a tidy story." Once is trust. Five times sounds like the narrator praising his own honesty.
6. **The "That's not X. That's Y." construction is everywhere:** "That is not a campfire. That is a kiln." "The doorway wasn't a door. It was a filter." "Not a metaphor, literally..." This pattern is one of the clearest signs of AI writing. Use it once per script at most.
7. **The runtime math is wrong.** ~2,360 words was sold as 15 minutes. The reference narrator speaks at ~230 words per minute (2,393 words in 10:24). At that pace the script runs about 10 minutes. vidIQ pointed this out itself in the one-shot notes.

**Two of my own earlier claims were wrong or incomplete:**

- *"No tool can pull the retention heatmap."* vidIQ MCP can't. But the "Most replayed" graph on the progress bar can be read by yt-dlp (`--dump-json`, `heatmap` field) on videos where YouTube shows it. This is from memory, not tested here, so run it once before relying on it. Also note it measures **replays**, not audience retention. It shows which moments people rewatched, not where they left.
- *"YouTube doesn't penalize AI scripts."* Mostly right, but incomplete. On 15 July 2025 YouTube renamed its "repetitious content" policy to **"inauthentic content."** AI help is allowed. What gets demonetized is content that follows a template with minimal variation, is easy to mass-produce, or lacks real author input. This matters for us: if we run one formula the same way on every video, the channel starts to look exactly like that.

---

## 3. Facts in these scripts that were wrong or shaky

Checked by web search during the audit:

| Claim in a script | What's actually true | Which script |
|---|---|---|
| Mezhyrich was "in use for over four hundred years" / "Nobody rebuilds a bad idea for four hundred years" | The 2025 study (Chu et al., *Open Research Europe*) gives a duration of **0 to 429 years**. That's the uncertainty range. The authors say it fits **a single occupation** or short repeat visits. The four-centuries line is a misreading. | Step B, both halves; one-shot ("used again and again for centuries") |
| Solutré hunters drove herds with fire / "the landscape does the killing" | The cliff-jump story came from an 1872 novel by one of the excavators. Modern view: hunters **ambushed** migrating horses in natural traps at the base of the slope. The bones aren't under the cliff and show no fall injuries. | One-shot (fire), Step B (implied) |
| The eyed needle is what made fitted clothing possible | Bone **awls** were already used for fitted clothing 70,000–80,000 years ago. Eyed needles (earliest ~40,000 years ago, Denisova Cave, per Gilligan et al., *Science Advances* 2024) made **finer, layered** clothing and decoration possible. | Both |

Not verified, and treat as risky until checked:

- Bone slit goggles as "the first sunglasses, tens of thousands of years" old. The known examples are Inuit and far more recent. Step B said so honestly. The one-shot didn't.
- Tallow smeared on the face *during the Ice Age*. That's ethnographic practice, not something found at an Ice Age site.
- A 600°C Ice Age hearth in Ukraine (taken from the reference, no source given).
- Mammoth meat sunk in ponds to keep it fresh (from the reference, no source given).
- A "cold trap" entrance passage *at Mezhyrich specifically*.
- The fix prompt's version of Darwin: "somehow looking comfortable" and "bodies measured consistently hotter." Darwin described the Fuegians as miserable, not comfortable. The metabolism studies were done on Fuegian groups decades later. Don't put words in a historical figure's mouth.
- Made-up numbers like "one reindeer is three days of calories for one family." It's plausible but nobody sourced it.

**Lesson:** an AI script that sounds well-sourced isn't checked. Citations appearing in the text doesn't mean anyone read the papers. Every number, date, name and quote gets checked before voiceover.

---

## 4. How vidIQ actually behaves (process facts)

**Scriptwriter tool**
- Inputs are just topic, Long/Short, duration, and Tone. Tone can be a preset, custom text, or "Match Reference Video."
- Match Reference Video takes **one** video. There's **no field for instructions**, so you can't tell it "don't copy." Matching is what it's built for, and it copies the reference's content, not just its style.
- It asks one clarifying question, then offers 3 concepts to pick from. The finished script has a "Refine" box with suggestions.
- Cost: about 1 credit per minute of script.
- **Verdict: don't use it for reference-based scripts.**

**AI Coach (main chat)**
- You attach **one** YouTube video through "+ → Add from YouTube." Extra links pasted as text are not pulled in. It also has "Attach a video" and "Attach image or file," and a Regular / Deep Thinking mode.
- About 10 credits per message regardless of length, so long, detailed prompts cost nothing extra.
- It reads the whole reference (it reported runtime and views) and can look up outside sources (it cited Wikipedia, journals, museum pages).
- A fix prompt in the same chat works well if you say "rewrite only these paragraphs, keep everything else."

**Why three prompts beat one**
- Asking for analysis + structure + script in one reply spreads quality thin. It falls back on the reference's facts.
- Analysis on its own first makes the model actually work out the mechanics (re-hook rhythm, transitions, voice) before it writes anything.
- Writing in two halves keeps quality even across the script. The second half takes on the voice the first half set.
- When we gave it space to research (prompt 2), it found new material: Volgu points, the Denisova needle, Gough's Cave, the Baffin Island goggles. That's the main reason Step B is more original.

**vidIQ MCP (for Test 3)**
- `vidiq_video_transcript` takes `videoId` (not a URL field), 5 credits.
- `vidiq_video_comments` costs 5 credits per page, sort by relevance, can filter by minimum likes.
- `vidiq_comment_insights` costs 5 credits and finds recurring questions and complaints across a niche.
- `vidiq_video_watch` costs 25 credits and gives a visual scene-by-scene breakdown.
- `vidiq_video_stats` costs 5 credits and returns views, likes, comments and VPH over time.
- No MCP tool returns audience retention.

---

## 5. Rules for writing any script

### Originality
1. **Take techniques from the reference, never its facts or wording.** Pacing, re-hook rhythm, transition style and voice are fine to borrow. The fact list, examples, hook and section order are not.
2. **Never build a "must include" list from the reference's own content.** Build it from your own research. That was our biggest mistake.
3. **Use two or three references, not one.** One reference makes a copy. Several give you patterns.
4. **Every script needs material the references don't have.** Aim for at least a third of the facts to come from sources no reference used.
5. **Vary the formula between videos.** Don't use the same hook type, the same counting device or the same dark-turn/humor placement every time. That's how "template with minimal variation" happens.

### Hook (first 30–60 seconds)
6. Open on something concrete and strange, like an object, a place or a finding. Don't open with a setup about the viewer's life. The reference already used "you're warm right now," so it's taken.
7. Plant one open loop that pays off near the end, and make it a real question.
8. Don't put disclaimers in the hook. Save the "scientists disagree" part for the payoff.
9. The hook has to pay off the title, quickly.

### Structure
10. **Order sections by what matters most for survival or stakes, not by time.** Each section fixes the problem the last one left open.
11. **Use problem-door transitions.** End each section by naming what it couldn't solve, and that becomes the next section's opening. ("Fire works, as long as you never leave. And you have to leave.")
12. **If you promise a count ("six jobs"), keep everything inside it.** Or make the last item the big one. Don't let the frame run out early.
13. **No separate "Introduction" after the hook.** Go straight into the first section.
14. **No announced roadmaps** that read like a table of contents.
15. **Re-hook roughly every 35–55 seconds and rotate the type:** mystery lead-in, myth correction ("everyone pictures X; the truth is better"), stakes raise, authority line, emotional hammer, tone shift. Two of the same type should never land back to back.
16. **Plant a second loop at the midpoint** so the back half has its own pull.
17. **Dark turn at about 60–70%.** One section that breaks the comfortable tone with a real, sourced human cost.
18. **Humor goes right after the dark turn.** It plays as relief instead of breaking the mood. It needs to be a real change in tone (three or four sentences), not a passing joke.
19. **End on a reframe that sticks.** No standalone "like and subscribe." Don't send viewers to the comments mid-video either.

### Voice (this is what makes it sound human)
20. Write it to be spoken. Short sentences, mostly under 12 words. Use fragments for rhythm ("Wrong body. Wrong place. Worst possible time.").
21. Talk to the viewer as "you" and make them part of the story ("you're the proof").
22. Be sure where the evidence is solid, and say "might," "one study suggests" where it's contested. Do that at the claim itself, once. Don't keep announcing how honest you're being.
23. Tie every number to a picture ("hotter than a pottery kiln"), never to a chart.
24. Use small, dry asides ("a little gross, and it worked") about once every couple of minutes.
25. **Patterns to cut:** "That's not X, that's Y" more than once; "Here's the thing/Here's what" openers piling up; "genuinely," "truly," "incredibly"; em dashes everywhere; three-item lists in every paragraph; "game-changer," "testament to," "delve," "tapestry"; closing lines that sum up the paragraph you just heard.
26. Read it out loud. If you run out of breath on a sentence, split it.

### Facts
27. Check every name, date, number and quote before voiceover. AI citations get checked like any other claim.
28. Say how far each claim goes: a real site and real finding stated firmly, an interpretation stated as one, a myth called a myth.
29. Never invent a quote or describe what a historical person "wrote" unless you have the text.
30. Never take a range like "0–429 years" and present it as a fact like "four hundred years."
31. Keep the evidence period straight. Don't use medieval or modern ethnographic examples as Ice Age evidence without saying so.

### Length
32. Set the length in **words at the narrator's real pace**, not in minutes. Time a sample of the TTS voice first. At 230 wpm, 15 minutes is ~3,450 words. At 150 wpm it's ~2,250.

---

## 6. Prompting rules that worked

- Give the goal and the context, list the **specific failures to avoid**, and show good vs. bad narration with an example line. That jump from vague to specific is why the one-shot did so much better than Test 1.
- Ask for analysis on its own first, then structure + first half, then the second half.
- Use one fix prompt for surgical edits: name each problem, say what to do about it, and "rewrite only the affected paragraphs."
- Tell it to research new sources. Don't hand it the reference's facts as requirements.
- Ask for a proof list (claim → source) next to the script so checking is quick.

---

## 7. Plan for the MCP-built script (Test 3)

1. Pick 2–3 strong references from different channels on the topic.
2. Pull each transcript (`vidiq_video_transcript`) and the top comments (`vidiq_video_comments`, relevance, minimum likes). The most-liked comments show which moments landed.
3. Optionally pull "Most replayed" data with yt-dlp for the references (check first that it works).
4. Analyze each reference: hook beats, section list with timings, re-hook positions and types, transitions, voice traits, words per minute.
5. Make a list of what the references have in common (the topic's core) and what none of them cover (our edge).
6. Research the edge material and build a proof list.
7. Build the skeleton using the rules in section 5, with a different hook type and order from every reference.
8. Write it in two halves.
9. Audit it against this file: originality vs. each transcript, the frame holds, re-hook rhythm, AI-pattern sweep, every fact checked, word count at measured pace.
10. Fix, then hand over one final script with a short pass/fail sheet, so it doesn't need multiple read-throughs.
