# Storage Cleanup Research via NotebookLM & Subagents

You've requested a deep, forensic analysis of what top YouTubers recommend for cleaning Windows storage, utilizing NotebookLM and a swarm of at least 10 subagents to accelerate the process. 

Per your strict instructions, **no files will be deleted**, the `Downloads` folder is strictly off-limits, and all `Antigravity` apps (including version 2.0) will be ignored. I will also strictly enforce the `anti-sycophancy` rules (providing honest counter-arguments to popular cleaning advice).

## Open Questions

> [!IMPORTANT]
> **Authentication Check:** The NotebookLM integration requires you to be logged into your Google account. Have you run `notebooklm login` in your terminal previously, or will I need to prompt you to do so if my initial authentication check fails?

## Proposed Approach

### Phase 1: Data Gathering
1. **YouTube Search:** I will use a dedicated subagent (via the `vidiq` MCP) to search for the most relevant and highly-rated YouTube tutorials on deep-cleaning Windows 11/10 storage.
2. **Notebook Creation:** I will create a new NotebookLM workspace titled "Windows Storage Optimization Research".
3. **Source Import:** I will import the transcripts of the top 5-10 YouTube videos directly into NotebookLM.

### Phase 2: The 10-Agent Swarm Analysis
Once the NotebookLM sources are indexed, I will launch 10 parallel subagents to query the notebook on specific vectors. 

Each subagent will focus on a distinct area:
1. **Agent 1: Windows Component Store (WinSxS) & DISM**
2. **Agent 2: AppData & LocalAppData Caches**
3. **Agent 3: Browser Cache Strategies**
4. **Agent 4: Temp folder and Prefetch safety**
5. **Agent 5: Windows Update Cleanup**
6. **Agent 6: System Restore Points & Shadow Copies**
7. **Agent 7: Hibernation File (hiberfil.sys) & Pagefile**
8. **Agent 8: Unnecessary pre-installed Bloatware**
9. **Agent 9: Storage Sense automation best practices**
10. **Agent 10: Advice Debunker** (Finds advice in the videos that is actually dangerous or outdated)

### Phase 3: Anti-Sycophancy Synthesis
After the 10 subagents report back, I will compile the final recommendations into a clear artifact. 

Crucially, following the `/anti-sycophancy` protocol, the final report will not just blindly agree with the YouTubers. For every major recommendation, I will provide:
*   **The Answer:** What they suggest removing.
*   **The Why:** The technical reason it takes up space.
*   **The Counter-Argument:** Why deleting it might be a bad idea (e.g., performance hits, stability issues).
*   **The Conditions:** When it is actually safe to delete.

## Verification Plan

*   **Dry Run:** I will present the final synthesis to you first.
*   **Zero Deletion:** I will not execute any `del`, `Remove-Item`, or `cleanmgr` commands during this entire run. I will only provide the verified commands for you to review and approve in a subsequent step. 
*   **Boundary Adherence:** All scripts and agents will be strictly instructed to exclude `C:\Users\renu5\Downloads` and `C:\Users\renu5\.gemini\antigravity`.

---
**Please click "Proceed" to approve this plan, or let me know if you want to adjust the focus of the 10 subagents!**
