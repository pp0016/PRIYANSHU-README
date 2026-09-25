# Audiobook / Book Summary Channel — Implementation Plan
# Status: UNDER EVALUATION — Sept 2026

> Research phase. NOT started. Evaluating viability before committing.
> For risk analysis → read `risk_notes.md` in this folder.

---

## The Idea

### Core Concept
Book summaries — mix of public domain classics + popular copyrighted bestsellers.
- **Length:** 45 minutes to 3 hours per video
- **Languages:** Testing both Hindi AND English to see which grows faster
- **Production:** ~90% AI (AI voice, AI-generated visuals, AI scripts). Manual script quality check only.
- **Monetization:** AdSense + book affiliate links (Amazon etc.) + sponsorships
- **Expansion:** Spotify audio distribution if YouTube works

### Why This Could Work
The format is "content-carries-the-value" — viewers LISTEN, they don't watch. The audio IS the product.
Simple visuals (captions on images, whiteboard style, static backgrounds) are enough because nobody is watching the screen.

### The EnglishAvenuee Proof
@EnglishAvenuee uses the simplest possible format:
- Real human voiceover (NOT AI)
- Captions written on a whiteboard or background image
- No fancy animation, no stock footage, no complex editing
- Earns ~$15k/month

**The key question:** Can I replicate this exact simple format using AI tools (AI voiceover instead of human, same caption-on-background style) and still get monetized without being flagged?

### Inspiration Channels
- @SoulArcStudios
- @LifeUpgrade27
- @AudiobooksArc
- @SwaroopSinghRajput
- @Antidote_thechannel
- @Elite_Audiobooks
- @EnglishAvenuee (human-made, NOT AI — the benchmark for simple format)

---

## Production Pipeline (Per Video — End to End)

```
Step 1: BOOK SELECTION
    → Pick book (check search volume via vidIQ keyword research)
    → Verify no copyright strikes on similar summaries for this book
    → Check if public domain or copyrighted (changes approach)

Step 2: SCRIPT (Day 1)
    → Pull transcripts from 5-10 top competitor videos on the topic
    → Have AI extract the most engaging/high-retention lines from all of them
    → Drop these lines into a proven script structure/format
    → Have AI write new connecting lines for flow and engagement
    → **MANDATORY HUMAN ELEMENT:** Add a "crazy example story" or personal take related to the book to force originality
    → YOU read and quality-check the script manually
    → Run through /humanizer + /ai-writing-gaps + /stop-slop
    → Save as script_v1.md in project folder

Step 3: VOICEOVER (Day 1)
    → ElevenLabs generation (clone YOUR voice or use premium voice)
    → Review for robotic artifacts, re-generate bad sections
    → Save audio file

Step 4: VISUALS (Day 1-2)
    → Simple format: captions over images / whiteboard backgrounds
    → AI-generated background images (Nano Banana / ChatGPT)
    → No complex animation needed — audio carries the value

Step 5: ASSEMBLY (Day 2)
    → Combine voiceover + captions + background images
    → FFmpeg or Remotion assembly
    → Export

Step 6: THUMBNAIL + PUBLISH (Day 2)
    → Thumbnail designed using OUTLIER METHOD (see below)
    → Title + description + tags (vidIQ scored)
    → Upload to YouTube
    → Check "Altered or Synthetic Content" box — ALWAYS, NEVER SKIP
```

---

## Thumbnail Design — Outlier Reverse-Engineering Method (ENFORCED)

> **This method applies to ALL channels, ALL videos, ANY time a thumbnail is being created.**
> Do NOT skip steps. Do NOT jump straight to generating a thumbnail.

### Priyanshu's Idea
Use vidIQ to find all outlier videos on the same TOPIC (not same title — same topic).
Extract every outlier's thumbnail. Fully reverse-engineer everything.
Then create thumbnails that are BETTER than every single outlier thumbnail analyzed.
Minimum bar: better than all existing outlier thumbnails on this topic.

### Execution Steps

```
Step 1: FIND OUTLIERS (vidIQ)
    → Use vidIQ outlier search on the TOPIC of the video
    → Cast wide: include different title variations, angles, phrasings
    → Collect 5-10+ outlier videos minimum

Step 2: EXTRACT THUMBNAILS
    → Use vidIQ similar_thumbnails or manually screenshot each outlier's thumbnail
    → Save all thumbnails for reference

Step 3: REVERSE-ENGINEER EACH THUMBNAIL
    For EVERY outlier thumbnail, document:
    → Composition: layout, focal point, rule of thirds, whitespace
    → Colors: dominant palette, contrast strategy, background
    → Text: what text (if any), font style, size, placement
    → Faces/Emotions: any faces, what emotion, eye direction
    → Objects/Props: key visual elements, scale, positioning
    → Curiosity trigger: what makes a viewer NEED to click?
    → What's hidden/cropped: what is NOT shown that creates curiosity?

Step 4: FIND PATTERNS
    → What do ALL top-performing thumbnails have in common?
    → What's DIFFERENT about the #1 outlier vs the rest?
    → What do ALL outlier thumbnails AVOID? (anti-patterns)

Step 5: DESIGN BETTER THUMBNAILS
    → Generate 3-5 thumbnail concepts that:
      - Use the winning patterns from outlier analysis
      - Fix weaknesses found in existing thumbnails
      - Are BETTER than every thumbnail analyzed — improvements, not copies
    → Each concept must explain WHY it would outperform existing outliers

Step 6: GENERATE
    → Use image generation (Nano Banana, ChatGPT, or vidIQ generate_thumbnail)
    → Generation prompt MUST reference specific insights from the outlier analysis
    → Pick best, refine if needed
```

### Why This Works
- Your baseline for any thumbnail becomes "better than every outlier on this topic"
- Skipping research = guessing = average thumbnails = no clicks
- Every thumbnail is data-informed, not vibes-informed
- Feed all the reverse-engineered data to Opus 4.6 and it knows exactly what to create

### Trigger Words (Agent must activate this workflow on ANY of these)
- "make a thumbnail"
- "thumbnail for [topic]"
- "design a thumbnail"
- "thumbnail ideas"
- "generate thumbnail"
- "CTR image"
- "video cover"
- Any mention of "thumbnail" in a video production context

---

## Research Status

### What's Been Done
- [x] Identified inspiration channels (7 channels)
- [x] Created 8-question vidIQ AI Coach prompt for full niche evaluation
- [x] Researched cash cow channel risks and YouTube policy changes (2025-2026)
- [x] Identified EnglishAvenuee as proof-of-concept for simple format

### What's Next
- [ ] Paste 8-question prompt into vidIQ AI Coach → get keyword data, channel analysis, niche viability
- [ ] Open each inspiration channel with NexLev extension → verify monetization status, RPM, revenue
- [ ] Bring vidIQ response + NexLev screenshots back for cross-check
- [ ] Final verdict: GO or NO-GO on this channel
- [ ] If GO: pick first 5 books, start production

### Key Files
| File | What It Contains |
|------|-----------------|
| `implementation_plan.md` | THIS FILE — the idea, pipeline, thumbnail method, status |
| `risk_notes.md` | YouTube policy risks, copyright risks, cash cow mitigation |
