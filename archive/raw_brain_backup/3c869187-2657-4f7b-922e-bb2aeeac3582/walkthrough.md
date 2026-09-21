# Walkthrough — NexLev MCP Skill + EverythingProfessor Report

## What Was Accomplished

### 1. EverythingProfessor Channel Report ✅

Extracted via NexLev MCP using 4 tools:
- `youtube_channel_about` → 618K subs, 45M views, joined Jan 2025, JDavo Media
- `youtube_channel_videos` → Top 30 videos sorted by views (5.2M top video)
- `check_channel_monetization` → ✅ Monetized
- `check_faceless_channel` → ✅ Faceless (98% confidence), educational/science

**Saved to:**
- [EverythingProfessor_channel_report.md](file:///C:/Users/renu5/.gemini/antigravity/brain/3c869187-2657-4f7b-922e-bb2aeeac3582/EverythingProfessor_channel_report.md)
- `C:\Users\renu5\Downloads\priyanshu readme\niche_research\EverythingProfessor_channel_report.md`

---

### 2. NexLev MCP Caller Skill — Permanent ✅

Created a reusable skill at `C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\` so you **never have to debug NexLev auth again**.

#### Files Created

| File | Purpose |
|------|---------|
| [SKILL.md](file:///C:/Users/renu5/.gemini/config/skills/nexlev-mcp-caller/SKILL.md) | Instructions, rate limits, troubleshooting, channel workflow template |
| [scripts/nexlev_call.py](file:///C:/Users/renu5/.gemini/config/skills/nexlev-mcp-caller/scripts/nexlev_call.py) | Call any single NexLev tool — the core reusable script |
| [scripts/nexlev_batch.py](file:///C:/Users/renu5/.gemini/config/skills/nexlev-mcp-caller/scripts/nexlev_batch.py) | Call multiple NexLev tools in one run from a JSON config |
| [scripts/nexlev_kill_stale.py](file:///C:/Users/renu5/.gemini/config/skills/nexlev-mcp-caller/scripts/nexlev_kill_stale.py) | Kill stale mcp-remote processes blocking port 28085 |

#### What Problems This Solves
- ❌ `call_mcp_tool` returns "server name nexlev not found" → ✅ Python scripts bypass this
- ❌ PowerShell mangles JSON args → ✅ Scripts read from file, handle BOM
- ❌ OAuth auth confusion / dangling processes → ✅ Tokens cached after first login, kill script for stale processes
- ❌ Unicode encoding crash on Windows → ✅ UTF-8 output handling built in

---

### Tested & Verified ✅

Ran `youtube_channel_about` for @EverythingProfessor using the new skill script — **connected, authenticated (cached tokens, no browser), returned full data.**

---

## How Future Conversations Will Use This

Next time you say "use nexlev to check this channel", the agent will:

1. Read the `nexlev-mcp-caller` SKILL.md (auto-discovered from skills folder)
2. Write a temp JSON args file
3. Run `python ~/.gemini/config/skills/nexlev-mcp-caller/scripts/nexlev_call.py <tool> <args_file>`
4. Parse the output — no debugging, no auth hassle

**Zero code rewriting required.**
