# 🎨 SOP 04: Visual Asset Generation (Quiet Money POV)

> **Purpose:** Batch-generate 550–700 high-impact stickman illustrations for fast-paced, hard-cut POV wealth psychology video editing across a 20–25 minute runtime using Two-Tier Dynamic Visual Pacing.

---

## 1. Visual Style DNA: Quiet Money POV

To maximize emotional resonance, watch time, and second-person immersion, the visual identity pairs **Minimalist 2D Ink-Outline Stick Figures** with **Warm, Culturally American Semi-Realistic Environments**:

* **Canvas / Primary Backgrounds:** Warm, semi-realistic environments grounded in relatable, everyday American settings (suburban living rooms, corporate break rooms, office cubicles, parking lots outside big-box stores, kitchen tables bathed in morning light).
* **Secondary / Conceptual Canvas:** Pure Cream (`#f4e9d0` / `#faf7ee`) or Dark Charcoal Slate (`#0f172a`), reserved strictly for abstract conceptual beats, balance sheets, ledger comparisons, or dramatic inflection points.
* **Line Art:** Solid bold black hand-drawn ink contours (no fuzzy airbrush lines, no 3D uncanny rendering, no photographic face-swapping).
* **Color Accents (Restricted Functional Palette):**
  - **Emerald Green (`#10b981`):** Portfolio growth, quiet compound interest, cash reserves, winning financial moves.
  - **Crimson Red (`#ef4444`):** Consumer debt traps, lifestyle inflation, finance charges, predatory car loans, warning signs.
  - **Cadmium Gold / Warm Amber (`#f59e0b`):** High-net-worth thresholds, treasury yields, private banking assets.
  - **Muted Earth Tones & Grays:** Natural wood finishes, asphalt, domestic interiors providing grounded realism.
* **Character Archetypes & Expression Laws:**
  - *The Protagonist (Consistent Face + Topic-Adaptive Wardrobe):*
    - **Face & Silhouette (Immutable across ALL videos):** 2D cel-shaded male character with neatly styled side-swept dark brown hair (`#2C1E18`), calm observant eyes, natural smooth jawline, and flat cel flesh tones (`#F3D7C5`). Clean black cartoon outlines.
    - **Expression Law (Strictly Stoic):** The protagonist maintains a **NEUTRAL, calm, and unreadable expression ALWAYS**. No smug smirks, no manic grins, no crying. The protagonist is the unflinching stoic emotional anchor.
    - **Topic-Adaptive Wardrobe (Story Requirement Rule):** The protagonist does **NOT** wear the exact same clothes in every video. Before generating images, the attire is adapted to the specific topic and narrative setting defined in `screenplay.md` (e.g., corporate office attire, blue-collar trade gear, institutional meeting blazer, young adult casual wear).
    - **Default Fallback Attire:** When the topic has no specific wardrobe requirement, use the embedded baseline look: heavy-gauge oatmeal cream ribbed knit crewneck sweater (`#EDE8D5`), dark olive tailored trousers (`#4A5D43`), and dark green jade signet ring on the left ring finger (`#1A5D3A`). (Reference: `C:\Users\renu5\Downloads\Man_sitting_in_study_2K_20261019183814.jpg` and `LOCKED_CHARACTER_DNA_CHEAT_SHEET.md`).
  - *The Coworker:* Carries visible corporate exhaustion, envy, confusion, or shock at the protagonist's quiet wealth moves.
  - *The Family Member:* Expresses unsolicited judgment, outdated advice, skepticism, or sudden demands at money milestones.
  - *The Friend:* Projects social pressure, disbelief, growing emotional distance, or reluctant admiration (often financing an illusion of wealth).
  - *The Stranger / Institution:* Makes superficial assumptions about the protagonist based on visible cues (assuming broke due to an older car, or treating with suspicion for paying cash).

---

## 2. Image Density & Two-Tier Dynamic Visual Pacing Formula

