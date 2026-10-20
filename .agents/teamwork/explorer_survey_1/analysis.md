# Audiobook Summary "05-cel-boil" Reference Specification & Porting Blueprint

**Author:** Explorer Survey 1 (`teamwork_preview_spec_miner`)  
**Date:** 2026-10-10  
**Target Architecture:** Python Manim Engine (`manim-port`)  
**Reference Source:** `C:\Users\renu5\Downloads\mg-styles-15-test\1st\demos\audiobook-summary` (`scene.js`, `engine.js`, `cues.js`, `cues.json`, `audio.py`, `index.html`)  

---

## 1. Executive Summary & Architecture Overview

The reference implementation is a 30.00-second, 24 FPS pure procedural vector animation (1920×1080, 16:9) designed to simulate traditional hand-drawn, boiling ink animation on paper cels. It incorporates zero external raster images (`.png` / `.jpg`), generating 10 distinct visual narrative beats, 12 kinetic Hinglish subtitle banners, and continuous "line boil" displacement via a 3D Simplex noise field.

This document extracts and formalizes the complete technical specification of the JavaScript reference to guide an exact Manim Python port, while explicitly omitting slate labels, exposure counters, peg holes, and the police siren sound effect per project requirements.

---

## 2. Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Visual Beat | Beat 1: Magnifying Glass & Cork Pop | Angled hand-drawn magnifying glass with cream lens, red wood handle, cork pop pulse and 6 radial twinkling sparks at 1.08s | `cx=960, cy=480, t in [0.00, 1.50)` | Rendered vector magnifying glass, pop scale, radial stars | Clamped to bounds if `t` outside range | `scene.js:139-195` |
| 2 | Visual Beat | Beat 2: Dual Seals (TRUST & RESPECT) | Two rotating 16-point starburst seals connected by a ribbon/handshake doodle, with golden ding ripple rings at 3.12s | `cx=960, cy=480, t in [1.50, 4.50)` | Dual red & yellow seals with text, handshake, expanding chime ripples | Clamped rotation and ripple radii | `scene.js:198-276` |
| 3 | Visual Beat | Beat 3: Difference Question & Alert | Giant vibrating question mark with red col-erase under-shadow, cross-hatching, 8 thought ticks, and 3 concentric alert rings | `cx=960, cy=480, t in [4.50, 9.00)` | Boiled question mark, vibration jitter, 3 alert rings, flashing beacons | Vibration amplitude scales with `t` | `scene.js:279-350` |
| 4 | Visual Beat | Beat 4: Communication Game | Two overlapping speech balloons ("TALK TALK..." / "LISTEN?!") and an isometric 3D game die with red pip | `cx=960, cy=480, t in [9.00, 12.20)` | Two speech balloons, 3-face isometric cube, tick sparkles at 11.76s | Fixed dimensions, dynamic boil | `scene.js:354-428` |
| 5 | Visual Beat | Beat 5: Brain Psychology | Hand-inked brain silhouette with sulci fissures, cerebrum hatching, and 3 orbiting atomic rings with traveling electron particles | `cx=960, cy=480, t in [12.20, 15.00)` | Brain vector with drop shadow, 3 angled orbital ellipses, thought sparkles at 14.18s | Particles cycle continuously on `theta` | `scene.js:431-490` |
| 6 | Visual Beat | Beat 6: Hero 3D Book Slam | Heavy 3D hardcover book with red cover, gold embossed frame, pages deck, dangling ribbon, elastic slam bounce and radial speed lines at 16.04s | `cx=960, cy=480, t in [15.00, 18.50)` | 3D book model, typography, 24 radial speedlines, 12 flying sparks | Clamped bounce scale `Math.max(0.1, bounce)` | `scene.js:493-577` |
| 7 | Visual Beat | Beat 7: Manipulation ❌ ➔ Rings | Two-phase transition: Phase A (18.50–21.00s) has red crossed brush strokes with gunshot splatter at 19.34s; Phase B (21.00–23.36s) has interlocking gold/red rings and central heart | `cx=960, cy=480, t in [18.50, 23.36)` | Heavy red X slash / sparks, or dual interlocking rings, heart, sparkle cascade | Temporal conditional switch at `t = 21.0s` | `scene.js:580-635` |
| 8 | Visual Beat | Beat 8: Zero Arguments Ribbons | Two-phase beat: Phase A (23.36–24.60s) clashing red/black lightning bolts; Phase B (24.60–26.14s) 4 flowing wave ribbons, peace dove/shield emblem, speedlines | `cx=960, cy=480, t in [23.36, 26.14)` | Lightning bolts / sparks, or 4 animated wave strokes, emblem with checkmark | Temporal branch at `t = 24.6s` | `scene.js:638-679` |
| 9 | Visual Beat | Beat 9: Inspire Flame Spirit | Cheerful animated flame character bobbing vertically, holding a glowing star aloft, with 14 background sunburst rays and chime burst at 28.74s | `cx=960, cy=480, t in [26.14, 29.58)` | Bobbing flame spirit, arms, eyes, smile, upward sunburst, 8-star chime burst | Continuous trigonometric bobbing | `scene.js:682-756` |
| 10 | Visual Beat | Beat 10: Chapter 1 Outro Lockup | Prestigious engraved plaque frame with 4 corner star flourishes, Dale Carnegie book title lockup, and yellow Chapter 1 teaser badge on living hold | `cx=960, cy=540, t in [29.58, 30.00]` | Outro lockup plaque, gold inner rule, corner stars, title and chapter text | Boils "on threes" (8 FPS displacement) | `scene.js:759-815` |
| 11 | Typography | Kinetic Hinglish Banners | 12 structured 3-line kinetic typography banners displayed inside an inked white pill backing with drop shadow and entrance bounce | `t in [0.00, 29.58)` | Scaled pill box at `y = 870px` containing Kicker, Hero, and Sub text lines | Fallback to final beat if out of range; hidden in Beat 10 | `scene.js:819-972` |
| 12 | Typography | Granular Voiceover Cues | 42 precise audio-synchronized word/phrase cues mapped to TTS timestamps | Voiceover playback timestamps | Mapped dialogue segments | Clamped start/end timestamps | `cues.js:1-43` |
| 13 | Cel Boil | World-Space Simplex Point Jitter | Perturbs vector control points using 3D Simplex noise evaluated at world coordinates, stepped by random seed slice | `pts, seed, amp=2.4, scale=70` | Perturbed polyline points `[x', y']` | Returns copy if `amp == 0` | `engine.js:154-162` |
| 14 | Cel Boil | Frame Stepping ("Twos" / "Threes") | Temporal rate quantization of boiling seed: 12 FPS ("on twos") for beats 1-9, 8 FPS ("on threes") for beat 10 | Time `t` in seconds | Integer `seed` value | `seed = Math.floor(t * 12)` or `Math.floor(t * 8)` | `scene.js:988` |
| 15 | Inking | Variable-Width Stroke Profiler | Generates contour polygon from polyline with pressure noise, calligraphic directional weighting, and endpoint tapering | Polyline `pts`, width function options | Closed outline polygon with round caps | Returns empty array if `pts.length < 2` | `engine.js:166-223` |
| 16 | Inking | Off-Register Cel Registration | Displaces color fill polygons from line art outlines to simulate traditional cel paint misalignment | Fill polygon, `dx=-5, dy=4` | Shifted fill polygon | Bounded by registration parameters | `engine.js:273-279`, `scene.js:16` |
| 17 | Aesthetic | Warm Cream Background & Grain | Paper cel background `#f4e9d0` with 40 procedural horizontal paper tooth / grain marks | Canvas dimensions `1920x1080` | Rendered textured background | Clamped to canvas bounds | `scene.js:991-1001` |
| 18 | Aesthetic | Outer Double Boil Border | Inset triple-line border: outer red 22px stroke, middle cream 12px stroke, inner black 3.5px rule | Canvas boundaries `W=1920, H=1080` | Boiled decorative border frame | Constant inset geometry | `scene.js:85-100` |
| 19 | Audio Track | SFX Synchronization Pipeline | 16 distinct non-looping sound effects synced to visual cues and mixed with 30s trimmed TTS audio | SFX events, TTS MP3 | 30.00s mixed stereo audio (`pcm_s16le`, 48kHz) | Requires FFmpeg mix with exact duration clamping | `audio.py:1-127` |
| 20 | Legacy Element | Corner Slate & Peg Bar (Omit) | Top-left "SC. 05 · AUDIOBOOK SUMMARY", bottom-right "No. XXX · on 2s" and "CEL BOIL", 3 top peg holes | Frame number `f`, seed | Rendered pencil slate & holes | **MUST BE OMITTED in Manim port** | `scene.js:102-134` |
| 21 | Audio Element | Police Siren Sweep (Omit) | 1.4-second synthesized police siren alert at 8.16s in Beat 3 | Synthetic sine chirp at `t = 8.16s` | Audio waveform | **MUST BE REMOVED from Manim audio mix** | `audio.py:15-22, 68` |

