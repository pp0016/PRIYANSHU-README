# Prompt Pack: Finishing the Script Experiment

## 0. Two facts you need first

**Step B is longer than vidIQ said.** I stripped it down to narration only (no clip notes, headers or source lists) and measured it: **2,803 words**. vidIQ claimed ~2,360. So both vidIQ and Genspark misreported their own length. Step B is ~17% over target, not on target. The clean file is here: [stepB_clean_narration.md](file:///C:/Users/renu5/Downloads/script%20writting%20idea/stepB_clean_narration.md). Use it for the blind judge prompt.

**The three ratings for Step B: 9.5 / 8.5 / 6.5.**
- 9.5 came from the earlier model in this chat (Opus 4.6), grading relative to Test 1 and Step A.
- 8.5 is my re-check on a fixed scale (10 = beats the reference video's retention).
- 6.5 came from your friend's Claude (Opus 5.5), judging "can this get millions of views."

These aren't contradictory, because they answer different questions. On the "millions" question I'd also say no. No script alone gets millions; the reference got 929K with its title, thumbnail and channel behind it. I won't drop my 8.5 to 6.5 without seeing its reasons. The blind judge prompt in Section 5 settles this properly: one scale, no names, no history.

---

## 1. What Genspark Opus can and can't do

**One correction first:** Genspark Opus **can** write the whole script. It wrote 3,560 words in one go without stopping. What it failed at was **length control and reporting its own length**, not capability.

| Job | Genspark Opus | Notes |
|---|---|---|
| Full script draft (one shot) | ✅ Strong | Proven. Best accuracy of all our tests |
| Cutting / tightening a draft | ✅ | Give per-section word budgets, not one total |
| Blind judging / comparing scripts | ✅ | It doesn't know which script is "ours," so it can't take sides |
| Analyzing transcripts you paste in | ✅ | You paste the text. It has no vidIQ MCP |
| Pulling transcripts / comments / stats | ❌ | Needs vidIQ MCP, which only Antigravity has |
| Measuring word counts | ❌ Unreliable | Check yourself at wordcounter.net (free) or in Antigravity |
| Usage limits | ❓ Unknown to me | Watch how many long replies one account gives before it caps |

### How to split the work to save Antigravity credits

| Step | Where | Why |
|---|---|---|
| Pull transcripts + comments, save as files | **Antigravity** (vidIQ MCP) | Only place MCP works. Cheap: a few tool calls |
| Analysis + structure + writing | **Genspark Opus** (paste the files) | Saves Antigravity credits on the heavy writing |
| Word count + copy check | **wordcounter.net** or one Antigravity call | Don't trust any model's own count |
| Blind judging | **Genspark** (fresh chat) | No memory of who wrote what |
| Same transcripts → vidIQ (Part 2) | **vidIQ web** | You have ~1,500 credits there |

**For Test 3 specifically:** you said you want the new Antigravity conversation to do the whole MCP run so you can test it. Prompts 3A–3D below do that. To save credits on later scripts, run only **3A** in Antigravity, then paste 3B–3D plus the saved files into Genspark.

---

## 2. Genspark: finish Test 4 (cut the 3,560-word script)

Paste into Genspark. Replace the bracket with the full script from `Four hundred and thirty thousand ye.md`, narration only (stop before "That runs about 2,500 words").

```
Below is a narration script for a 15-minute faceless YouTube explainer. It is 3,560 words. It needs to be 2,350–2,450 words. Cut it. Do not rewrite good material — remove and compress.

Word budget per section (stay within ±10%):
- Opening in the Pit of Bones, up to "Job one": 220
- Fire section: 200
- Stone tools / Volgu section: 200
- Hides, needle, tallow section: 240
- "Long weekend, not a winter" + doorway question: 120
- Mezhyrich house + doorway answer: 280
- Solutré + food storage: 200
- Body heat / who eats: 150
- Gough's Cave: 160
- Cows as heating: 140
- Snow goggles: 150
- Yaghan / Tierra del Fuego: 180
- Return to the Pit of Bones: 160
- Closing: 150

What to keep: the Solutré myth correction, the Volgu points being too fine to hunt with, the 429-year reuse of the Mezhyrich house, the Korman' 9 hearths, the Schöningen bear paws, the Gough's Cave details, the cow joke, the lemur torpor point.

What to cut first: navigation detail in the cave, the debate over whether burned bone was fuel, heat-treatment of flint, the 1965 farmer and room sizes at Mezhyrich, soot inside goggles, and one of the three callbacks in the closing.

Repetition fixes:
- The word "flaw" appears 7 times. Keep it at most twice. Rewrite the other section endings so each one uses a different sentence shape.
- "It's not settled" appears 3 times. Keep one. Express the other doubts in different words.
- Remove the line about turning up the thermostat.
- Use one-word paragraphs ("Hibernation." "The cow.") no more than three times in total.
- Do not add any new phrases that sound like slogans.

Output only the final narration. No notes, no word counts — I will measure it myself.

[PASTE SCRIPT HERE]
```

After it replies, paste the result into wordcounter.net. If it's outside 2,350–2,450, reply with: *"It's [X] words. Cut [section names] further to hit 2,400."*

---

## 3. Test 3: new Antigravity conversation (MCP), 4 prompts

**What I assumed:** same topic (Ice Age survival), but an original script that doesn't reuse Step B's "six jobs" skeleton. Otherwise we'd repeat the Test 4 problem, where Opus executed vidIQ's design instead of making its own.

Send these one at a time, in the same conversation.

### Prompt 3A: pull research (MCP)

```
Use the vidIQ MCP tools. Project: a 15-minute faceless YouTube explainer on how ancient humans survived the Ice Age, for a Tier-1 English audience.

1. Pull transcripts (vidiq_video_transcript, parameter videoId) for:
   - wt_7Hp7d7I8
   - tpfo9tRWQy4
2. Find ONE more long-form video on the same topic from a different channel: 8–25 minutes, ideally an outlier (views well above that channel's usual). Use vidiq_youtube_search or vidiq_outliers. Tell me which video you picked and why before pulling its transcript.
3. Pull the top comments for all three videos (vidiq_video_comments, order=relevance, maxResult=100, minLikes=10).
4. Save everything in the workspace under ice-age-test3/research/ — one file per transcript, one file per comment set.
5. Report for each video: title, channel, views, duration, measured word count (count with a script, don't estimate), and words per minute (word count ÷ duration).

Don't analyze anything yet. Don't use vidiq_video_watch. Keep total vidIQ credit use under 40 and tell me what you spent.
```

### Prompt 3B: analysis, gap map, original structure

```
Read the three transcripts and three comment files in ice-age-test3/research/.

A. For each video: how the first 45 seconds hook the viewer; the section order; how it moves between sections; how often it re-grabs attention and with what kind of moment; any open questions planted early and where they're answered; tone shifts; and the stretch where viewers are most likely to leave, with the reason.

B. From the comments: which moments viewers quote or praise, which facts they correct or dispute, and what they ask that none of the videos answered.

C. Overlap map. List facts and examples that appear in two or more videos — these are "saturated": we can mention them only briefly. Then list "fresh" material: things viewers asked for, things the videos got wrong, and well-documented findings none of them used.

D. Design an original structure for our script:
   - A central framing idea that none of the three videos use. Not a numbered list, not a countdown, not "six jobs."
   - Section-by-section word budgets totalling 2,350–2,450 words.
   - Mark where each open question is planted and where it's answered.
   - Mark where the darkest moment sits and where the tension releases with humor right after it.
   - At least 40% of the specific facts must come from the "fresh" list.

Show me A–D. Don't write the script yet.
```

### Prompt 3C: write the script

```
Write the full narration using structure D. Rules:

- Spoken narration only. No stage directions, no visual notes, no headings in the narration.
- Hit each section's word budget within ±10%. Save the script to ice-age-test3/script_v1.md, then measure each section's word count with a script. If the total is outside 2,350–2,450, fix it and measure again before showing me.
- Each section should end on something the previous solution couldn't handle, and that opens the next section. Every one of these endings must use a different sentence shape. Never reuse a phrase from one ending in another.
- When evidence is thin or disputed, say so in one clause, worded differently each time.
- Copy check: run a script that finds any 6-word sequence the script shares with any of the three transcripts. Rewrite every match.
- Banned anywhere: "fatal flaw", "it's not settled", "thermostat", "you are the proof", "you're the proof", "hit like", "subscribe", "in the comments", "delve", "testament", "tapestry", "in today's world".
- At most three one-word paragraphs in the whole script.
- No request to comment, like or subscribe anywhere. End on a closing thought, not a call to action.
- Below the narration, separately, list every claim that includes a number, date or named site, with a source. Mark any you couldn't confirm.

Show me the final script, the per-section word counts, and the copy-check result.
```

### Prompt 3D: fact-check and fix

```
Fact-check script_v1.md. For every claim with a number, date or named site, search the web and confirm it against a primary source or a reputable secondary source (journal, university, museum, major outlet).

Give me a table: claim | verdict (confirmed / overstated / wrong / can't verify) | source URL | fix.

Apply only the fixes for "overstated" and "wrong". Save as script_v2.md, re-measure the word count, and re-run the 6-word copy check. Don't change anything else.
```

---

## 4. Part 2: vidIQ with 2–3 transcripts (same files as Test 3)

Upload the transcript files saved by Prompt 3A (`ice-age-test3/research/`) to vidIQ AI Coach with **"Attach image or file."** Using the same inputs as Test 3 keeps the comparison fair. Send these in one conversation.

### Part 2 Prompt 1: analysis

```
I've attached transcripts of three high-performing YouTube videos about how ancient humans survived the Ice Age. I'm writing an original 15-minute faceless explainer on the same topic for a Tier-1 English audience.

Analyze only — don't write yet:
1. For each transcript: how the opening hooks the viewer, the section order, how it moves between sections, how often it re-grabs attention, open questions planted and answered, and tone shifts.
2. Which facts and examples appear in two or more transcripts (overused), and which strong ideas appear in only one.
3. Where each video is weakest — the stretch where a viewer would most likely leave, and why.
```

### Part 2 Prompt 2: structure + first half

```
Now design an original structure:
- A central framing idea none of the three videos use. Not a numbered list, not "six jobs."
- Word budgets per section, totalling 2,350–2,450 words.
- Mark where an open question is planted early and where it's answered near the end, and where a second question is planted at the midpoint and answered in the next section.
- Mark where the darkest moment sits and where humor releases the tension right after it.
- Overused facts only briefly; lean on the strongest ideas that appeared in only one video, plus well-documented findings none of them used.

Show the structure, then write the first half of the narration (sections up to the midpoint). Spoken narration only. Don't copy sentences from the transcripts. Never ask viewers to comment, like or subscribe. When evidence is disputed, say so briefly, worded differently each time.
```

### Part 2 Prompt 3: second half

```
Write the second half, continuing in the same voice. Stay within the word budgets. Every section ending must lead into the next section with a different sentence shape — never reuse a transition phrase. Answer the early open question honestly in the final section. End on a closing thought, with no call to action. Spoken narration only.
```

Measure both halves together at wordcounter.net afterwards.

---

## 5. Blind judge prompt (fresh Genspark chat)

**Before pasting:**
- Use [stepB_clean_narration.md](file:///C:/Users/renu5/Downloads/script%20writting%20idea/stepB_clean_narration.md) for the Step B script, not the raw vidIQ files. The clip notes and source lists would give away who wrote it.
- For the MCP script, paste narration only (no source list).
- **Flip a coin** to decide which one is Script A. Write down which is which, but don't tell the judge.
- Optionally add the cut Genspark script as Script C.

```
You are judging narration scripts for a 15-minute faceless YouTube explainer about how ancient humans survived the Ice Age. Audience: Tier-1 English-speaking viewers. You don't know who wrote them. Judge only what is on the page.

Scale for every category:
10 = would hold viewers better than a top video in this niche (~900K views)
7 = competitive with good channels in the niche
5 = watchable but forgettable
3 = generic AI writing

Categories:
1. Opening (first ~30 seconds of narration)
2. Retention structure — open questions planted and answered, how often attention is re-grabbed
3. Transitions between sections
4. Voice — does it sound like a person, or are there AI tells (repeated phrases, slogan lines, formula you can see)
5. Humor or tone shift
6. Emotional weight
7. Factual accuracy — flag any claim you believe is wrong, overstated, or stated with more certainty than the evidence allows
8. Originality — would someone who has watched other Ice Age videos learn new things
9. Length and pacing — estimate total words; target is 2,350–2,450

Output:
1. A score table for every script with a one-line reason per score.
2. The three weakest moments in each script: quote the line and say why a viewer would leave there.
3. A verdict, choosing exactly one:
   (a) One script wins and should be used, with its top fixes listed.
   (b) Merge — only if the merge would be clearly better than the best single script. Give a section-by-section plan: which section comes from which script, and which joining lines need rewriting.
4. Honestly: could any of these, with strong visuals, title and thumbnail, plausibly reach 1M+ views? What would that depend on besides the script?

Do not soften or average scores to be polite. If one script is clearly better, say so plainly.

SCRIPT A:
[paste]

SCRIPT B:
[paste]

SCRIPT C (optional):
[paste]
```

Bring the judge's output back here or to the new conversation, along with your coin-flip key.

---

## 6. Order of operations

1. Genspark: run the Section 2 cut prompt → measure → this finishes Test 4.
2. New Antigravity chat: Prompts 3A → 3D → this is Test 3.
3. vidIQ web: Part 2 Prompts 1–3, using the files from 3A.
4. Fresh Genspark chat: blind judge (Step B vs Test 3, plus optionally Test 4 and Part 2).
5. Then the handoff document, once all results are in.
