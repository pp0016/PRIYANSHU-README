# vidIQ — Full Capabilities Reference

> Based on your vidIQ web app (screenshots) + MCP server schemas (54 tools total). 
> **Your plan**: Free tier. **Current balance**: 250 credits (130 renewable, resets Aug 20 + 120 add-on).

---

## Your vidIQ Web App Features (From Screenshots)

Your screenshots show the web app at `app.vidiq.com` connected to the "Mad Monkeys vs crazy indians" channel (which you said is a burner — ignore it). The web interface gives you:

| Feature | Location | What It Does |
|---|---|---|
| **Script Writer** | Sidebar → Script Writer | Input a topic → generates a full script. Default: Long format, 10 mins. Adjustable tone. |
| **AI Title Generator** | Sidebar → Title Generator | Input a video idea or paste script → generates title suggestions. Long-form or Shorts toggle. **5 credits per call.** "Reference channels for style inspiration" requires **Boost (paid upgrade)**. |
| **Daily Ideas** | Sidebar → Daily Ideas | Auto-generates video ideas for your connected channel daily. **Customized ideas = English only.** Personalized ideas need at least 1 uploaded video. |
| **Learn** | Sidebar → Learn | Masterclasses from creators (Youari, Rob Wilson, Airrack). **Some locked behind "Upgrade to unlock."** |
| **Competitors** | Sidebar → Competitors | Track competitor channels. |
| **Research** | Sidebar → Research | Keyword/topic research. |
| **Optimize** | Sidebar → Optimize | SEO optimization for your videos. |
| **Calendar** | Sidebar → Calendar | Content calendar planning. |
| **Generate** | Sidebar → Generate | General AI generation hub. |
| **Subscribers** | Sidebar → Subscribers | Subscriber analytics. |
| **Video Generator** | Sidebar → Video Generator | AI video generation (likely credit-heavy). |

---

## MCP Server Tools — Complete List with Costs

### 🟢 Free / Zero-Cost Tools
| Tool | Purpose | Credits |
|---|---|---|
| `vidiq_balance` | Check your credit balance | **0** |
| `vidiq_voiceover_list_voices` | List available TTS voices | **0** |

### 🔵 Research & Intelligence Tools (5 credits each)
| Tool | Purpose | Key Params |
|---|---|---|
| `vidiq_keyword_research` | Search volume, competition, related/rising terms. 3 modes: `country_top`, `country_search`, `research` | `keyword`, `country` |
| `vidiq_outliers` | Find viral videos outperforming their channel average | Filters for niche, time range |
| `vidiq_trending_videos` | Videos gaining views fastest right now (views-per-hour velocity) | `videoFormat` (long/short) |
| `vidiq_channel_stats` | Subscriber count, total views, video count, historical growth | `channelId` |
| `vidiq_channel_videos` | List a channel's recent or top-performing videos | `channelId`, `videoFormat` |
| `vidiq_channel_search` | Find channels by niche/handle/title using semantic search | `query` or filters |
| `vidiq_channel_analytics` | Official YouTube Analytics for YOUR owned channels | `channelId` |
| `vidiq_similar_channels` | Find competitor channels similar to a target | `niche` |
| `vidiq_similar_videos` | Find high-performing videos similar to a seed video | `videoId` |
| `vidiq_video_stats` | Historical views, likes, comments, VPH for a video | `videoId`, `granularity` |
| `vidiq_video_transcript` | Full transcript/captions for a video | `videoId` |
| `vidiq_video_comments` | Comment threads + replies | `videoId` or `channelId` |
| `vidiq_video_earnings_estimate` | Estimated USD earnings for a video | `videoId` |
| `vidiq_score_title` | Score a title 0-100 for CTR potential | `title`, `type` |
| `vidiq_score_thumbnail` | Score a thumbnail for CTR with feedback | `videoId`, `title` |
| `vidiq_generate_titles` | Generate scored title suggestions | `videoId` or `title` or `description` |
| `vidiq_earnings_calculate` | Estimate monthly revenue from view count + niche | `subject`, `monthlyViews`, `category` |

