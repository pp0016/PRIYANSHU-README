# Omni Flash Test Prompts — Stikaman Channel (5 Videos)

> **Purpose:** 5 test clips, one per video. These test whether Omni Flash can produce the stickman dark-history visual style. Each prompt = one 10-second clip representing the most iconic moment from each video.
>
> **Format:** Google Flow / Omni Flash JSON prompts with time-indexed action blocks.
> **Duration:** 10 seconds each.
> **Aspect ratio:** 16:9 (YouTube long-form).

---

## Why These 5 Scenes

| # | Video | Scene Chosen | Why This Scene |
|---|-------|-------------|----------------|
| 1 | Banned Weapons | Crossbow kills knight | The class-warfare moment. A peasant one-shots an armored knight. Tests: can Omni Flash do a simple stickman action sequence with impact? This is the most repeated scene type across ALL 5 videos. |
| 2 | Banned Books | Dictionary being stamped "BANNED" | The absurdity hook. A normal dictionary gets a giant red BANNED stamp. Tests: can Omni Flash handle object + text overlay style? This is the comedic tone for the whole video. |
| 3 | Dumb War Tactics | Trojan Horse reveal | The most visually clear moment in the video. Giant wooden horse, soldiers climbing out. Tests: can Omni Flash handle a scene with multiple figures + a large prop? |
| 4 | Greek Mythology Monsters | Medusa turns soldier to stone | The most iconic Greek myth visual. A figure looks at Medusa, turns gray/stone. Tests: can Omni Flash do a transformation effect (color → gray)? Needed for multiple monsters. |
| 5 | Bullet Types | Bullet cross-section mushrooming on impact | The mechanism visual. A bullet enters a silhouette and the tip expands. Tests: can Omni Flash do slow-motion physics / cutaway style? This is the core visual for the entire bullet video. |

---

## Prompt 1: BANNED WEAPONS — Crossbow Kills a Knight

The thesis moment: a peasant with 2 hours of training kills a knight worth a fortune.

```json
{
  "scene_title": "Crossbow vs Knight — The Weapon That Broke Feudalism",
  
  "subject": "Two simplified stick-figure characters on a medieval battlefield. Frame LEFT: a small, thin stick figure in plain brown clothing holds a loaded crossbow at shoulder height, aiming across the field. Frame RIGHT: a large, imposing stick figure in full silver plate armor with a shield and sword, standing tall and confident. Background: flat green field with a distant treeline, overcast gray sky. Style: 2D hand-drawn animation, black ink outlines, minimal detail, dark parchment-toned background.",

  "action": {
    "0-2s": "Wide establishing shot. The armored knight stands tall on the right, sword raised, dominating the frame. The small peasant on the left is barely visible, crouching low with the crossbow. The size difference is exaggerated — the knight is twice the height of the peasant.",
    "2-4s": "Medium shot of the peasant. He cranks the crossbow string back with a winch mechanism. His hands shake slightly. A single crossbow bolt locks into position. The camera holds steady.",
    "4-6s": "Close-up of the peasant's hands releasing the trigger. The bolt launches with a sharp SNAP sound. The camera follows the bolt in a fast tracking shot across the field toward the knight.",
    "6-8s": "Impact. The bolt strikes the knight directly in the center of his chest plate. The knight stumbles backward, arms going wide. His sword drops from his hand. The armor cracks visually at the point of impact. A burst of stylized white sparks on impact — no blood, no gore.",
    "8-10s": "The knight topples backward like a felled tree, crashing to the ground with a heavy metallic thud. Dust rises. The peasant stands up slowly, still holding the crossbow. He looks stunned at what he just did. Hold on this wide shot for 2 seconds. The peasant is tiny. The knight is flat on his back."
  },

  "camera": {
    "shot_type": "Starts wide, shifts to medium close-up at 2s, tracking shot at 4s, returns to wide at 8s",
    "lens": "35mm equivalent for wide shots, 50mm for the close-up",
    "angle": "Eye-level throughout, slight low angle on the knight at 0-2s to emphasize his size",
    "movement": "Static establishing → handheld slight shake on close-up → fast lateral track following the bolt → static wide for the fall"
  },

  "lighting": "Overcast flat lighting, gray sky, no harsh shadows. The knight's armor has a dull silver sheen. The bolt is a dark brown wooden shaft. The overall palette is muted earth tones — browns, grays, dull greens.",

  "audio": {
    "ambient": "Wind across an open field. Distant crows.",
    "sfx": "Crossbow winch cranking at 2s. Sharp snap of release at 4s. Metallic impact clang at 6s. Heavy body-and-armor crash at 8s. Dust settling.",
    "dialogue": {
      "speaker": "NARRATOR (off-screen)",
      "line": "No dialogue — narrator voiceover added in post-production.",
      "voice": "NONE — narrator audio is post-production"
    }
  },

  "style": "2D stylized animation, stick-figure characters with minimal facial features (dots for eyes, no mouth), black ink outlines on parchment-toned background, hand-drawn aesthetic, NOT photorealistic, NOT 3D. Think Simple History or ExplainTory animation style. 16:9, clean composition.",

  "negative_constraints": "No blood. No gore. No realistic human faces. No 3D rendering. No photorealistic style. No text on screen. No modern elements. Keep it simple — stick figures, not detailed character models."
}
```

