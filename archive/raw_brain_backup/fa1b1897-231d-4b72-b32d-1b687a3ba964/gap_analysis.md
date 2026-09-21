# Prompt-Forge vs. Promptive Sentry: Gap Analysis

> [!IMPORTANT]
> I could NOT read the Chrome extension's actual source code, internal logic, or full documentation. What follows is based on publicly available descriptions, reviews, and the Open VSX listing for the IDE version. **My analysis has blind spots** — see the "What to give me" section at the end.

---

## What Promptive Sentry Does (Reconstructed from Public Sources)

### Browser Extension (Chrome)
1. **Prompt Enhancer** — one-click transformation of vague inputs into structured prompts
2. **Tone Modes** — Business, Creative, Technical, Auto
3. **Refinement Controls** — Balanced, Conservative, Radical (how aggressively it rewrites)
4. **Sentry Memory** — captures conversation context, saves to a 20-slot local vault, reloads into new sessions across platforms (ChatGPT, Claude, Gemini)
5. **Claude Token Monitor** — real-time 5-hour and 7-day usage tracking with pacing guidance
6. **Cross-Platform Context Transfer** — carry context from Claude to ChatGPT to Gemini
7. **Local-First Privacy** — all data stored on device, no cloud sync

### IDE Extension (VS Code / Cursor / Windsurf / Antigravity)
8. **7-Layer Context Engine** — automatic injection of:
   - Active file content (300 lines around cursor)
   - Full imports/dependencies
   - Open tabs (language, unsaved state)
   - Terminal output (recent history)
   - Stack trace (auto-detected errors)
   - Git context (branch, commits, active file diff)
   - Tech stack detection (framework, runtime, test runner, monorepo)
9. **Native Diff Review** — side-by-side comparison of original vs. upgraded prompt before accepting
10. **Zero-Knowledge Architecture** — no local API keys needed, hardened backend proxy

---

## What Prompt-Forge Already Covers Well

| Promptive Sentry Feature | Prompt-Forge Equivalent | Verdict |
|---|---|---|
| Prompt Enhancer (vague → structured) | ENHANCE mode with Diagnostic Checklist | ✅ Covered — and arguably deeper, because your checklist catches 37 specific failure patterns |
| Tone Modes (Business/Creative/Technical) | Template Auto-Selection (RTF, CO-STAR, CRISPE, etc.) | ✅ Covered differently — yours picks by task type not tone, which is more precise |
| Refinement Controls (Conservative/Radical) | Not explicitly present | ❌ Gap |
| Context Management (Sentry Memory) | Context Engineering Principles (Write/Select/Compress/Isolate) | ⚠️ Partial — you describe the theory but have no concrete memory block format |
| Cross-platform support | Model Routing (Gemini vs Opus) | ⚠️ Partial — you route between 2 models, not across platforms |
| Diff review | Not present | ❌ Gap (though less applicable in a skill vs. extension) |
| 7-Layer Context Engine | Antigravity Platform Patterns section | ⚠️ Partial — you mention using workspace context but have no structured extraction protocol |
| Token monitoring | Not present | ❌ Gap |

---

## Gaps: What Prompt-Forge Is Missing

### Gap 1: Refinement Intensity Controls
**What Promptive Sentry has:** Balanced / Conservative / Radical modes that control *how much* the enhancer changes.

**What you're missing:** Your ENHANCE mode has one speed — it runs the diagnostic checklist and rewrites. There's no way for the user to say "just tweak this lightly" vs. "tear it apart and rebuild."

**What to add:** A refinement level parameter in ENHANCE mode:
- **Conservative** — fix only the identified failures, preserve original structure and wording
- **Balanced** — fix failures + restructure for the target model
- **Radical** — rewrite from scratch using the intent, ignoring original structure entirely

---

### Gap 2: Concrete Memory Block / Context Persistence Format
**What Promptive Sentry has:** A structured, saveable "context snapshot" that captures conversation state, project requirements, and custom instructions. Users can reload these into new sessions.

**What you're missing:** Your skill talks about context engineering principles (Write, Select, Compress, Isolate) but never provides a **concrete memory block template** that users can generate, save, and paste into future prompts.