### 🟡 Content Creation Tools (Variable credits — USE CAREFULLY)
| Tool | Purpose | Credits | Worth It? |
|---|---|---|---|
| `vidiq_generate_script` | Full long-form script from topic + concept | **1 per minute** of script (10-min = 10 credits) | Maybe — test once against Opus |
| `vidiq_generate_thumbnail` | AI thumbnail from metadata/prompts | **22 credits** | **Expensive.** Only if you can't make one in Canva/AI |
| `vidiq_refine_thumbnail` | Edit an existing thumbnail with text instructions | **22 credits** | Same as above |
| `vidiq_generate_broll` | Stock B-roll clips with attribution | **1 credit** | Cheap — use freely |
| `vidiq_voiceover_generate` | TTS voiceover from text | **14 per 1000 chars** | Expensive for long scripts. ElevenLabs may be better |
| `vidiq_motion_graphics` | Animated motion graphics / typography cards → MP4 | **1 per 4 seconds** (min 2) | Could be useful for Stickman intros |
| `vidiq_compose` | Assemble scenes + VO + music + overlays → MP4 | **1 per 4 seconds** (min 2) | Full video assembly |
| `vidiq_generate_video` | AI video from text (Sora-2, Veo-3.1, Kling) | **Duration × model rate × 20** | **Very expensive.** A 5-sec Sora clip could be 100+ credits |
| `vidiq_generate_clips` | Slice long video into vertical shorts with captions | **9 per minute of source** | Useful for repurposing. 10-min video = 90 credits |

### ⚪ Other Tools (Not Directly Useful Now)
| Tool | Purpose |
|---|---|
| `vidiq_breakout_channels` | Find fast-growing new channels |
| `vidiq_subscriber_insights` | Subscriber behavior analytics |
| `vidiq_channel_performance_trends` | Performance trend data |
| `vidiq_trend_categories` | Trending topic categories |
| `vidiq_list_competitors` / `vidiq_update_competitors` | Manage competitor tracking |
| `vidiq_youtube_search` | Search YouTube videos |
| Instagram/TikTok tools | `ig_profile`, `ig_reels`, `ig_outlier_reels_search`, etc. — not relevant yet |
| `vidiq_voiceover_clone` / `vidiq_voiceover_clone_start` | Voice cloning |
| `vidiq_video_watch` / `vidiq_watch_shortform_content` | Watch/analyze videos |
| `vidiq_submit_feedback` | Send feedback to vidIQ |
| `vidiq_jobs_list` / `vidiq_job_poll` | Check async job status |

---

## Credit Budget Strategy

**You have 250 credits total.** Here's how to spend them wisely:

### High-Value Spending (DO this)
| Action | Credits | How Many Times | Total |
|---|---|---|---|
| Keyword research for Stickman niche | 5 | 4 sessions | 20 |
| Keyword research for Nishchay niche | 5 | 4 sessions | 20 |
| Score titles before publishing | 5 | 10 videos | 50 |
| Find outlier videos in your niches | 5 | 4 searches | 20 |
| Competitor channel stats | 5 | 6 channels | 30 |
| Channel videos (competitor top vids) | 5 | 6 channels | 30 |
| **Subtotal** | | | **170** |

### One-Time Test Spending
| Action | Credits | Notes |
|---|---|---|
| Generate 1 script (vs Opus comparison) | 10-15 | Test on a 10-15 min video topic |
| Generate 1 thumbnail | 22 | See if it's better than Canva/AI gen |
| B-roll clips | 1-5 | Cheap, grab what you need |
| **Subtotal** | | **~40** |

### Remaining buffer: ~40 credits

**Renewable credits (130) reset Aug 20.** Don't hoard them — they refill.

