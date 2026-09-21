# @cineporty Full Channel Analysis — NexLev Only

## Goal
Extract **all real data** about YouTube channel **@cineporty** (Cineporty) using **NexLev MCP tools only** (no vidIQ, no assumptions). Deliver as one comprehensive markdown report.

## What We Know (From Screenshot Only)
- Handle: `@cineporty`
- Display name: Cineporty
- Subscribers: ~12K
- Videos: 15
- Monetized: Yes (vidIQ badge visible)
- Bio mentions horror movies — but **NexLev will determine the actual niche**

## Extraction Steps (In Order)

### Step 1: Identify Channel & Niche
- Use NexLev to look up `@cineporty` and get the **actual niche classification** as determined by their system
- Extract: channel ID, niche category, sub-niche, content type classification

### Step 2: Niche RPM (Exact)
- Use NexLev to get the **exact RPM** for whatever niche @cineporty falls into
- Extract: RPM range (low/mid/high), CPM data if available, revenue estimates

### Step 3: Top 3 Competitors — Full Deep-Dive
- Use NexLev `similar_channels` or equivalent to find competitors
- For each of the **top 3 competitors**:
  - Channel name, handle, subscriber count, total views
  - Video count, upload frequency
  - RPM / estimated earnings
  - Content analysis (what they cover, their format)
  - Growth metrics

### Step 4: Competitor Landscape Overview
- Who dominates this niche at the top level
- Market saturation signal
- Where @cineporty sits relative to the landscape

### Step 5: New Creator Playbook
- Derived **ONLY from the real NexLev data** collected in Steps 1-4
- Entry strategy, content gaps, recommended positioning
- Revenue expectations based on real RPM data

## Tools Used
- **NexLev MCP** via the `nexlev-mcp-caller` skill (Python scripts)
- **NO vidIQ** — user explicitly opted out
- **NO assumptions** — all niche/RPM/competitor data comes from NexLev

## Output
- Single markdown artifact report with sections:
  1. Channel Profile (NexLev data)
  2. Niche & RPM Data
  3. Top 3 Competitors (deep-dive tables)
  4. Competitor Landscape
  5. New Creator Playbook

## Constraints
- ❌ No monetization check (user will verify manually)
- ❌ No assumed niche labels — NexLev determines the niche
- ❌ No vidIQ tools
- ✅ Credits are not a concern
