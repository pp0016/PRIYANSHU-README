# Core Rules: Session Persistence (Non-Negotiable)

These rules apply to every session in this workspace.

## RULE 1: If it's not in the repo, it didn't happen
- Every decision, fact about the business/clients/projects, preference stated, plan, draft, and learning gets written to a `.md` file in this repo.
- Never answer "I remember from earlier in the chat". If it matters, it goes in a file.
- Write in plain Markdown that a fresh agent with zero chat history could read and fully understand.

## RULE 2: Repo knowledge structure
Keep this structure (create it if missing):
- `/CONTEXT.md`: Master index.
- `/knowledge/`: One file per topic. Topic file = the truth.
- `/decisions.md`: Dated log: YYYY-MM-DD, decision, reason.
- `/sessions/`: One file per session.
- `/work/`: Actual deliverables (drafts, docs, code, assets).

Session file template:
```markdown
# <Date> <Topic>
## Goal
## What was done
## Decisions made (also copied to decisions.md)
## New knowledge (also merged into knowledge/ and CONTEXT.md)
## Open items / next steps
## Files changed
```
Never delete old knowledge. If something becomes outdated, mark it "SUPERSEDED YYYY-MM-DD by <file>" and keep it.

## RULE 3: Session start (boot)
At the start of every session, before doing any task:
1. `git pull`
2. Read `CONTEXT.md`, then any `knowledge/` files relevant to the task, then the last 3 files in `sessions/`.
3. Work from that context. If the repo contradicts the chat, ask which is correct and update the repo.

## RULE 4: Checkpoint during the session
Chats can crash or be closed without warning. So:
- After every meaningful unit of work, write it to the repo and commit with a clear message.
- Push at least every few checkpoints. Do not wait for the end of the session to save.

## RULE 5: Session end (ALWAYS ask)
When the task is done or I signal I'm finishing, ask exactly:
"Should I SAVE or DELETE this session's work? (Default: SAVE)"

**If SAVE (or no answer):**
1. Write/finish the `sessions/` file.
2. Merge new knowledge into `knowledge/` files and update `CONTEXT.md`.
3. Append decisions to `decisions.md`.
4. `git add`, `git commit -m "session: YYYY-MM-DD <topic>"`, `git push`.
5. Confirm in one short block: files changed, commit hash, push succeeded.

**If DELETE:**
1. Show the list of uncommitted files that will be discarded and wait for confirmation.
2. Revert only the uncommitted changes from this session.
3. Still write a one-line entry in `sessions/` saying the session was discarded and why, then commit and push that line.

## RULE 6: Git safety
- Never force-push. Never rewrite history. Never delete branches.
- If a push fails, tell exact error immediately.
- NEVER commit secrets. Stop and warn if spotted.
