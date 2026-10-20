# 🔍 SOP 01: Research & Outlier Validation (Quiet Money POV)

> **Purpose:** Mathematically validate POV wealth psychology topics, packaging formulas, and competitor intelligence before writing a single word of script.

---

## 1. Topic Selection Criteria (The Composite Velocity Index)

Every potential video topic must be scored against three strict criteria using the Composite Velocity Index (CVI):

$$\text{Composite Score} = (0.40 \times \text{Low Competition}) + (0.35 \times \text{Small-Channel Proof}) + (0.25 \times \text{Recent Velocity})$$

1. **Low Competition ($\le 35/100$ on vidIQ):** Ensures a zero-subscriber channel can penetrate suggested video feeds and high-CPM search rankings.
2. **Small-Channel Outlier Proof:** Verified proof that a small channel (<10K–50K subscribers) produced 100K–500K+ views on this exact POV topic angle (e.g., *Quiet Money Stories* generating a 201,553-view video at only 1,300 subscribers — a **1,413.9× breakout ratio**).
3. **Recent Velocity (High VPH):** Videos uploaded or trending within the last 90 days demonstrating sustained Views Per Hour ($\text{VPH} \ge 150$, e.g., *POV Wealth* clocking **1,177 VPH** on a fresh upload).

---

## 2. The 5–10 Competitor Outlier Scraping Protocol

1. **Identify the Top 5–10 Videos:**
   - Execute targeted searches for core POV wealth psychology topics:
     - `"stealth wealth habits"`
     - `"pov money psychology"`
     - `"how banks treat you at every level of wealth"`
     - `"old money mindset"`
     - `"why everything changes after 100k"`
   - Filter for videos where $\text{View Count} \ge 5\times \text{Channel Subscriber Count}$ (or Breakout Multiple $\ge 10\times$).
2. **Extract Transcripts & Timestamps:**
   - Run `vidiq_video_transcript` via vidIQ MCP in Antigravity IDE (5 credits per query) or execute local transcript extraction.
   - Archive cleaned raw transcripts into `projects/[NN]_[topic]/transcripts/`.
3. **Analyze Comment Heatmaps & Audience Psychology:**
   - Run `vidiq_video_comments` sorted by likes.
   - **Flag Permission & Affirmation Triggers:** Identify top-liked comments reflecting social and emotional relief (e.g., *"I needed to hear this," "This is me right now," "Nobody talks about how isolating it gets"*). These define the emotional anchor of our opening hook.
   - **Flag Inflated Math Backlash:** Viewers actively police return calculations (100+ like comments mocking 12% compounding or fantasy dividend figures). All channel calculations must reflect realistic historical baselines (7–8% inflation-adjusted S&P 500 returns).
   - **Flag Visual Artifact Grievances:** Viewers hunt and meme AI generation flaws (extra fingers, morphing faces, inconsistent clothes). Note recurring visual criticisms to prevent them during Nano Banana 2 batch prompting.

---

## 3. The Overlap / Gap Map Framework

Feed the 5–10 scraped competitor transcripts into Claude Opus / Gemini 3.1 Pro with the following POV extraction instruction:

```markdown
Analyze these [N] competitor transcripts on [POV Wealth Topic]. 
Produce two distinct lists:

1. Saturated Points: Surface-level financial advice, textbook definitions, and common tropes that appear in 2 or more competitor videos (e.g., "make a budget," "cut your daily coffee," generic compound interest definitions). We will mention these in at most 1 sentence or skip entirely.

2. Knowledge & Emotional Gaps: What social dynamics, relationship friction, or emotional isolation did the comments discuss that the videos skipped? (e.g., the silence when friends discover your net worth, the psychological guilt of frugal living, how institutions alter behavior across income brackets). What real-rate economic mechanisms were ignored?

Requirement: At least 40% of our script narrative must be built directly from Knowledge & Emotional Gaps.
```

---

## 4. Title Scoring & Packaging Protocol

### The 6 Research-Validated Title Formulas

Every video title must strictly follow one of these six proven archetypes:

| # | Formula Name | Structural Template | Validated Outlier Example | Peak Performance |
|---|---|---|---|---|
| 1 | **POV Consequence Hook** | `POV: You [action] — [quiet consequence]` | *POV: You Won the Lottery — And Showed Up to Work* | 337K views (1,177 VPH) |
| 2 | **Wealth Ladder** | `How [entity] Treats You at Every Level of Wealth — $0 to $[X]` | *How Banks Treat You at Every Level of Wealth — $0 to $25M* | 1.14M views (Ceiling) |
| 3 | **Binary Life-Math** | `You Pick [A], Your [Peer] Picks [B]: [Timeline]` | *You Pick a Trade, Brother Picks College: Debt vs Wages* | 155K views (785.8× ratio) |
| 4 | **Localized Incredulity** | `How Are [Demo] Affording [Asset] on [Wage]?!` | *How Are Brits Affording This?! The Fake Rich Trap* | 143K views |
| 5 | **Threshold Inflection** | `Why Everything Changes After $[X]` | *Why Net Worth EXPLODES After $100K* | High-conversion format |
| 6 | **Stealth Wealth Inversion** | `[#] [Habits/Rules] That Quietly Build [Fortune/Wealth]` | *Top 10 Habits That Build Quiet Wealth* | 197K views (116.6× ratio) |

### vidIQ Title Scoring Requirements

- Test candidate titles through the vidIQ Title Scorer.
- **Score Gate: Must score $\ge 85/100$** (Target $\ge 92/100$ for launch sprint priority).
- **Emotional Trigger Words:** Front-load quiet psychological tension using approved keywords:
  - **Approved:** `Quietly`, `Nobody`, `Secret`, `Weird`, `Changed`, `Noticed`
  - **Eliminated:** `Dangerous`, `Illegal`, `Accidentally`, `Collapse` (obsolete sensationalist explainer framing)

---

## 5. Primary Keyword Attack List

Focus topic ideation on low-competition, high-US-concentration search terms with validated growth trajectories:

| Keyword | Monthly Volume | Competition | US Audience Share | Trend / Signal | Recommended Format |
|---|---|---|---|---|---|
| `financial habits` | Medium | **9.0** | High | Lowest competition in niche | POV Story / Life-Path |
| `how pawn shops actually make money` | 85,646 | **20.9** | High | **+2,140% Growth** 🔥 | System Explainer |
| `budgeting` | 180,159 | **25.8** | **22.7% US** | Massive baseline | Binary Life-Math |
| `old money mindset` | 61,653 | **29.5** | High | Accelerating interest | Stealth Wealth Inversion |
| `how banks make money` | 45,272 | **31.7** | High | High CPM tier | Wealth Ladder |
| `how to budget` | 66,375 | **33.5** | 15,085 US | Evergreen demand | POV Consequence Hook |
| `frugal living` | 218,682 | **37.0** | **56,600 US** | Strong Tier-1 concentration | POV Wealth Psychology |
| `stealth wealth` | 111,057 | **38.5** | 17,086 US | High viral velocity | Stealth Wealth Inversion |
| `money psychology` | 477,745 | **41.5** | 30,296 US | Broad scale ceiling | POV Consequence Hook |

### Keyword Avoidance Matrix & Demand Shifts
- **Keywords to Avoid:**
  - `personal finance` (1.43M): Too generic; unbuildable into an immersive POV narrative.
  - `how to make money online` (1.31M): Saturated with low-quality spam; damages channel authority.
  - `day trading` (234K US): Attracts high-churn gambling audience; poor retention for wealth psychology.
  - `savings advice`: **-42.6% demand collapse**. Viewers reject preachy advice.
  - `pov finance` (4.99M): Heavily geo-diluted (26% Pakistan, only 5% US); destroys RPM.
- **Demand Vector:** System explainers (*"how [X] actually makes money"*), behavioral psychology, and stealth lifestyle stories are expanding rapidly. Generic saving tutorials are dying.

---

## 6. Competitor Scraping Targets (Tier S Intelligence)

