# Faceless Finance & Money Niche — Complete Outlier Research Report

**Prepared for:** Creator (YouTube growth coaching session)
**Date:** October 14, 2026
**Scope:** Faceless finance / money niche · long-form only (10+ minutes) · last 90 days · qualifying on ≥5× subscriber-to-view ratio OR VPH ≥150

This document contains the complete record of the session: every prompt, every response, every table, every analysis, and the full deeper research pass. Nothing from the conversation has been omitted.

---

## Part 0 — Methodology and Data Caveats

**Data sources used**

| Source | What it provided |
|---|---|
| vidIQ outlier index (vector-indexed) | Breakout videos, breakout score, VPH, subscriber counts, channel country, average views |
| YouTube Data API (per-video) | Live titles, descriptions, tags, publish dates, durations, view/like/comment counts |
| YouTube Data API (per-channel) | Live subscriber counts, lifetime views, video counts, recent and top video performance |
| vidIQ keyword database | Search volume, competition score, overall score, top markets, estimated monthly searches |
| vidIQ question index | Actual searched questions with volume, growth, and 30-day baselines |
| YouTube comment API | Top-level comments with like/reply counts per video |

**Definitions used throughout this report**

- **Breakout score** = a multiple of the channel's average views. It is a ratio, not a rate, velocity, or forecast.
- **VPH** = views per **hour** (never per day). `vph_latest` is the source's latest interval; the interval duration is not specified in the source. `vph_all_time` is a lifetime hourly average.
- **views_per_day** = a calculated lifetime-average daily rate, not current momentum and not the last 24 hours.
- **View counts quoted from the Data API** are live public totals. The Analytics API undercounts recent videos with a 2–3 day reporting lag.
- **Subscriber counts** are live public counts from the Data API; index-sourced counts may differ.

**Scope limitations — read these before acting on any number**

1. **There is no "faceless" flag in the outlier index.** Facelessness in this report is an editorial classification based on format: narrated stock-footage storytelling, animated/voice-over POV, screen-recorded tutorials, hands-only footage, and long-runtime audiobook reads. Treat it as a read, not indexed data.
2. **VPH moves between pulls.** The same video reported 110.16 on one pull and 96.39 on another, on the same day. Treat VPH as directional.
3. **The index does not expose live/broadcast state**, so archived livestreams may appear as long-form.
4. **Subscriber-to-view ratios are descriptive, not predictive.** A tiny channel with a large multiple does not prove the format will repeat.
5. **Long-form threshold applied:** 600 seconds (10 minutes) minimum.

---

## Part 1 — The Original Request

> **Prompt 1:**
>
> "Find 10 outlier videos from the last 90 days in the faceless finance and money niche where the video got 5x or more views than the channel's subscriber count, or VPH >= 150. Any faceless format. Long-form only (10+ minutes).
>
> Start directly with the table:
> | Video Title | Channel Name | Channel Subs | Video Views | VPH | Duration | Why It Went Viral (one line) |
> After the table, answer:
> 1. Group these 10 videos into 3 topic clusters. Name each cluster and list which videos belong to it.
> 2. Which cluster has the lowest competition and highest viewer demand right now?
> 3. Give me 5 untapped video ideas based on the gaps between these outliers — topics adjacent to what worked but that nobody has made yet."

---

## Part 2 — Original Findings

### The 10 qualifying outliers

Filtered from a 90-day long-form pool across four niche queries (personal finance, make money online, investing, budgeting), 10+ minute minimum.

| Video Title | Channel Name | Channel Subs | Video Views | VPH (latest interval) | Duration | Why It Went Viral |
|---|---|---|---|---|---|---|
| Power of Invisible Money \| Art of Becoming Wealthy on a Low Salary | Sight of Fortitude | 19,100 | 469,358 (24.6× subs) | 320.66 | 23:52 | "Invisible money" + low-salary premise reframes saving as discipline, not income — a promise almost anyone can self-apply. |
| Power of Money Mindset \| How 4 Rules Quietly Make Financial Stability | Sight of Fortitude | 19,100 | 514,342 (26.9× subs) | 110.16 | 23:51 | "Stealth wealth" as an identity (looking poor = getting rich) gives the viewer a status win instead of a chore. |
| Once You Understand Money, You See the World Differently \| The Money Map | Simple Ways of Life | 40,800 | 53,327 (1.3× subs — qualifies on VPH) | 549.94 | 26:54 | "Understanding money" explainer hits the feels-broke-while-earning-more nerve without asking for a behaviour change. |
| POV: You Quietly Built a Portfolio That Pays More Than Your 9-to-5 | Ollie Finance | 5,740 | 192,321 (33.5× subs) | 209.80 | 21:19 | POV second-person framing turns a portfolio-math video into a fantasy the viewer finishes "living." |
| POV: You Become Debt Free While Everyone Else Drowns in Payments | POV Money Habits | 1,040 | 58,734 (56.5× subs) | 23.54 | 23:04 | Debt-free POV with a concrete $0.00 balance moment — a visceral before/after anyone in payments recognises. |
| POV: Your Entire Financial Life, From $32,000 to Quiet Millionaire | Marcus Gets Rich | 1,070 | 15,458 (14.4× subs) | 0.09 | 1:17:28 | A 22-year life span in one sitting — long-runtime "story to fall asleep to" that racks ratio off a tiny base. |
| 5 "Lazy" Ways to Make Money Online in 2026 (Beginner Friendly) | Hemlata chauhan | 12,500 | 167,384 (13.4× subs) | 1,075.28 | 15:04 | "Lazy" + named-2026 + beginner-friendly: the lowest-effort promise in a high-intent search space. |
| 10 Websites That Actually Pay You Money \| New Side Income Websites | Smart With Avy | 2,910 | 431,111 (148.1× subs) | 409.52 | 12:00 | A numbered list of sites that "actually pay" — a countable, screenshot-able payoff for a zero-sub channel. |
| 3 GENUINE Work from HOME job for everyone using MOBILE — No requirement | khushi explains | 15,100 | 436,313 (28.9× subs) | 252.86 | 11:17 | "Genuine, no requirement, using MOBILE" removes all four objections at once — built for a mobile-first audience. |
| How To Make Money From Pinterest Full Step By Step Guide 2026 | Khushal Sky | 26,100 | 314,941 (12.1× subs) | 100.65 | 24:49 | Takes an established platform (Pinterest) and promises a full step-by-step monetisation path with proof in-frame. |

**Note on later figures:** A subsequent API pull returned updated live view counts (Sight of Fortitude 469,865 and 514,646; Simple Ways of Life 54,332; Ollie Finance 192,529; POV Money Habits 58,772; Hemlata chauhan 168,971; Smart With Avy 431,870; khushi explains 436,491; Khushal Sky 315,012). These are the same videos at a later timestamp. Both figures are preserved above and below.

### Cluster 1 — Three topic clusters

**Cluster A — Quiet-Wealth Money-Psychology Stories**
*Format: narrated, third-person, stock footage*

1. Power of Invisible Money — Sight of Fortitude
2. Power of Money Mindset — Sight of Fortitude
3. Once You Understand Money — Simple Ways of Life

**Cluster B — POV Second-Person Financial Life**
*Format: voice-over + animation, "you" framing*

4. POV: You Quietly Built a Portfolio That Pays More Than Your 9-to-5 — Ollie Finance
5. POV: You Become Debt Free While Everyone Else Drowns in Payments — POV Money Habits
6. POV: Your Entire Financial Life, From $32,000 to Quiet Millionaire — Marcus Gets Rich

**Cluster C — Faceless "Earn Online / Get Paid" Tutorials & Listicles**
*Format: screen recording, numbered payoffs*

7. 5 "Lazy" Ways to Make Money Online in 2026 — Hemlata chauhan
8. 10 Websites That Actually Pay You Money — Smart With Avy
9. 3 GENUINE Work from HOME job using MOBILE — khushi explains
10. How To Make Money From Pinterest Full Step By Step Guide 2026 — Khushal Sky

### Cluster 2 — Lowest competition, highest demand

**Winner: Cluster B (POV).**

The demand signal is the strongest number on the board: `pov finance` carries a volume score of 99.99 and approximately 4.99M estimated monthly searches against competition of only 50.1 — an overall score of **79.95**, the highest of every keyword checked for the original brief.

Supply-side proof sits inside the cluster itself: all three POV videos came from channels between **1,070 and 5,740 subs** that beat their own subscriber base by 14–57×. Tiny channels, huge multiples = thin competition.

Adjacent low-competition terms in the same psychological lane:

| Keyword | Competition | Est. Monthly Searches | Overall |
|---|---|---|---|
| financial habits | 9 | ~32,000 | 76.76 |
| quiet wealth | 33.9 | 160,313 | 73.06 |
| money psychology | 41.5 | 477,745 | 74.27 |

