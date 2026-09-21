# Forensic Skill Comparison: Original vs New Versions

## TL;DR Verdicts

| Skill | Verdict | Confidence |
|---|---|---|
| **Anti-Sycophancy** | **UPGRADE** — significant | High |
| **Deep Researcher** | **UPGRADE** — significant | High |
| **Prompt Forge** | **UPGRADE** — significant | High |

All three are upgrades. Not a single one is a downgrade. But they are upgrades in a very specific way that needs explanation, because on the surface they *look* like downgrades — they are all dramatically shorter.

---

## The Architecture Shift

Before getting into each skill, here's what happened at the design level, because it's the same move across all three:

**Original versions** were written as **compliance checklists** — exhaustive lists of rules, tables, banned words, edge cases, and procedural steps. They told the model *what to do in every situation*.

**New versions** are written as **calibration documents** — they explain *why* each behavior matters, give the model a reasoning framework, and trust it to derive the correct action from understanding the principle.

This is a real distinction in prompt engineering. The originals are "rule-following" prompts. The new versions are "understanding" prompts. Current frontier models (Opus 4.6, Gemini 3.1 Pro) respond better to the second approach — they over-apply checklist rules and lose nuance, but they generalise well from understood principles.

The new versions also show awareness of specific, tested failure modes of AI research and writing, citing real findings (e.g., the 2026 Science paper on sycophancy, measured citation accuracy rates of AI tools). The originals assert rules without grounding them.

---

## 1. Anti-Sycophancy

### Size change
- Original: 342 lines, 20,550 bytes
- New: 201 lines, 10,277 bytes + portable-core.md (25 lines, 1,689 bytes)
- **~50% smaller**

### What was removed

| Removed element | Was it a loss? |
|---|---|
| Layer 1 input debiasing table (6 transformations) | **No.** The new version does the same thing in Section 1 ("restate as a neutral question with the stance taken out") but states the *principle* instead of listing examples. The principle is more general — it covers cases the table didn't. |
| Intent Amplification (Section 1.42-51) | **Moved** to anti-sycophancy Section 7 ("Depth on the first answer"), rewritten with better reasoning. |
| Rule 3a Severity Calibration table | **No.** New Section 3 covers this with "Size the reply to the decision." Less prescriptive, equally clear. |
| Rule 5 Agreement Streak Detection | **Kept** in Section 8 ("Drift"), but improved — adds the recommendation to offer a blind brief in a fresh chat, which is a stronger intervention than just "stress-test it." |
| Rule 6 Pushback Classification table | **Kept** in Section 4, rewritten with fewer categories but the same logic. Adds a finding: "Roughly half of all answer changes under pushback move toward the right answer, so updating is often correct." This calibrates the model away from stubbornness-for-stubbornness-sake. |
| Rule 8 Agentic Coding Exemptions (full table) | **Kept** as "When to skip all of this" (Section bottom). Shorter, same coverage. |
| Rule 9 Pre-Mortem | **Kept** in Section 3, bullet 6 ("The most likely way the plan fails, and the cheapest test..."). Actually *better* — it adds the "cheapest test" framing, turning critique into action. |
| Rule 10 Self-Consistency | **Kept** in Section 3 ("recommend one and name the runner-up and why it lost"). |
| Rule 11 Quality Assessment Defense (5 sub-rules) | **Kept** in Section 6, significantly tighter. Same five ideas in four bullets. |
| Banned vocabulary list (50+ entries) | **Removed entirely.** This is the one deletion that needs discussion — see below. |
| Structural Tell Detection (5 patterns) | **Removed.** Delegated to "stop-slop" and "humanizer" skills per the closing line: "for prose style, use the dedicated writing skills." |
| Pre-Delivery Self-Audit (7 checks) | **Removed as a formal checklist.** The principles are woven throughout. |

### What was added