Continuously monitor and scrape transcripts from the top 6 Tier S channels driving breakout efficiency:

| Channel Name | Channel ID | Subscribers | Views/Sub Metric | Signature Performance & Format Focus |
|---|---|---|---|---|
| **Quiet Money Stories** | `UCNjyn0Q1L2Mx0O4nXnXvfAA` | 1,300 | ~25× | **1,413.9× breakout video** (201K views at 1.3K subs); stealth wealth storytelling |
| **POV Wealth** | `UCryM-LAkg31P_B0GeshJQjg` | 2,270 | 15.14× | **1,177 VPH velocity breakout** (337K views in 6 days); shock + secrecy consequence hooks |
| **Ollie Finance** | `UCFGLwmoU1SuT6t_m3gRERpQ` | 5,740 | 10.96× | **754K views across 12 videos** (+77% views); quality over volume benchmark |
| **Wealthy Logix** | `UCtH6Vum0T0y0wI3URAnvR4w` | 5,130 | 8.55× | Pioneer of **Binary Life-Math** (*"You Pick Trade, Brother Picks College"*) |
| **Money Life POV** | `UCCEwJbv7D1CYzxdKYYOH6AA` | 11,500 | ~2× | **50,000 avg views/video** (2.7M views on 53 vids); visual contrast (cars, cash, lifestyle) |
| **Dark Ledger** | `UCDglfjh__GM2RFM1oAL3a6A` | 29,900 | 2.25× | **1.14M views niche ceiling**; undisputed master of the **Wealth Ladder** format |

### Weekly Transcript Extraction Protocol
1. Monitor these 6 channels every Monday during the validation block.
2. When any channel posts a video with $\text{VPH} \ge 100$ or reaches $\ge 3\times$ subscriber count within 7 days, extract the full SRT/timestamped transcript immediately using vidIQ MCP:
   ```json
   {
     "tool": "vidiq_video_transcript",
     "parameters": {
       "videoId": "<TARGET_VIDEO_ID>"
     }
   }
   ```
3. Run the extracted transcript through the Overlap/Gap Map framework to identify what emotional or mathematical elements the creator overlooked.

---

## 7. Extended Competitor Intelligence (Tier A, Tier B & Clone Blacklist)

### 7.1 Tier A — Active Competitors to Track
Monitor these active mid-tier competitors for pacing and formatting shifts:

| Channel | Subs | Key Metric | Strategic Notes |
|---|---|---|---|
| **POV Finance** (benchmark) | 24,700 | +57% subs/30d, +83% views | Near-daily cadence, the baseline template |
| **Finance POV** | 12,500 | +28% subs, +63% views | Rebranded from "USA Finance with Liam" |
| **ЦЕНА РИСКА** | 14,100 | +25% subs, +45% views | Russian-language Dark Ledger clone — proves export works |
| **Primate Economics** | 576,000 | 55.7× views/sub | 29 videos only. Ceiling proof for quality-over-volume |
| **Sight of Fortitude** | 19,100 | 6.10× | 514K breakout; money mindset stories |
| **Lucas Grant** | 16,300 | 2.48× | Cash-for-cars POV; 303K outlier in 44 days |
| **Growth Story Studio** | 44,100 | 5.61× | Indian quiet wealth; 116.57× breakout |
| **British Finance w/ Jack** | 16,700 | +15% subs | UK localized "Fake Rich Trap" — 143K outlier |
| **Matty Invests** | 14,900 | 1.85× | Retirement realities niche; near-daily cadence |
| **Pigeon Finance** | 13,900 | 1.23× | Bird mascot; 2.7%-5.9% engagement (highest community engagement) |

### 7.2 Tier B — Cautionary Anti-Patterns & Operational Lessons
Learn specific operational lessons from these channels:

| Channel | Core Lesson & Strategic Anti-Pattern |
|---|---|
| **Sketchinance** (41.1K, dormant) | Shorts cannot save a dead long-form engine; abandoned May 2026. Prioritize long-form retention. |
| **Hudson Bay Finance** (12.4K) | Extreme geographic/tax topic narrowness kills: Canadian tax only dropped views into the hundreds. Keep themes broadly Tier-1 English. |
| **Crown & Fortune** (22.9K) | Volume spam (3 videos in 2.5 hrs) = 6K average views. Never spam multiple long-forms a day. |
| **Economic Historian** (23.8K) | Flat growth (-0.42% subs). Third-person documentary framing $\ne$ immersive POV; proven inferior in AVD. |
| **Liora Invest** (5.87K) | Sub/view divergence: +13.5% subs but -18.4% views. Vanity metric trap—focus on views per sub, not raw sub count. |
| **Ivan Invests** (27.8K) | 461 videos, 0.25× views/sub. High volume without psychological packaging = algorithmic death. |

### 7.3 Tier C — The 16 Clone Network Blacklist (Handle: `povfinance`)
Avoid becoming part of the clone army. 16 POV Finance clones were found via handle search. The largest non-original is POV Finance Bro (17.9K, but posts food content). The actual finance clones cap at 4,270 subs due to word-for-word description copying.

| Handle | Subs | Algorithmic Verdict |
|---|---|---|
| `@povfinanceusd` | 47 | Literal word-for-word clone of POV Finance description; zero impressions |
| `@povfinancemindset` | 321 | Template copycat; suppressed by algorithm |
| `@povfinance-s6s` | 329 | Low retention clone |
| `@povfinancedaily` | 265 | Daily spam clone |
| `@povfinanceinvesting` | 4,270 | Largest finance clone; hit severe ceiling |
| `@povfinance-5` | 26 | Dead clone |
| `@povfinanceexplorer` | 31 | Dead clone |
| `@povfinances12` | 2,300 | Spanish clone |
| `@povfinancewithreid` | 33,600 | Not finance (viral/fails) |
| `@povfinancebro1` | 17,900 | Not finance (food slicing) |

**Operational Mandate:** Avoid `"POV Finance [word]"` naming patterns. Brand identity is locked to **Quiet Money POV** (`@quietmoneypov`).

---

## 8. Outlier Forensics: Top 15 Benchmark Videos

Reverse-engineer the pacing, emotional anchors, and packaging of the top 15 outlier videos across the niche:

| # | Channel | Title | Views | Breakout Multiplier | VPH | Core Format Key |
|---|---|---|---|---|---|---|
| 1 | **Sketchinance** | *The Salary Trap — Why The System Keeps You Broke* | 1,363,637 | — | 192 | System critique |
| 2 | **Dark Ledger** | *How Banks Treat You at Every Level of Wealth — $0 to $25M* | 1,141,946 | 237.7× | 8.85 | LADDER format (Ceiling) |
| 3 | **Sight of Fortitude** | *Power of Money Mindset — A Stealth Wealth Story* | 514,646 | 22.4× | 96 | Stealth wealth |
| 4 | **Hudson Bay** | *TFSA Mistake Before Retirement* | 418,213 | — | 11.3 | Localized tax |
| 5 | **Wealthy Logix** | *POV: Your Side Hustle Started Paying More Than Your Job* | 402,335 | 52.5× | 126 | Side hustle POV |
| 6 | **POV Wealth** | *POV: You Won the Lottery — And Showed Up to Work* | 337,462 | 58.3× | **1,177** | Shock + secrecy |
| 7 | **Lucas Grant** | *POV: What Happens When You Start Paying Cash for Cars* | 303,639 | 32.2× | 291 | Behaviour change |
| 8 | **Quiet Money Stories** | *[Stealth Wealth Breakthrough]* | 201,553 | **1,413.9×** | — | **Highest breakout multiple recorded** |
| 9 | **Dark Ledger** | *How Much You Need Invested to Live Off Dividends* | 237,247 | 4.07× | 73 | Retirement math |
| 10 | **Ollie Finance** | *POV: You Quietly Built a Second Income and Told No One* | 197,613 | — | — | Stealth income |
| 11 | **Growth Story Studio** | *Top 10 Habits that Build Quiet Wealth* | 196,974 | 116.6× | 20 | Habit list |
| 12 | **Bille Finance** | *A Day in the Life of a Quiet Millionaire* | 192,120 | 121.4× | 10 | Day-in-life |
| 13 | **Ollie Finance** | *POV: You Quietly Built a Portfolio That Pays More Than Your 9-to-5* | 192,529 | 21.5× | 76 | Portfolio POV |
| 14 | **The Stoic Economist** | *Why Real Wealth Looks Boring: 7 Quiet Wealth Habits* | 182,432 | 132.5× | 1.95 | Australian stealth |
| 15 | **ЦЕНА РИСКА** | *Living by Old Money Rules* | 171,206 | — | 24,458/day | Non-English proof |