**What to add:** A "Memory Block Generator" mode or template that outputs a standardized block like:
```
<memory_block>
  <project>Project name and one-line description</project>
  <stack>Language, framework, versions, infrastructure</stack>
  <decisions>Key architectural decisions already made</decisions>
  <constraints>Hard constraints that must persist across sessions</constraints>
  <prior_failures>What was tried and didn't work</prior_failures>
  <current_state>Where the project/conversation left off</current_state>
</memory_block>
```
This is one of the biggest gaps. Promptive Sentry's entire "Sentry Memory" feature exists because context loss between sessions is the #1 user pain point, and your skill doesn't address it at all beyond abstract principles.

---

### Gap 3: Multi-Platform Awareness
**What Promptive Sentry has:** Works across ChatGPT, Claude, and Gemini, adapting prompts for each platform's behavior.

**What you're missing:** Your skill only routes between Gemini 3.1 Pro (High) and Claude Opus 4.6 (Thinking). There's no mention of GPT-4o / GPT-4.1, ChatGPT-specific syntax, or other models.

**What to add (if your scope allows):**
- GPT-4o / GPT-4.1 routing rules (system message patterns, tool_choice, JSON mode quirks)
- ChatGPT custom instructions vs. system prompt differences
- Platform-specific syntax: ChatGPT's `#` headers, Claude's XML tags, Gemini's JSON schemas

**Counter-argument:** Your skill is explicitly scoped to Antigravity, where only Gemini and Opus exist. Expanding to ChatGPT/GPT may be scope creep. But if users build prompts *for* those platforms, the gap is real.

---

### Gap 4: Automated Context Extraction (IDE-Aware Prompting)
**What Promptive Sentry has:** The 7-layer context engine that silently gathers active file, imports, open tabs, terminal output, stack traces, git context, and tech stack — and injects it into the prompt.

**What you're missing:** Your Antigravity Platform Patterns section tells the user to "organize context clearly" and "curate context, do not dump everything" — but there's no protocol for *which* context to gather and *how* to structure it for different task types.

**What to add:** A "Context Injection Protocol" section that maps task types to required context layers:

| Task Type | Required Context |
|---|---|
| Bug fix | Error message, stack trace, relevant file, recent git diff |
| New feature | Architecture docs, related existing files, test patterns |
| Code review | Full file, git diff, related tests |
| Refactor | Current implementation, dependency graph, test coverage |

This is the concept behind Promptive Sentry's 7-layer engine, translated into a skill instruction rather than automated code.

---

### Gap 5: Prompt Preview / Before-After Diff
**What Promptive Sentry has:** A diff view showing the original prompt vs. the enhanced version, letting users audit changes before accepting.

**What you're missing:** Your ENHANCE mode outputs the fixed prompt directly. There's no instruction to show what changed and why.

**What to add:** In ENHANCE mode output format, add a "Changes Made" section:
```
🔄 Changes Made:
- [Failure #5] Vague verb → precise operation: "help with" → "refactor"
- [Failure #14] Missing format → added: "3 bullet points, each under 20 words"
- [Failure #20] No scope boundary → added file lock
```
This gives users the same "audit before accept" transparency that Promptive Sentry's diff view provides.

---

### Gap 6: Token / Usage Awareness
**What Promptive Sentry has:** Claude Token Monitor with real-time 5-hour and 7-day usage tracking, pacing guidance.

**What you're missing:** Nothing about token costs, prompt length optimization, or context window management.

**What to add:** This one's debatable. A skill can't monitor API tokens. But you *could* add:
- **Prompt length awareness:** "If the generated prompt exceeds ~2000 tokens, warn the user and offer a compressed version"
- **Context budget allocation:** "For Gemini 3.1 High with 1M context, prioritize: instructions (5%), examples (10%), input data (85%). For Opus with 200K, compress harder."
- **Cost-conscious mode:** A flag that generates the most token-efficient version of the prompt

---

### Gap 7: No ADAPT Mode (for Cross-Platform Porting)
**What Promptive Sentry has:** Works across ChatGPT, Claude, and Gemini with implicit adaptation.

**What you're missing:** Your Mode Detection table lists "ADAPT" as a mode, but there's no dedicated section explaining *how* to adapt a prompt between platforms. The only routing you cover is Gemini ↔ Opus structural differences.