---

## Prompt 2: BANNED BOOKS — The Dictionary Gets Banned

The absurdity hook: a school district in California banned the Merriam-Webster Dictionary because a parent complained.

```json
{
  "scene_title": "The Dictionary Ban — When Words Became Dangerous",

  "subject": "A single large hardcover dictionary sits on a wooden school desk in a bright classroom. The dictionary is dark blue with gold lettering. Behind the desk, a clean chalkboard. The classroom is empty — no students, no teacher. Style: 2D stylized animation, clean lines, warm indoor lighting, slightly comedic oversized proportions.",

  "action": {
    "0-2s": "Static wide shot of the classroom. The dictionary sits peacefully on the desk, slightly angled. Warm morning sunlight comes through a window frame-left. Everything is calm and ordinary. A clock ticks on the wall.",
    "2-4s": "Slow push-in toward the dictionary. The book is the only object in focus. The camera narrows to a medium close-up. The gold title 'DICTIONARY' is clearly readable on the spine.",
    "4-6s": "A large red rubber stamp slams down from the top of frame onto the dictionary cover with a loud THWACK sound. The stamp leaves a massive red 'BANNED' impression across the entire cover. Red ink splatters slightly outward from the impact.",
    "6-8s": "Pull back to medium shot. A stick-figure hand (just the arm, no full character visible) pulls the stamp back up out of frame. The dictionary now sits with the giant red BANNED stamp across it. The book looks exactly the same — it's still just a dictionary. The absurdity is visual.",
    "8-10s": "Wide shot. The camera slowly pulls back further to reveal the empty classroom. The banned dictionary sits alone on the desk. A single question mark fades in above it — small, white, floating. Hold for 2 seconds on this composition."
  },

  "camera": {
    "shot_type": "Wide → slow push-in → medium close-up → pull-back to wide",
    "lens": "50mm throughout for clean, neutral framing",
    "angle": "Slightly above eye-level (looking down at the desk), like a student's perspective",
    "movement": "Smooth dolly push-in from 0-4s, static at 4-6s for the stamp impact, smooth dolly pull-back from 6-10s"
  },

  "lighting": "Warm classroom morning light from a window frame-left. Soft shadows on the desk. The red stamp ink is vivid and saturated against the muted classroom tones. Clean, bright, almost cheerful — contrast with the absurdity of banning a dictionary.",

  "audio": {
    "ambient": "Quiet empty classroom. Faint clock ticking. Distant hallway sounds.",
    "sfx": "Rubber stamp THWACK at 4s — heavy, authoritative. Ink splatter sound. Clock continues ticking after the stamp, emphasizing silence.",
    "dialogue": {
      "speaker": "NARRATOR (off-screen)",
      "line": "No dialogue — narrator voiceover added in post-production.",
      "voice": "NONE — narrator audio is post-production"
    }
  },

  "style": "2D stylized animation, clean flat colors, slight cartoon proportions (the stamp is oversized for comedy). Warm color palette — yellows, browns, soft blues. The red BANNED stamp is the only saturated color in the frame. 16:9.",

  "negative_constraints": "No characters visible except the arm with the stamp. No realistic human faces. No 3D rendering. No dark or moody lighting — this scene is intentionally bright and ordinary to contrast the absurdity. No violence."
}
```

---

## Prompt 3: DUMB WAR TACTICS — The Trojan Horse Reveal

The most visually iconic "dumb tactic that worked" — soldiers hidden inside a gift.

