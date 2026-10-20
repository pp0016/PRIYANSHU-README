import os
import sys
import json
import subprocess
from pathlib import Path

REPO_PATH = r"c:\Users\renu5\Downloads\manim_video_repo"
BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"

sys.path.insert(0, REPO_PATH)
from tests.test_helpers import validate_png_file

def run_cmd(args, expected_png=None):
    cmd = [BLENDER_PATH] + args
    print("=" * 60)
    print("Running:", " ".join(cmd))
    p = subprocess.run(
        cmd,
        cwd=REPO_PATH,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    print("Exit code:", p.returncode)
    for line in p.stdout.splitlines()[-6:]:
        print("  [stdout]", line)
    if p.returncode != 0:
        for line in p.stderr.splitlines()[-6:]:
            print("  [stderr]", line)

    if expected_png:
        png_full = os.path.join(REPO_PATH, expected_png)
        if os.path.exists(png_full):
            meta = validate_png_file(png_full, min_size_bytes=100000)
            print(f"  [PNG OK] {meta['width']}x{meta['height']} {meta['color_mode']}, {meta['file_size']} bytes")
        else:
            print("  [PNG ERROR] File does not exist:", png_full)
    return p.returncode

if __name__ == "__main__":
    test_type = sys.argv[1] if len(sys.argv) > 1 else "special"
    
    if test_type == "special":
        spec1 = "!@#$%^&*()_+-=[]{}|;':,.<>?/~`"
        spec2 = "QUOTES: 'Single' & \"Double\" / Backslash \\"
        rc = run_cmd([
            "-b", "-P", "blender/scene_generator.py",
            "--",
            "--start", "1",
            "--end", "1",
            "--samples", "1",
            "--text1", spec1,
            "--text2", spec2,
            "--output", "//output/challenger_special_chars_#####",
            "--render"
        ], expected_png="output/challenger_special_chars_00001.png")
        sys.exit(rc)
        
    elif test_type == "nested":
        rc = run_cmd([
            "-b", "-P", "blender/scene_generator.py",
            "--",
            "--start", "1",
            "--end", "1",
            "--samples", "1",
            "--output", "//output/nested/deep/challenger_nested_#####",
            "--render"
        ], expected_png="output/nested/deep/challenger_nested_00001.png")
        sys.exit(rc)
        
    elif test_type == "samples16":
        rc = run_cmd([
            "-b", "-P", "blender/scene_generator.py",
            "--",
            "--start", "1",
            "--end", "1",
            "--samples", "16",
            "--output", "//output/challenger_samples16_#####",
            "--render"
        ], expected_png="output/challenger_samples16_00001.png")
        sys.exit(rc)

    elif test_type == "workflow_native":
        rc = run_cmd([
            "-b", "-P", "blender/scene_generator.py",
            "-o", "//output/challenger_wf_#####",
            "-s", "1",
            "-e", "1",
            "-a"
        ], expected_png="output/challenger_wf_00001.png")
        sys.exit(rc)