For a **20.0 to 25.0 minute video (1,200 to 1,500 seconds)**, images are sequenced across two distinct pacing tiers:

### Tier 1: The 30–45s Hyper-Hook
* **Cut Cadence:** **0.8 to 1.2 seconds per cut** (average **1.0 second**).
* **Function:** Visual assault trapping viewer retention in the critical first 30 seconds. Rapidly contrasts physical real-world artifacts (crumpled debt notice $\rightarrow$ old reliable car key $\rightarrow$ flashy financed truck $\rightarrow$ smartphone green portfolio readout $\rightarrow$ wide-eyed coworker glance).
* **Images Needed:** **35 to 45 images** generated specifically for the opening hook.

### Tier 2: The Narrative Body (0:45 to 25:00)
* **Cut Cadence:** **1.8 to 2.5 seconds per cut** (average **2.2 seconds**). Accelerates back down to 1.0s–1.5s during dramatic tension resets at act pivots.
* **Function:** Maintains lively visual momentum without inducing cognitive fatigue over a 20–25 minute watch session.
* **Images Needed:**
  $$\text{Images (20.0 Min @ 2.2s avg)} \approx \frac{1{,}200 - 35}{2.2} \approx 530 + 35 = \mathbf{565\text{ Images}}$$
  $$\text{Images (25.0 Min @ 2.2s avg)} \approx \frac{1{,}500 - 45}{2.2} \approx 660 + 45 = \mathbf{705\text{ Images}}$$

* **Total Image Count Range:** **550 to 700 images per episode**.
* **Sequential Naming:** Save all generated PNGs sequentially into `projects/[NN]_[topic]/images/`:
  `img_001.png`, `img_002.png`, `img_003.png`, ... `img_NNN.png`.

---

## 3. Screenplay-Driven Image Prompting Protocol (Anti-Slop Directing)