---

## 3. Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | Main Render Function | `render(arg1, arg2, arg3)` with undefined or object arguments | Flexible parameter parsing: supports `render(t)` directly as well as harness format `render(ctx, f, t)`. Clamps `t` to `[0.0, 30.0]`. |
| 2 | Point Perturbation | Empty or single-point polyline (`pts.length < 2`) | `arclen` and `outline` gracefully return single point or empty array without crashing. |
| 3 | Catmull-Rom Spline | Non-closed spline with `n < 2` | Returns direct mapping of input points without interpolation. |
| 4 | Closed Polyline Resampling | Collinear or zero-length closed loop | `resample()` checks `tot < 1e-6` and returns first point slice. |
| 5 | Kinetic Banner Measurement | Abnormally long text string | Banner width dynamically adapts via `Math.max(540, maxTextWidth + 120)` ensuring padding is preserved. |
| 6 | Subtitle Banner Visibility | `t >= 29.58s` (Beat 10 outro window) | Kinetic banner drawing is explicitly bypassed (`if (t < 29.58)`); Beat 10 uses its own integrated plaque typography. |
| 7 | Temporal Beat Boundaries | Transition boundary frame (e.g. `t = 1.500s`) | Beats use strict `<` conditions (`t < 1.50`), ensuring zero double-drawing or missing frame gaps across scene transitions. |
| 8 | Book Slam Bounce | `age < 0` (prior to 16.04s) | Bounce scale is strictly locked to `1.0`. At `age >= 0`, piecewise keyframing applies `outBack` easing with elastic overshoot. |
| 9 | Alert Siren Visual Waves | `t < 8.16s` during Beat 3 | Alert rings and flashing beacons are disabled; only base vibrating question mark is drawn. |
| 10 | Manipulation Slash Transition | `t = 21.00s` midpoint of Beat 7 | Instant cut transition from aggressive red X slash (Phase A) to harmonious interlocking rings and heart (Phase B). |

---

## 4. Comprehensive 10-Beat Visual Timeline Specification

The canvas coordinates use an origin `(0, 0)` at the top-left, with positive X rightward and positive Y downward. The stage center for beats 1 through 9 is located at `stageX = 960`, `stageY = 480` (`H / 2 - 60`). Beat 10 is centered at `stageX = 960`, `stageY = 540` (`H / 2`).