### What NOT to Spend Credits On
- ❌ `generate_video` — too expensive, use Remotion/FFmpeg instead
- ❌ `voiceover_generate` — use ElevenLabs or your own voice
- ❌ `generate_clips` — 90 credits for a 10-min video is wasteful when CapCut does it free
- ❌ Multiple `generate_thumbnail` calls — 22 credits each adds up fast

---

## vidIQ Script Writer vs Opus 4.6 — Honest Comparison

You asked: **does vidIQ actually produce better scripts than Opus 4.6?**

| Dimension | vidIQ Script Writer | Opus 4.6 (me) |
|---|---|---|
| **YouTube-specific training** | Trained on top-performing video scripts. Knows what hooks, pacing, and structures get retention. | General-purpose. I know writing principles but not YouTube-specific retention patterns. |
| **Customization** | Limited — you input topic + tone, it outputs a script. Less control over style/voice. | Full control — you can iterate, add constraints, specify exact format, reference competitor scripts. |
| **Your niche context** | Generic. Doesn't know your specific channels, competitors, or audience. | I have your full context — channels, niches, competitors, goals, constraints. |
| **Cost** | 1 credit per minute of script. A 15-min Nishchay script = 15 credits. | Free (included in Antigravity). |
| **Quality floor** | Consistently decent — never terrible, rarely exceptional. | Variable — could be better or worse depending on prompt quality. |
| **Iteration** | Regenerate = another 15 credits. | Iterate infinitely, no cost. |

**My honest recommendation**: Test vidIQ's script writer ONCE on a Stickman topic (costs 10-15 credits). Compare it side-by-side with a script I write for the same topic. Then decide based on the actual output. Don't assume either is better — test it.

**The real edge isn't the AI tool, it's your workflow**: Feed me 3 competitor scripts that performed well → I analyze what made them work → I write a script that borrows the structure but uses your angle. vidIQ can't do that workflow.

---

## How to Actually Use NotebookLM Audio

### Step-by-step:
1. Go to [notebooklm.google.com](https://notebooklm.google.com)
2. Create a new notebook → name it (e.g., "Stickman YouTube Strategy")
3. Click **"Add Source"** → choose **YouTube URL** → paste the video link
4. Repeat for up to 50 sources per notebook
5. In the right panel, find **"Audio Overview"** → click **"Generate"**
6. NotebookLM creates a ~10-20 min podcast-style conversation between two AI hosts discussing ALL your sources
7. **Download the audio** → transfer to phone → listen during gym

### What it's good for:
- Strategy/talking-head videos where the value is in the IDEAS, not visuals
- Synthesizing multiple videos into one audio summary
- Testing your understanding via the Q&A chat after listening

### What it's bad for:
- Visual tutorials (editing, motion graphics, animation) — it only reads the transcript
- Videos where the creator shows their screen — all visual context is lost
- Short videos — not enough substance to generate a useful overview

### The move for your gym time:
Create 2 notebooks:
1. **"Stickman Strategy"** — feed the 6 priority strategy videos from the watch list
2. **"YouTube Growth"** — feed the demonetization + algorithm videos

Generate audio overviews for both. That's 6+ hours of processed content you absorb while lifting. Zero active time cost.

lessons i learned after using : 
Here is the rule for using vidIQ credits going forward, in the shortest way possible:

❌ DO NOT USE MCP FOR (Save Credits):
Checking stats of a channel we already know just tell me i can copy paste the data of by usinng vidiq extention 
Why: You can just open the channel in your browser and copy-paste the extension data to me for free. The extension actually gives more data (like estimated earnings).
✅ USE MCP FOR (Spend Credits):
Finding "Similar Channels" to one we already know in extention but this doesnt work propely so we can use
Finding NEW / Hidden Channels (vidiq_channel_search, vidiq_outliers).
Keyword & Trend Research (vidiq_keyword_research).
Title & Thumbnail Scoring (When we start making videos).
Why: The extension only works after you find a channel. The MCP tools can search YouTube's entire backend database to discover things you'd never find manually.
Bottom Line: If you have the channel link, YOU paste the stats. If we need to find something hidden, I use the MCP.