**What to add:** Flesh out the ADAPT mode with concrete translation rules:
- Opus XML tags → Gemini JSON schemas
- ChatGPT system messages → Claude system prompt placement
- GPT function calling → Claude tool_use format
- Platform-specific quirks (GPT's tendency to over-explain, Claude's literal interpretation, Gemini's grounding needs)

---

### Gap 8: Tone / Domain Mode Selection
**What Promptive Sentry has:** Explicit tone selector (Business, Creative, Technical, Auto) that shapes the enhancement style.

**What you're missing:** Your template selection is by *task type* (one-shot, document, creative, logic), not by *domain/tone*. If someone says "enhance this prompt for a business context," there's no explicit tone calibration.

**What to add:** A domain/tone modifier that layers on top of template selection:
- **Business** — formal language, metrics-oriented, executive-friendly structure
- **Technical** — precise terminology, code-heavy, specification-style
- **Creative** — looser structure, personality, voice preservation
- **Conversational** — casual, short, direct

---

## What Prompt-Forge Does Better Than Promptive Sentry

To be fair, your skill has substantial depth that a Chrome extension can't match:

1. **37 specific failure patterns** — Promptive Sentry's enhancer is a black box. Your diagnostic checklist is explicit and teachable.
2. **Agentic prompt engineering** — Stop conditions, HITL gates, scope locks, checkpoint output. Promptive Sentry has zero coverage of autonomous agent prompting.
3. **Prompt injection defense** — Data isolation, untrusted content tagging. Promptive Sentry doesn't address this.
4. **Premise sanity checking** — Catching contradictions in user goals before writing. Promptive Sentry just rewrites.
5. **Model-specific optimization** — Your Gemini vs Opus routing is specific and actionable (lost-in-the-middle, format tax, thinking depth). Promptive Sentry's cross-platform support is surface-level.
6. **Template library** — 13 task-specific templates with concrete examples. Promptive Sentry has one generic "enhance" function.
7. **Anti-sycophancy vocabulary cross-enforcement** — Scanning generated prompts for AI-ism vocabulary before delivery. Promptive Sentry doesn't do this.

---

## Priority Ranking of Gaps

| Priority | Gap | Effort | Impact |
|---|---|---|---|
| 🔴 High | Gap 2: Memory Block Format | Medium | Solves the #1 user pain point (context loss) |
| 🔴 High | Gap 1: Refinement Intensity Controls | Low | Simple addition, high UX improvement |
| 🟡 Medium | Gap 5: Before-After Diff in ENHANCE | Low | Transparency, builds user trust |
| 🟡 Medium | Gap 4: Context Injection Protocol | Medium | Makes context engineering actionable |
| 🟡 Medium | Gap 7: ADAPT Mode Details | Medium | You already list the mode but don't implement it |
| 🟢 Lower | Gap 8: Tone/Domain Modes | Low | Nice to have, not critical |
| 🟢 Lower | Gap 3: Multi-Platform | High | Scope question — may be intentional exclusion |
| ⚪ Skip | Gap 6: Token Monitoring | High | A skill can't do real-time monitoring |

---

## What You Should Give Me to Analyze Deeper

Since I cannot install or run the Chrome extension, here's what would let me do a proper deep analysis:

> [!IMPORTANT]
> ### Materials I Need

1. **Screenshots of every UI panel** — the prompt enhancer interface, the Sentry Memory vault, the Claude Token Monitor, the settings page. Every toggle, dropdown, and mode selector.

2. **Before/after examples** — take 5-10 real prompts, run them through Promptive Sentry's enhancer at each refinement level (Conservative, Balanced, Radical) and each tone (Business, Creative, Technical, Auto). Save the input and output pairs. This tells me the *actual* transformation logic, not just the marketing description.

3. **The extension's `manifest.json`** and any JavaScript source files — Chrome extensions are just HTML/CSS/JS bundles. You can find them at:
   ```
   chrome://extensions/ → enable Developer mode → find the extension → note the ID
   C:\Users\renu5\AppData\Local\Google\Chrome\User Data\Default\Extensions\ikbkijdgnelcijmdkcaaoabmobagakim\
   ```
   The JS files will show the exact prompt templates, transformation rules, and context injection logic the extension uses.

4. **The IDE extension's README and source** — the Open VSX listing has much more detail. The 7-layer context engine documentation would show exactly how they structure injected context.

5. **Saved Sentry Memory blocks** — export a few from the vault so I can see the exact format and structure they use for persistent context.

6. **Any published blog posts or documentation** by the creators (Xenriq Systems) — they likely have detailed technical write-ups explaining their design decisions.

> [!TIP]
> The single most valuable thing you can give me is **#3 — the extension's source files**. Chrome extensions are not compiled. The JavaScript is readable. That would let me reverse-engineer every prompt template, transformation rule, and context format they use, and map each one against your skill line by line.