```json
{
  "scene_title": "Trojan Horse — The Dumbest Brilliant Plan in Military History",

  "subject": "A massive crude wooden horse construction stands inside the walls of an ancient walled city at night. The horse is rough-built from dark timber planks, towering three times the height of the stick-figure soldiers below. Torches on the city walls cast warm orange flicker light. Several stick-figure city guards sleep on the ground around the horse, weapons dropped beside them. Style: 2D animation, dark palette, nighttime, torchlight contrast.",

  "action": {
    "0-2s": "Wide establishing shot from inside the city walls. The enormous wooden horse dominates the center of the frame. Torches flicker on the walls. Three stick-figure guards sleep on the ground around the horse's base. The city is silent. Stars visible in the dark blue sky above the walls.",
    "2-4s": "Close-up on the horse's belly. A thin crack appears in the wood. A small rectangular hatch slowly creaks open — just an inch. Two small white dots (eyes) peer out from the darkness inside.",
    "4-6s": "Medium shot. The hatch drops open fully. A stick-figure soldier in dark clothing drops silently from the horse's belly to the ground, landing in a crouch. He holds a short sword. A second figure begins climbing down behind him.",
    "6-8s": "Wide shot. Four stick-figure soldiers are now on the ground, moving quickly and silently toward the city gates. One sleeping guard stirs but doesn't wake. The soldiers reach the massive wooden gate and begin lifting the bar lock.",
    "8-10s": "The city gates swing open. Beyond them, hundreds of tiny stick-figure soldiers with torches and weapons stand in formation outside, waiting. The light from their torches floods through the opening. The camera holds on this wide shot — the massive army revealed. The sleeping guards haven't moved."
  },

  "camera": {
    "shot_type": "Wide establishing → close-up on horse belly → medium → wide reveal",
    "lens": "35mm for wide shots, 85mm for the close-up of the hatch",
    "angle": "Eye-level for establishing, low angle looking up at the horse at 2-4s, eye-level for the gate opening",
    "movement": "Static establishing → slow push-in on hatch → static medium → slow dolly toward the opening gates"
  },

  "lighting": "Nighttime. Primary light from wall-mounted torches — warm orange flicker, strong shadows. The interior of the horse is pure black darkness. When the gates open at 8s, the massed torches of the army create a warm glow flooding inward. The contrast between the dark sleeping city and the lit army is the key visual.",

  "audio": {
    "ambient": "Night insects. Crackling torches. One guard snoring softly.",
    "sfx": "Wood creaking at 2s. Soft thud of feet landing at 4s. Heavy wooden bar scraping at 6s. Gate hinges groaning at 8s. Then silence — then the faint sound of marching feet.",
    "dialogue": {
      "speaker": "NARRATOR (off-screen)",
      "line": "No dialogue — narrator voiceover added in post-production.",
      "voice": "NONE — narrator audio is post-production"
    }
  },

  "style": "2D stylized animation, dark moody palette dominated by deep blues, blacks, and warm orange torchlight. Stick figures are simple black silhouettes with white dot eyes. The horse is the most detailed object — rough wooden planks, visible joints, rope lashings. 16:9.",

  "negative_constraints": "No blood. No combat. No violence in this clip — the tension is in the stealth, not fighting. No realistic human faces. No 3D rendering. No text on screen. No daylight — this is a nighttime scene only."
}
```

---

## Prompt 4: GREEK MYTHOLOGY MONSTERS — Medusa Petrification

The most universally recognized Greek myth visual — a warrior turns to stone.