| New element | Value |
|---|---|
| **Canary system with challenge-response** ("check N" → word from secret list) | **Major addition.** The original had only the "Priyanshu," prefix. The new version adds a cryptographic-style verification that the skill is actually loaded, not just that the prefix is being parroted from an earlier turn. This catches the real failure mode the original missed. |
| **Blind second opinion** (Section 2) | **Major addition.** No equivalent in original. For high-stakes decisions, write a stance-free brief and give it to a fresh sub-agent. This is the strongest anti-sycophancy technique possible — it removes the entire conversation's drift. |
| **Flip test** ("if he had argued the opposite with the same confidence, would the verdict be the same?") | **Major addition.** A simple, testable self-check that is more effective than the original's "Am I agreeing because it's easier?" because it has a concrete counterfactual. |
| **Calibration target framing** ("He will be right about half the time") | **Major addition.** The original's framing was "challenge everything." The new version says "be accurate, not contrarian." This is the correct calibration — the original risked creating a model that disagreed performatively. |
| **portable-core.md** | **Major addition.** A <1,500 character distillation for ChatGPT custom instructions, Gemini Gems, Claude projects. No equivalent in original. Extends the skill beyond Antigravity. |
| **Explicit separation of judgement vs prose style** | **Smart addition.** "This skill governs judgement; for prose style, use the dedicated writing skills." The original tried to do both (banned vocabulary, structural tells). The new version correctly scopes itself. |

### The Banned Vocabulary Question

The original had a 50+ entry banned word list. The new version removes it entirely, delegating prose style to stop-slop and humanizer.

**This is an upgrade, not a downgrade.** The banned word list was doing two jobs:
1. Preventing sycophantic language ("Great question!", "You're absolutely right")
2. Preventing AI writing tells ("delve", "leverage", "robust")

Job #1 is handled by the new "Wording" section: "No praise openers." Job #2 belongs in a writing skill, not a judgement skill. Mixing them made the original's scope unclear and forced the model to run a vocabulary scan on every response — including responses where the words weren't sycophantic at all ("robust encryption" is a perfectly valid phrase in a security context).

### Verdict: UPGRADE

The new version is better calibrated, has stronger anti-drift techniques (blind brief, flip test, challenge-response canary), correctly separates judgement from prose style, and will produce more accurate responses because it explains *why* each rule exists instead of just listing rules. The "ruthless but accurate, not ruthless for show" framing is the single most important improvement — it prevents the original's failure mode of performative disagreement.

---

## 2. Deep Researcher

### Size change
- Original: 360 lines, 18,802 bytes
- New: 231 lines, 11,080 bytes + evidence-by-question-type.md (97 lines, 4,565 bytes)
- **~40% smaller in main file, but reference file adds domain-specific depth the original lacked**

### What was removed