### What These Outliers Prove:
1. **Stealth Wealth = Highest Breakout Multiples:** $116\times$ to $1,413\times$ breakout scores live exclusively in "quiet wealth / boring wealth" territory.
2. **The LADDER Format Has the Highest Ceiling:** Dark Ledger's "$0 to $25M" reached 1.14M views—the single largest video in the entire niche.
3. **POV Framing Crushes Explainer Framing:** Every video above 300K views uses second-person POV or the wealth ladder. Zero third-person documentaries exist in the top 15.
4. **Velocity (VPH) Outweighs Total View Count:** POV Wealth's 1,177 VPH proved the algorithm immediately recommends high-tension secrecy hooks over slow compounding topics.

---

## 9. Scored Titles Database (vidIQ Benchmarks)

Use these pre-tested titles and their respective scores as benchmarks when drafting new titles:

**High-Priority Benchmark Scores ($\ge 92/100$):**
- `"POV: You Kept the Same Car for 20 Years — Here's What It Built"` → **99**
- `"POV: You Checked Into a $10 Motel — Here's What the Room Really Cost"` → **97**
- `"Why Your Family Treats You Differently When You Become the First Millionaire"` → **97**
- `"POV: You Started Investing With $100 — Here's What Happened"` → **96**
- `"POV: You Bought the $600,000 House Everyone Said You Should Own"` → **96**
- `"POV: You Lived on $40,000 While Everyone Else Made $200,000"` → **95**
- `"Two Women. Same Salary. 15 Years Later, $740,000 Apart"` → **94**
- `"POV: You Saved $10,000 on an Average Salary"` → **94**
- `"POV: You Learned Why Old Money Stays Rich and New Money Goes Broke"` → **93**
- `"How Pawn Shops Actually Make Money (They Hope You Never Return)"` → **93**
- `"POV: You Won the Lottery — Then Went Back to Work"` → **92**
- `"Your Life at Every Level of Credit Score (300 to 850)"` → **92**
- `"Why Maxing Out Your 401(k) Quietly Costs High Earners the Most"` → **92**

---

## 10. 30-Day Research-Validated Topic Calendar

Execute this validated queue rotating across the 6 proven formulas:

### Week 1 — Launch Week (Format Baseline & Massive Viral Hooks)
| Slot | Title | Formula | Target Keyword | Strategic Rationale |
|---|---|---|---|---|
| **Mon (Vid 1)** | POV: You Kept the Same Car for 20 Years — Here's What It Built | POV | `how much does a car really cost` | VidIQ score 99; universal cold reach; 501K benchmark proof |
| **Tue (Vid 2)** | Two Women. Same Salary. 15 Years Later, $740,000 Apart | BIN | `money psychology` | VidIQ score 94; binary life-math; 277× proven breakout |
| **Wed (Vid 3)** | Why You Must Look Like a Loser to Escape the Rat Race | STL | `stealth wealth` | VidIQ score 98; channel manifesto; high subscriber conversion |
| **Thu (Vid 4)** | How Luxury Hotels Make Money From Rooms Nobody Sleeps In | System | `how hotels make money` | VidIQ score 90/97; lowest competition (18); 4,351× breakout ratio |
| **Fri (Vid 5)** | Your Life at Every Level of Credit Score (300 to 850) | LAD | `financial habits` | VidIQ score 92; maximum AVD viewer self-identification |
| **Sat (Vid 6)** | Why Your Family Treats You Differently When You Become the First Millionaire | POV | `money psychology` | VidIQ score 97; deep taboo; comment section ignition |
| **Sun (Vid 7)** | POV: You Bought the $600,000 House Everyone Said You Should Own | POV | `frugal living` | VidIQ score 96; cognitive dissonance; 30-year amortization math |

