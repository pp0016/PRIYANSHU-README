"""
Local batch render script for all 72 Manim math clips.
Runs using the venv manim executable.
Output destination: projects/03_boss_building_rents/images/manim_math/

Usage: python projects/03_boss_building_rents/render_manim_local.py [start_idx] [end_idx]
"""

import subprocess
import sys
import os
import shutil

MANIM_EXE = r"C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe"
WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCENES_FILE = os.path.join(WORKSPACE_ROOT, "projects", "03_boss_building_rents", "images", "manim_math", "scenes.py")
OUTPUT_DIR  = os.path.join(WORKSPACE_ROOT, "projects", "03_boss_building_rents", "images", "manim_math")

# All 72 scene class names in render order
SCENES = [
    "Anim048","Anim049","Anim054","Anim060","Anim069","Anim070","Anim072",
    "Anim082","Anim083","Anim086","Anim087","Anim088","Anim093","Anim107",
    "Anim120","Anim122","Anim123","Anim124","Anim129","Anim141","Anim146",
    "Anim165","Anim170","Anim172","Anim173","Anim174","Anim177","Anim181",
    "Anim182","Anim196","Anim197","Anim199","Anim200","Anim215","Anim216",
    "Anim219","Anim221","Anim225","Anim227","Anim229","Anim237","Anim238",
    "Anim241","Anim242","Anim251","Anim256","Anim257","Anim264","Anim287",
    "Anim288","Anim289","Anim290","Anim292","Anim294","Anim295","Anim296",
    "Anim307","Anim308","Anim312","Anim313","Anim314","Anim318","Anim320",
    "Anim321","Anim322","Anim323","Anim324","Anim325","Anim330","Anim351",
    "Anim372","Anim412",
]

def render_scene(scene_name):
    cut_num = scene_name.replace("Anim","")
    out_name = f"anim_{cut_num}.mp4"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        print(f"[SKIP] {out_name} already exists.")
        return True

    cmd = [
        MANIM_EXE, "render",
        "-qm",           # medium quality, 720p / 25fps (fast, crisp)
        "--fps", "25",
        "--format", "mp4",
        SCENES_FILE,
        scene_name,
    ]
    print(f"[RENDER] {scene_name} -> {out_name}")
    result = subprocess.run(cmd, cwd=WORKSPACE_ROOT, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] {scene_name}: {result.stderr[-500:]}")
        return False

    # Check root workspace media directory first
    root_media = os.path.join(WORKSPACE_ROOT, "media")
    for root, dirs, files in os.walk(root_media):
        for f in files:
            if f.startswith(scene_name) and f.endswith(".mp4"):
                src = os.path.join(root, f)
                shutil.move(src, out_path)
                print(f"  [OK] Saved -> {out_path} ({os.path.getsize(out_path)} bytes)")
                return True

    # Search local project media directory as fallback
    proj_media = os.path.join(os.path.dirname(SCENES_FILE), "media")
    if os.path.exists(proj_media):
        for root, dirs, files in os.walk(proj_media):
            for f in files:
                if f.startswith(scene_name) and f.endswith(".mp4"):
                    src = os.path.join(root, f)
                    shutil.move(src, out_path)
                    print(f"  [OK] Saved -> {out_path} ({os.path.getsize(out_path)} bytes)")
                    return True

    print(f"  [WARN] Could not locate output mp4 for {scene_name}")
    return False

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end   = int(sys.argv[2]) if len(sys.argv) > 2 else len(SCENES)
    subset = SCENES[start:end]
    print(f"Rendering scenes {start}–{end-1}: {len(subset)} clips")
    ok = 0
    for scene in subset:
        if render_scene(scene):
            ok += 1
    print(f"\nDone: {ok}/{len(subset)} scenes rendered successfully.")