```json
{
  "scene_title": "Medusa's Gaze — The Monster Who Turned Men to Stone",

  "subject": "Two stick-figure characters in a dark cave. Frame LEFT: a female figure with wild snake-like hair tendrils radiating from her head (Medusa) — her hair is made of animated green serpentine lines that move independently. Her eyes glow bright acid green. Frame RIGHT: a stick-figure Greek warrior in a simple tunic with a round shield and short sword, facing Medusa. The cave walls are rough dark stone with faint green bioluminescent moss. Style: 2D animation, dark cave environment, green-dominant color scheme.",

  "action": {
    "0-2s": "Medium shot of the warrior walking cautiously into the cave from frame-right, shield raised, sword drawn. The cave is dark. His footsteps echo. He doesn't see what's ahead. The snake-hair tendrils of Medusa are barely visible in the deep shadow frame-left, writhing slowly.",
    "2-4s": "Close-up on the warrior's face (simple stick figure — dot eyes, no mouth). His eyes widen. He's seen something. The camera is on HIM, not on Medusa. Two bright green glows reflect in his dot-eyes from off-screen — Medusa's gaze hitting him.",
    "4-6s": "Wide shot. The full confrontation. Medusa stands frame-left, snake-hair fully animated and writhing, eyes blazing green. Two bright green beams of light extend from her eyes across the frame toward the warrior. The warrior's body begins changing color — from black ink to stone gray, starting at his feet and creeping upward.",
    "6-8s": "Close-up on the warrior. The stone-gray transformation reaches his torso, then his arms. His sword arm freezes mid-raise. His shield arm locks in position. The transformation reaches his neck, then his face. His dot-eyes are the last thing to change — going from white to solid gray. He is now a complete stone statue.",
    "8-10s": "Wide shot. Medusa turns away slowly, her snake-hair settling. The warrior stands frozen as a gray stone statue in his last pose — shield up, sword half-raised, permanently terrified. The cave is silent except for the faint hissing of Medusa's snake-hair. Camera slowly pulls back to reveal other stone statues deeper in the cave — previous victims. Hold on this composition."
  },

  "camera": {
    "shot_type": "Medium → close-up on warrior face → wide two-shot → close-up on transformation → wide pull-back reveal",
    "lens": "50mm for medium shots, 85mm for close-ups, 35mm for the final wide reveal",
    "angle": "Eye-level throughout. The final pull-back is slightly higher angle to show the cave floor with multiple statues.",
    "movement": "Slow tracking following the warrior at 0-2s, static for the confrontation, slow pull-back for the final reveal"
  },

  "lighting": "Dark cave. Primary light source: Medusa's glowing green eyes — they cast green light across the cave walls and the warrior's body. Secondary: faint green bioluminescent moss on cave walls providing ambient fill. The stone transformation is shown through color change (black ink → matte gray) under the green light. No warm tones — everything is cool greens and dark grays.",

  "audio": {
    "ambient": "Cave dripping water. Faint echo on footsteps. Distant wind through cave tunnels.",
    "sfx": "Snake hissing (continuous, subtle). A crystalline 'cracking' sound as the stone transformation spreads at 4-8s — like ice forming rapidly. Final heavy stone 'clunk' as the transformation completes at 8s.",
    "dialogue": {
      "speaker": "NARRATOR (off-screen)",
      "line": "No dialogue — narrator voiceover added in post-production.",
      "voice": "NONE — narrator audio is post-production"
    }
  },

  "style": "2D stylized animation, dark horror-adjacent palette. Dominant colors: black, dark gray, acid green. Medusa's snake-hair is the most animated element — constantly moving green lines. The stick figures are simple (dot eyes, no detailed faces) but expressive through body pose. The stone transformation is the key effect — clean color shift from black to matte gray. 16:9.",

  "negative_constraints": "No blood. No gore. No severed heads. No graphic violence. The horror is in the TRANSFORMATION, not in physical injury. No realistic human faces. No 3D. No photorealistic rendering. Keep Medusa as a stick figure with snake-hair — she should NOT look like a detailed monster illustration."
}
```

---

## Prompt 5: BULLET TYPES — Expanding Bullet Cross-Section

The core mechanism visual: what happens inside a body when a hollow-point bullet hits.

