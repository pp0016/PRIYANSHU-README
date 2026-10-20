# Handoff Report: Requirement R2 (Pure Native Visuals) Survey & Architecture

**Agent**: `explorer_survey_cel_1` (Visual & Cel-Boil Explorer)  
**Parent Orchestrator ID**: `0f8e4fb8-a2fa-47ce-8c50-3fd4f7082d53`  
**Working Directory**: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\explorer_survey_cel_1`  
**Target Project**: `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary`  
**Milestone**: Requirement R2 Survey & Specification

---

## 1. Observation

### 1.1 Direct Inspection of `demos/audiobook-summary/js/scene.js`
In `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\js\scene.js`, the following external image dependencies and rendering logic were directly observed:
- **Lines 7**:
  ```javascript
  let ctx, MAIN, LY, IMG = {}, DPR = 1;
  ```
- **Lines 9–17**:
  ```javascript
  const IMAGES = [
    "mafia1.png",
    "man.png",
    "mafia2.png",
    "police.png",
    "gun.png",
    "book.png",
    "car.png"
  ];
  ```
- **Lines 28–38**:
  ```javascript
  const loadImg = (src) => new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => resolve(null);
    img.src = src;
  });

  for (const file of IMAGES) {
    const img = await loadImg('/demos/audiobook-summary/assets/' + file);
    if (img) IMG[file] = img;
  }
  ```
- **Line 54**:
  ```javascript
  MAIN.fillStyle = '#000';
  MAIN.fillRect(0, 0, W, H);
  ```
- **Lines 57–96**:
  ```javascript
  // Fast-paced image switching
  // Brutal engagement: switch every 1.2 seconds for the first 60s, then every 2s
  const switchInterval = t < 60 ? 1.2 : 2.0;
  
  // Hardcoded thematic snaps based on time
  let imgName = IMAGES[Math.floor(t / switchInterval) % IMAGES.length];
  if (t > 15 && t < 25) imgName = "book.png";
  if (t > 56 && t < 61) imgName = "car.png";
  if (t >= 61 && t < 67) imgName = "police.png";
  if (t >= 67 && t < 70) imgName = "mafia1.png";
  if (t >= 70 && t < 77) imgName = "mafia2.png";
  if (t >= 77 && t < 80) imgName = "gun.png";

  const img = IMG[imgName];

  if (img) {
    // scale to fit
    const s = Math.max(W / img.width, H / img.height);
    const w = img.width * s;
    const h = img.height * s;
    
    // Zoom in over the interval
    const progress = (t % switchInterval) / switchInterval;
    const zoom = 1 + progress * 0.15;
    
    MAIN.save();
    MAIN.translate(W / 2, H / 2);
    MAIN.scale(zoom, zoom);
    
    // camera shake on first minute for brutal engagement
    if (t < 60) {
      const shakeX = (Math.random() - 0.5) * 20 * (1 - progress);
      const shakeY = (Math.random() - 0.5) * 20 * (1 - progress);
      MAIN.translate(shakeX, shakeY);
    }

    MAIN.globalAlpha = 1;
    MAIN.drawImage(img, -w / 2, -h / 2, w, h);
    MAIN.restore();
  }
  ```

### 1.2 Direct Inspection of `demos/audiobook-summary/index.html`
In `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\index.html`:
- Background is styled as:
  ```css
  html, body { margin: 0; padding: 0; background: #f4e9d0; overflow: hidden; }
  ```
- Canvas dimensions:
  ```html
  <canvas id="c"></canvas>
  ```
- Demo configuration:
  ```javascript
  window.DEMO = { width: W, height: H, fps: FPS, duration: 30, motionBlur: { samples: 1, shutter: 0.5 } };
  ```
- Fonts loaded:
  - `LXGW Marker Gothic`
  - `Caveat` (weights 600 and 700)
  - `Long Cang`
- Zero external `.png` or `.jpg` images are loaded in `index.html`.

### 1.3 Inspection of Style `05-cel-boil` Library & Primitives
In `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\js\engine.js` (and identical `demos/05-cel-boil/js/engine.js`), the following native primitives are fully implemented and available:
- **Color Palette (`PAL`)**:
  - `PAL.ink = '#1c1613'` (deep Sumi ink)
  - `PAL.red = '#e5402b'` (warm tomato/vermilion)
  - `PAL.yel = '#ffc425'` (sunny marigold yellow)
  - `PAL.cream = '#f4e9d0'` (warm antique paper vellum)
  - `PAL.hi = '#fff6e2'` (paper-white highlight)
  - `PAL.pencil = '#d9573f'` (red col-erase underdrawing)
- **Mathematical & Interpolation Functions**:
  - `mulberry32(seed)` & `N3` (3D Simplex noise generator)
  - `clamp`, `lerp`, `inv`, `sstep`
  - `E` easing library (`lin`, `in2`, `out2`, `in3`, `out3`, `out4`, `io2`, `io3`, `outBack`, `inBack`, `outElastic`)
  - `K(t, keys)`: Piecewise keyframing interpolator
- **Geometry & Splines**:
  - `spline(P, closed, step)`: Centripetal Catmull-Rom spline interpolation
  - `arclen`, `resample`, `prefix` (progressive draw/trim reveal)
  - `circlePts(cx, cy, r, n, rx)`: Elliptical and circular point generators
  - `xf(P, { x, y, r, sx, sy, kx })`: Affine matrix transformations
- **Cel Boiling & Variable-Width Ink Brush**:
  - `boil(pts, seed, amp, scale)`: Pure procedural noise displacement re-seeded per frame/drawing
  - `outline(pts, wfn, caps)`: Polygon contour generator with round caps
  - `inkW(opts)`: Taper, pressure noise, and directional shadow weighting
  - `inkStroke(ctx, P, opts)`: Open hand-inked line drawing
  - `inkLoop(ctx, dense, opts)`: Closed polygon inked loop with split cuts and pen overshoot
  - `fillShape(ctx, dense, color, opts)`: Flat off-register hand-colored cel fill
  - `hatch(ctx, clipPoly, opts)`: Cross-hatching and diagonal pencil shading
  - `Layers` and `blit`: Offscreen layer management

### 1.4 Audio Cues in `audio.py`
In `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\audio.py`, the explicit SFX timestamps are:
- `0.05s`: Paper entrance slide (`sfx.paper('slide')`)
- `1.08s`: Curiosity pop (`sfx.pop('cork')`)
- `3.12s`: Chime (`sfx.ding(note=72)`)
- `8.16s`: Police Siren alert (`police_siren(1.4)`)
- `14.18s`: Deeper science subtle chime (`sfx.blip(note=67)`)
- `16.04s`: Hero Book Slam (`book_slam()`)
- `19.34s`: Gunshot accent (`gunshot(0.7)`)
- `21.86s`: Sparkle chime (`sfx.sparkle(dur=0.5)`)
- `23.36s`: Second Book Slam (`book_slam()`)
- `25.00s`: Swift whoosh (`sfx.whoosh(0.35)`)
- `28.74s`: High bell (`sfx.ding(note=79)`)

### 1.5 Narration Breakdown in `cues.js` (0.00s – 30.00s)
Cues 1 to 42 in `cues.js` span exactly 0.00s to 29.58s:
- `0.00 - 1.08s`: "کیا آپ نے کبھی notice کیا"
- `1.08 - 4.02s`: "...kuch log bina force kiye hi dusron ka trust aur respect gain kar lete hain"
- `4.56 - 8.78s`: "Jabki kuch log ... bina logon ko convince nahi kar paate... aakhir difference kya hai?"
- `9.22 - 12.20s`: "Kya logon ko influence karna sirf achhi communication skills ka game hai?"
- `12.20 - 14.76s`: "Ya iske peeche human psychology ko samajhne ka ek deeper science hai?"
- `15.16 - 18.08s`: "Dale Carnegie ki legendary book: How to Win Friends and Influence People"
- `18.66 - 23.36s`: "Aapko logon ko manipulate karna nahi balki unhe genuinely samajhna aur better relationships build karna sikhati hai"
- `23.36 - 26.14s`: "Is book mein aap jaanenge ki bina argument ke apni baat kaise rakhein"
- `26.14 - 29.58s`: "Criticism ke bina doosron ko improve karne ke liye kaise inspire karna"
- `29.58 - 30.00s`: Outro settle & Chapter 1 teaser

---

## 2. Logic Chain

1. **Premise**: Requirement R2 and Acceptance Criteria specify:
   - "Delete all image imports, preloading, and rendering logic from `scene.js`."
   - "`scene.js` contains zero references or rendering logic for external `.png` or `.jpg` files."
   - "Revert to the pure native `05-cel-boil` text elements, scribbles, and shapes."
   - "Sync the kinetic text exactly to the voiceover timestamps."
2. **Analysis of Current `scene.js`**:
   - `scene.js` currently relies on an array of 7 external images (`mafia1.png`, `man.png`, `mafia2.png`, `police.png`, `gun.png`, `book.png`, `car.png`) which are preloaded in `init()` and drawn using `MAIN.drawImage()`.
   - The canvas background is set to `#000` solely to frame those raster images.
   - Deleting the `IMAGES` array, `loadImg`, `IMG` dictionary, and the `MAIN.drawImage` call will remove 100% of the raster dependencies and fulfill the zero `.png`/`.jpg` acceptance criterion.
3. **Replacement Strategy via Native `05-cel-boil` Primitives**:
   - Instead of static or panning raster cutouts, each scene beat must be rendered using pure vector primitives from `engine.js` on top of a native cream paper canvas (`MAIN.fillStyle = PAL.cream`).
   - The aesthetic requires line boil on twos (12 fps displacement at 24 fps master: `seed = Math.floor(t * 12)`).
   - Each narrative beat in the 30-second summary aligns directly with the audio SFX timestamps in `audio.py`.
4. **Scene Choreography Design**:
   - By creating 10 distinct procedural visual scenes matching the 10 audio SFX timestamps, visual transitions occur every 2.5–3 seconds, preserving high audience retention without relying on external assets.
   - Hero typography rendered with double-ink dropshadows (`PAL.ink` offset behind `PAL.yel` or `PAL.hi`) and scale pop-in transitions (`txtScale = 1 + Math.max(0, 0.2 - dt) * 2`) achieves authentic hand-drawn cel energy.

---

## 3. Caveats

1. **Font Support**:
   - The loaded fonts in `index.html` (`Caveat` and `LXGW Marker Gothic`) excel at Latin (Hinglish/English) and CJK characters.
   - To prevent fallback font ugliness or tofu blocks, all on-screen hero display titles must be rendered in **Hinglish** (as mandated in `ORIGINAL_REQUEST.md`: *"All on-screen typography is translated to Hinglish"*).
2. **Deterministic Time**:
   - `scene.js` must be a pure deterministic function of time `t`. No `Math.random()` should be evaluated without deterministic seeding; instead, use `hs(seed)` or `N3` to ensure reproducible frame rendering across Puppeteer workers.
3. **Audio Duration**:
   - `window.DEMO.duration` in `index.html` is already set to `30`. Audio mixing in `audio.py` cuts to 30.0s. The timeline is calibrated to complete at 30.0s.

---

## 4. Conclusion

Requirement R2 can be completely satisfied with zero architectural compromises:
1. **Complete Removal**: Delete lines 7 (`IMG = {}`), 9–17 (`IMAGES`), 28–38 (`loadImg`), and 57–96 (`drawImage` block) from `demos/audiobook-summary/js/scene.js`.
2. **Native Canvas Ground**: Switch background from `#000` to `#f4e9d0` (`PAL.cream`).
3. **Pure Procedural Primitives**: Implement the 10-beat vector timeline designed below, utilizing `engine.js`'s `inkStroke`, `inkLoop`, `fillShape`, `hatch`, `spline`, and `circlePts`.
4. **Kinetic Typography**: Deploy Hinglish hero kinetic text synced to the exact voiceover cue timestamps and `audio.py` SFX triggers.

### The 10-Beat Kinetic Visual Timeline

| Beat | Time Range | Audio SFX Trigger | Spoken Voiceover Beat | On-Screen Kinetic Hinglish Text | Cel-Boil Vector / Doodle Primitives |
|---|---|---|---|---|---|
| **1** | 0.00s – 1.50s | 0.05s: Paper slide<br>1.08s: Cork pop | "Kya aapne kabhi notice kiya..." | `KYA AAPNE...`<br>**`KABHI NOTICE KIYA?`** | Hand-drawn Magnifying Glass (`inkLoop` lens + `inkStroke` handle), `drawTwinkle` sparks on 1.08s pop, boiling double border. |
| **2** | 1.50s – 4.50s | 3.12s: Ding chime | "...kuch log bina force kiye hi trust aur respect gain kar lete hain" | `BINA FORCE KIYE...`<br>**`TRUST & RESPECT`** | Two dual boiled seals: Red stamp (`PAL.red`) for `TRUST` & Yellow stamp (`PAL.yel`) for `RESPECT`, connected by handshake doodle + 4-point stars. |
| **3** | 4.50s – 9.00s | 8.16s: Police Siren | "Jabki kuch log convince nahi kar paate... aakhir difference kya hai?" | `CONVINCE NAHI HOTE...`<br>**`DIFFERENCE KYA HAI?!`** | Vibrating Giant Question Mark (`spline` + `inkStroke`), red cross-hatch shading (`hatch`), flashing alert concentric rings on siren onset. |
| **4** | 9.00s – 12.20s | 11.76s: Beat tick | "Kya logon ko influence karna sirf communication skills ka game hai?" | `SIRF COMMUNICATION?`<br>**`KA GAME HAI?`** | Two overlapping cartoon speech balloons (`inkLoop` + `fillShape`), questioning dice / game token with corner overshoots. |
| **5** | 12.20s – 15.00s | 14.18s: Sub blip | "Ya iske peeche human psychology ka deeper science hai?" | `HUMAN PSYCHOLOGY...`<br>**`DEEPER SCIENCE`** | Hand-inked brain silhouette (`cloud` / `drawPuff`), 3 orbiting electron rings (`circlePts` + `xf`), golden central core with `drawTwinkle`. |
| **6** | 15.00s – 18.50s | 16.04s: Book Slam | "Dale Carnegie ki legendary book: How to Win Friends and Influence People" | `DALE CARNEGIE`<br>**`HOW TO WIN FRIENDS`**<br>`& INFLUENCE PEOPLE` | Hero 3D Book Cover slamming down at 16.04s (`fillShape` in `PAL.red`, yellow title badge, hatched page edges, radiating speed lines). |
| **7** | 18.50s – 23.36s | 19.34s: Gunshot<br>21.86s: Sparkle | "Manipulate karna nahi, genuinely samajhna aur better relationships..." | `MANIPULATION ❌`<br>➔ **`GENUINE RELATIONSHIPS`** | Heavy red crossed brush strokes (`PAL.red` "X" slash on 19.34s gunshot) morphing into interlocking friendship rings and sparkling heart doodle on 21.86s. |
| **8** | 23.36s – 26.14s | 23.36s: Book Slam<br>25.00s: Whoosh | "...bina argument ke apni baat kaise rakhein" | `IS BOOK MEIN JAANENGE...`<br>**`ZERO ARGUMENTS`** | Two clashing zigzag lightning bolts deflecting into smooth parallel flowing wave ribbons (`spline`), horizontal motion speed lines. |
| **9** | 26.14s – 29.58s | 28.74s: High bell | "...criticism ke bina inspire karna" | `NO CRITICISM`<br>➔ **`INSPIRE KARNA!`** | Rising flame spirit / lightbulb with radiant upward sunburst (`badgeCircles`), golden rays, directional sparks (`drawSpark`). |
| **10** | 29.58s – 30.00s | 29.58s: Living hold | Transition into Chapter 1 | **`HOW TO WIN FRIENDS`**<br>`CHAPTER 1` | Living line boil hold on threes (`seed = Math.floor(f / 3)`), centered title lockup framed by hand-inked borders. |

---

## 5. Verification Method

### 5.1 Verification Commands
Once the implementer updates `scene.js`:
1. **Source Code Cleanliness Check**:
   Confirm that zero references to `.png` or `.jpg` exist in `scene.js`:
   ```powershell
   Get-ChildItem "C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary\js\scene.js" | Select-String -Pattern "\.(png|jpg|jpeg|webp)"
   ```
   *Expected result*: Zero matches found.

2. **Still Frame Generation & Inspection**:
   Generate key test frames across the 10 beats using the render harness:
   ```powershell
   node C:\Users\renu5\Downloads\mg-styles-15-test\1st\harness\render.mjs C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary --stills 1.08,3.12,8.16,14.18,16.04,19.34,21.86,25.0,28.74
   ```
   Inspect the PNG files written to `demos/audiobook-summary/out/stills/` to confirm:
   - Background is warm cream `#f4e9d0` (not black).
   - Pure vector elements (magnifying glass, seals, question mark, brain rings, book cover, spark burst) render crisply.
   - Kinetic Hinglish text is centered and clearly legible.

3. **Full 30-Second Render Verification**:
   ```powershell
   node C:\Users\renu5\Downloads\mg-styles-15-test\1st\harness\render.mjs C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary --pix_fmt yuv420p
   ```
   Check that `demos/audiobook-summary/out/video.mp4` is generated, exactly 30 seconds long, with audio present and yuv420p pixel format.

### 5.2 Invalidation Conditions
The implementation shall be considered invalid if:
- Any `.png` or `.jpg` file path appears anywhere in `scene.js`.
- The background remains black (`#000`) instead of paper cream (`PAL.cream`).
- Visual changes desync from the voiceover timestamps.
- Text uses unrendered font glyphs resulting in missing characters or fallback tofu boxes.