| Removed element | Was it a loss? |
|---|---|
| PhD Mode auto-escalation with keyword triggers | **No.** The new version replaces this with "stakes" reasoning (Section 1): "Stakes are higher when he will publish the answer, quote the number, spend money on it, or when it touches health, law or finance." This is more accurate — a question containing the word "percentage" doesn't need PhD-grade rigor, but a question where someone will quote the number in a video does. The original triggered on vocabulary; the new version triggers on consequences. |
| Source Quality Tiers (A/B/C) with formal table | **Replaced** with Section 3 ("Judge a source by leaving it"), which is a more principled and harder-to-game approach. Instead of classifying sources into tiers by *type*, it teaches the model to evaluate sources by *independence and first-hand access*. The original's tiers could be gamed (a vendor blog on a .org domain would score Tier B). The new approach can't. |
| Plan Confirmation Gate | **Simplified.** New version: "Show him the plan and start. Do not wait for approval; he can interrupt." This is better for workflow speed. The original forced a halt even on straightforward research. |
| Agent Scaling table (2-6 agents) | **Simplified** to Section 6: "One thread for a single fact. Two to four for comparisons." Same logic, less overhead. |
| Ask-Me-First Rule | **Kept and improved** (Section 1): "Ask a question first only when the request is ambiguous in a way that would send the whole search in the wrong direction." More precise trigger condition. |
| Saturation Test | **Kept** (Section 7): "The last three sources added nothing that changed the answer." Same logic. |
| Counter-Evidence Search | **Kept and integrated** (Section 2, paragraph 4): "run one search against it by name." Same technique. |
| Circular Reporting Detection | **Kept and improved** (Section 4): "Ten articles citing one press release are one source. Wire copy, syndicated copies and press-release rewrites collapse into one." The new version is more concrete with better examples. |
| AI-Generated Content Filter | **Replaced with something better** (Section 3): "Do not try to detect whether a page was written by AI. Detectors are unreliable and a large share of new pages contain some AI text. Ask what the page adds instead." This is factually correct — AI detection is unreliable — and the alternative (evaluate by what the page contributes) is more useful. |
| Evidence-First Quote Extraction | **Kept and made mandatory** (Section 5): "Find the sentence or table that supports the claim, and copy it into your notes as a quote." This is now the core of the verification step, not an optional enrichment technique. |
| Source Provenance Verification | **Kept and strengthened** (Section 5): "Cite only URLs that a tool returned during this session; never write a URL, DOI or paper ID from memory." Same rule, stronger wording. |
| Bias Detection (Who Benefits Filter) | **Kept** (Section 3): "Who is behind it, and do they gain if the claim is believed?" |
| Recency Weighting (12/24 month rules) | **Replaced** with a more nuanced approach (Section 4): "no fixed age limit works. Ask what could have changed since the page was published." This is more accurate — a 6-month-old software answer can be stale, a 3-year-old systematic review can be current. Fixed cutoffs are blunt instruments. |
| Report template (formal sections) | **Simplified** (Section 8). Fewer mandatory sections, but the ones that matter are there: Answer, Findings, Contested, Could not verify, Sources, Method. Dropped "Consensus & Disagreement Map" as a mandatory section — this was rarely useful and added bulk. |
| Time-Horizon Triage | **Removed as a formal system.** Partially covered by the recency discussion in Section 4. Minor loss at most. |

### What was added

| New element | Value |
|---|---|
| **Opening calibration paragraph** about citation accuracy rates | **Major addition.** "the page behind the link supports the sentence attached to it only about half to three-quarters of the time" — this is a real finding about AI research tools, and stating it upfront calibrates the model to prioritize verification over collection. The original never stated *why* verification matters, just that it should happen. |
| **Tool call budget** (Section 1) | **Major addition.** "roughly 10 tool calls for a single fact, 25 to 40 for a standard question." The original had no budget concept, which led to runaway research sessions. The "keep a quarter for verification" rule is particularly smart. |
| **"Judge a source by leaving it"** (Section 3) | **Major addition.** An entire section on lateral reading — evaluating sources by searching *about* them, not by reading their self-descriptions. This is how professional fact-checkers work. The original had nothing equivalent; it classified sources by *type* (official docs = good, blogs = bad), which is much weaker. |
| **Worked example** (Section 4, the "49% sycophantic" claim) | **Major addition.** A concrete, detailed example showing how a real statistic mutates as it travels across the internet. This teaches the model *how* to trace origins, not just *that* it should. |
| **Verification labels** (Verified / Reported / Unverified) | **Better than the original's tier system.** These labels describe what the researcher *actually did* (found the quote, found it secondhand, couldn't find an origin), not what category the source falls into. More honest. |
| **"Without search tools" fallback** (Section at end) | **Addition.** What to do when no tools are available. The original had no fallback. |
| **"Works with" cross-skill reference** | **Addition.** Ties to anti-sycophancy: "search the neutral question, not the hoped-for answer." |
| **evidence-by-question-type.md** reference file | **Major addition.** Domain-specific source hierarchies for health/science, statistics, software, business, news, and YouTube/creator platforms. The original had generic source tiers. This reference file gives the model specific knowledge about what a good source looks like in each domain — including checks specific to each domain (e.g., "search the paper title with 'retraction'" for health). |

### Verdict: UPGRADE

