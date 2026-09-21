Title: Live Content

Description: Fetched live

Source: https://dashboard.nexlev.io/docs-md/mcp/channel-search.md

---

---
title: "Channel Search"
description: "Search NexLev's channel database to discover and analyse YouTube channels — both long-form and Shorts — using natural language prompts in your AI assistant."
source: "https://dashboard.nexlev.io/docs/mcp/channel-search"
---

# Channel Search

Search NexLev's channel database to discover and analyse YouTube channels — both long-form and Shorts — using natural language prompts in your AI assistant.

## Prerequisites

- **Connected AI assistant** — Claude, ChatGPT, or any other supported platform
- **Active NexLev account** — [Connect to your AI assistant](/docs/mcp/quickstart) to get started. [Upgrade to Pro](?required_nexlev_lite_pro_access=true) for higher quota limits.

## Tools

### Long Form

#### Long-Form Channel Search

Find and analyse traditional YouTube channels (videos typically over 8 minutes) across any niche, size, or performance threshold.

**Basic prompt structure:**

```
Find [number] long-form channels [niche/criteria]
```

**Example prompts:**

```
Find 20 long-form channels in the Minecraft niche
```

```
Find 20 monetized faceless long-form channels in finance with good RPM
```

```
Find 25 long-form channels under 1 year old with high outlier scores
```

```
Find 30 long-form channels with high average views but low subscriber count
```

**Filters you can apply in your prompt:**

- Monetization status, faceless vs on-camera, kids content
- Subscriber range, average views range, RPM threshold
- Content category and format, video length
- Channel age, upload frequency, outlier score
- Revenue ranges, growth rate

> **Tip**
>
> Combine multiple filters in one prompt — e.g. "Find 20 monetized, faceless
> long-form channels in gaming with 10K–100K subscribers and RPM over $5."

### Short Form

#### Short-Form Channel Search

Find and analyse YouTube Shorts channels — viral creators, emerging trends, and high-performing short-form content across any niche.

**Basic prompt structure:**

```
Find [number] short-form channels [niche/criteria]
```

**Example prompts:**

```
Find 20 short-form channels in the comedy niche
```

```
Find 15 viral YouTube Shorts channels with high average views
```

```
Find 25 AI-generated short-form channels in entertainment
```

```
Find 20 short-form channels under 30 days old with exceptional outlier scores
```

```
Find 15 English-language short-form channels targeting a US audience
```

**Filters you can apply in your prompt:**

- Subscriber count, total views, average views per Short
- Outlier score, revenue range
- AI content, category, language, country
- First upload date, upload frequency

> **Tip**
>
> Include filter criteria directly in your prompt — e.g. "Find 20
> English-language AI-generated Shorts channels in comedy with 100K–500K views
> per Short and high outlier scores."

## Troubleshooting

**No results returned?**

- Broaden your criteria or reduce the number of combined filters
- Try alternative niche terms (e.g. "cooking" vs "culinary")
- Some niches have limited coverage — try a parent category

**Results don't match your query?**

- Rephrase your prompt more specifically
- Include exact numbers and named criteria
- Break a complex query into a simpler one first, then refine

**Tool not responding?**

- Check your NexLev account is active and the MCP connection is complete (see [Quickstart](/docs/mcp/quickstart))
- If you've hit your daily quota, [Upgrade to Pro](?required_nexlev_lite_pro_access=true) for higher limits

## Rate Limits

Both tools share the same limit — per user, and reset every 24 hours.

| Plan | Calls per 24h |
| --- | --- |
| Free | 10 |
| Lite | 150 |
| Pro | 300 |

## What's Next?

- **[Channel Analytics](/docs/mcp/channel-analytics)** — Deep-dive metrics for any channel
- **[Similar Channels](/docs/mcp/similar-channel)** — Find channels similar to any channel
- **[Faceless Channels](/docs/mcp/faceless-channels)** — Check or discover faceless channels
- **[Daily Analytics](/docs/mcp/daily-analytics)** — Track day-by-day growth trends