### Beat 1: Magnifying Glass & Cork Pop
- **Active Range:** `0.00s <= t < 1.50s` (Duration: 1.50s, Frames: 0–35)
- **Audio SFX Sync:**
  - `0.05s`: Paper slide entrance
  - `1.08s`: Curiosity cork pop (`sfx.pop('cork', 1.0)`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  1. *Lens Glass Fill:* Circle at relative `(-40, -40)`, radius `R = 140px`. Filled with `PAL.hi` (`#fff6e2`), boiled with amplitude `1.5`, registration offset `dx = -2.5, dy = 2`.
  2. *Glass Shine Crescent:* 3-point curved arc `[[-131, -96], [-96, -131], [-40, -140.8]]`. Stroke width `8px`, color `PAL.cream` (`#f4e9d0`), boil amp `1.2`.
  3. *Outer Lens Metal Rim:* Heavy closed contour around lens. Stroke width `9px`, color `PAL.ink` (`#1c1613`), boil amp `2.0`, shadow weight `0.35`.
  4. *Inner Fine Lens Rule:* Inset circle at `(-40, -40)`, radius `R = 126px`. Stroke width `3.5px`, color `PAL.pencil` (`#d9573f`), boil amp `1.2`.
  5. *Handle Ferrule (Metal Connector):* Line segment from `(58, 58)` to `(170, 170)`. Stroke width `24px`, color `PAL.ink`, boil amp `1.5`.
  6. *Handle Grip (Red Wood):* Line segment from `(170, 170)` to `(282, 282)`. Stroke width `30px`, color `PAL.red` (`#e5402b`), boil amp `2.0`.
  7. *End Knob:* Circle at `(282, 282)`, radius `20px`. Fill `PAL.yel` (`#ffc425`), outline stroke width `5.5px`, color `PAL.ink`.
- **Animations & Dynamic Effects:**
  - *Cork Pop Scale Pulse:* Triggered at `1.08s <= t < 1.45s`. Scale factor: `pop = 1 + 0.25 * sin(((t - 1.08) / 0.37) * PI)`. Peak scale is `1.25x` at ~1.26s.
  - *Twinkle Particle Burst:* Active at `t >= 1.08s`, `dt = t - 1.08`. 6 twinkles radiating along `angle = (k / 6) * 2 * PI + dt * 2`, distance `d = 150 + dt * 450px`. Twinkle star radius shrinks as `32 * max(0, 1 - dt * 2)`. Alternating fill colors `PAL.yel` and `PAL.red`.

---

### Beat 2: Dual Boiled Seals: TRUST & RESPECT
- **Active Range:** `1.50s <= t < 4.50s` (Duration: 3.00s, Frames: 36–107)
- **Audio SFX Sync:** `3.12s`: Warm chime / ding C5 (`sfx.ding(note=72)`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  1. *Ribbon / Connection Bar:* Spline connecting seals `[[-230, 20], [-100, 45], [0, 20], [100, 45], [230, 20]]`. Double stroke: base white highlight width `16px` (`PAL.hi`), inner ink rule width `4px` (`PAL.ink`).
  2. *Handshake Center Doodle:* Left hand `[[-45, 12], [-15, 27], [0, 22]]` width `9px` `PAL.ink`; Right hand `[[45, 12], [15, 27], [0, 22]]` width `9px` `PAL.red`.
  3. *Seal 1: TRUST (Left at `(-240, -10)`):*
     - Starburst contour: 16-point star (`rOut = 115px, rIn = 100px`), rotating at `rot1 = (t - 1.5) * 0.15 rad`.
     - Inked drop shadow: offset `(+8, +8)`, fill `PAL.ink`.
     - Main body: fill `PAL.red`, registration offset `(-5, 4)`, outer ink loop width `6.5px`.
     - Inner concentric ring: circle radius `78px`, stroke width `3.5px`, color `PAL.hi`.
     - Text: `"TRUST"` (`LXGW Marker Gothic` 900 36px, `PAL.hi`), `"★ 100% ★"` (`Caveat` 700 20px, `PAL.yel`).
  4. *Seal 2: RESPECT (Right at `(240, -10)`):*
     - Starburst contour: 16-point star (`rOut = 115px, rIn = 100px`), rotating inversely at `rot2 = -(t - 1.5) * 0.15 rad`.
     - Inked drop shadow: offset `(+8, +8)`, fill `PAL.ink`.
     - Main body: fill `PAL.yel`, registration offset `(-5, 4)`, outer ink loop width `6.5px`.
     - Inner concentric ring: circle radius `78px`, stroke width `3.5px`, color `PAL.ink`.
     - Text: `"RESPECT"` (`LXGW Marker Gothic` 900 34px, `PAL.ink`), `"★ EARNED ★"` (`Caveat` 700 20px, `PAL.red`).
- **Animations & Dynamic Effects:**
  - Continuous slow counter-rotation of both starburst seals.
  - *Ding Chime Ripple (t >= 3.12s):* Concentric gold ripple rings expand outward from both seal centers: `rippleR = 120 + dt * 260px`, stroke width fades `max(1, 4 * (1 - dt))`, color `PAL.yel`.
  - *Twinkle Stars:* Center `(0, -80)` radius `42px` `PAL.yel`; Left `(-120, -110)` radius `26px` `PAL.hi`; Right `(120, -110)` radius `26px` `PAL.red`.

---

### Beat 3: Difference Question & Police Alert Siren
- **Active Range:** `4.50s <= t < 9.00s` (Duration: 4.50s, Frames: 108–215)
- **Audio SFX Sync:**
  - `6.80s`: Rising tension sweep alert burst
  - `8.16s`: Police siren frequency sweep (NOTE: Siren is omitted in Manim audio per R3)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  1. *Giant Question Mark Hook:* Control points `[[-65, -160], [-20, -220], [65, -200], [85, -130], [45, -70], [0, -40], [0, 15]]`.
     - Under-shadow stroke: width `28px`, color `PAL.pencil`, boil amp `3.0`.
     - Main ink stroke: width `26px`, color `PAL.ink`, boil amp `2.0`.
     - Hatching: red diagonal line shading inside hook head, gap `14px`, angle `0.6 rad`, stroke width `2.5px`, color `PAL.red`.
  2. *Question Mark Dot:* Circle at relative `(0, 88)`, radius `28px`. Drop shadow offset `(+5, +5)` `PAL.ink`, fill `PAL.red`, outline width `6.5px` `PAL.ink`.
  3. *Radiating Thought Ticks:* 8 radial tick strokes around `(0, -40)` between radii `210px` and `250–270px`. Stroke width `5px`, color `PAL.ink`.
- **Animations & Dynamic Effects:**
  - *Vibration Jitter:* Shake amplitude intensifies: `vibAmp = 2` (4.5–7.0s), `vibAmp = 5` (7.0–8.16s), `vibAmp = 9` (8.16–9.0s). Whole question mark translates randomly by `[-vibAmp, +vibAmp]`.
  - *Alert Waves (t >= 8.16s):* 3 concentric expanding alert rings from `(0, -40)`: `radius = 160 + ((dt * 300 + i * 90) % 360)px`, stroke width `5px`, alternating `PAL.red` and `PAL.yel`.
  - *Flashing Alert Beacons:* Two star twinkles at `(-380, -60)` and `(380, -60)`, radius `45px`, alternating colors between `PAL.red` and `PAL.yel` at `sin(dt * 20) > 0`.

---

### Beat 4: Communication Speech Balloons & Game Die
- **Active Range:** `9.00s <= t < 12.20s` (Duration: 3.20s, Frames: 216–292)
- **Audio SFX Sync:** `11.20s`: Mechanical gear tick (`mechanical_tick()`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  1. *Speech Balloon 1 (Yellow, Left at `(-170, -50)`):*
     - Polygon: `[[-150, -75], [150, -75], [150, 55], [30, 55], [-20, 115], [0, 55], [-150, 55]]`.
     - Drop shadow `(+8, +8)` `PAL.ink`, fill `PAL.yel`, outer loop width `6.5px` `PAL.ink`.
     - Text: `"TALK TALK..."` (`LXGW Marker Gothic` 900 32px, `PAL.ink`).
  2. *Speech Balloon 2 (Red, Right at `(170, 10)`):*
     - Overlapping polygon: `[[-150, -65], [150, -65], [150, 65], [-10, 65], [30, 125], [-40, 65], [-150, 65]]`.
     - Drop shadow `(+8, +8)` `PAL.ink`, fill `PAL.red`, outer loop width `6.5px` `PAL.ink`.
     - Text: `"LISTEN?!"` (`LXGW Marker Gothic` 900 32px, `PAL.hi`).
  3. *Isometric Game Die (Center Bottom at `(0, 110)`):*
     - Cube size `52px`.
     - Top face: vertices `[0, -52], [44.7, -26], [0, 0], [-44.7, -26]`. Fill `PAL.hi`, loop width `5px`, center red pip circle radius `7px` at `(0, -26)`.
     - Left face: vertices `[-44.7, -26], [0, 0], [0, 52], [-44.7, 26]`. Fill `PAL.cream`, hatch lines gap `10px`, angle `0.5 rad`, loop width `5px`.
     - Right face: vertices `[0, 0], [44.7, -26], [44.7, 26], [0, 52]`. Fill `PAL.hi`, loop width `5px`.
- **Animations & Dynamic Effects:**
  - *Beat Tick Sparkle:* At `t >= 11.76s`, a golden twinkle star explodes directly above the die at `(0, 48)`, radius `32px`, fill `PAL.yel`.

---

### Beat 5: Brain Psychology & Orbiting Atomic Rings
- **Active Range:** `12.20s <= t < 15.00s` (Duration: 2.80s, Frames: 293–359)
- **Audio SFX Sync:** `14.18s`: Sub bell blip G4 (`sfx.blip(note=67)`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  1. *3 Orbiting Atomic / Science Rings:*
     - Inclination angles: `-0.6 rad (-34.4°)`, `+0.6 rad (+34.4°)`, `1.57 rad (90°)`.
     - Geometry: Ellipses with major radius `190px`, minor radius `70px`. Stroke width `3.5px`, colors: Ring 0 `PAL.red`, Ring 1 `PAL.yel`, Ring 2 `PAL.ink`.
     - Traveling Electron Particles: Angle `theta = (t - 12.2) * 4.5 + (i * 2 * PI / 3)`. Positions `(190 * cos(theta), 70 * sin(theta))` rotated by ring tilt. Circle radius `11px`, fill `PAL.yel`, outline width `3px`.
  2. *Hand-Inked Brain Silhouette:*
     - 16 control points forming dual cerebral hemispheres `[-15, -115] .. [15, -115]`.
     - Drop shadow `(+8, +8)` `PAL.ink`, body fill `PAL.hi`, red pencil hatch shading on cerebrum (gap `14px`, angle `-0.4 rad`, width `2px`), contour loop width `6.5px`.
     - Center longitudinal fissure: vertical wavy stroke `[[0, -110], [-5, -60], [5, -10], [0, 55]]`, width `5px` `PAL.ink`.
     - Sulci folds: 2 left lateral strokes (width `4px`), 2 right lateral strokes (width `4px`).
- **Animations & Dynamic Effects:**
  - Orbiting electrons cycle along ellipses at angular velocity `4.5 rad/s`.
  - *Thought Sparkle Flash (t >= 14.18s):* Center twinkle star bursts at `(0, -25)`, radius `48 * min(1, dt * 4)px`, fill `PAL.yel`. Flanked by dual white sparkles at `(-80, -40)` and `(80, -40)`, radius `28px`, fill `PAL.hi`.

---

### Beat 6: Hero 3D Book Slam & Impact
- **Active Range:** `15.00s <= t < 18.50s` (Duration: 3.50s, Frames: 360–443)
- **Audio SFX Sync:** `16.04s`: Hero 3D book slam impact (`book_slam()`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  1. *3D Hardcover Book Model:* Dimensions `Wb = 480px, Hb = 310px, Th = 80px`.
     - Pages Deck: Rect `[-228, -75] .. [228, 235]`. Fill `PAL.cream`, horizontal hatching gap `10px`, loop width `5.5px`.
     - Hardcover Drop Shadow: Rect `[-240, -155] .. [240, 155]` offset `(+12, +12)`, fill `PAL.ink`.
     - Hardcover Body: Fill `PAL.red`, heavy outer ink loop width `8px`, shadow weight `0.35`.
     - Gold Embossed Border: Inset rect by `30px`, stroke width `4.5px`, color `PAL.yel`.
     - Silk Bookmark Ribbon: Hanging wavy spline `[[0, -180], [20, -80], [-15, 220], [25, 270]]`, stroke width `16px`, color `PAL.yel`.
     - Cover Typography:
       - `"HOW TO WIN FRIENDS"` (`LXGW Marker Gothic` 900 38px, `PAL.hi`, `y = -55`)
       - `"& INFLUENCE PEOPLE"` (`LXGW Marker Gothic` 700 28px, `PAL.yel`, `y = -12`)
       - `"DALE CARNEGIE"` (`Caveat` 700 26px, `PAL.hi`, `y = 48`)
     - Ribbon Top Twinkle: Position `(0, -215)`, radius `42px`, fill `PAL.yel`.
- **Animations & Dynamic Effects:**
  - *Elastic Slam Bounce:* Prior to `16.04s`, scale is `1.0`. At `age = t - 16.04 >= 0`:
    `K(age, [[0, 1.28], [0.12, 0.94, 'outBack'], [0.24, 1.05], [0.38, 1.0]])`. The book slams downward from scale `1.28` to `0.94`, overshoots to `1.05`, and settles smoothly at `1.0`.
  - *Impact Shockwave (0 <= age < 0.9s):*
    - 24 radial speedlines erupting outwards: inner radius `240px`, outer radius `220 + age * 850px`, stroke width `9px`, color `PAL.ink`.
    - 12 flying sparks shooting radially: distance `230 + age * 650px`, size `9px`, alternating `PAL.red` and `PAL.yel`.

---

### Beat 7: Manipulation ❌ Slash ➔ Interlocking Friendship Rings
- **Active Range:** `18.50s <= t < 23.36s` (Duration: 4.86s, Frames: 444–560)
- **Audio SFX Sync:**
  - `19.34s`: Gunshot crack accent (`gunshot(0.7)`)
  - `21.86s`: Celebration sparkle chime (`sfx.sparkle(dur=0.55)`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  - **Phase A (18.50s <= t < 21.00s): Aggressive Manipulation Slash**
    1. *Red Brush X-Slash:* Two heavy intersecting strokes: `[[-240, -110], [240, 110]]` and `[[240, -110], [-240, 110]]`. Stroke width `26px`, color `PAL.red`, boil amp `2.5`.
    2. *Gunshot Splatter (t >= 19.34s):* 10 spark particles exploding outward from center, `distance = 110 + dt * 480px`, size `8px`, color `PAL.red`.
  - **Phase B (21.00s <= t < 23.36s): Friendship Rings & Heart**
    1. *Interlocking Rings:* Radius `90px`. Left ring at `(-70, 0)` with gold outer stroke width `8px` (`PAL.yel`) and black inner loop width `3px`. Right ring at `(70, 0)` with red outer stroke width `8px` (`PAL.red`) and black inner loop width `3px`.
    2. *Central Hand-Inked Heart:* Located at ring intersection `(0, 0)`. 6 control points `[[0, -25], [28, -60], [55, -35], [0, 25], [-55, -35], [-28, -60]]`. Fill `PAL.red`, outline width `5.5px` `PAL.ink`.
    3. *Sparkle Chime Cascade (t >= 21.86s):* Golden star at `(0, -85)` radius `42px` `PAL.yel`, left star at `(-140, -50)` radius `30px` `PAL.hi`, right star at `(140, -50)` radius `30px` `PAL.yel`.

---

### Beat 8: Zero Arguments & Smooth Flowing Ribbons
- **Active Range:** `23.36s <= t < 26.14s` (Duration: 2.78s, Frames: 561–627)
- **Audio SFX Sync:**
  - `23.36s`: Tactile page turn & open book spread foley
  - `24.20s`: Sticker slap 1 hit (`sfx.sticker_slap(seed=11)`)
  - `25.00s`: Directional gesture whoosh (`sfx.whoosh(0.35, 'heavy')`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  - **Phase A (23.36s <= t < 24.60s): Clashing Lightning**
    1. *Clashing Zigzags:* Left bolt `[[-260, -50], [-150, -10], [-190, 25], [-80, 60]]` width `14px` `PAL.red`; Right bolt `[[260, 50], [150, 10], [190, -25], [80, -60]]` width `14px` `PAL.ink`. Central impact spark at `(0, 0)` radius `35px` `PAL.yel`.
  - **Phase B (24.60s <= t < 26.14s): Peaceful Flow & Shield**
    1. *4 Parallel Wave Ribbons:* Y-offsets `[-50, -15, 20, 55]`. Spline control points `[-380, y + sin(t*8+i)*15], [-180, y - sin(t*8+i)*20], [80, y + sin(t*8+i)*20], [380, y - sin(t*8+i)*15]`. Alternating width `8px` `PAL.yel` and `PAL.ink`.
    2. *Peace Emblem / Shield:* Circle at `(0, 0)`, radius `75px`. Fill `PAL.hi`, outline width `6px`.
    3. *Peace Checkmark / Olive Branch:* Polyline `[[-30, 0], [-8, 25], [35, -20]]`, stroke width `7px`, color `PAL.red`.
    4. *Radial Whoosh Lines:* 10 speed lines from radius `95px` to `140px`, stroke width `4px`, color `PAL.yel`.

---

### Beat 9: Rising Flame Spirit & Upward Sunburst
- **Active Range:** `26.14s <= t < 29.58s` (Duration: 3.44s, Frames: 628–709)
- **Audio SFX Sync:**
  - `26.20s`: Sticker slap 2 hit (`sfx.sticker_slap(seed=22)`)
  - `28.20s`: Hero shimmer bloom G5 (`sfx.shimmer_hit('G5')`)
  - `28.74s`: Hero star flourish high bell G5 (`sfx.ding(note=79)`)
- **Center Origin:** `(960, 480)`
- **Visual Elements:**
  1. *Upward Sunburst Rays:* 14 radial rays fanning across upper semicircle `[-PI, 0]`. Inner radius `90px`, outer radius `280–310px`. Stroke width `6px`, color `PAL.yel`.
  2. *Flame Spirit Character (Height ~105px):*
     - Continuous vertical floating bob: `bob = sin(t * 11) * 9px`.
     - Outer flame contour: 8 spline control points `[[0, 15], [30, -10], [38, -45], [18, -75], [0, -105], [-18, -75], [-38, -45], [-30, -10]]`. Fill `PAL.red`, outline width `6px`.
     - Inner flame core: 6 spline control points, fill `PAL.yel`.
     - Eyes: Dual ink circles (radius `5px`) at `(-10, -42)` and `(10, -42)`.
     - Wide Smile: Inked arc `[[-8, -30], [0, -25], [8, -30]]`, stroke width `3.5px`.
     - Waving Arms: Left arm `[[-26, -35], [-45, -55 + sin(t*12)*10]]` width `5px`; Right arm `[[26, -35], [48, -65 - cos(t*12)*10]]` width `5px`.
     - Held Star: Glowing star atop right arm at `(52, starY)`, radius `34px`, fill `PAL.hi`.
- **Animations & Dynamic Effects:**
  - Character bobs at `1.75 Hz`, waving arms with trigonometric rhythm.
  - *High Bell Chime Cascade (t >= 28.74s):* 8 twinkles burst outward from the held star: distance `d = 60 + dt * 380px`, radius `24px`, alternating `PAL.yel` and `PAL.hi`.

---

### Beat 10: Prestigious Chapter 1 Outro Lockup & Living Hold
- **Active Range:** `29.58s <= t <= 30.00s` (Duration: 0.42s, Frames: 710–719)
- **Audio SFX Sync:** `29.00s`: End hold audio decay
- **Center Origin:** `(960, 540)` (Exact Screen Center)
- **Visual Elements:**
  1. *Prestigious Plaque Frame:* Dimensions `Pw = 680px, Ph = 360px`.
     - Inked drop shadow offset `(+10, +10)`, fill `PAL.ink`.
     - Plaque body: Fill `PAL.hi` (`#fff6e2`), outer ink loop width `7px` `PAL.ink`.
     - Inner Gold Filigree Rule: Inset frame scaled `0.92 x 0.88`, stroke width `3.5px`, color `PAL.yel`.
     - 4 Corner Star Flourishes: Located at `(+-(340 - 45), +-(180 - 45)) = (+-295, +-135)`. Radius `26px`, fill `PAL.red`.
  2. *Outro Typography:*
     - `"★ DALE CARNEGIE ★"`: `Caveat` 700 28px, `PAL.pencil` (`#d9573f`), `y = -95`.
     - `"HOW TO WIN FRIENDS"`: `LXGW Marker Gothic` 900 48px, `PAL.ink`, `y = -40`.
     - `"& INFLUENCE PEOPLE"`: `LXGW Marker Gothic` 900 36px, `PAL.red`, `y = 10`.
  3. *Chapter 1 Teaser Badge:*
     - Rectangular pill `bw = 280px, bh = 55px` at `y = 75`. Fill `PAL.yel`, outline width `4.5px` `PAL.ink`.
     - Text: `"CHAPTER 1: THE SECRET"` (`LXGW Marker Gothic` 900 26px, `PAL.ink`, `y = 84`).
- **Animations & Dynamic Effects:**
  - Living hold boiling at "on threes" (`seed = Math.floor(t * 8)`), producing an organic hand-inked shimmer. Subtitle banners are hidden.

---

## 5. Kinetic Hinglish Subtitle System Specification

### 5.1 Structured Kinetic Banners (`KINETIC_BEATS`)
The reference subtitles use an on-screen lower-third pill-shaped banner centered at `x = 960px, y = 870px` (`H - 210px`).

| Beat # | Time Range (s) | Kicker Line (Red Pencil) | Main Hero Line (Bold Inked) | Subtitle Line (Red Pencil) | Hero Acc Color |
|---|---|---|---|---|---|
| 1 | 0.00 – 1.50 | `KYA AAPNE...` | `KABHI NOTICE KIYA?` | `Audiobook Summary Hook` | `PAL.yel` (`#ffc425`) |
| 2 | 1.50 – 4.50 | `BINA FORCE KIYE...` | `TRUST & RESPECT` | `Logon Ka Dil Jeetna` | `PAL.hi` (`#fff6e2`) |
| 3 | 4.50 – 7.00 | `JABKI KUCH LOG...` | `CONVINCE NAHI HOTE` | `Baat Kyun Nahi Banti?` | `PAL.yel` (`#ffc425`) |
| 4 | 7.00 – 9.00 | `AAKHIR DONO MEIN...` | `DIFFERENCE KYA HAI?!` | `The Real Difference` | `PAL.red` (`#e5402b`) |
| 5 | 9.00 – 12.20 | `SIRF COMMUNICATION SKILLS?` | `KA GAME HAI?` | `Communication Vs Psychology` | `PAL.yel` (`#ffc425`) |
| 6 | 12.20 – 15.00 | `YA PHIR ISKE PEECHE...` | `HUMAN PSYCHOLOGY KA SCIENCE` | `A Deeper Science` | `PAL.hi` (`#fff6e2`) |
| 7 | 15.00 – 18.50 | `DALE CARNEGIE KI LEGENDARY BOOK` | `HOW TO WIN FRIENDS` | `& INFLUENCE PEOPLE` | `PAL.yel` (`#ffc425`) |
| 8 | 18.50 – 21.00 | `LOGON KO MANIPULATE KARNA NAHI...` | `MANIPULATION ❌` | `Dhoka Ya Asli Rishte?` | `PAL.red` (`#e5402b`) |
| 9 | 21.00 – 23.36 | `BALKI UNHE SAMAJHNA AUR...` | `GENUINE RELATIONSHIPS ❤` | `Build Real Connections` | `PAL.hi` (`#fff6e2`) |
| 10 | 23.36 – 26.14 | `IS BOOK MEIN JAANENGE...` | `ZERO ARGUMENTS 🕊️` | `Bina Vivaad Ke Apni Baat Rakhein` | `PAL.yel` (`#ffc425`) |
| 11 | 26.14 – 29.58 | `CRITICISM KE BINA...` | `INSPIRE KARNA! ✨` | `Inspire Others To Improve` | `PAL.hi` (`#fff6e2`) |
| 12* | 29.58 – 30.00 | `HOW TO WIN FRIENDS` | `CHAPTER 1: COMING UP` | `Next Video Teaser` | `PAL.yel` (`#ffc425`) |

*\*Note: Beat 12 is superseded by Beat 10's full-screen plaque outro lockup in `scene.js`.*

### 5.2 Banner Styling & Geometry
- **Position:** Screen bottom center `(960, 870)`.
- **Dimensions:** Height `145px`. Width dynamic: `Math.max(540, maxTextWidth + 120px)`.
- **Pill Layers:**
  1. *Drop Shadow:* Offset `(+8, +8)`, fill `PAL.ink` (`#1c1613`), boiled with amplitude `1.5`.
  2. *Body Fill:* Fill `PAL.hi` (`#fff6e2`), registration offset `dx = -2.5, dy = 2`, boiled with amplitude `1.8`.
  3. *Inked Contour:* Heavy stroke width `5.5px`, color `PAL.ink`, boil amp `1.8`, shadow weight `0.3`.
- **Entrance Pop Animation:**
  - Upon each cue transition (`dt = t - beat.start < 0.22s`):
    `pop = 1 + (0.22 - dt) * 1.4`. Scale springs down from `1.308x` to `1.0x` within 220 ms.
- **Living Text Boil Jitter:**
  - Random position perturbation applied per boil frame:
    `tx = (hs(seed, 91) - 0.5) * 4px`, `ty = (hs(seed, 92) - 0.5) * 4px`.
- **Typography Hierarchy:**
  1. *Kicker Line (Top):* Font `700 24px "Caveat"`, color `PAL.pencil` (`#d9573f`), at `ty - 42px`.
  2. *Hero Line (Middle):* Font `900 54px "LXGW Marker Gothic"`. Drop shadow `rgba(28, 22, 19, 0.25)` offset `(+4, +4)`, main fill `PAL.ink`, at `ty`.
  3. *Sub Line (Bottom):* Font `600 22px "Caveat"`, color `PAL.pencil` (`#d9573f`), at `ty + 42px`.

### 5.3 Granular Speech Cues (`cues.js`)
For fine-grained mouth/word sync reference, `cues.js` contains 42 granular transcript segments:
1. `0.00 – 0.48`: "Kya aapne"
2. `0.48 – 1.08`: "kabhi notice kiya"
3. `1.08 – 1.50`: "hai ki kuch"
4. `1.50 – 2.02`: "log bina force"
5. `2.02 – 2.60`: "kiye hi dusron"
6. `2.60 – 3.12`: "ka trust aur"
7. `3.12 – 3.70`: "respect gain kar"
8. `3.70 – 4.02`: "lete hain?"
9. `4.56 – 5.06`: "Jabki kuch"
10. `5.06 – 5.80`: "log sahi baat"
11. `5.80 – 6.38`: "keh kar bhi"
12. `6.38 – 6.86`: "logon ko convince nahi"
13. `6.86 – 8.16`: "kar paate hain. Aakhir"
14. `8.16 – 8.78`: "difference kya hai?"
15. `9.22 – 9.96`: "Kya logon ko"
16. `9.96 – 10.80`: "influence karna sirf"
17. `10.80 – 11.76`: "achi communication skills"
18. `11.76 – 12.20`: "ka game hai?"
19. `12.20 – 12.90`: "Ya iske peeche"
20. `12.90 – 13.70`: "human psychology ko"
21. `13.70 – 14.18`: "samajhne ka ek"
22. `14.18 – 14.76`: "deeper science hai?"
23. `15.16 – 16.04`: "Dale Carnegie ki"
24. `16.04 – 16.70`: "legendary book How"
25. `16.70 – 17.16`: "to Win Friends"
26. `17.16 – 18.08`: "and Influence People"
27. `18.66 – 19.34`: "aapko logon"
28. `19.34 – 19.96`: "ko manipulate karna"
29. `19.96 – 20.84`: "nahi balki unhe"
30. `20.84 – 21.86`: "genuinely samajhna aur"
31. `21.86 – 22.66`: "better relationships build"
32. `22.66 – 23.36`: "karna sikhati hai."
33. `23.36 – 24.32`: "Is wonderful book"
34. `24.32 – 25.00`: "mein hum jaanenge ki"
35. `25.00 – 25.72`: "bina argument ke"
36. `25.72 – 26.14`: "apni baat kaise"
37. `26.14 – 27.48`: "rakhein, criticism"
38. `27.48 – 28.12`: "ke bina dusron"
39. `28.12 – 28.74`: "ko improve karne"
40. `28.74 – 29.08`: "ke liye kaise"
41. `29.08 – 29.58`: "inspire karein."

---

## 6. Procedural Cel-Boil Engine Specification

### 6.1 The Noise Field & Math Formulation
The boil algorithm in `engine.js` creates an organic, turbulent displacement field across 2D Euclidean canvas space:

$$\mathbf{p}' = \mathbf{p} + \text{amp} \cdot \begin{bmatrix} N_3\left(\frac{x}{\text{scale}}, \frac{y}{\text{scale}}, z\right) \\ N_3\left(\frac{x}{\text{scale}} + 41.3, \frac{y}{\text{scale}} - 17.9, z\right) \end{bmatrix}$$

Where:
- $N_3(u, v, w)$ is 3D Simplex noise seeded deterministically with PRNG `mulberry32(0x5eed1e)`.
- Spatial Frequency Scale: $\text{scale} = 70.0\text{ px}$. This ensures smooth spatial correlation across adjacent vertices.
- Temporal Slice: $z = \text{seed} \times 2.371 + 0.5$. Because $z$ advances by $2.371$ per boil step, successive boil states sample completely uncorrelated noise slices.
- Orthogonal Decorrelation: The Y displacement samples coordinates shifted by $(+41.3, -17.9)$ to prevent diagonal vector shearing.

### 6.2 Frame Rate & Boil Stepping ("On Twos" / "On Threes")
- Master Output: 24.0 FPS ($T_{\text{frame}} = 1/24\text{ s}$).
- Action Beats 1–9 (`t < 29.58s`): $\text{seed} = \lfloor t \times 12 \rfloor$.
  - Generates 12 unique noise seeds per second.
  - Updates every 2 master video frames (animating "on twos").
- Living Hold Beat 10 (`t >= 29.58s`): $\text{seed} = \lfloor t \times 8 \rfloor$.
  - Generates 8 unique noise seeds per second.
  - Updates every 3 master video frames (animating "on threes").

### 6.3 Polyline Inking & Stroke Width Profiler
In the Canvas2D implementation, lines are resampled every $3.2\text{ px}$ and expanded into outline ribbons using:
$$w(s) = w_0 \cdot \left[1 + \text{jit} \cdot N_3\left(\frac{s}{60}, \text{seed} \times 1.37, 3.1\right)\right] \cdot \left[1 + \text{heavy} \cdot \max(0, \mathbf{n} \cdot \mathbf{l})\right] \cdot \text{taper}(s)$$
- $\text{jit} = 0.35$ (pressure hand tremor along curve length $s$).
- $\mathbf{l} = (0.55, 0.83)$ (calligraphic down-right pen pressure angle).
- $\text{taper}(s)$: Smoothstep taper at start ($t_0 = 14\text{ px}$) and end ($t_1 = 26\text{ px}$) to minimum ratio $0.25$.

### 6.4 Off-Register Cel Registration Offset
To emulate vintage multi-cel animation setups where hand-painted cel paint is slightly misaligned with ink outlines:
$$\mathbf{p}_{\text{fill}} = \text{boil}(\mathbf{p}, \text{seed} + 0.5) + \begin{bmatrix} -5.0 \\ +4.0 \end{bmatrix}$$
Fills use offset $(dx = -5, dy = +4)$ and an independent seed slice ($\text{seed} + 0.5$).

### 6.5 Manim Porting Architecture Mapping
In Manim Community Edition, this effect should be implemented as follows:
1. **Vector Point Perturbation Updater:**
   Attach an updater to each `Mobject` or composite `VGroup`:
   ```python
   def cel_boil_updater(mobject, dt):
       t = scene.renderer.time  # or frame tracker
       seed = int(t * 8) if t >= 29.58 else int(t * 12)
       z = seed * 2.371 + 0.5
       # Perturb mobject.points relative to original cached base_points
       pts = mobject.base_points
       dx = amp * noise3d(pts[:, 0] / 70.0, pts[:, 1] / 70.0, z)
       dy = amp * noise3d(pts[:, 0] / 70.0 + 41.3, pts[:, 1] / 70.0 - 17.9, z)
       mobject.points[:, 0] = pts[:, 0] + dx
       mobject.points[:, 1] = pts[:, 1] + dy
   ```
2. **Caching `base_points`:**
   Crucial rule: Never perturb `mobject.points` cumulatively in place. Always store `mobject.base_points = mobject.points.copy()` on instantiation, and perturb from `base_points`.

---

## 7. Global Aesthetic & Environment Parameters

### 7.1 Canvas & Video Parameters
- Resolution: $1920 \times 1080$ pixels (Full HD)
- Aspect Ratio: 16:9 widescreen
- Master Frame Rate: 24.0 FPS
- Total Duration: Exactly 30.00 seconds (720 rendered frames: 0 through 719)
- Audio Specs: 48,000 Hz, 16-bit PCM stereo (`pcm_s16le`), exactly 30.000000s duration

### 7.2 Color Palette Reference (`PAL`)
| Token | Hex Code | Semantic Role |
|---|---|---|
| `PAL.cream` | `#f4e9d0` | Primary paper canvas background |
| `PAL.ink` | `#1c1613` | Dense carbon black line art, outer contours, drop shadows |
| `PAL.red` | `#e5402b` | Tomato red accent, Trust seal, Book cover, Flame spirit |
| `PAL.yel` | `#ffc425` | Sunny Marigold yellow, Respect seal, sparkles, gold filigree |
| `PAL.hi` | `#fff6e2` | Paper-white highlight tint, banner background, brain fill, plaque |
| `PAL.pencil` | `#d9573f` | Col-Erase red pencil, subtitle kicker/sub text, underdrawing |
| Paper Grain | `rgba(28, 22, 19, 0.025)` | 40 procedural horizontal paper tooth flecks |

### 7.3 Border Frame Specifications
The reference features a triple-layered hand-boiled border frame:
- Outer Red Stroke: Inset $L = 28\text{ px}$, width $22\text{ px}$, color `#e5402b`, boil amp $3.5$.
- Inner Cream Highlight: Inset $L = 28\text{ px}$, width $12\text{ px}$, color `#fff6e2`, boil amp $2.5$.
- Fine Inner Inked Rule: Inset $L_2 = 42\text{ px}$, width $3.5\text{ px}$, color `#1c1613`, boil amp $1.8$.

---

## 8. Omission Specification: Slates, Counters & Peg Holes to Exclude

Per project requirements (R3 in `ORIGINAL_REQUEST.md`), the Manim port must achieve a clean cinematic presentation by removing production slates, exposure counters, and peg holes.

### 8.1 Visual Elements to Exclude (`drawPencil`)
The Manim port must completely omit the following elements present in `scene.js:102-134`:
1. **Top-Left Production Slate Text:**
   - Location: `x = 65px, y = 82px`
   - Rendered String: `SC. 05 · AUDIOBOOK SUMMARY`
   - Omission: DO NOT render any text in the top-left margin.
2. **Bottom-Right Exposure Counter Text:**
   - Location: `x = 1855px, y = 1015px`
   - Rendered String: `No. XXX · on 2s` (e.g. `No. 074 · on 2s`)
   - Omission: DO NOT render exposure frame counters in the bottom-right corner.
3. **Bottom-Right Cel Boil Style Label:**
   - Location: `x = 1855px, y = 975px`
   - Rendered String: `CEL BOIL ANIMATION`
   - Omission: DO NOT render style badge text in the bottom-right margin.
4. **Top Edge Peg Bar Holes:**
   - Locations: Three circles at `y = 38px`, `x in [460px, 960px, 1460px]`
   - Omission: DO NOT draw peg bar circles or cutouts along the top edge.

### 8.2 Audio Elements to Exclude
In `audio.py:67-69`, the police siren frequency sweep:
```python
# 8.16: "Aakhir difference kya hai?" - Police Siren frequency sweep
m.sfx(police_siren(1.4), at=8.16)
```
- **Omission:** The synthesized police siren effect (`police_siren(1.4)`) MUST BE REMOVED from the audio mix in the Manim port. All other 15 synchronized sound effects must be preserved.

---

## 9. Manim Porting Implementation Recommendations

1. **Scene Structure:**
   Create a single master `AudiobookSummaryScene(Scene)` with `camera.background_color = "#f4e9d0"`.
2. **Cel Boil Updater System:**
   - Implement a lightweight Simplex Noise module (using `scipy.interpolate` or `opensimplex` / `numpy`).
   - Group beat elements into distinct `VGroup` containers.
   - Attach a boiling updater that updates `points` based on `time * 12` (or `time * 8` during the final hold).
3. **Timeline Manager:**
   - Use a piecewise schedule or sequential `self.play()` / `self.wait()` transitions matching the exact beat timeline:
     - Beat 1: `0.00s – 1.50s`
     - Beat 2: `1.50s – 4.50s`
     - Beat 3: `4.50s – 9.00s`
     - Beat 4: `9.00s – 12.20s`
     - Beat 5: `12.20s – 15.00s`
     - Beat 6: `15.00s – 18.50s`
     - Beat 7: `18.50s – 23.36s`
     - Beat 8: `23.36s – 26.14s`
     - Beat 9: `26.14s – 29.58s`
     - Beat 10: `29.58s – 30.00s`
4. **Kinetic Typography Banner:**
   - Build a reusable `KineticBanner(VGroup)` containing a background rounded rectangle / pill with an inked drop shadow and three `Text` Mobjects (Kicker, Hero, Sub).
   - On each cue change, trigger a `ScaleInPlace` pulse (`1.3x -> 1.0x` over `0.22s`).
5. **Windows FFmpeg Encoding:**
   - Per project requirement R4, export using `-pix_fmt yuv420p` to guarantee native playback on Windows Media Player without green screen / codec errors.
