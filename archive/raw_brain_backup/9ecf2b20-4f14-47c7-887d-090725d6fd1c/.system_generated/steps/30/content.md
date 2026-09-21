Title: Live Content

Description: Fetched live

Source: https://dashboard.nexlev.io/docs-md/mcp/quickstart.md

---

---
title: "Quickstart"
description: "Connect NexLev MCP to your preferred AI assistant and start analyzing YouTube channels in under 5 minutes. Choose the platform you use below."
source: "https://dashboard.nexlev.io/docs/mcp/quickstart"
---

# Quickstart

Connect NexLev MCP to your preferred AI assistant and start analyzing YouTube channels in under 5 minutes. Choose the platform you use below.

## Prerequisites

Before you begin, make sure you have:

- **Active NexLev account** — Free for all users. [Upgrade to Pro](?required_nexlev_lite_pro_access=true) for higher quota limits.

### Claude

#### Calude Web/Desktop

##### Via Claude's custom connector

**Step 1 — Active NexLev account**

Make sure your NexLev account is active before proceeding.

**Step 2 — Open Claude Connectors**

Go to **claude.ai → Settings → Connectors → Add custom connector**. You can also open the connectors page directly:

[Connect on Claude →](https://claude.ai/customize/connectors)

![Claude Settings → Connectors → Add custom connector](https://dashboard.nexlev.io/images/documentation/mcp/claude-add-custom-connector.png)

**Step 3 — Enter the connector details**

Fill in the following information exactly as shown:

| Field | Value |
| --- | --- |
| Name | `NexLev` |
| Server URL | `https://prod.dashboard.nexlev.io/api/claude-mcp` |
| Authentication | `OAuth` |

![Enter NexLev connector details in Claude](https://dashboard.nexlev.io/images/documentation/mcp/claude-step-3-connector-details.png)

**Step 4 — Approve the connection**

After adding the connector, please click the **Connect** button and Claude will redirect you to sign in with your NexLev account.

> **Warning**
>
> **Sign in with the right NexLev account.** If you have a paid NexLev plan
> (Lite, Pro, or Premium), make sure you log in with that account — your rate
> limits are tied to the account you connect. Signing in with a different
> account will apply Free plan limits instead.

**Step 5.A — Set tool permissions**

Go to **claude.ai → Settings → Connectors**, find NexLev, and click **Configure**. Then set **Tool permissions** to **Always allow** — this lets Claude use your NexLev tools automatically without asking you every time.

![Set NexLev tool permissions to Always allow in Claude](https://dashboard.nexlev.io/images/documentation/mcp/claude-step-5-permissions.png)

**Step 5.B — Allow write/delete tools**

In the same permissions panel, scroll down through the tools list and make sure you also set **Always allow** for any write or delete tools (such as **Swipe File**). These are listed separately and require individual approval.

![Allow write and delete tool permissions for NexLev in Claude](https://dashboard.nexlev.io/images/documentation/mcp/claude-swipe-file-allow.png)

> **Info**
>
> **Free plan limitation.** Attempting to use Write and delete tools — on the
> Free plan, it will return a message prompting to upgrade NexLev subscription.

**Step 6 — Verify NexLev is active in chat**

Before starting, confirm NexLev is enabled in your Claude chat window. Click the **+** button in the message bar, hover over **Connectors**, and check that the toggle next to **NexLev** is turned on.

![Verify NexLev connector is enabled in Claude chat](https://dashboard.nexlev.io/images/documentation/mcp/claude-nexlev-permission.png)

> **Info**
>
> **No API key needed.** Claude.ai uses OAuth to connect directly to your NexLev
> account. Works on web and mobile — your tools sync across all devices.

[Connect on Claude →](https://claude.ai/customize/connectors)

#### Claude Code CLI

##### Via Claude Code CLI

> **Warning**
>
> Requires the **Claude Code CLI**. If you don't have it yet, install it first:
> ```bash npm install -g @anthropic-ai/claude-code ``` Verify with `claude
> --version`.

**Step 1 — Active NexLev account**

Make sure your NexLev account is active before proceeding.

**Step 2 — Add the NexLev MCP server**

Run this once from any terminal:

```bash
claude mcp add -s user --transport http nexlev https://prod.dashboard.nexlev.io/api/claude-mcp
```

| Field | Value |
| --- | --- |
| Name | `nexlev` |
| Server URL | `https://prod.dashboard.nexlev.io/api/claude-mcp` |
| Transport | `HTTP` |
| Scope | `user — available in all projects on your machine` |

The `-s user` flag registers the server globally so it's available in every project. Omit it (or use `-s local`) to restrict it to the current directory only.

**Step 3 — Authenticate**

1. Start Claude Code in any directory:
   ```bash
   claude
   ```
2. Run the `/mcp` slash command inside the Claude prompt:
   ```
   /mcp
   ```
3. Select **nexlev** from the list, then choose **Authenticate**.
4. Your browser opens to `dashboard.nexlev.io` — log in with your NexLev account and approve the connection.

> **Warning**
>
> **Sign in with the right NexLev account.** If you have a paid NexLev plan
> (Lite, Pro, or Premium), make sure you log in with that account — your rate
> limits are tied to the account you connect. Signing in with a different
> account will apply Free plan limits instead.

5. Back in the terminal you'll see:
   ```
   Authentication successful. Connected to nexlev.
   ```

**Step 4 — Verify the connection**

```bash
claude mcp list
```

You should see:

```
nexlev: https://prod.dashboard.nexlev.io/api/claude-mcp (HTTP) - ✓ Connected
```

**Step 5 — Use it**

Just talk to Claude in natural language — it picks the right NexLev tool automatically:

```
Find 10 faceless YouTube channels in the personal finance niche earning over $5K/month
```

```
Pull the full analytics for @MrBeast — subscriber growth, RPM, and top videos
```

> **Info**
>
> **Token stored locally.** Your OAuth token lives in `~/.claude.json` — treat
> it like a credential and don't commit it. It persists across sessions
> automatically. If it ever expires, re-run `/mcp` → select `nexlev` →
> **Authenticate** to refresh.

**Managing the server**

| Task                          | Command                                                          |
| ----------------------------- | ---------------------------------------------------------------- |
| List all MCP servers          | `claude mcp list`                                                |
| Inspect NexLev's config       | `claude mcp get nexlev`                                          |
| Remove the NexLev server      | `claude mcp remove nexlev`                                       |
| Re-authenticate (token issue) | Inside `claude`, run `/mcp` → select `nexlev` → **Authenticate** |

If `claude mcp list` shows `✗ Failed to connect`, the server URL is unreachable. Remove and re-add it with the correct URL.

**Troubleshooting**

**`! Needs authentication` after running `/mcp`**
The browser flow didn't complete. Re-run `/mcp` and make sure you finish the login on `dashboard.nexlev.io` until the browser tab shows a success page.

**`✗ Failed to connect`**

- Confirm the URL is correct: `https://prod.dashboard.nexlev.io/api/claude-mcp`
- Check your network / VPN / firewall — the CLI must reach `*.nexlev.io` over HTTPS
- Run `curl -I https://prod.dashboard.nexlev.io/api/claude-mcp` to test reachability

**Tool call returns `access_denied` or `rate_limited`**

- `access_denied` — your NexLev plan doesn't include this tool. [Upgrade your plan](?required_nexlev_lite_pro_access=true) in the dashboard.
- `rate_limited` — you've hit your plan's daily quota. Wait and retry, or upgrade.

**Claude doesn't seem to use NexLev tools**
Run `/mcp` to confirm `nexlev` is **Connected**. If you added it with `local` scope, you must launch `claude` from that project directory. Re-add with `-s user` to make it global.

### ChatGPT

#### ChatGPT Web/Desktop

##### Via ChatGPT custom MCP app (OAuth)

**Step 1 — Active NexLev account**

Make sure your NexLev account is active before proceeding.

**Step 2 — Enable Developer mode**

Go to **chatgpt.com → Settings → Apps → Advanced settings** and toggle on **Developer mode**.

[Connect on ChatGPT](https://chatgpt.com/#settings/Connectors)

![Enable Developer mode in ChatGPT Advanced settings](https://dashboard.nexlev.io/images/documentation/mcp/chatgpt-step-1-developer-mode.png)

**Step 3 — Create a new app**

Go to **Settings → Apps → Create App**.

**Step 4 — Enter the app details**

Fill in the following information exactly as shown:

| Field | Value |
| --- | --- |
| Name | `NexLev` |
| MCP Server URL | `https://prod.dashboard.nexlev.io/api/mcp` |
| Authentication | `OAuth` |

![Create App in ChatGPT Settings](https://dashboard.nexlev.io/images/documentation/mcp/chatgpt-step-2-create-app.png)

**Step 5 — Confirm and connect**

Tick **"I understand and want to continue"**, then click **Create**. ChatGPT will auto-discover the OAuth settings — no Client ID or secret needed.

When you first use a NexLev tool, ChatGPT will redirect you to sign in with your NexLev account. Click **Approve** to connect.

> **Warning**
>
> **Sign in with the right NexLev account.** If you have a paid NexLev plan
> (Lite, Pro, or Premium), make sure you log in with that account — your rate
> limits are tied to the account you connect. Signing in with a different
> account will apply Free plan limits instead.

> **Info**
>
> **No API key needed.** ChatGPT uses OAuth to connect directly to your NexLev
> account. You can use the same NexLev account across both ChatGPT and Claude —
> each gets its own connection.

#### Codex CLI

##### Via Codex CLI

> **Warning**
>
> Requires the **Codex CLI**. If you don't have it yet, install it first:
> ```bash npm install -g @openai/codex ``` Verify with `codex --version`.

**Step 1 — Active NexLev account**

Make sure your NexLev account is active before proceeding.

**Step 2 — Add the NexLev MCP server**

Run this once from any terminal:

```bash
codex mcp add nexlev --url https://prod.dashboard.nexlev.io/api/codex-mcp
```

| Field | Value |
| --- | --- |
| Name | `nexlev` |
| Server URL | `https://prod.dashboard.nexlev.io/api/codex-mcp` |
| Transport | `Streamable HTTP` |

This registers the server globally in `~/.codex/config.toml`, available across all projects.

**Step 3 — Authenticate**

1. Start Codex in any directory:
   ```bash
   codex
   ```
2. Run the `/mcp` slash command inside the Codex prompt:
   ```
   /mcp
   ```
3. Select **nexlev** from the list, then choose **Authenticate**.
4. Your browser opens — log in with your NexLev account and approve the connection.

> **Warning**
>
> **Sign in with the right NexLev account.** If you have a paid NexLev plan
> (Lite, Pro, or Premium), make sure you log in with that account — your rate
> limits are tied to the account you connect. Signing in with a different
> account will apply Free plan limits instead.

**Step 4 — Verify the connection**

```bash
codex mcp list
```

You should see `nexlev` listed as connected.

**Step 5 — (Optional) Manual config edit**

Alternatively, you can directly edit `~/.codex/config.toml` and add:

```toml
[mcp_servers.nexlev]
url = "https://prod.dashboard.nexlev.io/api/codex-mcp"
```

> **Info**
>
> **Config shared across CLI and IDE.** Once you set up the server in
> `~/.codex/config.toml`, it works across both the Codex CLI and IDE extension
> without redoing setup.

**Managing the server**

| Task                 | Command                                                         |
| -------------------- | --------------------------------------------------------------- |
| List all MCP servers | `codex mcp list`                                                |
| Remove NexLev        | `codex mcp remove nexlev`                                       |
| Re-authenticate      | Inside `codex`, run `/mcp` → select `nexlev` → **Authenticate** |

### OpenClaw

#### Via OpenClaw

> **Info**
>
> **How it works.** OpenClaw doesn't talk to NexLev directly — it routes tasks
> through **Claude Code CLI** or **Codex CLI** already installed on your machine
> via its ACP (Agent Client Protocol). The flow is: **You (messaging app) →
> OpenClaw Gateway → Claude Code / Codex CLI → NexLev MCP tools**

**Prerequisites — CLI installed & NexLev registered**

Before setting up OpenClaw, confirm at least one CLI is installed and NexLev MCP is already registered in it — OpenClaw calls the CLI, which in turn calls NexLev.

Register NexLev in **Claude Code CLI** (if using Claude):

```bash
claude mcp add -s user --transport http nexlev https://prod.dashboard.nexlev.io/api/claude-mcp
```

Register NexLev in **Codex CLI** (if using Codex):

```bash
codex mcp add nexlev --url https://prod.dashboard.nexlev.io/api/mcp
```

See the **Claude** or **ChatGPT** tabs above for full CLI setup instructions.

---

**Step 1 — Install OpenClaw**

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

This installs the Gateway daemon and walks you through pairing with your messaging channel (Telegram, Discord, WhatsApp, etc.).

---

**Step 2 — Install the acpx plugin**

ACP sessions are powered by the `acpx` plugin. Install and enable it:

```bash
openclaw plugins install @openclaw/acpx
openclaw config set plugins.entries.acpx.enabled true
openclaw config set plugins.allow '["acpx"]'
```

Then enable ACP and set your default CLI:

```bash
openclaw config set acp.enabled true
openclaw config set acp.backend acpx
openclaw config set acp.allowedAgents '["claude", "codex"]'

# Pick your default (whichever CLI you have installed):
openclaw config set acp.defaultAgent claude
# or:
openclaw config set acp.defaultAgent codex
```

---

**Step 3 — Register NexLev inside OpenClaw**

The URL depends on which CLI OpenClaw will call:

```bash
# If your default CLI is Claude Code:
openclaw mcp set nexlev '{"url":"https://prod.dashboard.nexlev.io/api/claude-mcp","transport":"streamable-http"}'

# If your default CLI is Codex:
openclaw mcp set nexlev '{"url":"https://prod.dashboard.nexlev.io/api/mcp","transport":"streamable-http"}'
```

Verify it was saved:

```bash
openclaw mcp list
```

> **Note**
>
> **Prefer manual config?** Edit `~/.openclaw/openclaw.json` directly and add
> your server entries under `mcp.servers`, then run `openclaw gateway restart`.

---

**Step 4 — Authenticate NexLev**

OpenClaw inherits auth from the CLI it calls. Authenticate inside that CLI:

```bash
claude    # or: codex
/mcp
# Select nexlev → Authenticate
# Browser opens → log in to dashboard.nexlev.io → approve
```

> **Warning**
>
> **Sign in with the right NexLev account.** If you have a paid NexLev plan
> (Lite, Pro, or Premium), make sure you log in with that account — your rate
> limits are tied to the account you connect. Signing in with a different
> account will apply Free plan limits instead.

---

**Step 5 — Spawn a session & use NexLev**

From your connected messaging app (Telegram, Discord, etc.), spawn a session:

```
/acp spawn claude --bind here
```

The `--bind here` flag pins the conversation to the session so follow-up messages route to the same CLI instance. Then just ask in natural language:

```
Find 10 faceless YouTube channels in the finance niche earning over $5K/month
```

```
Pull full analytics for @MrBeast — subscriber growth, RPM, and top videos
```

---

**Managing the server**

| Task                         | Command                     |
| ---------------------------- | --------------------------- |
| List MCP servers in OpenClaw | `openclaw mcp list`         |
| Remove NexLev from OpenClaw  | `openclaw mcp unset nexlev` |
| Check ACP health             | `/acp doctor` (in chat)     |
| Check active sessions        | `/acp status` (in chat)     |
| Close a session              | `/acp close` (in chat)      |
| Restart the gateway          | `openclaw gateway restart`  |

**Troubleshooting**

**NexLev tools not visible**
OpenClaw calls the CLI — the CLI is what talks to NexLev. Verify the CLI itself has NexLev registered: `claude mcp list` or `codex mcp list`.

**Wrong endpoint**
Using the Claude Code URL with Codex (or vice versa) will silently fail.

- Claude Code → `https://prod.dashboard.nexlev.io/api/claude-mcp`
- Codex → `https://prod.dashboard.nexlev.io/api/mcp`

**ACP spawn blocked**
ACP sessions run on the host runtime. If your session is sandboxed, use `runtime="subagent"` or disable sandboxing for the session.

### Hermes

#### Via Hermes Agent

> **Info**
>
> **How it works.** Hermes is a self-hosted autonomous agent that connects
> natively to NexLev as an MCP server — no intermediary CLI required. The flow
> is: **You (messaging app) → Hermes Gateway → NexLev MCP tools**
>
> Unlike the OpenClaw path (which routes through Claude Code / Codex CLI),
> Hermes talks to MCP servers directly via its built-in MCP client.
>

**Prerequisites — Hermes installed**

**macOS / Windows (recommended):** Download the Hermes Desktop installer from [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com) — it installs both the desktop app and the CLI in one step.

**Linux / macOS / WSL2 (CLI only):**

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc   # or source ~/.zshrc
```

---

**Step 1 — Run first-time setup**

```bash
hermes setup
```

Walks you through choosing a model provider (Nous Portal, OpenRouter, Anthropic, etc.). If you already have `~/.openclaw`, the setup wizard detects it and offers to migrate your settings, memories, and API keys automatically.

---

**Step 2 — Register NexLev as an MCP server**

Add NexLev to `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  nexlev:
    url: "https://prod.dashboard.nexlev.io/api/claude-mcp"
    auth: oauth
```

Verify it was saved:

```bash
hermes mcp list
```

Test the connection:

```bash
hermes mcp test nexlev
```

---

**Step 3 — Authenticate NexLev**

On first connection, run:

```bash
hermes mcp login nexlev
```

A browser opens → log in to `dashboard.nexlev.io` → approve. Tokens are cached at `~/.hermes/mcp-tokens/nexlev.json` and reused silently on subsequent runs.

> **Warning**
>
> **Sign in with the right NexLev account.** If you have a paid NexLev plan
> (Lite, Pro, or Premium), make sure you log in with that account — your rate
> limits are tied to the account you connect. Signing in with a different
> account will apply Free plan limits instead.

> **Note**
>
> **On a remote / headless host?** When Hermes runs on a VPS, the loopback OAuth
> callback can't reach your browser. Hermes will print an authorize URL and a
> paste-back prompt. Open the URL in your browser, approve, copy the full
> redirect URL (a connection error on that page is expected), and paste it at
> the prompt.

---

**Step 4 — Connect a messaging platform (e.g. Telegram)**

Interactive setup (recommended):

```bash
hermes gateway setup
```

Select **Telegram** when prompted. The wizard asks for your bot token and allowed user IDs and writes the config automatically.

Manual setup — add credentials to `~/.hermes/.env`:

```bash
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
TELEGRAM_ALLOWED_USERS=123456789    # comma-separated for multiple users
```

> **Note**
>
> **Don't have a bot token?** Create one via **@BotFather** (`/newbot`). Get
> your numeric user ID via **@userinfobot**.

Then start the gateway in the foreground:

```bash
hermes gateway
```

Or, if you've installed it as a background service:

```bash
hermes gateway start
```

---

**Step 5 — Use NexLev from your messaging app**

Message your bot in natural language:

```
Find 10 faceless YouTube channels in the finance niche earning over $5K/month
```

```
Pull full analytics for @MrBeast — subscriber growth, RPM, and top videos
```

---

**Managing the server**

| Task                            | Command                       |
| ------------------------------- | ----------------------------- |
| List MCP servers                | `hermes mcp list`             |
| Remove NexLev                   | `hermes mcp remove nexlev`    |
| Test NexLev connection          | `hermes mcp test nexlev`      |
| Re-authenticate NexLev          | `hermes mcp login nexlev`     |
| Re-select NexLev tools          | `hermes mcp configure nexlev` |
| Check gateway service status    | `hermes gateway status`       |
| Restart the gateway service     | `hermes gateway restart`      |
| Check platform status (in chat) | `/platforms`                  |
| Reload MCP config (in chat)     | `/reload-mcp`                 |

**Troubleshooting**

**NexLev tools not visible**
Run `hermes mcp list` to confirm the entry exists, then `hermes mcp test nexlev` to verify it's reachable. If the connection succeeded but tools are missing, run `hermes mcp configure nexlev` to check your tool selection checklist.

**Wrong endpoint**
Hermes uses the Claude-MCP endpoint. Make sure your config has:
`https://prod.dashboard.nexlev.io/api/claude-mcp`
Not the Codex/plain variant (`/api/mcp`).

**Auth expired**
Run `hermes mcp login nexlev` to refresh the OAuth token.

**Gateway not responding**
Check with `hermes gateway status`. Restart with `hermes gateway restart`.

> **Info**
>
> **Coming from OpenClaw?** Run `hermes claw migrate` to import your settings,
> memories, skills, and API keys in one step. The setup wizard also auto-detects
> `~/.openclaw` if you run `hermes setup` fresh.

## What You Can Do Next

Once connected, start using NexLev tools directly inside your AI chat:

### Long Form Channel Search

```
Find 20 long-form channels related to the minecraft niche
```

### Short Form Channel Analysis

```
Show me 15 viral YouTube Shorts channels in the comedy niche
```

### Keyword Research

```
Find high-volume, low-competition keywords for cooking content
```

### Content Strategy

```
What content strategy should I use for a tech review channel with 10K subscribers?
```

### Competitive Research

```
Compare successful channels in the fitness niche and identify common patterns
```

### Thumbnail Generation

```
Generate a thumbnail for my video "I Tried Waking Up at 4AM for 30 Days" — match the style of the top productivity channels
```

### Off-Platform Earnings

```
What does @AliAbdaal sell outside of ads, and which brands sponsor the most finance channels?
```

### Network Research

```
Which network is MrBeast signed to, and what other channels are under it?
```

## Understanding NexLev Responses

When you use NexLev through Claude, ChatGPT, or Claude Code CLI, you'll receive interactive widgets displaying:

- **Channel data** — Comprehensive metrics, performance indicators, and growth analytics
- **Sortable results** — Click column headers to sort by different metrics
- **Expandable details** — View in-depth information for each result
- **Filtering options** — Refine results by various criteria
- **Pagination** — Navigate through large result sets

> **Tip**
>
> **Pro Tip:** Results are interactive! You can sort, filter, and expand
> channels directly within the chat interface for deeper analysis.

## Rate Limits

All limits are **per user, per tool, and reset every 24 hours**.

> **Note**
>
> Lite and Premium share identical rate limits across all tools. If you're on
> the Premium plan, the numbers in the Lite column apply to you.

### Networks & CMS

> **Note**
>
> CMS tools are available on **Lite, Pro, and Premium** plans only — Free plan
> users do not have access.

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Content owner lookup (`get_content_owner`) | 0 | 5 | 15 |
| CMS network search (`search_cms_networks`) | 0 | 5 | 15 |

With **usage credits** enabled, calls past the daily limit cost $0.05 each for both tools. See [CMS Networks](/docs/mcp/cms-networks).

### Channel Discovery

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Long-form channel search (`find_long_form_channels`) | 10 | 150 | 300 |
| Short-form channel search (`find_shorts_channels`) | 10 | 150 | 300 |
| Similar channels (`get_similar_channels`) | 5 | 20 | 30 |
| Latest discovered faceless niches (`latest_discovered_faceless_niches`) | 20 | 150 | 300 |
| Faceless channel check (`check_faceless_channel`) | 5 | 100 | 300 |
| Channel resolver (`channel_resolver`) | 10 | 100 | 500 |
| Niche channel search (`search_niche_finder_channels`) | 10 | 100 | 200 |

### Video Intelligence

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Similar videos (`get_similar_videos`) | 5 | 20 | 30 |
| Video search (`search_videos`) | 10 | 150 | 300 |
| YouTube search (`youtube_search`) | 50 | 100 | 500 |
| Video details (`youtube_video_details`) | 10 | 100 | 300 |
| Video comments (`youtube_video_comments`) | 10 | 150 | 300 |
| Video transcript (`get_video_transcript`) | 5 | 150 | 300 |
| Bulk video transcripts (`get_bulk_video_transcripts`) | 5 | 50 | 100 |
| Video subtitle (`get_video_subtitle`) | 5 | 150 | 300 |
| Bulk video subtitles (`get_bulk_video_subtitles`) | 5 | 50 | 100 |
| Channel outlier videos (`youtube_channel_outliers`) | 10 | 50 | 100 |
| YouTube suggested videos (`search_youtube_suggested_videos`) | 20 | 150 | 300 |
| Viral videos — small channels (`search_viral_videos_small_channels`) | 20 | 150 | 300 |
| Faceless outlier videos (`faceless_outliers_videos`) | 20 | 150 | 300 |

### Visual Search

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Similar thumbnails (`get_similar_thumbnails`) | 5 | 20 | 30 |

### Visual Video Analysis

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Watch YouTube video and ask (`watch_youtube_video_and_ask`) | 1 | 5 | 15 |
| Watch Instagram video and ask (`watch_instagram_video_and_ask`) | 1 | 5 | 15 |
| Watch TikTok video and ask (`watch_tiktok_video_and_ask`) | 1 | 5 | 15 |

### Channel Analytics

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Channel analytics (`get_channel_analytics`) | 5 | 20 | 30 |
| Daily analytics (`get_daily_analytics`) | 5 | 20 | 30 |
| Short vs long views (`get_short_vs_long_views`) | 5 | 20 | 30 |
| Geography & revenue (`get_geography_revenue`) | 5 | 20 | 30 |
| Batch channel metrics (`get_batch_channel_metrics`) | 5 | 20 | 30 |
| Channel categories (`get_channel_categories`) | 10 | 100 | 500 |
| Channel formats (`get_channel_formats`) | 10 | 100 | 500 |
| Channel videos (`youtube_channel_videos`) | 50 | 100 | 300 |
| Channel shorts (`youtube_channel_shorts`) | 50 | 100 | 300 |
| Channel playlists (`youtube_channel_playlists`) | 50 | 100 | 300 |
| Channel about (`youtube_channel_about`) | 50 | 100 | 300 |

### Monetization

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Channel monetization check (`check_channel_monetization`) | 5 | 100 | 300 |
| Video monetization check (`check_video_monetization`) | 5 | 100 | 300 |
| Video RPM (`get_video_rpm`) | 5 | 150 | 300 |

### Niche Intelligence

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Niche overview (`get_niche_overview`) | 5 | 20 | 30 |
| Niche categories (`get_niche_finder_categories`) | 10 | 100 | 500 |
| Niche formats (`get_niche_finder_formats`) | 10 | 100 | 500 |
| Niche tags (`get_niche_finder_tags`) | 5 | 100 | 500 |

### Swipefile

> **Note**
>
> Swipefile is available on **Lite, Pro, and Premium** plans only — Free plan
> users do not have access.

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| List swipefile folders (`list_swipefile_folders`) | 0 | 200 | 500 |
| List swipefile items (`list_swipefile_items`) | 0 | 200 | 500 |
| Get folder insights (`get_swipefile_folder_insights`) | 0 | 100 | 300 |
| Save to swipefile (`save_to_swipefile`) | 0 | 100 | 300 |
| Update swipefile item (`update_swipefile_item`) | 0 | 50 | 200 |
| Move swipefile item (`move_swipefile_item`) | 0 | 30 | 100 |
| Delete swipefile item (`delete_swipefile_item`) | 0 | 30 | 100 |
| Create swipefile folder (`create_swipefile_folder`) | 0 | 20 | 50 |

### Personal Channel Analytics

> **Note**
>
> Personal Channel Analytics tools is available on **Lite, Pro, and Premium**
> plans only — Free plan users do not have access.

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| List my YouTube channels (`list_my_youtube_channels`) | 0 | 100 | 200 |
| Channel overview (`get_my_channel_overview`) | 0 | 20 | 50 |
| Channel analytics (`get_my_channel_analytics`) | 0 | 20 | 50 |
| Revenue report (`get_my_revenue_report`) | 0 | 15 | 40 |
| Top videos (`get_my_top_videos`) | 0 | 15 | 40 |
| Audience demographics (`get_my_audience_demographics`) | 0 | 15 | 40 |
| Traffic sources (`get_my_traffic_sources`) | 0 | 15 | 40 |
| Device & OS report (`get_my_device_report`) | 0 | 15 | 40 |
| Geography report (`get_my_geography_report`) | 0 | 15 | 40 |
| Playback locations (`get_my_playback_locations`) | 0 | 15 | 40 |
| Content sharing (`get_my_content_sharing`) | 0 | 15 | 40 |
| Subscriber status (`get_my_subscriber_status`) | 0 | 15 | 40 |
| Video analytics (`get_my_video_analytics`) | 0 | 20 | 50 |
| Audience retention (`get_my_audience_retention`) | 0 | 15 | 40 |

### Thumbnail Lab

> **Note**
>
> Thumbnail Lab is available on **Lite, Pro, and Premium** plans only, and
> requires an **OAuth** connection — API-key connections cannot use it. Its
> allowance is a shared monthly and daily budget rather than a per-tool call
> limit, and it is shared with the Thumbnail Lab in your dashboard. See
> [Thumbnail Lab](/docs/mcp/thumbnail-lab) for the full breakdown.

| Plan | Generations          | AI edits             |
| ---- | -------------------- | -------------------- |
| Free | — (not available)    | — (not available)    |
| Lite | 3 / day · 10 / month | 3 / day · 15 / month |
| Pro  | 5 / day · 25 / month | 5 / day · 25 / month |

With **usage credits** enabled, extra actions past the included allowance cost $0.15 (lite model) or $0.40 (pro model) per generation and $0.10 / $0.25 per AI edit, capped at 30 generations and 30 edits per rolling hour. Failed jobs are refunded automatically.

### Promotions & Sponsorships

| Tool | Free | Lite | Pro |
| --- | --- | --- | --- |
| Channel promotions (`get_channel_promotions`) | 5 | 100 | 250 |
| Live promotions analysis (`get_channel_promotions_realtime`) | 2 | 10 | 20 |

With **usage credits** enabled, calls past the daily limit cost $0.02 each for `get_channel_promotions` and $0.05 each for `get_channel_promotions_realtime`. See [Channel Promotions](/docs/mcp/channel-promotions).

## Get Help

- **Dashboard** — [dashboard.nexlev.io](https://dashboard.nexlev.io)
- **Support** — [contact@nexlev.io](mailto:contact@nexlev.io)
- **Community** — [Discord server](https://discord.com/invite/youtubefaceless)


