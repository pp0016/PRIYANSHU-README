# Learning Proposal — NexLev MCP Direct Caller

## What Happened

In this session, calling NexLev MCP tools was painful because:

1. **The built-in `call_mcp_tool` couldn't find the NexLev server** — it returned `server name nexlev not found` despite the server being configured in `mcp_config.json`
2. **OAuth auth was required** — NexLev uses OAuth via `mcp-remote`, which needs browser authorization the first time. After that, tokens are cached
3. **Dangling `mcp-remote` processes** blocked re-auth — old node processes holding port 28085 had to be killed manually
4. **PowerShell mangles JSON** — inline JSON args with `{` and `"` get destroyed by PowerShell, requiring separate `.py` script files

The working solution: a **Python script** using the official `mcp` SDK that calls NexLev tools via `stdio_client` → `npx.cmd mcp-remote`. Once authenticated once, tokens are cached and subsequent calls work instantly.

---

## Classification: **New Skill**

No existing skill covers calling NexLev MCP tools programmatically. The `youtube-data-extractor` skill uses browser-based opencli scraping (which also failed — browser bridge not connected). This is a different approach entirely.

---

## Proposed Skill: `nexlev-mcp-caller`

**Location:** `C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\SKILL.md`

### SKILL.md Content

```markdown
---
name: nexlev-mcp-caller
description: >-
  Calls NexLev MCP tools directly via Python + mcp SDK when the built-in
  call_mcp_tool fails or NexLev server is not found. Use when the user asks
  to "use nexlev", "call nexlev mcp", "get channel analytics via nexlev",
  "check monetization", "find similar channels", or any NexLev tool call
  that fails through the normal MCP path. Also use when the user says
  "nexlev not working", "nexlev auth", or "fix nexlev".
---

# nexlev-mcp-caller

You call NexLev MCP tools directly using a Python script + the `mcp` SDK
when the built-in `call_mcp_tool` tool returns "server not found" or fails.

---

## How It Works

NexLev uses OAuth authentication via `mcp-remote`. After first-time browser
auth, tokens are cached at `~/.mcp-auth/` and subsequent calls work instantly.

### The Reusable Caller Script

Location: `C:\Users\renu5\.gemini\antigravity\scratch\nexlev_call.py`

To call any NexLev tool, create a small Python script that imports asyncio
and the mcp SDK, then calls the specific tool:

```python
import asyncio
import json
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

async def call_tool(tool_name, arguments):
    server_params = StdioServerParameters(
        command="npx.cmd",
        args=["-y", "mcp-remote", "https://prod.dashboard.nexlev.io/api/claude-mcp"],
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            return result

async def main():
    result = await call_tool("TOOL_NAME", {"arg": "value"})
    for content in result.content:
        print(content.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### Key Rules

1. **ALWAYS use `npx.cmd`** on Windows (not `npx`)
2. **NEVER pass JSON as inline PowerShell args** — write a .py file instead
3. **If auth fails with "Another instance is running":**
   - Kill the process holding port 28085: `netstat -ano | findstr :28085` → `taskkill /PID <pid> /F`
   - Then retry
4. **If auth fails with "Authorization code has been used or expired":**
   - Kill ALL mcp-remote processes: `wmic process where "commandline like '%mcp-remote%'" call terminate`
   - Then retry — a fresh browser auth window will open
5. **For multiple tool calls**, create ONE script with sequential `await call_tool()` calls (each opens its own connection, which is fine since tokens are cached)

---

## NexLev Rate Limits (Free Plan)

ALWAYS check remaining limits before calling. Reference file:
`C:\Users\renu5\Downloads\Nexlev's official rate-limt mcp.md`

| Limit | Tools |
|-------|-------|
| **50/day** | youtube_search, youtube_channel_videos, youtube_channel_shorts, youtube_channel_playlists, youtube_channel_about |
| **20/day** | latest_discovered_faceless_niches, search_youtube_suggested_videos, search_viral_videos_small_channels, faceless_outliers_videos |
| **10/day** | channel_resolver, search_niche_finder_channels, search_videos, youtube_video_details, youtube_video_comments, youtube_channel_outliers, find_long_form_channels, find_shorts_channels |
| **5/day** | get_similar_channels, check_faceless_channel, get_similar_videos, get_video_transcript, get_channel_analytics, get_daily_analytics, check_channel_monetization, get_video_rpm, get_niche_overview, get_batch_channel_metrics |
| **2/day** | get_channel_promotions_realtime |
| **1/day** | watch_youtube_video_and_ask, watch_instagram_video_and_ask, watch_tiktok_video_and_ask |

**Strategy:** Use 50/day tools first (youtube_channel_about, youtube_channel_videos) before burning 5/day tools (get_channel_analytics, check_channel_monetization).

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `server name nexlev not found` | Use this skill's Python approach instead of `call_mcp_tool` |
| `RATE LIMIT EXCEEDED` | Check limits above. Wait 24h or enable usage credits in NexLev dashboard |
| Browser auth window doesn't appear | Kill process on port 28085 and retry |
| `Connection closed` error | Old mcp-remote process is stale. Kill all and retry |
| `npx` not found | Use `npx.cmd` on Windows |
```

---

## Proposed Rule (Optional)

### `nexlev-rate-limit-awareness`

**Location:** `C:\Users\renu5\.gemini\config\rules\nexlev-rate-limits.md`

```markdown
# NexLev Rate Limit Awareness

When using NexLev MCP tools, ALWAYS:
1. Prefer high-limit tools first (50/day: youtube_channel_about, youtube_channel_videos)
2. Use low-limit tools sparingly (5/day: get_channel_analytics, check_channel_monetization)
3. If a tool returns RATE LIMIT EXCEEDED, tell the user which tool hit the limit and suggest waiting 24h
4. Reference rate limits at: C:\Users\renu5\Downloads\Nexlev's official rate-limt mcp.md
```

---

## Files to Create

1. `C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\SKILL.md` — The skill file above
2. `C:\Users\renu5\.gemini\config\rules\nexlev-rate-limits.md` — (Optional) Rate limit awareness rule

Approve to proceed with creation.
