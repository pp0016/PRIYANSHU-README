# Screenplay Director Manifest: FFmpeg & Remotion Production Capabilities

> **Purpose:** Feed this file directly to an LLM (Claude 3.5/3.7 Sonnet, Opus, Gemini 1.5/2.0 Pro/Flash) as system context or instructions so it writes video screenplays with exact, machine-parseable visual transitions, sound effect cues, and kinetic typography badges.
>
> 🧭 **Quiet Money POV Pipeline Position:**
> - **Placement:** Step 2.5 (Directly between Step 02 Scripting + Step 03 Audio Timestamps, and Step 04 Visuals + Step 05 Assembly).
> - **Input:** Audited script (`projects/[NN]_[topic]/script_v1.md`) + word/sentence timestamp boundaries (`projects/[NN]_[topic]/audio/cut_durations.json`).
> - **Output:** Scene-by-scene production blueprint (`projects/[NN]_[topic]/screenplay.md`).
> - **Why it exists (The Anti-Slop Bridge):** Without a screenplay director, AI channels produce generic slideshow "slop" (static slides with no transitions, blind image prompts, unaligned audio, and generic music). This manifest forces the AI to act as an expert human Video Editor & Director: determining camera transitions (`xfade`), sound design cues (-60ms pre-roll), kinetic typography badges, and composition headroom before images are generated and compiled.

---

## 1. Quick Concept Explanations