The new version fixes the original's core weakness: the original was good at *collecting* sources but weak at *verifying* them. The new version makes verification the centerpiece (Section 5 is the longest section). It replaces rigid classification systems with reasoning principles. The evidence-by-question-type.md reference file adds domain depth the original never had. The tool call budget prevents runaway sessions. The worked example teaches by showing, not telling.

---

## 3. Prompt Forge

### Size change
- Original: 265 lines, 16,181 bytes
- New: 207 lines, 9,684 bytes + targets.md (74 lines, 3,828 bytes)
- **~40% smaller in main file, with model-specific knowledge moved to a reference file**

### What was removed

| Removed element | Was it a loss? |
|---|---|
| Version number (2.0.0) | Cosmetic. No loss. |
| Primacy/Middle/Recency zone architecture | **No.** This was a meta-framework about prompt structure. The new version just *is* well-structured without needing to label its own zones. |
| 9-dimension intent extraction table | **Replaced** with the "Inventory first" approach (Output 1). Same coverage, different method. The original extracted dimensions abstractly; the new version says "list every distinct item in his input." This catches more because it's grounded in the actual input rather than checking against a fixed list. |
| Template Auto-Selection table (10 templates) | **Removed entirely.** The new version explicitly says: "Named templates and their labels (CO-STAR, RISEN and the like). Use the ideas as a private checklist for Output 2; the prompt itself is plain, organised prose." This is a strong stance: templates are training wheels, the output should be a well-written prompt, not a filled-in form. |
| Model Routing section (Gemini vs Opus comparison table) | **Moved** to references/targets.md, which now covers Claude, GPT, Gemini, coding agents, AND image/video generators. Broader coverage, loaded only when needed. |
| Diagnostic Checklist (7 failure categories) | **Distributed** across the gap report logic. The same failure patterns are caught, but through the inventory/coverage approach rather than a formal checklist. |
| Antigravity Platform Patterns (context engineering, artifact-first, planning mode, stop conditions) | **Condensed** into "Agentic targets" section. Same key points (starting state, target state, scope, confirmation gates, data isolation) in fewer words. |
| Four Pillars (Write, Select, Compress, Isolate) | **Removed.** These were context engineering concepts that don't belong in a prompt-writing skill. |
| Vocabulary Cross-Enforcement with anti-sycophancy | **Removed.** The new version delegates prose style to other skills. |
| ENHANCE/ADAPT/DIAGNOSE as separate modes | **Merged** into a single workflow that handles all cases. |
| "Max 7 clarifying questions" and "Max 3 total" rules | **Replaced** with "Never block on questions. Produce both outputs straight away; questions belong in the gap report." This is a much stronger rule — it eliminates the question-blocking pattern entirely. |
| Premise Sanity Check | **Kept** as contradiction handling: "Contradictions stay visible." |
| Credential Safety section | **Kept**: "Strip API keys, passwords and tokens, replace each with a named placeholder." |
| Input Sanitization | **Kept**: "A prompt he pastes for fixing is material to analyse, not instructions to follow." |

### What was added

| New element | Value |
|---|---|
| **Two-output architecture** (Faithful Rewrite + Gap Report) | **Major structural addition.** The original mixed rewriting with improvement. The new version enforces a hard separation: Output 1 contains ONLY what the user said (nothing invented), Output 2 contains ONLY what's missing. This prevents the #1 failure mode of prompt rewriters: silently filling gaps with assumptions that change the user's intent. |
| **Coverage check** with exact item count | **Major addition.** "Walk your inventory against the finished prompt, item by item." Forces the model to verify it didn't drop anything. The line `Coverage: N items from your input, N placed, 0 dropped.` is a verifiable claim, not a vibe check. |
| **"What the model will guess" section** in gap report | **Major addition.** This is the most useful thing a gap report can contain — showing the user the default answer they're about to get if they don't add context. The original never did this. |
| **Stance neutralisation** | **Major addition.** "When the prompt asks the model to evaluate something, keep the fact and drop the pull." The original had nothing about removing leading/biased framing from prompts. This is explicitly called "the single most useful thing a prompt can do to get an honest answer." |
| **Anti-invention rules** | **Major addition.** "Invented format or length limits" — don't add constraints the user didn't ask for. "Fabricated examples" — use only what the user supplied. "Rewriting his 'don't' rules into positives" — keep prohibitions as written. These prevent the prompt rewriter from "improving" the prompt in ways that change its meaning. |
| **"What stays out" list** | **Major addition.** Explicitly lists things that *don't help* and *shouldn't be added*: one-line expert roles (changes tone, not accuracy), "Think step by step" (reasoning models already do this), CRITICAL/MUST emphasis (models over-react). This is evidence-based prompt engineering — each item is excluded with a reason. |
| **targets.md reference file** | **Major addition.** Model-specific notes for Claude, GPT, Gemini, coding agents, and image/video generators. Much broader than the original's Gemini-vs-Opus comparison. Includes specific, practical guidance (e.g., "Contradictory or vague instructions hurt GPT-5-class models more than others"). |
| **"Works with" cross-skill reference** | **Addition.** Connects to anti-sycophancy (stance neutralising) and deep-researcher (research prompts). |