```json
{
  "scene_title": "The Expanding Bullet — How a Dum-Dum Mushrooms on Impact",

  "subject": "A technical cross-section diagram view. Frame LEFT: a single copper-jacketed bullet with a hollow point tip, shown in cutaway profile (half the bullet is sliced open to show the internal structure — lead core, copper jacket, hollow cavity at the tip). Frame RIGHT: a translucent blue silhouette representing a ballistic gel target (NOT a human body — a rectangular gel block). Background: clean dark gray with faint grid lines, like a technical blueprint. Style: 2D technical diagram animation, clean vector lines, educational infographic aesthetic.",

  "action": {
    "0-2s": "Static close-up of the bullet in cross-section profile, centered in frame. The camera slowly rotates around it — the hollow point cavity is clearly visible at the tip. The copper jacket is orange-brown, the lead core is dark gray. Clean white label lines point to 'COPPER JACKET', 'LEAD CORE', 'HOLLOW CAVITY' — but these labels are added in post, not generated by AI.",
    "2-4s": "The bullet moves from frame-left toward the gel block on frame-right. The camera follows with a fast tracking shot. The bullet is now moving at high speed — motion blur on the background. The gel block is stationary, slightly wobbling like gelatin.",
    "4-6s": "IMPACT. The bullet tip contacts the gel block surface. In slow motion: the hollow point begins to deform. The copper jacket peels back like petals of a flower opening. The lead core spreads outward. The bullet's diameter doubles. Ripples spread through the gel block from the entry point.",
    "6-8s": "Continued slow motion. The mushroomed bullet is now fully expanded inside the gel block, creating a large temporary cavity — a dark sphere of disruption around the bullet. The gel block bulges outward at the sides from internal pressure. The expanded bullet has stopped — all its energy is transferred into the gel.",
    "8-10s": "Pull back to wide shot. The gel block settles. The bullet is embedded inside — now a flat mushroom shape, three times its original diameter. Camera holds on this final cross-section view. Clean, clinical, educational. The gel block has a large permanent wound channel visible through its translucent blue surface."
  },

  "camera": {
    "shot_type": "Close-up cross-section → fast tracking → slow-motion impact → wide cross-section",
    "lens": "Macro lens equivalent for the bullet close-up (0-2s), 50mm for tracking, macro again for the slow-motion impact",
    "angle": "Perfect profile (side view) throughout — this is a technical diagram, not a dramatic scene",
    "movement": "Slow orbit at 0-2s, fast lateral track at 2-4s, static slow-motion for impact at 4-8s, slow pull-back at 8-10s"
  },

  "lighting": "Clean, even studio lighting — no dramatic shadows. The bullet has slight metallic sheen. The gel block is translucent blue with internal light showing the wound channel. The background is dark gray with subtle grid lines. This is NOT cinematic lighting — it's technical/educational lighting like a Discovery Channel slow-motion segment.",

  "audio": {
    "ambient": "Near silence. Clean studio environment.",
    "sfx": "At 2-4s: sharp metallic whistle of the bullet in flight. At 4s: deep, heavy THUD of impact — not a sharp crack, a low wet impact sound. At 4-8s: slow-motion sound of gel deformation — a deep, stretched, wobbling bass. At 8s: silence settles.",
    "dialogue": {
      "speaker": "NARRATOR (off-screen)",
      "line": "No dialogue — narrator voiceover added in post-production.",
      "voice": "NONE — narrator audio is post-production"
    }
  },

  "style": "2D technical diagram animation. Clean vector lines. Educational infographic aesthetic — NOT cinematic, NOT dramatic. Think Kurzgesagt meets ballistics lab footage. Color palette: dark gray background, orange-copper bullet, dark gray lead core, translucent blue gel. White grid lines for scale reference. 16:9.",

  "negative_constraints": "No human bodies. No stick figures in this clip — this is a TECHNICAL DIAGRAM, not a narrative scene. The target is a GEL BLOCK, not a person. No blood. No gore. No red colors. No text generated by AI — all labels added in post. No 3D photorealistic rendering. Keep it flat 2D vector style."
}
```

---

## How to Use These Prompts

1. **Copy the full JSON block** for each prompt
2. **Paste into Google Flow** (Omni Flash)
3. **Set duration to 10 seconds**
4. **Set aspect ratio to 16:9**
5. **Generate and compare results**

### What You're Testing

| Prompt | Tests This Capability | If It Works | If It Fails |
|--------|----------------------|-------------|-------------|
| #1 Crossbow | Action sequence + impact between two characters | Omni Flash can handle your core scene type (character A attacks character B) | You need Remotion for all action scenes — use Omni only for static/slow scenes |
| #2 Dictionary | Object + comedic timing + stamp effect | Omni Flash handles prop-focused comedy beats | Comedy scenes go to Remotion with Nano Banana static images |
| #3 Trojan Horse | Night scene + multiple figures + reveal | Omni Flash handles complex compositions and lighting contrast | Simplify to fewer figures per scene, composite in Remotion |
| #4 Medusa | Transformation effect (color change) + horror mood | Omni Flash can do visual effects within animation style | Effects scenes need Remotion code (color transitions programmatic) |
| #5 Bullet | Technical diagram + slow-motion physics | Omni Flash handles educational/mechanism visuals | Mechanism scenes use Nano Banana static cross-sections + Remotion Ken Burns |

### After Testing

- If 3+ prompts produce usable results → Omni Flash is viable for accent clips
- If 1-2 work → Omni Flash only for those specific scene types, Remotion for the rest
- If 0 work → Full Remotion + Nano Banana pipeline, Omni Flash is out

**Send me the results. Don't judge them alone — I need to see what Omni Flash actually outputs to adjust the pipeline.**