> [!IMPORTANT]
> **Core Directing Rule:** Images are NEVER prompted blindly from raw script text. They are prompted directly from the scene blocks defined in `projects/[NN]_[topic]/screenplay.md` (generated via [`screenplay_director_manifest-part-of-4-or-screenplay-writing-.md`](file:///c:/Users/renu5/Downloads/priyanshu%20readme/youtube/Stickman/finance%20Stickman/screenplay_director_manifest-part-of-4-or-screenplay-writing-.md)).

Each prompt must account for the scene's editorial metadata:
1. **Transition Awareness:** When `[TRANSITION: zoomin]` or `[TRANSITION: slideleft]` is designated, compose with strong center anchors or clear lateral vectors to maximize transition motion impact.
2. **Typography Headroom:** When `[TYPOGRAPHY: punch]` or `[TYPOGRAPHY: odometer]` is called, leave clean negative space (upper quadrant or lateral third) so badges don't collide with character ink art.
3. **Void Canvas Handling:** When the screenplay tags Void Archetypes (`terminal`, `waterfall`, `strikethrough`), no unnecessary static image is generated—the video compiler directly renders the dynamic typography card on slate `#0f172a` or cream `#faf7ee`.
4. **Diegetic Sync with SFX:** When `[SFX: shutter-modern.wav]` or `[SFX: switch.wav]` is cued, prompt extreme close-up evidence shots (receipts, lease contracts, balance graphs).

### Master Prompt Template (Consistent Face + Topic Wardrobe):
> **Reference File:** `LOCKED_CHARACTER_DNA_CHEAT_SHEET.md`  
> **Reference Image:** `C:\Users\renu5\Downloads\Man_sitting_in_study_2K_20261019183814.jpg`

```text
A high-quality 2D cartoon animation still. The scene is cel-shaded, with clean, prominent black outlines and a subdued, muted pastel color palette, primarily featuring soft oatmeal, warm parchment cream, desaturated sage, and olive-charcoal tones. Even, soft flat lighting.

Core Character (Quiet Money Protagonist):
A 2D cel-shaded male character with neatly styled, side-swept dark brown hair and calm, observant eyes. His face is completely peaceful and neutral, projecting effortless financial serenity. [INSERT DESIGNATED WARDROBE FROM SCREENPLAY e.g.: 'He wears a signature heavy-gauge oatmeal cream-colored ribbed knit crewneck sweater, dark olive tailored trousers, and a distinct polished dark green jade signet ring on his left ring finger' OR 'He wears a rumpled light blue oxford shirt with rolled sleeves, dark charcoal chinos, and an understated leather watch'].

Recurring Aesthetic Elements:
linework: precise, elegant, clean black cartoon outlines.
colors: warm neutral pastels, desaturated cream, soft olive, pale gray.
atmosphere: serene, upscale, minimalist, chalky matte feel.

Scenario ([SCENE_NAME]):
[SCENE_ACTION_AND_ENVIRONMENT_DETAILS - keep background colors matched to muted sage, cream, light oak wood, and slate].
```

### Core Scene Archetypes for Quiet Money POV:

1. **The Hyper-Hook Flash Cut (Physical Contrast):**
   ```text
   Minimalist 2D hand-drawn stick figure illustration, clean black ink linework. Extreme close-up on a worn wooden desk: a weathered 2008 car key with a chipped plastic fob resting right beside an unpretentious paper coffee cup. In the blurred background, through an office window, a shiny brand-new lifted black truck is visible in the parking lot. High contrast, warm ambient daylight, 16:9 aspect ratio, no text overlays, no watermarks.
   ```
2. **The Quiet Milestone (Stoic Hero vs Diegetic Numbers):**
   ```text
   Minimalist 2D hand-drawn stick figure illustration, clean black ink style. A quiet stickman with a signature dark grey flat cap sitting at a sunlit suburban kitchen table with a completely neutral, calm expression. He holds a smartphone displaying an illuminated emerald green balance readout of '$100,240'. A half-eaten bowl of cereal sits beside him. Warm domestic morning light, bold black contours, emerald green screen glow, 16:9 aspect ratio, no floating text.
   ```
3. **The Social Friction (Coworker Judgment / Disbelief):**
   ```text
   Minimalist 2D hand-drawn stick figure illustration, clean ink linework. Corporate office breakroom. Our signature stickman in a grey cap sits calmly on a stool with an unreadable, stoic face, eating a packed brown-bag sandwich. Standing over him, a coworker stickman with wide disbelieving eyes and an agitated expression aggressively waves a shiny platinum dealership lease contract. Warm office fluorescent lighting, bold ink outlines, strong character emotional contrast, 16:9 aspect ratio, no text overlays.
   ```
4. **The Bank Desk Discovery (Institutional Mechanism):**
   ```text
   Minimalist 2D hand-drawn stick figure illustration, clean black ink style. Across a polished mahogany desk inside an upscale suburban bank office. Our signature stickman sits upright with a calm, neutral posture. Across the desk, a banker in a sharp suit stares at a computer monitor with furrowed brows and a stunned expression, realizing the protagonist's modest checking account masks a massive six-figure automated brokerage balance. Warm interior lighting, bold black vector lines, 16:9 aspect ratio, no floating headlines.
   ```

---

## 4. Visual Quality Assurance (Anti-Artifact Sweep)

Before passing images into `assemble_video.py`, perform a rapid batch scan:
1. **Character Linework Continuity:** Verify the stickman's signature cap/accessory does not morph shape or disappear across frames.
2. **Facial Stoicism Audit:** Ensure the protagonist never smiles, sneers, or cries. The hero is the emotional anchor.
3. **Zero Floating Headline Text:** Confirm all numbers exist strictly as diegetic UI on surfaces (screens, envelopes, papers) and no giant floating text words appear.
4. **Zero 3D Distortion:** Reject any frame exhibiting uncanny photographic textures, realistic human eyes, or 3D computer graphics.