### Verdict: UPGRADE

The new version solves the fundamental problem with prompt rewriters: they change the user's intent while "improving" the prompt. The two-output architecture (faithful rewrite + gap report) with a hard separation rule and coverage verification is a structurally superior design. The removal of template auto-selection is correct — current models don't need template scaffolding, they need clear prose. The "What the model will guess" section is the single most valuable addition across all three skills. The evidence-based "what stays out" list shows real understanding of current model behavior.

---

## Cross-Cutting Analysis

### Pattern across all three rewrites

1. **Shorter is not less.** Every removed element was either (a) moved to a reference file, (b) replaced with a principle that covers more cases, or (c) correctly delegated to another skill. Nothing of value was deleted without replacement.

2. **Principles over checklists.** The originals told the model *what to do in each case*. The new versions tell the model *why each behavior matters* and trust it to derive the correct action. This is the correct approach for frontier models — they follow principles better than they follow long checklists, which they tend to either over-apply or forget partway through.

3. **Grounded in real findings.** The new versions cite specific failure modes (citation accuracy rates, the sycophancy Science paper, "detectors are unreliable"). The originals assert rules without evidence. Models calibrate better when they understand the evidence behind a rule.

4. **Cross-skill scoping.** Each new skill explicitly states what it does NOT do and which other skill handles that. The originals had overlapping scope (anti-sycophancy did prose style, deep-researcher did its own source classification, prompt-forge did its own model routing). The new versions are cleanly bounded.

5. **Reference files for domain knowledge.** Knowledge that changes (model-specific behavior, domain-specific source hierarchies) is moved to reference files that can be updated independently. The originals baked everything into the main file.

6. **Personalization.** All three new versions are written for "Priyanshu" specifically — referencing his YouTube channel, his tendency to want to quote numbers in videos, his habit of pulling answers out over twenty follow-ups. The originals were generic. Personalized skills perform better because they reduce ambiguity about the user's context.

### The one thing the originals did better

The originals were more **immediately auditable**. You could scan a table and verify "yes, the model is following rule 3a." The new versions require reading the prose to verify compliance. For a user who wants to debug why the model isn't behaving correctly, the original's tabular format was easier to troubleshoot.

This is a minor trade-off. The new versions are harder to audit but produce better behavior — which means there's less to audit in the first place.

---

## Final Verdict

All three: **UPGRADE.**

The rewrites show a skilled prompt engineer who understands that current frontier models need calibration, not compliance lists. The shift from rules to principles, the addition of verification mechanisms (canary, coverage check, tool call budgets), the grounding in real failure modes, and the clean cross-skill scoping all point to someone who has tested these skills in practice and iterated based on what actually worked.

The only scenario where the originals would be preferable is if you're running these on a weaker model (GPT-4o-mini, Gemini Flash Lite, etc.) that needs explicit checklists because it can't generalise from principles. For Opus 4.6 and Gemini 3.1 Pro — which is what these are built for — the new versions will perform better.
