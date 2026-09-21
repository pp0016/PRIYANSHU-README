# Update agent-reach-skill for Fast Web Extraction

We will update the `/agent-reach-skill` to use the faster `opencli browser` capabilities, specifically the `extract` command, to retrieve full page content as markdown without needing manual clicks or screenshots.

## User Review Required

Please review the proposed changes below. The updated skill will use `opencli browser open <url>` and `opencli browser extract` to dramatically speed up web scraping on any website. 

## Open Questions

None at this time. This approach will fulfill your request to eliminate the long wait times associated with taking multiple screenshots.

## Proposed Changes

### agent-reach-skill

We will overwrite the existing skill file to modernize its instructions.

#### [MODIFY] [SKILL.md](file:///C:/Users/renu5/.gemini/config/skills/agent-reach-skill/SKILL.md)
The new skill instructions will guide the agent to:
1. Use `opencli browser reach open <url>` to open the target website.
2. Use `opencli browser reach extract` to instantly get the page content as markdown.
3. Suggest using `opencli browser reach click <target>` only when necessary (e.g. pagination or specific dynamic actions).
4. Emphasize speed and efficiency over manual screenshot loops.

## Verification Plan

### Manual Verification
Once the skill is updated, you can invoke it by typing `/agent-reach-skill extract https://some-website.com` in your future workflows. It should now execute the extraction rapidly using `opencli`.
