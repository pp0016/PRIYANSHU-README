# Editing Style Extraction Prompt — For vidIQ AI Coach

> **How to use:** Copy the prompt below and paste it into the vidIQ AI Coach chat box (the video should already be uploaded/attached). The AI Coach will analyze the video and return a structured editing style breakdown you can hand to any Remotion developer or AI coding agent.

---

## ✂️ Copy Everything Below This Line

```
You are a professional video editor and motion designer who specializes in reverse-engineering editing styles from reference videos. Your job is to watch this video and extract ONLY the editing techniques, visual patterns, and motion design decisions — not the content, topic, or script.

I want to replicate this exact editing style in Remotion (an open-source programmatic video editor built on React). Give me a complete technical breakdown I can hand to a developer.

Analyze and document every one of these categories. Be specific with exact timings, colors, and measurements — not vague descriptions:

**1. CUT RHYTHM & PACING**
- Average shot/scene duration in seconds
- How fast are cuts? (rapid-fire, medium, slow cinematic)
- Is there a pattern? (e.g., starts slow → speeds up at key points)
- Any jump cuts, smash cuts, or L/J cuts?
- Breath gaps between scenes (how many seconds of silence or pause between sections)

**2. TEXT & TYPOGRAPHY**
- What types of text appear on screen? (titles, subtitles, labels, callouts, keywords, stats)
- Font style (serif, sans-serif, bold, thin, handwritten, monospace)
- Approximate font sizes relative to the frame (small corner text vs. large center text)
- Text colors and any outline/shadow/glow effects
- How does text ENTER the screen? (fade in, slide from left/right/bottom, scale pop, typewriter, instant appear)
- How does text EXIT? (fade out, slide away, instant disappear)
- How long does text stay on screen?
- Any text highlight or underline animations?

**3. TRANSITIONS BETWEEN SCENES**
- What transitions are used? (hard cut, cross dissolve, wipe, zoom transition, slide, morph, glitch, swipe)
- Are transitions consistent throughout or do they vary?
- Transition duration (fast snap vs. smooth blend)
- Any custom/signature transitions unique to this video?

**4. MOTION & CAMERA MOVEMENT**
- Any zoom-in or zoom-out effects? How aggressive? (subtle 5% drift vs. dramatic 50% zoom)
- Any pan/slide movements on static images or footage?
- Ken Burns effect on photos/screenshots?
- Screen shake or handheld simulation?
- Any parallax or depth-of-field effects?

**5. COLOR & VISUAL TREATMENT**
- Overall color temperature (warm, cool, neutral)
- Background color (exact hex if possible, or describe: dark navy, pure black, off-white, gradient)
- Any color grading style? (high contrast, desaturated, neon, vintage, cinematic teal-orange)
- Accent colors used for highlights, text, or UI elements
- Any vignette or film grain overlays?

**6. OVERLAYS, GRAPHICS & VISUAL ELEMENTS**
- Any lower thirds, progress bars, chapter markers, or UI-style overlays?
- Icons, emojis, or illustrations — how are they animated?
- Any split-screen layouts or picture-in-picture?
- Background elements (particles, gradients, geometric shapes, subtle patterns)
- Any border/frame/outline effects around footage or images?

**7. B-ROLL & MEDIA HANDLING**
- How is B-roll footage or images introduced? (full screen, floating window, side-by-side, masked shape)
- Rounded corners or straight edges on media?
- Any drop shadow or border on floating media?
- How are screenshots or screen recordings presented? (device mockup, clean crop, with browser chrome)

**8. AUDIO-VISUAL SYNC**
- Do visual cuts sync to music beats?
- Any bass-drop zoom effects?
- Text or graphics appearing on spoken keywords?
- Any visual emphasis when the narrator stresses a point?

**9. INTRO & OUTRO PATTERN**
- How does the video open? (cold open → title card, immediate hook, montage preview)
- Opening animation style and duration
- How does it end? (CTA card, fade to black, loop, abrupt end)
- Any recurring visual motifs or branding elements?

**10. UNIQUE SIGNATURE MOVES**
- What makes this editing style recognizable?
- Any techniques that repeat throughout that define the "feel"?
- What would a viewer point to and say "that's their style"?

FORMAT YOUR RESPONSE AS:
For each category, give me:
- WHAT: The exact technique used
- WHEN: Timestamp examples (MM:SS) showing where it happens
- HOW (for Remotion): Brief technical note on how to implement this in code (e.g., "spring animation with bounce", "CSS translateX with easing", "opacity interpolation over 15 frames")

Do NOT summarize the video's topic, message, or script content. I only want the visual editing DNA. Pretend the video is on mute and in a language you don't understand — focus purely on what you SEE happening on screen.
```

---

## 🎯 What Happens Next

After the AI Coach returns the analysis, you can:

1. **Paste the AI Coach's response into Antigravity** and say:
   > "Convert this editing style breakdown into a reusable Remotion style guide with TypeScript code for spring presets, color palette, typography scale, transition components, and animation utilities."

2. Or use it as a **reference document** every time you edit a new video in Remotion — keeping the same visual DNA across all your videos.

---

*Prompt engineered with Prompt Forge (RISEN template) + Remotion Craft defaults. Optimized for vidIQ AI Coach's multimodal video analysis.*