### What is Multi-Stream Audio Mixing?
**In Short:** Multi-stream audio mixing is the process of taking several separate audio tracks (e.g., narrator's voiceover, background music, and multiple sound effects) and combining them into a single, polished master audio output.
* **Why it matters:** In FFmpeg, naive mixing causes the narrator's volume to drop drastically (up to -14 dB) whenever sound effects play. The production mixing filter `amix=inputs=N:duration=first:dropout_transition=0:normalize=0,alimiter=limit=0.95` keeps the narrator's voice at constant, broadcast-level volume and prevents distortion.

### What is Audio Sidechain Ducking?
**In Short:** Sidechain ducking is an automatic volume control system where the **background music volume automatically "ducks" (lowers) whenever the narrator speaks**, and smoothly swells back up when the narrator pauses.
* **Why it matters:** It eliminates the need for manual volume keyframes. The narrator's voice remains 100% crisp and intelligible, while the background music keeps the video energetic during pauses.
* **FFmpeg Syntax:** `[bgm][voice]sidechaincompress=threshold=0.08:ratio=6:attack=100:release=350[ducked_bgm]`

---

## 2. Mandatory First Step: Topic-Adaptive Character Wardrobe & Consistent Face Law

> [!IMPORTANT]
> ### 🚨 THE IMMUTABLE CHARACTER LAW (Read Before Writing Any Screenplay):
> When creating a screenplay, **the main character does NOT wear the exact same clothes in every video.**
> 1. **Consistent Face Across All Videos (Zero Face Drift):**
>    - The protagonist's face, hair, and expression are permanent and immutable:
>      - **Hair:** Rich chocolate brown (`#2C1E18`), side-swept wave, neat parting, clean sides.
>      - **Face:** Soft clean contours, natural jawline, smooth chin, calm closed lips, flat cel flesh (`#F3D7C5`), clean black 2D cartoon outlines.
>      - **Expression:** Strictly 100% NEUTRAL, peaceful, calm, unreadable stoic composure ALWAYS (never smiles, smirks, laughs, or cries; supporting cast carries all drama).
> 2. **Topic-Adaptive Wardrobe & Costumes (Story Requirement Rule):**
>    - **EVERY TIME** before generating screenplay scenes, the LLM / Director **MUST FIRST DESIGN THE CHARACTER'S WARDROBE** based on the specific setting, career, social tier, and narrative requirement of the topic video!
>    - *Corporate / Office / Wall Street topics:* Crisp commuter jacket, light blue oxford dress shirt (rolled sleeves), dark slate trousers, minimalist commuter backpack.
>    - *Blue-Collar / Trade / Utility topics:* Rugged utility canvas jacket or flannel over a neutral tee, dark work pants, steel-toe boots.
>    - *Bank / Mortgage / High-Stakes Institutional topics:* Understated dark charcoal unconstructed blazer or minimal tailored collared shirt contrasting a flashy banker's suit.
>    - *College / Young Saver / Early 20s topics:* Neutral collegiate hoodie/crewneck, dark denim, canvas tote.
> 3. **The Default Fallback Rule:**
>    - **When there is no specific career or environmental requirement**, default to the embedded baseline character anchor:
>      - Heavy-gauge oatmeal-cream ribbed knit crewneck sweater (`#EDE8D5`), dark olive relaxed tailored trousers (`#4A5D43`), dark green jade signet ring on left ring finger (`#1A5D3A`). Reference image: `C:\Users\renu5\Downloads\Man_sitting_in_study_2K_20261019183814.jpg`.

---

## 3. Standard Screenplay Tagging Syntax (For LLMs)

When writing screenplays, the LLM must **first output the Episode Protagonist Wardrobe Specification block**, followed by the scene blocks:

```markdown
## EPISODE PROTAGONIST DESIGN SPECIFICATION
* **Core Facial Identity:** 2D cel-shaded male, side-swept dark brown hair, calm observant eyes, neutral stoic expression ALWAYS.
* **Topic-Driven Wardrobe:** [Specify episode-tailored attire, e.g., 'Corporate Commuter: Rumpled sky-blue oxford shirt with rolled sleeves, charcoal chinos, canvas commuter bag'].
* **Environmental Palette:** Muted cream, soft sage, warm oak wood, dark slate.

---

### [SCENE 01 | 00:00.00 - 00:03.50]
* **Visual:** [TRANSITION: zoomin | dur: 0.5s] Split screen showing financial graph crashing. Protagonist in designated episode wardrobe stands calm on left.
* **Typography:** [TYPOGRAPHY: punch | badge: yellow | text: "$40 BILLION"]
* **SFX Cue 1:** [SFX: shutter-modern.wav | at: 00:00.00 | vol: 1.0] (Cold open screenshot snap)
* **SFX Cue 2:** [SFX: whoosh.wav | at: 00:02.40 | vol: 0.8 | offset: -60ms] (Pre-roll for cutaway)
* **Audio Track:** [MUSIC: high-tension-beat | ducking: on]
* **Narrator (Spoken):** "In 2024, this single mistake wiped out forty billion dollars."
```

---

## 4. Complete FFmpeg Visual Transitions Catalog (All 58 `xfade` Filters)

FFmpeg 8.0.1 includes 58 hardware-accelerated transitions via the `xfade` filter. The LLM can specify any transition name below:

```
[TRANSITION: <name> | dur: <seconds>]
```

### A. Dynamic Zooms & Motion Blur (Best for Hook Openers & Fast Pacing)
1. `zoomin` — Rapid push-in zoom through the next clip. (Top choice for high-retention reel hooks).
2. `hblur` — Horizontal directional motion blur whip.
3. `fadefast` — Rapid exponential flash crossfade.
4. `fadeslow` — Slow gradual cinematic crossfade.
5. `distance` — Spatial perspective transform between clips.

### B. Directional Slides (Best for Lateral Argument Progression)
6. `slideleft` — Previous clip pushed left by incoming clip.
7. `slideright` — Previous clip pushed right by incoming clip.
8. `slideup` — Previous clip pushed upward.
9. `slidedown` — Previous clip pushed downward.
10. `smoothleft` — Anti-aliased eased slide to the left.
11. `smoothright` — Anti-aliased eased slide to the right.
12. `smoothup` — Anti-aliased eased slide upward.
13. `smoothdown` — Anti-aliased eased slide downward.

### C. Directional Wipes & Unveils (Best for Revealing Evidence & Documents)
14. `wipeleft` — Crisp horizontal curtain wipe left.
15. `wiperight` — Crisp horizontal curtain wipe right.
16. `wipeup` — Vertical curtain wipe upward.
17. `wipedown` — Vertical curtain wipe downward.
18. `wipetl` — Diagonal wipe from top-left.
19. `wipetr` — Diagonal wipe from top-right.
20. `wipebl` — Diagonal wipe from bottom-left.
21. `wipebr` — Diagonal wipe from bottom-right.
22. `diagtl` — Diagonal angular wipe top-left.
23. `diagtr` — Diagonal angular wipe top-right.
24. `diagbl` — Diagonal angular wipe bottom-left.
25. `diagbr` — Diagonal angular wipe bottom-right.

### D. Geometric Open & Close (Best for Flashbacks & Framing)
26. `circlecrop` — Iris circle shrinking to center.
27. `rectcrop` — Rectangular border shrink.
28. `circleopen` — Circle expands outward from center (classic iris open).
29. `circleclose` — Circle shrinks down to black (classic iris close).
30. `vertopen` — Vertical barn doors parting from center.
31. `vertclose` — Vertical barn doors closing inward.
32. `horzopen` — Horizontal barn doors parting open.
33. `horzclose` — Horizontal barn doors snapping shut.
34. `radial` — Radar clock-sweep reveal.

### E. Dissolves & Fades (Best for Mood Changes & Narrative Holding)
35. `fade` — Standard linear crossfade between two video streams.
36. `fadeblack` — Dip to complete black, then fade up into the next scene.
37. `fadewhite` — Flash to bright white, then fade into the next scene.
38. `fadegrays` — Desaturates to grayscale during crossfade.
39. `dissolve` — Granular dissolve (film cross-dissolve).
40. `pixelize` — Digital 8-bit mosaic pixelation dissolve.

### F. Covers & Reveals (Best for Slide-over Overlays)
41. `coverleft` — New clip slides over existing clip from right to left.
42. `coverright` — New clip slides over existing clip from left to right.
43. `coverup` — New clip slides over existing clip from bottom to top.
44. `coverdown` — New clip slides over existing clip from top to bottom.
45. `revealleft` — Top clip slides away revealing bottom clip underneath.
46. `revealright` — Top clip slides away to the right.
47. `revealup` — Top clip slides away upward.
48. `revealdown` — Top clip slides away downward.

### G. Slices, Squeezes & Winds (Stylized Accents)
49. `squeezeh` — Horizontal accordion squeeze.
50. `squeezev` — Vertical accordion squeeze.
51. `hlslice` — Horizontal left interlocking blind slices.
52. `hrslice` — Horizontal right interlocking blind slices.
53. `vuslice` — Vertical up interlocking blind slices.
54. `vdslice` — Vertical down interlocking blind slices.
55. `hlwind` — Wind-blown dissolve effect to the left.
56. `hrwind` — Wind-blown dissolve effect to the right.
57. `vuwind` — Wind-blown dissolve upward.
58. `vdwind` — Wind-blown dissolve downward.

---

## 5. Complete Remotion Sound Effects Library (31 Verified Assets)

Location: `assets/sfx/<name>.wav` (48kHz Stereo, -18 LUFS broadcast normalized).  
The LLM can cue any sound using: `[SFX: <name>.wav | at: <time> | vol: <0.1-1.2> | offset: <-60ms>]`

### Category 1: Transitions & Camera Moves
| File Name | Duration | Acoustic Character | Screenplay Placement |
| :--- | :--- | :--- | :--- |
| `whoosh.wav` | 0.3s | Fast air displacement | Push-in zooms, quick cuts, text badges flying in. |
| `whip.wav` | 0.4s | High-velocity snap | Fast camera whip pan, topic shifts, chapter cards. |
| `page-turn.wav` | 0.8s | Tactile paper rustle | Revealing leaked emails, dossiers, documents, news clippings. |
| `switch.wav` | 0.3s | Snappy toggle click | Contrasting "What they claimed" vs "What actually happened". |
| `skedaddle.wav` | 3.5s | Cartoon running legs | Rapid time-lapses, hasty corporate exits. |

### Category 2: UI, Accents & Micro-Interactions
| File Name | Duration | Acoustic Character | Screenplay Placement |
| :--- | :--- | :--- | :--- |
| `mouse-click.wav` | 0.2s | Clean mechanical click | Highlighting bullet points, digital UI actions, URL clicks. |
| `shutter-modern.wav` | 0.4s | Crisp DSLR camera snap | Freeze-frame evidence holds, screenshot citations, photo holds. |
| `shutter-old.wav` | 0.6s | Mechanical vintage shutter | Archival black-and-white photos, historical flashbacks. |
| `ding.wav` | 0.9s | Bright high-register chime | Key takeaways, "Aha!" insights, golden rules. |
| `loading-lag.wav` | 1.8s | Dial-up glitch buffering | Explaining overcomplicated tech jargon, bureaucratic lag. |
| `snapchat-notification.wav` | 0.2s | Modern phone alert ping | Leaked text messages, whistleblower DMs, alert banners. |

### Category 3: Impacts, Drops & Braams
| File Name | Duration | Acoustic Character | Screenplay Placement |
| :--- | :--- | :--- | :--- |
| `vine-boom.wav` | 1.1s | Heavy 808 sub-drop | Instant pattern interrupt, shocking revelations, punchlines. |
| `dramatic-boomer.wav` | 1.8s | Cinematic trailer braam | Existential threats, cliffhangers before commercial/chapter cuts. |
| `record-scratch.wav` | 1.0s | Vinyl needle drag stop | Abrupt silence, debunking statements, reality checks. |
| `bone-crack.wav` | 0.7s | Visceral physical crunch | Highlighting catastrophic financial losses or painful errors. |
| `wilhelm-scream.wav` | 1.2s | Classic movie scream | Total collapse, chaotic sell-offs, comedic disaster. |

### Category 4: Reactions & Viral Pattern Interrupts
| File Name | Duration | Acoustic Character | Screenplay Placement |
| :--- | :--- | :--- | :--- |
| `windows-xp-error.wav` | 0.8s | Critical stop chime | Highlighting broken logic, failed schemes, corporate excuses. |
| `yippee.wav` | 1.4s | High-energy cheering | Major breakthroughs, successful milestones. |
| `fah.wav` | 0.5s | Punchy short vocal hit | Comic relief, deadpan narrator delivery. |
| `spongebob-fail.wav` | 2.1s | Sad trombone slide | Broken promises, failed launches, disappointed expectations. |
| `omg-hell-nah.wav` | 2.8s | Vocal disbelief reaction | Shocking corporate audacity or outrageous lies. |
| `price-is-right-fail.wav` | 3.0s | Descending loser horn | Total bankruptcy, market collapse, catastrophic failure. |
| `romance-meme.wav` | 4.2s | Cheesy saxophone riff | Ironic praise, shady corporate partnerships. |
| `anime-wow.wav` | 2.5s | Mind-blown vocal chime | Unbelievable statistics, exponential growth figures. |
| `mac-quack.wav` | 0.4s | Retro system error quack | Absurd misconceptions, obvious blunders. |
| `nelly-ahh.wav` | 1.0s | Viral vocal sigh | Highlighting an awkward or uncomfortable truth. |
| `sanctuary-guardian-what.wav` | 4.8s | Sci-fi freeze-frame stinger | Complete bewilderment: "Wait... what actually just happened?" |
| `minecraft-hurt.wav` | 0.3s | Snappy physical grunt | Minor financial losses, ego checks. |
| `oh-my-god-vine.wav` | 1.1s | Dramatic viral gasp | Unexpected plot twists, sudden betrayal. |
| `illuminati-confirmed.wav` | 5.2s | Eerie mysterious whistle | Hidden conspiracies, secret agreements. |
| `triggered.wav` | 0.5s | Red-flash distorted bass | Extreme outrage, corporate panic, red alerts. |

---

## 6. Remotion Motion Graphics & "Void Canvas" Archetypes

When the screenplay enters stretches without footage, b-roll, or graphics, the LLM can tag one of the 6 Void Archetypes:

```
[TYPOGRAPHY: <archetype> | text: "<string>" | highlight: <yellow|red|neutral>]
```

1. `punch` — High-impact solo keyword or metric (100px Montserrat 900 on `#FFE600` or `#EF4444` badge). Snappy spring damping.
2. `waterfall` — Spoken cadence waterfall: active word pops into yellow at 1.08x scale; inactive words dim to 45% white.
3. `terminal` — Monospace decryption memo in `JetBrains Mono` with blinking cursor (`▋`). Best for leaked emails and code.
4. `escalator` — Vertical list of escalating arguments or chronological steps. As Step 2 enters, Step 1 shifts up and dims.
5. `strikethrough` — Myth debunking: False claim appears, red SVG line strikes through it, and ground truth slams underneath.
6. `odometer` — Rapid numerical counter using cubic easing. Best for dollar amounts, percentages, and death tolls.

---

## 7. Zero-Degradation FFmpeg Execution Rules

When translating the screenplay into render commands, enforce these non-negotiable rules:
* **WinGet Path:** `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe`
* **Video Quality Preservation:**
  * Re-encoding transitions: `-pix_fmt yuv420p -crf 17`
  * Audio overlays without video re-encoding: `-c:v copy`
* **Audio Pre-Roll Offset:** Always place whooshes and whip sounds **1 to 2 frames (33ms to 60ms) before the video cut** so the audio peak hits exactly on the visual contact frame.
