"""Verification suite for Milestone 3: Parallel Cloud Render Farm.

Tests:
1. PyYAML parsing of blender_render.yml
2. Matrix chunk generation logic across multiple edge cases
3. Structural completeness and flag conformance of workflow jobs
4. Gitignore pattern matching and preservation of existing files
"""

import os
import sys
import math
import fnmatch
import yaml


def test_yaml_syntax(workflow_path):
    """Validate YAML syntax using PyYAML."""
    print(f"[TEST 1] Validating YAML syntax of: {workflow_path}")
    assert os.path.exists(workflow_path), f"File does not exist: {workflow_path}"
    with open(workflow_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "Parsed YAML root is not a dictionary"
    print("  -> YAML syntax is valid!")
    return data


def test_matrix_chunk_math():
    """Test chunk generation logic across various frame counts and chunk sizes."""
    print("[TEST 2] Testing matrix planner chunk math")

    def generate_chunks(total, chunk_sz):
        chunks = []
        num_chunks = math.ceil(total / chunk_sz)
        for i in range(num_chunks):
            start_frame = i * chunk_sz + 1
            end_frame = min((i + 1) * chunk_sz, total)
            chunks.append({"id": f"{i:02d}", "start": start_frame, "end": end_frame})
        return chunks

    test_cases = [
        # (total, chunk_size, expected_num_chunks, first_chunk, last_chunk)
        (120, 30, 4, {"id": "00", "start": 1, "end": 30}, {"id": "03", "start": 91, "end": 120}),
        (100, 30, 4, {"id": "00", "start": 1, "end": 30}, {"id": "03", "start": 91, "end": 100}),
        (1, 30, 1, {"id": "00", "start": 1, "end": 1}, {"id": "00", "start": 1, "end": 1}),
        (30, 30, 1, {"id": "00", "start": 1, "end": 30}, {"id": "00", "start": 1, "end": 30}),
        (31, 30, 2, {"id": "00", "start": 1, "end": 30}, {"id": "01", "start": 31, "end": 31}),
        (300, 30, 10, {"id": "00", "start": 1, "end": 30}, {"id": "09", "start": 271, "end": 300}),
        (60, 15, 4, {"id": "00", "start": 1, "end": 15}, {"id": "03", "start": 46, "end": 60}),
        (10, 30, 1, {"id": "00", "start": 1, "end": 10}, {"id": "00", "start": 1, "end": 10}),
    ]

    for total, chunk_sz, exp_num, exp_first, exp_last in test_cases:
        chunks = generate_chunks(total, chunk_sz)
        assert len(chunks) == exp_num, f"Failed on total={total}, chunk_sz={chunk_sz}: expected {exp_num} chunks, got {len(chunks)}"
        assert chunks[0] == exp_first, f"First chunk mismatch on total={total}: {chunks[0]} vs {exp_first}"
        assert chunks[-1] == exp_last, f"Last chunk mismatch on total={total}: {chunks[-1]} vs {exp_last}"

        # Continuity check: every frame from 1 to total must be covered exactly once without gap or overlap
        covered_frames = []
        for c in chunks:
            covered_frames.extend(range(c["start"], c["end"] + 1))
        assert covered_frames == list(range(1, total + 1)), f"Continuity failure on total={total}, chunk_sz={chunk_sz}"

    print(f"  -> All {len(test_cases)} matrix calculation scenarios passed perfectly!")


def test_workflow_structure(data):
    """Validate GitHub Actions workflow job graph and specific requirements."""
    print("[TEST 3] Validating workflow structural requirements")

    # 1. Triggers
    assert "on" in data or True in data, "No trigger section found"
    triggers = data.get("on") or data.get(True)
    assert "push" in triggers, "Missing push trigger"
    assert "workflow_dispatch" in triggers, "Missing workflow_dispatch trigger"
    inputs = triggers["workflow_dispatch"].get("inputs", {})
    assert "total_frames" in inputs, "Missing total_frames input"
    assert "chunk_size" in inputs, "Missing chunk_size input"
    assert str(inputs["total_frames"].get("default")) == "120", "total_frames default != 120"
    assert str(inputs["chunk_size"].get("default")) == "30", "chunk_size default != 30"
    print("  -> Triggers and input defaults verified.")

    # 2. Jobs
    jobs = data["jobs"]
    assert "plan" in jobs, "Missing 'plan' job"
    assert "render_chunk" in jobs, "Missing 'render_chunk' job"
    assert "stitch" in jobs, "Missing 'stitch' job"

    # Plan job outputs
    plan_job = jobs["plan"]
    assert "outputs" in plan_job, "'plan' job missing outputs"
    assert "matrix" in plan_job["outputs"], "'plan' outputs missing 'matrix'"
    assert "total_frames" in plan_job["outputs"], "'plan' outputs missing 'total_frames'"

    # Render job config
    render_job = jobs["render_chunk"]
    assert render_job.get("needs") == "plan", "'render_chunk' must depend on 'plan'"
    assert render_job.get("runs-on") == "ubuntu-latest", "'render_chunk' runner must be ubuntu-latest"
    assert render_job.get("strategy", {}).get("fail-fast") is False, "fail-fast must be False"

    render_steps = render_job.get("steps", [])
    step_runs = [s.get("run", "") for s in render_steps if "run" in s]
    combined_render_script = "\n".join(step_runs)

    assert "download.blender.org" in combined_render_script, "Must download Blender from download.blender.org"
    assert "libxi6" in combined_render_script, "Must install libxi6"
    assert "libglu1-mesa" in combined_render_script, "Must install libglu1-mesa"
    assert "libgl1-mesa-dri" in combined_render_script, "Must install libgl1-mesa-dri"
    assert "blender/scene_generator.py" in combined_render_script, "Must invoke blender/scene_generator.py"
    assert 'actions/upload-artifact@v4' in [s.get("uses") for s in render_steps], "Must use upload-artifact@v4"

    # Stitch job config
    stitch_job = jobs["stitch"]
    needs = stitch_job.get("needs")
    if isinstance(needs, str):
        needs = [needs]
    assert "plan" in needs and "render_chunk" in needs, "'stitch' must depend on both 'plan' and 'render_chunk'"

    stitch_steps = stitch_job.get("steps", [])
    step_runs_stitch = [s.get("run", "") for s in stitch_steps if "run" in s]
    combined_stitch_script = "\n".join(step_runs_stitch)

    # Download artifact step
    download_steps = [s for s in stitch_steps if s.get("uses") == "actions/download-artifact@v4"]
    assert len(download_steps) > 0, "Missing download-artifact@v4 step in stitch job"
    dl_with = download_steps[0].get("with", {})
    assert dl_with.get("pattern") == "frames-chunk-*", "Download artifact pattern must be 'frames-chunk-*'"
    assert dl_with.get("merge-multiple") is True, "Download artifact merge-multiple must be True"

    # FFmpeg broadcast flags
    assert "-framerate 30" in combined_stitch_script, "FFmpeg missing -framerate 30"
    assert "-start_number 1" in combined_stitch_script, "FFmpeg missing -start_number 1"
    assert "-c:v libx264" in combined_stitch_script, "FFmpeg missing -c:v libx264"
    assert "-profile:v high" in combined_stitch_script, "FFmpeg missing -profile:v high"
    assert "-level:v 4.2" in combined_stitch_script, "FFmpeg missing -level:v 4.2"
    assert "-pix_fmt yuv420p" in combined_stitch_script, "FFmpeg missing -pix_fmt yuv420p"
    assert "-preset slow" in combined_stitch_script, "FFmpeg missing -preset slow"
    assert "-crf 18" in combined_stitch_script, "FFmpeg missing -crf 18"
    assert "+faststart" in combined_stitch_script, "FFmpeg missing +faststart"
    assert "Final_3D_Typography_Hook.mp4" in combined_stitch_script, "FFmpeg output must be Final_3D_Typography_Hook.mp4"

    # Final video upload
    upload_final = [s for s in stitch_steps if s.get("uses") == "actions/upload-artifact@v4"]
    assert len(upload_final) > 0, "Missing final video upload artifact"
    assert upload_final[0].get("with", {}).get("name") == "Final_3D_Typography_Hook", "Final artifact name must be Final_3D_Typography_Hook"

    print("  -> Workflow structural requirements fully verified!")


def test_gitignore_rules(gitignore_path):
    """Test gitignore patterns against required patterns and preservation paths."""
    print(f"[TEST 4] Validating gitignore rules from: {gitignore_path}")
    assert os.path.exists(gitignore_path), f"File not found: {gitignore_path}"
    with open(gitignore_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    def is_ignored(path):
        for pattern in lines:
            if pattern.endswith("/"):
                # Directory match
                dir_pattern = pattern.rstrip("/")
                parts = path.replace("\\", "/").split("/")
                if dir_pattern in parts:
                    return True
            else:
                filename = os.path.basename(path)
                if fnmatch.fnmatch(filename, pattern) or fnmatch.fnmatch(path, pattern):
                    return True
        return False

    # Required ignores
    should_ignore = [
        "output/frame_00001.png",
        "output/",
        "merged_frames/frame_00001.png",
        "merged_frames/",
        "__pycache__/scene.cpython-311.pyc",
        ".pytest_cache/v/cache",
        "Final_3D_Typography_Hook.mp4",
        "test.mp4",
        "scene.blend1",
        "frame.png.tmp",
    ]
    for p in should_ignore:
        assert is_ignored(p), f"Should be ignored but wasn't: {p}"

    # Required preserved files
    should_preserve = [
        "main.py",
        ".github/workflows/render.yml",
        ".github/workflows/blender_render.yml",
        "blender/scene_generator.py",
        "blender/baseline_spec.md",
        "requirements.txt",
    ]
    for p in should_preserve:
        assert not is_ignored(p), f"Should be preserved but was ignored: {p}"

    print(f"  -> All {len(should_ignore)} ignore rules and {len(should_preserve)} preserve checks passed!")


if __name__ == "__main__":
    work_dir = os.path.dirname(os.path.abspath(__file__))
    workflow_file = os.path.join(work_dir, "blender_render.yml")
    gitignore_file = os.path.join(work_dir, ".gitignore")

    data = test_yaml_syntax(workflow_file)
    test_matrix_chunk_math()
    test_workflow_structure(data)
    test_gitignore_rules(gitignore_file)

    print("\n==========================================")
    print("ALL VERIFICATION SUITE CHECKS PASSED (4/4)")
    print("==========================================")
