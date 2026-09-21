# AI Handoff Context: Procedural Animation Pipeline (2D/3D)

**Conversation ID:** `6f71b575-d73e-4413-b861-a66d8f356c8c`
**Goal:** Transitioning from basic procedural math animation (stickmen) to professional, YouTube-ready, 16:9 cinematic animation using Python, Manim, and Blender.

## 1. User Preferences & Vision
* **Art Style:** The user strongly dislikes basic, raw "math-style" stickmen without fingers or backgrounds. For future tasks, characters MUST have defined limbs, fingers, and exist in rich, colorful environments.
* **Approved Styles:** 
  * *2D:* Flat vector graphics (Kurzgesagt / Vox style) using filled geometric shapes, vibrant triadic colors (purples, oranges, teals).
  * *3D:* Isometric, stylized low-poly / voxel art (Monument Valley / Crossy Road style). Allows for procedural generation while looking highly intentional and professional.
* **Workflows:** The user prefers a multi-agent approach. When a prompt is given, spawn 2 to 5 subagents to execute different stylistic variations of the task independently. Do NOT ask for permission repeatedly; execute proactively.
* **Content:** Philosophical voiceovers (e.g., a script about "finding purpose by doing the work, rather than waiting for it").

## 2. Technical Infrastructure & Gotchas (CRITICAL)

### Manim (2D Engine)
* **Environment:** A virtual environment is established at `C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv`.
* **Execution:** You MUST prepend the PATH when rendering via PowerShell:
  `$env:Path = [Environment]::GetEnvironmentVariable("Path", "User") + ";" + [Environment]::GetEnvironmentVariable("Path", "Machine"); & "C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe" render -qm script.py ClassName`
* **Z-Indexing:** When using `always_redraw` with overlapping shapes, ensure elements are added to the scene in strict back-to-front order.

### Blender (3D Engine)
* **Executable:** `C:\Program Files\Blender Foundation\Blender 5.2\blender.exe`
* **CRITICAL BUG:** Rendering directly to `FFMPEG` (MP4) inside the Blender 5.2 Python script throws an enum crash (`TypeError: enum "FFMPEG" not found`). 
* **The Fix:** ALWAYS render 3D scenes as a PNG sequence (`scene.render.image_settings.file_format = 'PNG'`) to a temporary folder, and then stitch them together via CLI using `ffmpeg`:
  `ffmpeg -y -r 30 -i "C:\path\to\frames\%04d.png" -c:v libx264 -pix_fmt yuv420p "output.mp4"`
* **Rigging via Python:** Do not calculate complex global matrices. Create Empties as joints, set their `.parent`, and immediately set `.location` to place them in *local coordinate space*. Animate using `.rotation_euler` and `.keyframe_insert()`.

## 3. Project History & Milestones

1. **The Math Stickman (`Stickman_Main.mp4`)**: Replicated a Cyanide & Happiness character exactly using Manim geometry (Arcs, Ellipses). Spawned 4 subagents to test variations.
2. **The Continuous Walk (`Walking_Main.mp4`)**: Built an infinitely looping walk cycle and laughing animation using pure `ValueTracker(t)` kinematics (sine/cosine math).
3. **The 3D Translation (`True_3D_Stickman.mp4`)**: Translated the 2D sine/cosine kinematics directly into a 3D Blender Rig via python. Built a 3D skeleton out of cylinders and spheres.
4. **The Professional Prototypes**: 
   * **`Concept1_Manim.mp4`**: A Kurzgesagt-style prototype with colorful vector environments and non-stickman characters.
   * **`Concept2_Blender.mp4`**: An isometric 3D voxel-styled prototype rendered via Blender Python with lighting and soft shadows.

## 4. Current State & Next Steps
The user has provided a philosophical script about "Finding Purpose". We have rendered 10-second proof-of-concept clips for both the 2D and 3D professional styles. 

**Next Step for New Agent:** 
1. Review this document to understand the rendering constraints (especially the Blender PNG->FFMPEG workaround).
2. Ask the user which of the two styles (Concept 1 or Concept 2) they selected.
3. Begin breaking down the voiceover script into scenes and programmatically generating the final YouTube-ready animation.
