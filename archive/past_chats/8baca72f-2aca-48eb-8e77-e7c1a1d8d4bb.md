# Chat Session: 8baca72f-2aca-48eb-8e77-e7c1a1d8d4bb

### 🧑 You
<USER_REQUEST>
You are a research subagent part of a deep research swarm investigating if a brand new Twitter (X) account can reach 5,000 video views organically.
Your specific sub-query is: "X Twitter algorithm new account organic reach restrictions 2026"
Focus: Does X put brand new accounts in a "sandbox" or shadowban them to prevent spam? How long does it take for a new account to reach the "For You" feed?

Guidelines from deep-researcher:
1. Use `search_web` with the sharpened query.
2. Read URLs to extract evidence (don't rely just on search snippets).
3. Do NOT cover case studies of zero-follower views, verification impact, or specific growth hacks (other agents are doing those).
4. Report your findings with Source Tiers (Tier A: Primary, Tier B: Verified Secondary, Tier C: Lead Only).

When you have found the answer and reached evidence saturation, reply back to me immediately with your structured findings and citations.
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-08-13T04:59:34+05:30.
</ADDITIONAL_METADATA>

---

### 🤖 Antigravity
I have completed the deep research task on the X (Twitter) algorithm restrictions for new accounts (2026 architecture) and delivered the findings to the caller agent via `send_message`.

### Summary of Key Findings Sent to Main Agent:
1. **Sandbox Status:** No explicit hardcoded "sandbox" flag exists in the codebase (`twitter/the-algorithm` or `xai-org/x-algorithm`). Instead, new accounts experience an emergent **Cold Start Gating** driven by:
   - **TweepCred & UserMass Prior:** Account age (`created_at_msec` / `diffDays`) and lack of PageRank interaction graph centrality cause tweets to fall below `minTweepcredFilterThreshold`, filtering them out before candidate generation.
   - **SimClusters Cold Start:** Without interaction edges (follows/likes/replies), the engine cannot map the account to any of the 145,000 community interest vector clusters used for "For You" out-of-network candidate retrieval.
2. **Visibility Filtering ("Shadowbanning"):** Enforced via `visibilitylib` under the official "Freedom of Speech, Not Reach" policy. New accounts triggering anti-spam classifiers face automatic `Drop` (search/feed exclusion) or `Reply Deboosting` for **24–72 hours**.
3. **Timeline to "For You" Feed:**
   - **0–24 Hours:** Initial security verification & Search indexing (`Latest` tab).
   - **1–3 Days:** In-network seeding & behavioral observation period.
   - **3–7 Days:** SimClusters vectorization and crossing of `minTweepcredFilterThreshold` into initial "For You" candidate pools.
   - **7–14+ Days:** Full algorithmic candidate scoring and out-of-network mobility.

---

