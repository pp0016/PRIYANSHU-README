# Session Summary — Aug 21-22, 2026

## What Got Done

### 1. Research Phase — COMPLETE
- `research_notes.md` created with 25+ weapons across 7 eras, 14 recommended for video, 6 overused facts to skip, 5 fresh angles
- vidIQ cross-check integrated: 6 agreements, 3 disagreements (Diana = skip, "bans redirect cruelty" = add, structural spine = hybrid)
- vidIQ's closer line saved: "Every weapon on this list was banned after it was used. The one being debated right now might be the first banned before it ever fires a shot."

### 2. vidIQ Files Reviewed
- **`script overview done by vidiq.md`** → should be renamed `beat_map_and_hook.md` (it's a 12-min beat map + hook draft + title scoring + B-roll links, not a "script overview")
- **`banned-weapons-script.md`** → full script draft from vidIQ. Issues found:
  - Macuahuitl "banned their own weapons" claim is historically shaky — needs primary source
  - Bat bomb was CANCELLED, not BANNED — factual error
  - "Here's the thing" / "here's the kicker" = AI tells
  - Second half (synthesis) is thinner than first half
  - Needs `/humanizer` + `/ai-writing-gaps` + `/stop-slop` pass before use

### 3. Weapon Count Decision
- vidIQ's 4 weapons = too few for catalog format
- My 14 weapons = too many for 12 min
- **Decision: 8 weapons** with full treatment + 3 more in Loophole Museum + nukes in synthesis = 11 on screen

### 4. Production Pipeline Decision (from test)
Remotion SVG-only test was garbage. No engagement, no texture, no life.

**Final pipeline:**

| Layer | Tool | Purpose |
|-------|------|---------|
| **Images** | Nano Banana 2 / AI image gen | Generate scene illustrations (stickman art style) — the PRIMARY visual asset |
| **Video clips** | Omni Flash | Short AI-generated video for moments that NEED motion (weapon swings, explosions, impact moments) |
| **Assembly** | Remotion | Fast-paced image animation — Ken Burns zoom/pan, transitions, text overlays, captions, timing to voiceover |
| **Voiceover** | ElevenLabs | Voice carries the storytelling |

**Key insight:** Remotion's value = assembling and animating GOOD assets at speed, not generating assets from scratch. Images first, Remotion animates them, Omni Flash for accent video clips only.

### 5. Files Status

| File | Location | Status |
|------|----------|--------|
| `research_notes.md` | `projects/01_banned_weapons/` | ✅ Done |
| `project_brief.md` | `projects/01_banned_weapons/` | ✅ Exists (research_notes status needs update to "Done") |
| `beat_map_and_hook.md` | vidIQ Downloads (needs rename + move) | ⏳ Not moved yet |
| `banned-weapons-script.md` | vidIQ Downloads (needs revision) | ⏳ Not moved yet |
| `script_v1.md` | `projects/01_banned_weapons/` | ❌ Not started |
| `stikaman-test/` | `youtube/Stickman/` | Created but can be deleted — test served its purpose |

## Next Steps
1. Generate test images (Nano Banana 2) for 2-3 scenes in the stickman art style
2. Use Remotion to animate those images with fast-paced Ken Burns + transitions
3. Use Omni Flash for one short video accent clip
4. Compare the hybrid result — if it looks good, commit to this pipeline
5. THEN write the full script (visual capabilities affect what you can write)