### Week 2 — Corporate Autopsies & Stealth Dynamics
| Slot | Title | Formula | Target Keyword | Strategic Rationale |
|---|---|---|---|---|
| **Mon (Vid 8)** | How Pawn Shops Actually Make Money (They Hope You Never Return) | System | `how pawn shops make money` | VidIQ score 93; +2,140% search surge; lowest competition (20.9) |
| **Tue (Vid 9)** | Why Maxing Out Your 401(k) Quietly Costs High Earners the Most | System | `old money mindset` | VidIQ score 92; high comment debate among corporate earners |
| **Wed (Vid 10)** | POV: Your $650 Car Payment Built Someone Else's $793,000 | POV | `car loan mistakes` | VidIQ score 95; dealer finance kickback disclosure |
| **Thu (Vid 11)** | POV: You Started Investing With $100 — Here's What Happened | POV | `how to budget` | VidIQ score 96; 4-tier milestone ladder ($100 to $500k) |
| **Fri (Vid 12)** | How Banks Treat You at Every Level of Wealth — $0 to $10M | LAD | `how banks make money` | VidIQ score 92; 1.14M views proven ceiling |
| **Sat (Vid 13)** | POV: You Lived on $40,000 While Everyone Else Made $200,000 | POV | `frugal living` | VidIQ score 95; social isolation and stealth accumulation |
| **Sun (Vid 14)** | You Pick a Trade, Your Brother Picks College: The 20-Year Math | BIN | `financial habits` | VidIQ score 91; 155K views proven format |

### Week 3 — Social Friction & System Mechanics
| Slot | Title | Formula | Target Keyword | Strategic Rationale |
|---|---|---|---|---|
| **Mon (Vid 15)** | POV: You Won the Lottery — Then Went Back to Work | POV | `money psychology` | VidIQ score 92; 337K views benchmark (1,177 VPH) |
| **Tue (Vid 16)** | POV: You Learned Why Old Money Stays Rich and New Money Goes Broke | POV | `old money mindset` | VidIQ score 93; high cultural curiosity |
| **Wed (Vid 17)** | POV: You Saved $10,000 on an Average Salary | POV | `budgeting` | VidIQ score 94; relatable milestone; 22.7% US share |
| **Thu (Vid 18)** | How Insurance Companies Actually Make Money | System | `money psychology` | System explainer demand surge; policy retention mechanics |
| **Fri (Vid 19)** | POV: You Quietly Stopped Paying Car Payments — Everything Changed | POV | `how much does a car really cost` | VidIQ score 86; Lucas Grant cash-for-cars proof (303K) |
| **Sat (Vid 20)** | 7 Quiet Wealth Habits That Secretly Build Millions | STL | `stealth wealth` | The Stoic Economist proof (182K views, 132× breakout) |
| **Sun (Vid 21)** | POV: Your Friends Found Out You're a Millionaire — Things Got Weird | POV | `money psychology` | Comment forensics proof; intense relational drama |

### Reserve Backlog (Data-Driven Iteration Queue)
- *Two Brothers. Same Salary. $740,000 Apart at 50* (BIN, 785.8× breakout ratio)
- *How Costco Actually Makes Money (It's Not What You Think)* (System Explainer, massive curiosity gap)
- *POV: You Built Wealth While Everyone Else Financed Their Life* (POV, VidIQ score: 89)
- *How Government Treats You at Every Level of Wealth — $0 to $1T* (LAD, high browse ceiling)
- *POV: Your Passive Income Replaced Your Salary — Nobody Noticed* (POV, ultimate stealth wealth payoff)