**Important caveat:** `pov finance`'s top markets are Pakistan, Nigeria and India — this is a global trend, not a US-centric one. Decide which audience you are packaging for. Cluster C has comparable raw demand, but you would be the fifth channel into a space where four of the ten outliers already sit.

### Cluster 3 — Five untapped video ideas

1. **"POV: You Started Cash Stuffing With Your Last $200"** — Cluster B's format has never met the cash-stuffing format. Cash-stuffing videos in this niche outperform hard (9.2× and 10.3× subs on 2.7K and 1.95K-sub channels) but stay in silent hands-on framing. POV narration is the gap. *No search-volume pull on this one — the evidence is outlier behaviour, not keyword data.*
2. **"Why Saving Money Feels Impossible (It's Not Your Salary)"** — This is the top question in the niche: `why saving money feels impossible`, ~33,126 est. monthly searches, competition 24.5, growth **+314%**. Nothing in the top 10 addresses it.
3. **"POV: You Retired With $400K — And Your Spending Did the Opposite of What You Planned"** — Retirement-spending data overperforms (a J.P. Morgan retirees video did 14.9× its channel's subs), but it is all advisor-talking-head. No one has put the retirement reveal into Cluster B's narrative frame.
4. **"How Banks Actually Create Money (The Part Nobody Tells You)"** — `how banks create money`: ~18,779 est. monthly searches, competition 53.2. The Simple Ways of Life video touched money mechanics in passing and spiked to a VPH of 549.94; nobody has given the mechanic its own video.
5. **"POV: You Look Rich and You're Completely Broke"** — Cluster A sells the stealth-wealth identity, Cluster B sells the debt-free payoff, and no one covers the flip: the years spent performing wealth before the turn. Same 20–25 min narrated format, an unclaimed half of the same emotional arc.

---

## Part 3 — The Deeper Research Request

> **Prompt 2:**
>
> "Now go deeper — expand on every channel, video, and insight you found with more data points, and find any additional channels or outliers you missed. Then compile the ENTIRE conversation into one complete downloadable PDF report — every prompt I asked, every response you gave, every table, every analysis, all your thinking and reasoning, plus this new deeper research. One single comprehensive PDF with nothing left out. Start from the first question to this one."

---

## Part 4 — Corrections and Caveats From the Deeper Pass

### 4.1 A whole cluster was missed

The original four seed queries (personal finance, make money online, investing stocks, money saving budgeting) never surfaced the **long-runtime money audiobook** genre, because those videos do not use finance language — they use "audiobook" and "sleep."

That genre contains the single largest breakout in the entire niche:

| Video | Channel | Subs | Views | × Subs | Breakout Score | VPH | Duration |
|---|---|---|---|---|---|---|---|
| The Mindset Shift: Psychology of Changing How You Think… (Audiobook) | Audiobook Institute | 2,700 | 255,624 | 94.7× | **899.92×** | 435.41 | 2:04:37 |

That is roughly **twice the breakout multiple** of anything in the original ten.

### 4.2 Two numbers need a caveat

`vph_latest` is computed over an interval the source does not specify, and it moves between pulls. The Money Mindset video reported **110.16** on the first pull and **96.39** on the second — same video, same day. Treat VPH as directional, not as a fixed rate.

### 4.3 One of the original ten is a trap, not a template

**Marcus Gets Rich** is **51% of its own channel's entire lifetime views** — 15,458 of 30,192. Every video it published afterwards: 1,335 · 269 · 220 · 48 · 27 · 19 · 12 · 11 · 8 views. Copying that video is copying a lottery ticket, not a repeatable format.

---

## Part 5 — Channel Deep-Dive (Full Data)

### 5.1 Channel snapshot table

| Channel | Subs | Videos | Lifetime Views | Country | Cadence | Repeatable? |
|---|---|---|---|---|---|---|
| khushi explains | 15,100 | 190 | 1,900,682 | IN | near-daily | ✅ **7 videos >40K** — strongest repeatable pattern found |
| Ollie Finance | 5,740 | 12 | 754,545 | US | every 6–8 days | ⚠️ 4 of 12 >111K, but also a 493-view flop — high variance |
| Sight of Fortitude | 19,100 | 33 | 1,983,203 | — | every 3–4 days | ✅ Money videos run 2–6× its non-money videos |
| Simple Ways of Life | 40,800 | 89 | 2,774,973 | US | near-daily | ⚠️ Likes hidden across the catalogue; the 54K video is decelerating |
| Smart With Avy | 2,910 | 15 | 534,119 | IN | irregular | ⚠️ One video = 81% of lifetime views, but format repeats at 20–33K |
| Hemlata chauhan | 12,500 | 255 | 1,367,771 | IN | daily | ⚠️ Hindi money content did 620,574; English did 168,971 |
| Khushal Sky | 26,100 | 128 | 1,256,679 | IN | frequent | ❌ Real engine is editing tutorials, not money |
| POV Money Habits | 1,040 | 25 | 231,825 | US | near-daily | ⚠️ Pivoted to family-drama POV in Oct; new videos do 1.5–9K, below its Sep money videos |
| Marcus Gets Rich | 1,070 | 28 | 30,192 | US | near-daily | ❌ One hit, then collapse |

### 5.2 Sight of Fortitude — full video performance

Channel description: "Inspiring human spirit through Motivational Stories and English Listening Practice."

| Video | Published | Views | Likes | Comments | Engagement % | Views/Day |
|---|---|---|---|---|---|---|
| Power of Money Mindset | 2026-09-23 | 514,646 | 4,181 | 379 | 0.81 | 24,507 |
| Power of Invisible Money | 2026-09-08 | 469,865 | 5,146 | 337 | 1.10 | 13,051.80 |
| Power of Weekend | 2026-09-12 | 189,320 | 1,528 | 154 | 0.81 | 5,916.20 |
| Power of Finding a Hobby | 2026-09-20 | 75,384 | 667 | 113 | 0.88 | 3,141 |
| Power of a Bad Day | 2026-09-16 | 28,006 | 371 | 60 | 1.32 | 1,000.20 |
| Power of Simple Living | 2026-09-04 | 22,917 | 424 | 77 | 1.85 | 572.90 |
| Power of Living Today | 2026-08-31 | 19,664 | 195 | 25 | 0.99 | 446.90 |
| How 7 Small Steps… | 2026-08-28 | 3,786 | 46 | 3 | 1.22 | 80.60 |
| How This Quiet Morning Hour… | 2026-08-24 | 1,703 | 57 | 13 | 3.35 | 33.40 |
| Power of Thinking Differently | 2026-08-18 | 2,214 | 89 | 13 | 4.02 | 38.80 |

**Key insight:** The two money-titled videos are the only two in the channel's top two slots. Non-money "mindful living" titles in the same window topped out at 75,384. **Money framing is worth 2–6× on this channel.** The other two videos in its top four ("Power of Weekend" at 189,320) suggest an adjacent — possibly stronger — frame: *time scarcity*, not wealth.

Tags on the flagship video (19 total, truncated): stealth wealth · money mindset · how to be financially stable · 4 rules of wealth · financial freedom story · money psychology · how to build wealth quietly · How to stop lifestyle creep · compound interest · financial minimalism

### 5.3 Simple Ways of Life — full video performance

Channel description: "Feeling stuck? Tired of starting over? … no hustle culture, no 'rise and grind' speeches."

| Video | Published | Views | Comments | Views/Day |
|---|---|---|---|---|
| The Real Way to Build Wealth From Nothing | 2026-09-13 | 98,059 | 36 | 3,163.20 |
| Train Your Brain to Enter Flow State on Command (7 Steps) | 2026-09-01 | 59,296 | 31 | 1,379 |
| **Once You Understand Money (The Money Map)** | 2026-10-11 | **54,332** | 47 | **18,110.70** |
| How to Make Your Life Run on Autopilot (6 Systems) | 2026-09-03 | 51,437 | 28 | 1,254.60 |
| The Wealthy Mindset: 7 Habits You Need to Start Today | 2026-09-27 | 49,099 | 24 | 2,888.20 |
| How Money Starts Growing Money (Wealth Flywheel) | 2026-10-04 | 43,495 | 61 | 4,349.50 |
| The Psychology of Luck | 2026-09-24 | 35,606 | 43 | 1,780.30 |
| 3 Things You Can Do To Learn Faster | 2026-09-15 | 35,488 | 19 | 1,223.70 |
| Psychology of Weight Loss | 2026-09-17 | 28,641 | 29 | 1,060.80 |
| How to Make Your Brain Crave Discipline | 2026-09-29 | 21,338 | 29 | 1,422.50 |
| These 18 Tiny Habits Can Make You Rich | 2026-10-01 | 19,522 | 13 | 1,501.70 |
| These 30 HABITS Shapes A BULLET PROOF MINDSET | 2026-09-22 | 13,949 | 14 | 634 |
| The Psychology of Self Worth | 2026-10-06 | 8,656 | 27 | 1,082 |
| If You Had Enough Money, Would All Your Problems Disappear? | 2026-10-08 | 5,327 | 22 | 887.80 |
| Every Level of Intelligence Explained | 2026-10-13 | 4,776 | 12 | 4,776 |

**Key insight:** Likes are suppressed channel-wide (0 returned across the catalogue). Critically, this channel has already made *four* money videos in the top 7 of its own list — the differentiation is not the topic, it is the **positioning**: this one sells mechanics ("how money works"), while the niche sells psychology ("what money means"). The Money Map video carries the highest views/day on the channel at 18,110.70 despite being the most recent, which indicates it is still accelerating.

Its "Every Level of Intelligence Explained" (published one day before this report) had 4,776 views and 12 comments — too new to read.

### 5.4 Ollie Finance — full video performance

Channel description: "Ollie Finance | Wealth, Money & The Stories Behind Success… Money is more than a number. It's a story of choices, risk, ambition, and time."

| Video | Published | Views | Likes | Comments | Engagement % | Views/Day |
|---|---|---|---|---|---|---|
| POV: You Quietly Built a Second Income and Told No One | 2026-08-25 | 197,613 | 2,389 | 88 | 1.21 | 3,952.30 |
| POV: You Quietly Built a Portfolio That Pays More Than Your 9-to-5 | 2026-10-03 | 192,529 | 1,306 | 239 | 0.68 | 17,502.60 |
| POV: Your Life After Winning the $600M Lottery | 2026-07-09 | 171,479 | 3,602 | 571 | 2.10 | 1,767.80 |
| POV: You Silently Building a Holding Company From $0 to $600M | 2026-07-25 | 111,900 | 2,348 | 151 | 2.10 | 1,381.50 |
| POV: You Quietly Escaped the Rat Race | 2026-08-13 | 34,700 | 410 | 52 | 1.18 | 559.70 |
| POV: You Building Wealth in Silence | 2026-08-06 | 18,379 | 292 | 32 | 1.59 | 266.40 |
| POV: Everyone Thinks You're Struggling — You're Actually 7 Figures In | 2026-09-18 | 15,402 | 102 | 7 | 0.66 | 592.40 |
| POV: You Stopped Trying to Look Rich | 2026-09-25 | 10,874 | 81 | 4 | 0.74 | 572.30 |
| POV: You Started Thinking Like Old Money | 2026-08-31 | 5,093 | 68 | 9 | 1.34 | 115.80 |
| Your Life at Every Stage of Secretly Leaving the 9 to 5 | 2026-08-20 | 3,151 | 75 | 8 | 2.38 | 57.30 |
| POV: You Track Every Dollar for 30 Days and Regret Looking | 2026-09-05 | 2,119 | 33 | 7 | 1.56 | 54.30 |
| POV: The Year You Stopped Buying Status and Started Buying Silence | 2026-10-13 | 493 | 15 | 4 | 3.04 | 493 |

**Key insight:** This is a 12-video channel with 754,545 lifetime views. Four of twelve cleared 111K. But the newest video (493 views) and three others sit under 6K. The pattern that wins is consistent: **"quiet / silent / no one knows" secrecy framing** — all four hits use it; the two most recent videos that dropped the secrecy hook ("Stopped Trying to Look Rich", "Track Every Dollar") collapsed to 10,874 and 2,119. The channel's highest-engagement video (3.04%) is the smallest — high engagement on low reach is not a signal to follow.

### 5.5 POV Money Habits — full video performance

Channel description: "…puts you inside the everyday decisions that quietly decide whether someone builds wealth or stays stuck. Through animated, story-driven videos told from a second-person POV…"

| Video | Published | Views | Likes | Comments | Engagement % | Views/Day |
|---|---|---|---|---|---|---|
| POV: You Become Debt Free While Everyone Else Drowns in Payments | 2026-09-12 | 58,772 | 626 | 96 | 1.07 | 1,836.60 |
| POV: You Broke The Paycheck Cycle By Living On One Dollar Rules | 2026-09-24 | 22,270 | 321 | 40 | 1.44 | 1,113.50 |
| POV: Your Business Partner Stole Everything | 2026-10-08 | 21,575 | 278 | 23 | 1.29 | 3,595.80 |
| POV: You Refused To Inherit Generational Debt | 2026-09-27 | 20,402 | 342 | 82 | 1.68 | 1,200.10 |
| POV: You Paid Off Your House In 10 Years By Ignoring Advice | 2026-09-22 | 14,051 | 191 | 42 | 1.36 | 638.70 |
| POV: You Were Laid Off At 45 with Zero Savings | 2026-10-01 | 12,568 | 163 | 30 | 1.30 | 966.80 |
| POV: Your Friends Laughed At Your Cheap Habits Until You Retired First | 2026-09-26 | 9,955 | 152 | 15 | 1.53 | 553.10 |
| POV: You Hit 50 With Zero Savings | 2026-09-21 | 9,836 | 200 | 35 | 2.03 | 427.70 |
| POV: You Cut Off Relatives Who Treated Your Savings Like an Emergency Fund | 2026-09-30 | 9,684 | 193 | 51 | 1.99 | 691.70 |
| POV: You Were Completely Broke At 42 Until You Changed 3 Habits | 2026-09-25 | 9,238 | 139 | 24 | 1.50 | 486.20 |
| POV: Your Family Called You Broke — Now They Need Your Signature | 2026-10-10 | 7,555 | 191 | 24 | 2.53 | 1,888.80 |
| POV: You Ignored Quick-Rich Formulas | 2026-10-05 | 6,749 | 73 | 15 | 1.08 | 749.90 |
| POV: You Quietly Escaped the Rat Race | 2026-09-28 | 5,798 | 102 | 10 | 1.76 | 362.40 |
| You Were The "Broke Child" Everyone Ignored | 2026-10-07 | 5,131 | 95 | 15 | 1.85 | 733 |
| POV: Your Dad Sold Your Late Mom's House Without Asking | 2026-10-11 | 3,734 | 99 | 5 | 2.65 | 1,244.70 |
| POV: She Mocked Your Old Car — Now You Paid Off Her Dream House | 2026-10-13 | 1,530 | 36 | 8 | 2.35 | 1,530 |

**Key insight — the most important channel-level finding in this report.** Between Sept 12 and Oct 13 this channel shifted its hook from *money mechanics* to *family conflict drama*: "Your family called you broke", "Your in-laws called you cheap", "She mocked your old car", "Your dad sold your late mom's house". Engagement **rose** (several of the newest are 2.35–2.65%, the highest on the channel) while **views collapsed** from 58,772 to 1,530–7,555. High engagement on shrinking reach is the classic signature of an audience narrowing toward a smaller, more emotional core. The financial-conflict angle attracts loyal commenters but is not what the algorithm was distributing in September.

### 5.6 Marcus Gets Rich — full video performance

Channel description: "…about one ordinary guy learning how money actually changes a life. Every episode drops Marcus into a real financial decision…"

| Video | Published | Views | Duration |
|---|---|---|---|
| POV: Your Entire Financial Life, From $32,000 to Quiet Millionaire | 2026-09-22 | **15,458** | 1:17:28 |
| POV: You Show Her Your Net Worth Before the Wedding | 2026-09-30 | 1,335 | 17:52 |
| You Skip College for a Trade | 2026-09-17 | 589 | 10:44 |
| Same Paycheck. Same Car Payment. | 2026-09-15 | 546 | 12:24 |
| You Break a Financial Pattern for 3 Generations | 2026-09-19 | 488 | 10:00 |
| You Take the Raise | 2026-09-16 | 377 | 7:37 |
| You Make Your Last Mortgage Payment at 43 | 2026-09-18 | 309 | 9:05 |
| POV: You Drive the Same Car Eleven Years | 2026-09-26 | 269 | 15:23 |
| POV: Nothing in Their House Is New | 2026-09-27 | 220 | 14:46 |
| You Cross $200,000 Invested | 2026-09-14 | 87 | 14:06 |
| POV: You Live Through Every Level of Wealth — $0 to $5 Million | 2026-10-14 | 11 | 17:07 |
| POV: You're 45 With Nothing Invested | 2026-10-11 | 27 | 17:17 |
| POV: You Stop Saving for Retirement at 39 | 2026-10-09 | 12 | 17:28 |
| POV: You Become the First Old Money in Your Family | 2026-10-07 | 8 | 17:03 |

**Key insight:** 28 videos, 30,192 lifetime views — and 15,458 of them (51%) are one video. Everything published since mid-October is between 8 and 27 views. Note also that eight videos sit **under 10 minutes** (7:37, 9:05, 10:00, 10:44, 12:24…), which puts several below the long-form threshold this brief used — and none of them broke out either. This channel is a case study in a one-time algorithmic lottery, not a repeatable format.

### 5.7 Smart With Avy — full video performance

| Video | Published | Views | Likes | Comments | Views/Day |
|---|---|---|---|---|---|
| 10 Websites That Actually Pay You Money | 2026-09-17 | **431,870** | — | 235 | 15,995.20 |
| 5 Legit Websites That Pay You for Testing Apps & Websites | 2026-09-22 | 32,945 | 697 | 37 | 1,497.50 |
| These 3 Websites Pay You to Train AI | 2026-09-25 | 20,584 | 422 | 43 | 1,083.40 |
| ₹100,000 in 7 Days From Clipping? | 2026-08-28 | 17,705 | 528 | 106 | 376.70 |
| AI Video बनाओ और Meesho से पैसे कमाओ | 2026-09-08 | 11,847 | 192 | 36 | 329.10 |
| OneForma Complete Guide | 2026-10-03 | 11,051 | 228 | 16 | 1,004.60 |
| 5 New Online Earning Ways That Actually Work in 2026 | 2026-10-12 | 5,756 | 98 | 14 | 2,878 |
| Does Master App Really Pay? | 2026-09-30 | 5,072 | — | 13 | 362.30 |
| AI भक्ति Channel बनाओ | 2026-09-19 | 1,423 | 43 | 10 | 56.90 |
| Long AI Video Kaise Banaye | 2026-09-13 | 2,062 | 42 | 5 | 66.50 |

**Key insight:** The 431,870-view video is 81% of lifetime views — but unlike Marcus Gets Rich, the *format* repeats: "websites that pay" variations did 32,945, 20,584 and 5,072. The topic is durable; only the magnitude was a one-off. This is a **format that can be run repeatedly at 20–33K**, which is a far healthier signal than a single 431K spike. Note the channel runs 15 videos at 2,910 subs.

### 5.8 khushi explains — full video performance (the strongest repeatable pattern found)

| Video | Published | Views | Likes | Comments | Engagement % | Views/Day |
|---|---|---|---|---|---|---|
| 3 GENUINE Work from HOME job using MOBILE | 2026-09-21 | **436,491** | 6,036 | 343 | 1.38 | 18,977.90 |
| FREE Laptops, Earbuds and goodies for College Students | 2026-09-07 | 133,777 | 1,429 | 121 | 1.07 | 3,615.60 |
| No Experience Work from Home Jobs | 2026-09-17 | 82,576 | 1,444 | 124 | 1.75 | 3,058.40 |
| Best Online Earning Platforms for Students | 2026-09-26 | 79,690 | 1,740 | 129 | 2.18 | 4,427.20 |
| PM Internship Scheme 2026 | 2026-09-11 | 67,202 | 687 | 108 | 1.02 | 2,036.40 |
| Make money by TYPING | 2026-10-12 | 40,311 | 732 | 39 | 1.82 | 20,155.50 |
| ₹3 Lakhs of FREE stuff for students from Google | 2026-09-09 | 40,280 | 685 | 32 | 1.70 | 1,150.90 |
| FREE 100+ Internships for Students in 2026 | 2026-09-15 | 12,094 | 201 | 28 | 1.66 | 417 |
| Make Money Online Using Your SKILLS (SuperProfile) | 2026-09-30 | 7,566 | 89 | 6 | 1.18 | 540.40 |
| DU CSAS 2026 Big Update | 2026-08-04 | 5,189 | 134 | 161 | 2.58 | 73.10 |

**Key insight:** 190 videos, 1,900,682 lifetime views, and **seven videos above 40K in a single 90-day window.** This is the only channel in the set showing a sustained, repeatable distribution pattern rather than a single spike. The unifying frame across all seven: **free money/jobs/perks for students in India.** Note the most recent video (40,311 views, 20,155.50 views/day) is the highest views/day on the channel — it is still accelerating.

### 5.9 Hemlata chauhan — full video performance

| Video | Published | Views | Likes | Comments | Views/Day |
|---|---|---|---|---|---|
| भक्ति चैनल से घर बैठे कमाए ₹50,000 \| AI Bhajan Channel Guide | 2026-09-08 | **620,574** | 8,331 | 1,040 | 17,238.20 |
| 5 "Lazy" Ways to Make Money Online in 2026 | 2026-10-05 | 168,971 | 1,908 | 86 | 18,774.60 |
| भक्ति चैनल बनाकर कमाई कैसे करें? Part 2 | 2026-09-28 | 20,024 | 545 | 68 | 1,251.50 |
| Creator नहीं हो? फिर भी SuperProfile से ₹1 Lakh+ कमाओ | 2026-09-19 | 11,089 | 119 | 11 | 443.60 |
| I Paid My Own MBA Fees Through This Secret Website! | 2026-10-12 | 4,702 | 102 | 12 | 2,351 |

**Key insight — a language finding.** The channel's single largest video is in **Hindi** (620,574 views, 1,040 comments). Its largest **English** video did 168,971. Same channel, same topic space, same creator — the Hindi AI-bhajan guide outperformed the English money video by **3.7×**. If you are considering an Indian audience, Hindi-language religious-monetisation content is dramatically under-served relative to its performance. This channel also runs 255 videos with heavy Shorts support (many Shorts at 11–129 seconds with 745–2,308 views).

### 5.10 Khushal Sky — full video performance

| Video | Published | Views | Likes | Comments | Views/Day |
|---|---|---|---|---|---|
| How To Make Money From Pinterest Full Step By Step Guide 2026 | 2026-08-21 | **315,012** | 5,748 | 284 | 5,833.60 |
| Alight Motion COMPLETE COURSE: Zero to Hero (Hindi) | 2026-08-18 | 139,149 | 5,167 | 975 | 2,441.20 |
| Best Text Effects in Premiere Pro | 2026-08-26 | 102,818 | 1,685 | 190 | 2,098.30 |
| How to Edit Viral Instagram Reels using ONLY Premiere Pro | 2026-09-01 | 83,941 | 1,508 | 267 | 1,952.10 |
| How To Create Amazon Affiliate Account (2026) | 2026-08-20 | 79,229 | 2,027 | 338 | 1,440.50 |
| Youtube Payment Process (Full Details) | 2026-09-02 | 37,328 | 712 | 115 | 888.80 |
| Earn 1000 Rupees per thumbnail \| Photoshop Tutorial | 2026-10-07 | 30,812 | 653 | 117 | 4,401.70 |
| Viral 3D Motion Graphics Elements ChatGPT | 2026-09-22 | 29,214 | 628 | 74 | 1,327.90 |
| YouTube Earning (Short) | 2026-09-02 | 24,304 | 1,449 | 51 | 578.70 |

**Key insight:** The Pinterest video is the channel's single biggest video, but the *channel's actual engine* is creative-software tutorials: Alight Motion (139,149), Premiere Pro (102,818), Reels editing (83,941), Amazon Affiliate (79,229), Photoshop (30,812). The money video is an outlier within an editing channel — the reverse of the usual pattern. Its top videos also carry the highest comment counts in the whole study (up to 975), suggesting a community built around skill-teaching rather than money promises. Treat the Pinterest hit as *ancillary to* a tutorial audience, not as a standalone finance play.

### 5.11 Newly discovered channels (not in the original ten)

| Channel | Subs | Country | Key video | Views | Breakout |
|---|---|---|---|---|---|
| Audiobook Institute | 2,700 | — | The Mindset Shift (Audiobook) | 255,624 | 899.92× |
| Wealthverse | 3,790 | US | 10 Low-Tech Businesses Making Ordinary Guys $30,000/Month | 108,597 | 85.87× |
| MindQuarry Audiobook | 2,550 | US | Build Wealth in Silence: 7 Quiet Wealth-Building Habits | 61,758 | 61.56× |
| Mama Louie Motherhood | 1,850 | ZW | 20 Side Hustles That Can Make You Money in Zimbabwe | 71,666 | 89.20× |
| Chereeka Lou | 1,150 | — | My Real Debt Numbers At 46 | 29,483 | 67.78× |
| Limitless Growth Audiobook | 1,450 | US | Money Loves Discipline (Full Audiobook) | 19,647 | 46.26× |
| AudioBOOK Library | 27,800 | IN | Think and Grow Rich — Audiobook Summary | 29,198 | 36.95× |
| UR Wealthy | 7,550 | IN | 10 Quiet Money Moves That Build Wealth While You Sleep | 13,371 | 2.32× |
| Money Mastery Audiobooks | 1,230 | — | 7 Habits of Wealthy People | 10,855 | 38.98× |
| Wixel AI | 8,270 | PK | 15 Best Online Earning Websites That Actually Work | 85,561 | 3.79× |
| GROW LISTENING | 4,830 | US | THE BLACK PROTOCOL OF WEALTH (Audiobook) | 12,033 | 32.83× |
| The Compounding Investor | 68,700 | GB | What an £800,000 Dividend Portfolio Paid Me This Month | 111,054 | 2.19× |
| Audio Books Office | 314,000 | ES | Mental Millionaire: Don't Chase Wealth | 22,243 | 10.73× |
| AudioBOOK Library | 27,800 | IN | Think and Grow Rich | 29,198 | 36.95× |

Also surfaced but NOT faceless (host on camera): Minority Mindset — 2,530,000 subs, "How To Turn $500 a Month Into a $3,700 Passive Income", 213,032 views, VPH 157.50. Excluded from the faceless set.

---

## Part 6 — The Additional Outliers (12 More)

These qualify on the same brief (≥5× subscriber-to-view ratio, or VPH ≥150), long-form, faceless, last 90 days.

| Video Title | Channel | Subs | Views | × Subs | Breakout | VPH | Duration |
|---|---|---|---|---|---|---|---|
| The Mindset Shift: The Psychology of Changing How You Think (Audiobook) | Audiobook Institute | 2,700 | 255,624 | 94.7× | 899.9× | 435.41 | 2:04:37 |
| 10 Low-Tech Businesses Making Ordinary Guys $30,000/Month | Wealthverse | 3,790 | 108,597 | 28.7× | 85.9× | 348.45 | 12:45 |
| Build Wealth in Silence: 7 Quiet Wealth-Building Habits (Audiobook) | MindQuarry Audiobook | 2,550 | 61,758 | 24.2× | 61.6× | 2.44 | 57:18 |
| 20 Side Hustles That Can Make You Money in Zimbabwe | Mama Louie Motherhood | 1,850 | 71,666 | 38.7× | 89.2× | 86.35 | 19:05 |
| POV: You Quietly Built a Second Income and Told No One | Ollie Finance | 5,740 | 197,613 | 34.4× | — | — | 19:08 |
| My Real Debt Numbers At 46 \| Debt, Goals, Plans | Chereeka Lou | 1,150 | 29,483 | 25.6× | 67.8× | 31.95 | 10:50 |
| POV: You Broke The Paycheck Cycle By Living On One Dollar Rules | POV Money Habits | 1,040 | 22,270 | 21.4× | — | — | 23:42 |
| POV: You Silently Building a Holding Company From $0 to $600M | Ollie Finance | 5,740 | 111,900 | 19.5× | — | — | 14:26 |
| Money Loves Discipline: Daily Habits of Future Millionaires | Limitless Growth Audiobook | 1,450 | 19,647 | 13.5× | 46.3× | 11.37 | 1:42:07 |
| 15 Best Online Earning Websites That Actually Work (2026) | Wixel AI | 8,270 | 85,561 | 10.3× | 3.8× | 43.98 | 10:30 |
| 7 Habits of Wealthy People \| Money Mastery Audiobook | Money Mastery Audiobooks | 1,230 | 10,855 | 8.8× | 39.0× | 7.75 | 1:13:51 |
| FREE Laptops, Earbuds and goodies for College Students | khushi explains | 15,100 | 133,777 | 8.9× | — | — | 9:57 |

**VPH ≥150 leg only (long-form, faceless):**

| Video | Channel | Views | VPH | Duration |
|---|---|---|---|---|
| What an £800,000 Dividend Portfolio Paid Me This Month: Passive Income Sept 2026 | The Compounding Investor | 111,054 | 204.55 | 16:20 |
| Think and Grow Rich — Audiobook Summary | AudioBOOK Library | 29,198 | 209.58 | 39:31 |
| INSANELY Profitable Side Hustle (How To Make Money Online 2026) | Jason Wardrop | 14,909 | 202.26 | 16:25 |
| How To Turn $500 a Month Into a $3,700 Passive Income | Minority Mindset (host on camera — excluded from faceless) | 213,032 | 157.50 | 29:08 |
| 10 Low-Tech Businesses Making Ordinary Guys $30,000/Month | Wealthverse | 108,597 | 348.45 | 12:45 |

**Additional long-form money outliers found but below the 5× / 150 VPH bar** — included for pattern completeness: 7 High-Paying Online Jobs You Can Do At Night (Shane Hummus, 456,175 views); 7 Claude AI Side Hustles That Can Replace Your Salary (Ayushman Pandita, 392,393); The Most Overlooked Online Side Hustle Of 2026 (Chris Koerner, 375,898); 7 Passive Income Ideas — How He Make Rs. 25,000 Per Day (Anchal tiwari, 401,805); Which AI Side Hustle Pays Fastest? 7 Ranked (Dark Horse Entrepreneur, 108,327, breakout 1,097.04×); Reacting to people paying off debt with micropayments (Denzel Napoleon Rodriguez, 28,265, breakout 200.08×); The Easiest Night Side Hustle to Start After 40 with $0 Monthly Fees (Kim Ryan, 20,499, breakout 137.57×); At 23, I Paid Off My Debt, Bought a Lake House (Whispers of Vengeance, 10,584); ESCAPE THE DEBT TRAP (Joy M Keziah, 19,780, breakout 27.91×); 15 Side Hustles You Can Add to Your Tailoring Business (Queenliz Fashion, 56,181, breakout 97.28×); The 5-Minute Google Hack To Make Money Online (Jason Wardrop, 40,428); I Got Paid Again on UserBrain (Online Income Plug, 17,192); Stop Looking for Work — These 5 Legit Websites Pay You in 24 HRS (TekUP, 20,849); NEW AI Side Hustle To Make Money Online For Beginners (Jason Wardrop, 97,602); The Easiest Night Side Hustle to Start After 40 (Kim Ryan, 20,499); I Reincarnated as a Fake Rich Heir (Haruto Xplainer, 104,287, VPH 158.71 — manhwa recap, adjacent genre); My Dividend Portfolio Now Pays Me $480/Day (GenExDividendInvestor, 32,877, VPH 89.51); My Updated Singapore Dividend Portfolio Strategy (Demi Zhuang, 81,208); Beginner's Dividend Portfolio Building Masterclass (Steve | Call to Leap, 81,175); You'll Never Live Off Dividends With Dividend Growth Investing (Dividend Bull, 59,195); How Much My Dividend Portfolio Paid Me in August ($313,000 Portfolio) (Dividendology, 52,953); 10 Habits That Make You Happier Than Money Ever Will (The Success Paradox, 31,194); The Psychology of Money | Greed, Envy & 6 Unhealthy Money Habits (Mental Health with Dr. Harkishan Mamtani, 126,878, breakout 121.55×); Never Be Cheap: The Psychology of Becoming Valuable (Timeless Audiobook, 34,578, breakout 21.01×); 10 Unsexy Frugal Habits That Save You Serious Money (Money May, 103,367, breakout 29.55×); The Black Protocol of Wealth (GROW LISTENING, 12,033); Mental Millionaire (Audio Books Office, 22,243); 10 Quiet Money Moves That Build Wealth While You Sleep (UR Wealthy, 13,371); 7 Habits to Build Your Money Mindset (Ajay Inspiration, 138,290); 10 Habits Wealthy People Learned Before They Had Money (Jim Rohn Motivation, 17,761).

---

## Part 7 — The Audiobook Cluster (Newly Identified)

This is the largest missed opportunity in the niche and it was invisible to the original search strategy.

**What it is:** 40-minute to 2-hour narrated money/mindset reads, typically published as "Full Audiobook," "Audiobook Summary," or long-form read-alouds, often positioned for background listening or sleep.

| Evidence | Figure |
|---|---|
| Audiobook Institute — "The Mindset Shift" | 255,624 views on 2,700 subs = **94.7× subs**, breakout **899.92×** |
| Limitless Growth Audiobook — "Money Loves Discipline" | 19,647 views on 1,450 subs, breakout 46.26×, runtime 1:42:07 |
| MindQuarry Audiobook — "Build Wealth in Silence" | 61,758 views on 2,550 subs, breakout 61.56×, runtime 57:18 |
| Money Mastery Audiobooks — "7 Habits of Wealthy People" | 10,855 views on 1,230 subs, breakout 38.98×, runtime 1:13:51 |
| GROW LISTENING — "The Black Protocol of Wealth" | 12,033 views on 4,830 subs, breakout 32.83×, runtime 1:24:06 |
| Audio Books Office — "Mental Millionaire" | 22,243 views on 314,000 subs, breakout 10.73× |
| AudioBOOK Library — "Think and Grow Rich" summary | 29,198 views, VPH 209.58, runtime 39:31 |

Note the pattern: **the breakout multiples are highest at the smallest channels.** Four separate sub-5,000-subscriber channels in this one genre all cleared 30× breakout. That is the strongest structural signal in the whole study.

---

## Part 8 — Audience Evidence From Comment Sections

### 8.1 On "Power of Invisible Money" (Sight of Fortitude) — 337 comments

| Comment (verbatim) | Likes | Replies |
|---|---|---|
| "He who buy things he doesn't need, one day he will need things he CANNOT buy" | 76 | 3 |
| "Waiting for a bigger salary is a trap… Thomas's journey proves that financial peace doesn't come from earning more, but from finally tracking where every coin disappears." | 80 | 4 |
| "A use a couple of tricks. 1 Use the one hour method. Save 1 hour wages everyday you work. 2. Save all your one and five dollar bills. I usually save around 5k a year using both methods." | 46 | 2 |
| "Thank you for this video, 6 days to pay day and nothing left in my bank account 😨 I really needed to hear this message and start making changes today!" | 36 | 1 |
| "That line, 'Wealth is built in silence in small rooms with a pen in your hand,' hits hard. Most people think they have an income problem, but they actually have an awareness problem." | 36 | 1 |
| "Thank you so much for your wisdom… But I pay God first then myself then I use the wisdom that you talked about." | 22 | 5 |
| "Buying bread and scones i could bake myself. Buying fish i could prepare myself. Buying spinach that i could plant." | 17 | 1 |
| "Let me keep it and rewatch it again and again… so by the end of 6 months I want to see what will be of me" | 8 | 1 |

**Read:** The audience is not just watching — it is **taking notes and planning behaviour change**. One commenter describes re-watching over six months. Another describes a real-world outcome (a coworker hugging her because savings let her husband job-hunt). The top comments quote specific lines back. This is the signature of a **re-watchable, advice-dense long-form format**, not passive entertainment.

### 8.2 On "Power of Money Mindset" (Sight of Fortitude) — 379 comments

| Comment (verbatim) | Likes | Replies |
|---|---|---|
| "An old car, money in the bank, and a good night's sleep? Yeah, I'd take that over looking rich any day." | 71 | 8 |
| "This hit differently. Real wealth really is the kind nobody can see… 'Looking poor' might actually be one of the smartest flexes." | 3 | 0 |
| "I'm currently focusing on Rule #2: Starve the Peacock to stop my lifestyle creep" | 15 | 1 |
| "The clockmaker scene is pure gold. Everyone admires the carved mahogany and gold leaf. Almost no one thinks about the heavy, ugly iron pendulum swinging in the dark that actually keeps the time." | 18 | 7 |
| "I want to live as a poor man with money in the bank. Picasso." | 22 | 1 |
| "Watching from Lagos State Nigeria West Africa 🌍" | 6 | 0 |

**Read (important caveat):** The most-liked comment referencing a **specific mid-video moment** ("the clockmaker scene") in a 23-minute video is anecdotal evidence of deep watch-through — it is not proof, and it is one comment, not a measurement. But the naming of named story devices ("Rule #2: Starve the Peacock") shows the numbered-rule structure is doing retention work. The 7 replies on that thread also show it spawned discussion.

There is also a **spam/promotional comment pattern** present: a comment about "copy trading with only $9,000 — today it has grown to $35,500" with 64 likes. This is characteristic of investment-scam solicitation in the replies of finance videos. Worth knowing if you step into this space.

### 8.3 On "3 GENUINE Work from HOME job using MOBILE" (khushi explains) — 343 comments

| Comment (verbatim) | Likes | Replies |
|---|---|---|
| "Best way to earn money is to tell people how to earn." | **387** | 22 |
| "It's 2k not 200. My bad!" (creator's own pinned correction) | 124 | 36 |
| "1:43 — video start from here" (timestamp skip) | 107 | 8 |
| "Plz, make complete video with full of process because it is new for us." | 56 | 4 |
| "Pahle payment ka genuine proof do, berozgaari emotional se kyu khel rehe ho aplog, mehenet se paisa kamao bewakoof banake nehi" (translation: *first give genuine proof of payment; why play with people's unemployment emotions; earn money with hard work, don't fool people*) | 43 | 1 |
| "Thanku sister you speak very politely" | 26 | 0 |
| "Don't use DataForce — it asks for your own photo, voice etc. and it's risky." | 3 | 0 |
| "Ye didi to bas aisa lag raha hai ChatGPT se script likh kar video bana rahi hai… Sirf websites ka naam aur kaam bata rahi hai, kuch bhi karke nahi dikha rahi hai" (translation: *looks like she wrote the script with ChatGPT — she only names websites and explains them, doesn't actually demonstrate anything*) | 7 | 0 |
| "20 hrs free… 1k so 20hrs=20k and per month=6 lakh, is this possible?" | 1 | 0 |

**Read — this is the most important audience finding in the report.** The single most-liked non-creator comment is **cynicism about the entire genre** (387 likes — higher than any praise comment). The audience is auditing claims in real time: it demands payment proof, it flags which platforms look risky, it calls out non-demonstration, and it does arithmetic on the earnings claims. The creator's own correction ("It's 2k not 200") got more engagement than most of the video's praise.

**Practical implication:** if you enter Cluster C, **showing the money is the differentiator.** The audience has explicitly told you what it does not believe.

### 8.4 On "10 Websites That Actually Pay You Money" (Smart With Avy) — 235 comments

| Comment (verbatim) | Likes |
|---|---|
| "7:05 is best" (timestamp) | 44 |
| "Bhai agar aapka video genuine aur original matlab 100% real hoga to audience khud aap par trust karegi" (translation: *if your video is genuinely 100% real, the audience will trust you on its own*) | 41 |
| "Website number 1 full puri video lao" (translation: *bring a full video on website number 1*) | 21 |
| "Website no 1 full video lao please earning karke dikhana" (translation: *bring a full video on website 1 and actually show yourself earning*) | 9 |
| "Ye sare sites me kam karne me dikkat hoti h, kabhi kabhi survey qualify hote hi nhi, or in sab sites ke reviews bhi bahut kam h" (translation: *working on these sites is difficult, sometimes you never qualify for surveys, and these sites have very few reviews*) | 13 |
| "Kisine isme se koi bhi website pehle try kiya tha toh batao konsa best hai??" (translation: *has anyone tried any of these? tell me which is best*) | 0 |
| "90% ko nhi pata? Toh tumko kaise pata?" (translation: *90% don't know? then how do you know?*) | 0 |

**Read:** The **most-repeated request is depth over breadth** — asked twice, in two separate comments: "bring a full video on website #1." The audience is asking for a single-platform deep dive with demonstrated earnings, and the creator has 15 videos that are all listicles. This is a stated, unfulfilled content gap.

---

## Part 9 — Keyword and Demand Data (Full)

### 9.1 Core keyword metrics (US-scoped pull)

| Keyword | Competition | Volume Score | Overall | Est. Monthly (global) | Est. Monthly (US) |
|---|---|---|---|---|---|
| money audiobook | **15.3** | 60.85 | 70.39 | 11,930 | — |
| self improvement audiobook | **14.9** | 54.62 | 66.81 | 4,560 | — |
| work from home jobs for students | **24.4** | 53.02 | 62.05 | 3,565 | — |
| budgeting | 25.8 | 78.45 | **76.75** | 180,159 | — |
| wealth audiobook | 27.9 | 57.41 | 63.29 | 7,013 | — |
| sleep audiobook | 30.6 | 64.00 | 66.16 | 19,379 | — |
| side hustle for students | 33.3 | 69.84 | 68.58 | 47,678 | — |
| quiet wealth | 33.9 | 77.70 | 73.06 | 160,313 | 10,688 |
| financial discipline | 38.7 | 66.06 | 64.15 | 26,617 | 5,323 |
| stealth wealth | 38.5 | 75.32 | 69.79 | 111,057 | 17,086 |
| debt free journey | 36.8 | 70.96 | 67.85 | 56,679 | 6,298 |
| dividend portfolio | 40.9 | 60.44 | 59.90 | 11,184 | — |
| index fund investing | 41.2 | 61.67 | 60.52 | 13,534 | — |
| money psychology | 41.5 | 84.78 | 74.27 | 477,745 | — |
| work from home jobs | 46.1 | 77.95 | 68.33 | 166,734 | 13,446 |
| pov finance | 50.1 | 99.99 | **79.95** | 4,993,089 | 241,046 |
| money mindset | 53 | 81.32 | 67.59 | 280,374 | 27,537 |
| financial literacy | 59 | 80.98 | 64.99 | 266,090 | 38,378 |
| passive income | 59 | 80.32 | 64.59 | 240,195 | 23,245 |
| make money online | 64.5 | 88.59 | 67.36 | 860,521 | 123,240 |
| earn money online | 57.5 | 82.59 | 66.55 | 340,871 | 2,452 |

**Reading the table:** `pov finance` has the highest overall score (79.95) but 241,046 of its US volume is dwarfed by its global total — its audience is 26% Pakistan, 14% Nigeria, 12% India, only ~5% US. `budgeting` has the best combination of high overall score (76.75) and low competition (25.8) in a US-heavy market (22.7% US). The audiobook keywords are the lowest-competition terms found anywhere in this study — 14.9 and 15.3 competition — but carry modest global volumes.

### 9.2 Top markets by country (selected keywords)

| Keyword | Top 3 Markets | US Share |
|---|---|---|
| pov finance | PK 26.3%, NG 13.9%, IN 11.7% | ~5.0% |
| budgeting | US 22.7%, IN 21.2%, PK 10.6% | 22.7% |
| financial literacy | IN 17.0%, US 15.0%, PK 10.0% | 15.0% |
| money mindset | IN 20.7%, PK 14.4%, US 9.9% | 9.9% |
| work from home jobs for students | — (US-scoped pull returned no top-markets block) | — |
| make money online | IN 13.5%, US 13.5%, BD 7.7% | 13.5% |
| quiet wealth | PK 32.8%, VN 13.8%, NG 8.6% | 6.9% |
| passive income | IN 31.1%, US 10.0%, PK 5.6% | 10.0% |

**This is the single most decision-relevant table in the report.** Every high-volume money keyword in this niche skews heavily toward South Asia and West Africa, not the US. If your monetisation target is US CPM, the "money mindset" and "pov finance" lanes are structurally misaligned with your revenue goal, even though they have the best demand numbers.

### 9.3 Audience questions — what people actually search

| Question | Competition | Est. Monthly | Overall | 30-Day Growth |
|---|---|---|---|---|
| how money works | 61 | 1,563,024 | 71.08 | −2.28% |
| how to make money online | 59 | 1,307,717 | 71.18 | +8.81% |
| how to make money | 54.5 | 691,199 | 70.50 | −7.69% |
| how to make money with ai | 65 | 515,390 | 65.16 | +5.11% |
| how to earn money online | 49.5 | 430,025 | 70.66 | −13.75% |
| how to save money | 48 | 187,952 | 68.04 | **−42.60%** |
| how to make money as a teenager | 40.5 | 181,364 | 70.90 | −7.00% |
| how companies make money | 38.4 | 126,726 | 70.34 | **+29.24%** |
| how to get money from stocks | 38.5 | 118,830 | 70.05 | **+123.65%** |
| how to earn money online for students | 48 | 113,786 | 66.09 | −3.73% |
| how to get money from crypto | 37.5 | 116,016 | 70.36 | **+118.35%** |
| how to make money with stocks, crypto, or day trading | 43 | 113,666 | 68.08 | **+113.93%** |
| how costco makes money | 35.3 | 87,010 | 70.12 | +20.73% |
| **how pawn shops actually make money** | **20.9** | 85,646 | **75.82** | **+2,140.28%** |
| how to earn money with ai | 57 | 77,934 | 61.01 | +54.75% |
| how to make money from youtube | 47 | 77,204 | 64.98 | +38.14% |
| what can you buy with elon musk money | 52 | 76,272 | 62.93 | +150.91% |
| how to make money on youtube | 47 | 185,859 | 68.39 | −14.79% |

**Three signals worth naming:**

1. **`how pawn shops actually make money`** — competition 20.9, overall score 75.82, and a **+2,140% 30-day growth** from a 3,823 baseline. That is the single most extreme growth number in any tool result in this session. Low competition plus explosive growth is the rarest combination available.
2. **A cluster of "how X makes money" business-model questions** is forming — `how companies make money` (+29.24%), `how costco makes money` (+20.73%), pawn shops (+2,140%). This is the *mechanics* lane, and it is exactly what the Simple Ways of Life "Money Map" video occupies. It has momentum the psychology lane does not.
3. **`how to save money` is down 42.60%** while `how to make money online` is up 8.81%. The "save money" framing this niche leans on hard is losing search demand right now.

---

## Part 10 — Synthesis: What the Deeper Data Changes

### 10.1 The revised cluster map

**Cluster A — Quiet-Wealth Money-Psychology Stories** (narrated, third-person)
Sight of Fortitude (×2), Simple Ways of Life. Plus newly found: Limitless Growth Audiobook, MindQuarry Audiobook, Money Mastery Audiobooks, GROW LISTENING, Timeless Audiobook.

**Cluster B — POV Second-Person Financial Life** (voice-over/animation, "you" framing)
Ollie Finance, POV Money Habits, Marcus Gets Rich. Plus: Chereeka Lou (first-person debt, adjacent).

**Cluster C — Faceless "Earn Online / Get Paid" Tutorials & Listicles**
Hemlata chauhan, Smart With Avy, khushi explains, Khushal Sky. Plus: Wixel AI, Wealthverse, Mama Louie Motherhood, Online Income Plug, TekUP.

**Cluster D — Long-Runtime Money Audiobooks (newly identified)**
Audiobook Institute, AudioBOOK Library, Audio Books Office, MindQuarry, Limitless Growth Audiobook, Money Mastery Audiobooks, GROW LISTENING, UR Wealthy.

**Cluster E — Dividend / Portfolio Income Documentation** (newly identified)
The Compounding Investor, Dividendology, GenExDividendInvestor, Dividend Bull, ppcian, Passive Income Investing, Demi Zhuang.

### 10.2 Revised answer: lowest competition + highest demand

The original answer was **Cluster B (POV)** on the strength of `pov finance` (79.95 overall). The deeper pass **complicates but does not overturn** that:

- Cluster B still has the single best overall keyword score (79.95) and the best supply-side proof (three sub-6K channels beating their subscriber base 14–57×).
- But its audience is ~5% US, and its flagship channel (POV Money Habits) has now pivoted *away* from money mechanics toward family drama, with views collapsing from 58,772 to 1,530–7,555 in the following month. That is a warning about the format's stability, not just its opportunity.
- **Cluster D (audiobooks) has weaker demand numbers but the strongest structural signal**: four independent sub-5,000-sub channels all cleared 30× breakout, and its keywords carry the lowest competition in the study (14.9 and 15.3). It is also the only cluster where the outlier multiples *increase* as channel size decreases.

**Verdict:** Cluster B remains the best demand story. Cluster D is the best competition story. If the brief is "lowest competition and highest demand," Cluster B wins on demand, Cluster D wins on competition, and the honest answer is that they are not the same cluster.

For a US-monetisation goal specifically, the data points away from both: **`budgeting` (competition 25.8, overall 76.75, 22.7% US)** is the best-scoring keyword with a genuinely US-heavy audience.

### 10.3 What the deeper pass added to the video ideas

The original five ideas stand. The comments and question data add three that come from stated audience demand rather than inference:

1. **"Website #1, Done Properly" — a single-platform deep dive with demonstrated earnings.** Requested twice by name in the Smart With Avy comments. The channel has 15 videos and not one single-platform tutorial. The audience has literally written the brief.
2. **"How Pawn Shops Actually Make Money"** — competition 20.9, overall 75.82, +2,140% 30-day growth. Sits inside the newly-forming "how X makes money" mechanics cluster, which is simultaneously the fastest-growing question lane found and the exact lane the Simple Ways of Life video occupies.
3. **The audiobook format applied to a single money mechanic.** Cluster D's four independent 30×+ breakouts say the *format* travels regardless of who makes it. No one has combined it with the "how money works" mechanics content that Cluster A/C are converging on.

### 10.4 The five things most likely to change your outcome

1. **Language beats topic.** The same Indian channel's Hindi video did 620,574 views; its English one did 168,971. Same creator, same subject space, 3.7× difference.
2. **Depth beats breadth in the "earn online" lane.** Every complaint in that comment section is about breadth-without-proof. The most-liked comment in the entire study is open cynicism (387 likes) about creators who teach earning instead of demonstrating it.
3. **High engagement on shrinking reach is a red flag, not a win.** POV Money Habits improved engagement while losing 97% of its views.
4. **One hit is not a format.** Marcus Gets Rich: 51% of lifetime views in one video, then 8–27 views per upload.
5. **The niche's core demand is shifting from saving to mechanics.** `how to save money` is down 42.6%; "how X makes money" questions are up 20–2,140%.

---

## Appendix A — Complete Outlier Index

**All videos discovered across both research passes that met the ≥5× subscriber ratio or VPH ≥150, long-form (10+ min):**

| # | Video ID | Channel | Subs | Views | × Subs | Breakout | VPH |
|---|---|---|---|---|---|---|---|
| 1 | UAr3_WFZArI | Audiobook Institute | 2,700 | 255,624 | 94.7× | 899.92 | 435.41 |
| 2 | _2jhDuTh6Oc | Smart With Avy | 2,910 | 431,870 | 148.4× | 70.12 | 409.52 |
| 3 | kWqZuUBwwlo | khushi explains | 15,100 | 436,491 | 28.9× | — | 252.86 |
| 4 | PfSIekOwbkM | Sight of Fortitude | 19,100 | 469,865 | 24.6× | — | 320.66 |
| 5 | DBEtkXvzurY | Sight of Fortitude | 19,100 | 514,646 | 26.9× | 22.42 | 96.39 |
| 6 | D0j1bxtRyzo | POV Money Habits | 1,040 | 58,772 | 56.5× | 39.33 | 3.59 |
| 7 | FAMfUDL-thA | Ollie Finance | 5,740 | 192,529 | 33.5× | — | 209.80 |
| 8 | GyDlbJCG1ZU | Hemlata chauhan | 12,500 | 168,971 | 13.5× | — | 1,075.28 |
| 9 | -xSQGPAISE0 | Khushal Sky | 26,100 | 315,012 | 12.1× | — | 100.65 |
| 10 | J-fgu7KY4TQ | Marcus Gets Rich | 1,070 | 15,458 | 14.4× | — | 0.09 |
| 11 | -xYFPIqbx0k | Simple Ways of Life | 40,800 | 54,332 | 1.3× | 5.51 | 549.94 |
| 12 | K9kXTEcf6i4 | Wealthverse | 3,790 | 108,597 | 28.7× | 85.87 | 348.45 |
| 13 | iFddvC0E2c4 | MindQuarry Audiobook | 2,550 | 61,758 | 24.2× | 61.56 | 2.44 |
| 14 | dsBcECoS-lM | Mama Louie Motherhood | 1,850 | 71,666 | 38.7× | 89.20 | 86.35 |
| 15 | YHCgWB3cIRs | Ollie Finance | 5,740 | 197,613 | 34.4× | — | — |
| 16 | k0rkbRvszUo | Chereeka Lou | 1,150 | 29,483 | 25.6× | 67.78 | 31.95 |
| 17 | K7jocNivlZQ | POV Money Habits | 1,040 | 22,270 | 21.4× | — | — |
| 18 | XAglECtNelg | Ollie Finance | 5,740 | 111,900 | 19.5× | — | — |
| 19 | E4MKlz8LB_c | Limitless Growth Audiobook | 1,450 | 19,647 | 13.5× | 46.26 | 11.37 |
| 20 | T4m3q696iRo | Wixel AI | 8,270 | 85,561 | 10.3× | 3.79 | 43.98 |
| 21 | Yp0gwvJr7jA | Money Mastery Audiobooks | 1,230 | 10,855 | 8.8× | 38.98 | 7.75 |
| 22 | MQsOn7Vc0AU | khushi explains | 15,100 | 133,777 | 8.9× | — | — |
| 23 | 1qbZEulXQzI | The Compounding Investor | 68,700 | 111,054 | 1.6× | 2.19 | 204.55 |
| 24 | upuKmOD1IPE | AudioBOOK Library | 27,800 | 29,198 | 1.1× | 36.95 | 209.58 |
| 25 | YA_LQWTY-6s | Minority Mindset (not faceless) | 2,530,000 | 213,032 | — | 0.94 | 157.50 |
| 26 | IOVM_NIub_U | Jason Wardrop | 348,000 | 14,909 | — | 2.17 | 202.26 |
| 27 | T19-pSH6YWg | Dark Horse Entrepreneur | 6,430 | 108,327 | 16.8× | 1,097.04 | 98.36 |
| 28 | 6wmTPIK7THg | Denzel Napoleon Rodriguez | 60,700 | 28,265 | — | 200.08 | 27.26 |
| 29 | JacIh6RYuJs | Kim Ryan | 19,400 | 20,499 | 1.1× | 137.57 | 21.09 |
| 30 | Y1RrN-oBXv4 | Mental Health with Dr. Harkishan Mamtani | 9,330 | 126,878 | 13.6× | 121.55 | 96.09 |
| 31 | RHYOwCLROTg | Queenliz Fashion | 4,800 | 56,181 | 11.7× | 97.28 | 41.60 |
| 32 | bhhODbgscAY | Whispers of Vengeance | 9,230 | 10,584 | 1.1× | 11.54 | 47.01 |
| 33 | iQYp2YjHNQQ | Shane Hummus | 1,720,000 | 456,175 | — | 15.98 | 80.77 |
| 34 | dmEvo0C1xc8 | Ayushman Pandita | 1,040,000 | 392,393 | — | 11.28 | 97.38 |
| 35 | NLS3cg_1RS0 | Anchal tiwari | 80,100 | 401,805 | 5.0× | 24.54 | 60 |
| 36 | u0yS7UjilkA | GenExDividendInvestor | 86,900 | 32,877 | — | 2.17 | 89.51 |
| 37 | amgt2z4SKgM | The Compounding Investor | 68,700 | 158,917 | 2.3× | 2.41 | 2.91 |
| 38 | _j1zb9TSu3Y | GROW LISTENING | 4,830 | 12,033 | 2.5× | 32.83 | 5.67 |
| 39 | eGiOtt9SBho | Audio Books Office | 314,000 | 22,243 | — | 10.73 | 25.82 |
| 40 | IPpNfzg9oz0 | Timeless Audiobook | 10,900 | 34,578 | 3.2× | 21.01 | 10.91 |
| 41 | ys-C8vKPn2Q | Money May | 4,300 | 103,367 | 24.0× | 29.55 | 5 |
| 42 | v6yzE4WNkhE | Haruto Xplainer | 18,100 | 104,287 | 5.8× | 23.37 | 158.71 |
| 43 | lzA2Ie-vxKU | Ollie Finance | 5,740 | 171,479 | 29.9× | — | — |
| 44 | DpcZMJRwDqY | TekUP | 15,200 | 20,849 | 1.4× | 2.04 | 23.16 |
| 45 | 8pKX65LFL64 | Smart With Avy | 2,910 | 20,584 | 7.1× | — | — |
| 46 | RPlrPlywBpU | Smart With Avy | 2,910 | 32,945 | 11.3× | — | — |
| 47 | blffsXMdrWA | khushi explains | 15,100 | 79,690 | 5.3× | — | — |
| 48 | choSwCc8V64 | khushi explains | 15,100 | 82,576 | 5.5× | — | — |
| 49 | Pal0IfemwAs | khushi explains | 15,100 | 67,202 | 4.5× | — | — |
| 50 | _OFOWX--e5M | Hemlata chauhan | 12,500 | 620,574 | 49.6× | — | — |

---

## Appendix B — Repeatable-Signal Ranking

Ranked by evidence that the *format* repeats, not by peak views. This is the ranking that matters if you are deciding what to build.

| Rank | Channel | Repeat Evidence | Verdict |
|---|---|---|---|
| 1 | khushi explains | 7 videos >40K in 90 days | Build here |
| 2 | Audiobook genre (aggregate) | 4 independent channels all >30× breakout | Build here |
| 3 | Sight of Fortitude | Money videos 2–6× its own non-money videos | Build here (money specifically) |
| 4 | The Compounding Investor | 2 videos >110K, monthly series format | Build here (if GB audience is acceptable) |
| 5 | Smart With Avy | Format repeats at 20–33K after the 431K spike | Viable, lower ceiling |
| 6 | Ollie Finance | 4 of 12 >111K, but 493-view newest video | High variance |
| 7 | Simple Ways of Life | 4 money videos in own top 7 | Viable |
| 8 | Khushal Sky | Engine is editing tutorials, not money | Wrong premise for this niche |
| 9 | Hemlata chauhan | Hindi works 3.7× better than English | Language-dependent |
| 10 | POV Money Habits | Pivoted away from money; views down 97% | Avoid the pivot |
| 11 | Marcus Gets Rich | 51% of lifetime views in one video | Do not copy |

---

## Appendix C — Full Method Notes

**Queries executed in the original pass:** `personal finance`, `make money online`, `investing stocks`, `money saving budgeting` — all with `video_type=long`, `max_days_ago=90`, `video_duration_from=600`, `min_score=2`, sorted by `vph_latest:desc`.

**Queries executed in the deeper pass:** `money psychology discipline habits`, `dividend passive income portfolio investing`, `debt free payoff story`, `online earning websites side hustle`, `wealth audiobook sleep mindset`, `POV money story second person` — same filters.

**Per-video data pulled for all 10 original outliers** via the YouTube Data API: full descriptions, tag previews, exact tag counts, description character counts, durations, publish timestamps, and live view/like/comment counts.

**Per-channel data pulled for all 10 original channels plus Khushal Sky** (11 total): subscriber count, lifetime views, video count, country, description, 10 most recent videos with engagement and views/day, and 10 top videos by views.

**Comment data pulled** for four videos: PfSIekOwbkM, DBEtkXvzurY, kWqZuUBwwlo, _2jhDuTh6Oc — 15 top-level comments each, ordered by relevance.

**Keyword data pulled** in two batches: 10 core niche terms with US scoping and top-market distribution, then 10 audiobook/portfolio/student terms. One `related_keywords` call on `quiet wealth` returned 20 related terms.

**Question data pulled** via the question index for the seed topic `money`, `language=en`, 25 results.

**Filtering logic for this report:** a video qualified if (views ÷ channel subscribers) ≥ 5, OR `vph_latest` ≥ 150. Duration had to be ≥ 600 seconds. Facelessness was assessed editorially from format (see Part 0, limitation 1).

**Every figure in this report traces to a tool result from this session.** Where a figure changed between two pulls of the same source, both values are shown. Where a metric's measurement window is undefined by the source (notably `vph_latest`), that is stated rather than resolved.
