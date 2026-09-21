# SoulArc Studios — Thumbnail Replication Guide (No Designer Needed)

## The Channel's Thumbnail DNA

![SoulArc Studios Thumbnails](C:/Users/renu5/.gemini/antigravity/brain/2b145ed9-35fe-4974-bd1c-54311bc3cd9c/.user_uploaded/media_1789861487641.png)

**Channel:** @SoulArcStudios • 53.9K subs • Hindi Book Summary / Audiobook niche  
**Niche:** Self-help & psychology book summaries in Hindi  

### Visual Pattern Breakdown

| Element | What SoulArc Does Consistently |
|---|---|
| **Layout** | Split-frame: physical book cover on **left 30-40%**, bold text fills **right 60-70%** |
| **Book Cover** | 3D-angled book mockup, slightly tilted, realistic lighting — NOT a flat scan |
| **Typography** | Massive bold sans-serif, mixed color hierarchy (white + yellow/red accent for key words) |
| **Background** | Dark cinematic gradient — deep navy/black with subtle environmental elements |
| **Color Palette** | Dark base (#0A0A1A) + White text (#FFFFFF) + Yellow accent (#FFD700) or Red accent (#FF2020) |
| **Text Hierarchy** | Article/preposition words small → Key concept words HUGE and colored |
| **Supporting Visual** | Sometimes a brain, silhouette, or thematic image behind/beside the book (Thumbnail 3 has a brain) |
| **Composition** | Z-Pattern — book at left, title cascading right, key word dominates center-right |

---

## Can vidIQ Website Create These? — YES, Here's Exactly How

### Method 1: vidIQ AI Thumbnail Generator (Direct on Website) — ⭐ RECOMMENDED

**Cost:** 22 credits per generation on website

**Step-by-step on vidIQ website:**

1. Go to **vidiq.com → AI Thumbnail Generator** (or access it from any video's tools)
2. Upload **SoulArc's thumbnails as reference images** — this is the key feature
   - The tool has a **"Reference Images"** field that accepts up to 10 images
   - Upload 2-3 of their best thumbnails as references
   - This switches the generator from "Quick Generate" to **"Pro / Improve flow"** which emulates the style and composition
3. Fill in YOUR video's title and description
4. Add a **userQuery** (creative direction) describing exactly what you want

### What to Paste into vidIQ Website's AI Coach (10 credits only)

> [!TIP]
> Instead of using the 22-credit thumbnail generator multiple times, paste this into the **vidIQ AI Coach** on the website for 10 credits to get concepts + prompts you can use anywhere.

---

## 🎯 Ready-to-Use vidIQ AI Coach Prompts

### Prompt 1: "Atomic Habits" Style Thumbnail

```
I run a Hindi audiobook/book summary channel similar to @SoulArcStudios.
I need a thumbnail for my upcoming video:

TITLE: "Atomic Habits | Hindi Audiobook | By James Clear"

THUMBNAIL STYLE TO MATCH:
- SoulArc Studios style: 3D book mockup on left side (30-40% of frame),
  angled slightly with realistic lighting
- Right side (60-70%): massive bold sans-serif text with color hierarchy
- Dark cinematic background (deep navy/black gradient)
- Text hierarchy: small words "of" "your" in white, KEY words "ATOMIC"
  and "HABITS" in bright yellow (#FFD700) and MUCH larger
- Optional supporting visual: a small chain-link or habit-loop icon
  behind the text, subtle and semi-transparent

LAYOUT: Split frame — book left, text right, Z-pattern reading flow
COLOR PALETTE: Background #0A0A1A, primary text #FFFFFF, accent #FFD700
ASPECT RATIO: 16:9 (1280x720)

Please generate this thumbnail concept OR give me the exact prompt
I can use to generate it with your thumbnail AI tool.

ALSO: What are 3 alternative text arrangements that would get
higher CTR for Hindi audiobook thumbnails?
```

### Prompt 2: "Rich Dad Poor Dad" Style Thumbnail

```
I run a Hindi audiobook/book summary channel similar to @SoulArcStudios.
I need a thumbnail for my upcoming video:

TITLE: "Rich Dad Poor Dad | Hindi Audiobook | By Robert Kiyosaki"

THUMBNAIL STYLE TO MATCH:
- SoulArc Studios style: 3D book mockup on left side, angled with
  realistic shadows and lighting
- Right side: massive bold text, stacked vertically
- "RICH DAD" in green (#00CC44) — large, dominant
- "POOR DAD" in red (#FF2020) — equally large, creating contrast
- Small subtitle text below: "HINDI AUDIOBOOK" in white
- Dark background with subtle money/wealth imagery
  (faded dollar signs or gold coins, very subtle)

LAYOUT: Book on left 30%, bold contrasting text on right 70%
COLOR PALETTE: Background #0A0A1A, green text #00CC44, red text #FF2020, white #FFFFFF
ASPECT RATIO: 16:9 (1280x720)

Please generate this thumbnail OR give me the exact creative
direction prompt for your thumbnail AI tool.

ALSO: Should I add "By Robert Kiyosaki" text on the thumbnail
or keep it title-only? What performs better for Hindi book channels?
```

---

## Method 2: Using vidIQ MCP API (Through Antigravity) — For Iteration

If you want to do this through the API instead of the website:

### Step 1: Get Reference Thumbnails
Use `vidiq_channel_videos` to get SoulArc's video IDs, then use those as `referenceImages` in `vidiq_generate_thumbnail`.

### Step 2: Generate with References
```
Tool: vidiq_generate_thumbnail
Parameters:
  - title: "Your Book Title | Hindi Audiobook"
  - referenceImages: [SoulArc thumbnail URLs]
  - userQuery: "3D book mockup on left, massive bold text on right,
    dark cinematic background, color-coded text hierarchy,
    key words in yellow, book summary channel style"
  - orientation: "landscape"
```

### Step 3: Score → Refine Loop
```
Tool: vidiq_score_thumbnail → get feedback
Tool: vidiq_refine_thumbnail → fix weaknesses
Repeat until score > 75
```

> [!IMPORTANT]
> **Credit costs per cycle:**
> - Generate: 22 credits
> - Score: 5 credits  
> - Refine: 22 credits
> - Total per iteration: ~49 credits
> 
> **Recommendation:** Use the website AI Coach (10 credits) to get the concept right FIRST, then use the API for final generation only.

---

## Your Full AI Thumbnail Pipeline (No Designer Needed)

| Step | Tool | Cost | What It Does |
|---|---|---|---|
| 1. Concept | vidIQ AI Coach (website) | 10 credits | Get the layout, colors, text arrangement right |
| 2. Generate | vidIQ Thumbnail Generator | 22 credits | Create the actual image with reference style |
| 3. Score | vidIQ Score Thumbnail | 5 credits | Get CTR prediction + specific feedback |
| 4. Refine | vidIQ Refine Thumbnail | 22 credits | Fix specific issues from scoring |
| 5. Alt: Generate with Opus | ChatGPT / Nano Banana 2 | Free (API cost) | Use the prompt from Step 1 in external generators |

### Total Cost for One Polished Thumbnail: **37-59 credits**

> [!TIP]
> **Credit-saving hack:** After Step 1, take the concept from the AI Coach and paste it into **ChatGPT image generation** or **Nano Banana 2** instead of using vidIQ's 22-credit generator. This gives you unlimited iterations for free (or at API cost). Use vidIQ's `score_thumbnail` (5 credits) at the end to validate.

---

## Key Takeaway

**YES**, vidIQ can create thumbnails matching SoulArc's style — the critical feature is the **`referenceImages`** parameter in the thumbnail generator. When you upload their thumbnails as references, it switches to "Pro Generate" mode and actively emulates the style, composition, and color treatment.

Your best workflow: **AI Coach (concept) → External generator (iterate free) → vidIQ Score (validate)**
