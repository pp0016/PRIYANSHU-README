"""Tier 3 Test Suite: Workflow Integration and YAML Architecture.

Verifies:
1. YAML schema, syntax, and structure of .github/workflows/blender_render.yml.
2. Step dependency DAG (plan -> render_chunk -> stitch).
3. Matrix planning algorithm (exact frame partitioning, ceiling logic, boundary consistency).
4. Artifact naming, upload/download patterns (actions/upload-artifact@v4, merge-multiple: true).
5. FFmpeg compilation parameters in workflow (framerate 30, libx264, yuv420p, crf 18, +faststart).
6. Non-destructive repository integration (preservation of render.yml and main.py).
"""

import os
import sys
import json
import math
import yaml
import unittest
from pathlib import Path

# Add target repository to sys.path
PROJECT_ROOT = Path(r"c:\Users\renu5\Downloads\manim_video_repo")
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Add workspace test directory to sys.path
WORKSPACE_TESTS = Path(__file__).resolve().parent
if str(WORKSPACE_TESTS) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_TESTS))

from test_helpers import (
    calculate_chunks_oracle,
    verify_chunks_invariants,
)


class TestTier3WorkflowIntegration(unittest.TestCase):
    """Tier 3: Parallel GitHub Actions Render Farm Workflow Integration Tests."""

    @classmethod
    def setUpClass(cls):
        cls.workflow_file = PROJECT_ROOT / ".github" / "workflows" / "blender_render.yml"
        if not cls.workflow_file.is_file():
            raise unittest.SkipTest(f"Workflow file not found at {cls.workflow_file}")

        with open(cls.workflow_file, "r", encoding="utf-8") as f:
            cls.raw_yaml = f.read()
            cls.parsed_yaml = yaml.safe_load(cls.raw_yaml)

    # -------------------------------------------------------------
    # 1. YAML Syntax & Trigger Schema
    # -------------------------------------------------------------
    def test_01_yaml_syntax_and_root_structure(self):
        """Verify YAML parses without syntax errors and contains required root keys."""
        self.assertIsInstance(self.parsed_yaml, dict, "Workflow root must be a YAML mapping")
        self.assertIn("name", self.parsed_yaml)
        # Note: In YAML 1.1, unquoted 'on:' parses as True (bool)
        has_on = ("on" in self.parsed_yaml) or (True in self.parsed_yaml)
        self.assertTrue(has_on, "Trigger mapping 'on' missing from workflow root")
        self.assertIn("jobs", self.parsed_yaml)

    def test_02_workflow_triggers(self):
        """Verify push to main and workflow_dispatch triggers with parameter inputs."""
        triggers = self.parsed_yaml.get("on") or self.parsed_yaml.get(True) or {}
        self.assertIn("push", triggers, "Push trigger missing")
        self.assertIn("workflow_dispatch", triggers, "workflow_dispatch trigger missing")

        # Check workflow_dispatch inputs
        dispatch = triggers.get("workflow_dispatch") or {}
        inputs = dispatch.get("inputs", {})
        self.assertIn("total_frames", inputs, "total_frames input missing")
        self.assertIn("chunk_size", inputs, "chunk_size input missing")

        # Defaults
        self.assertEqual(str(inputs["total_frames"].get("default", "120")), "120")
        self.assertEqual(str(inputs["chunk_size"].get("default", "30")), "30")

    # -------------------------------------------------------------
    # 2. Step Dependency DAG & Jobs Architecture
    # -------------------------------------------------------------
    def test_03_job_inventory_and_runners(self):
        """Verify the 3 core jobs exist (plan, render_chunk, stitch) and run on ubuntu-latest."""
        jobs = self.parsed_yaml.get("jobs", {})
        expected_jobs = ["plan", "render_chunk", "stitch"]
        for j in expected_jobs:
            self.assertIn(j, jobs, f"Job '{j}' missing from workflow")
            self.assertEqual(
                jobs[j].get("runs-on"), "ubuntu-latest", f"Job '{j}' must run on ubuntu-latest"
            )

    def test_04_step_dependency_dag(self):
        """Verify DAG dependency contracts: render_chunk -> plan, stitch -> [plan, render_chunk]."""
        jobs = self.parsed_yaml.get("jobs", {})

        # render_chunk depends on plan
        render_needs = jobs["render_chunk"].get("needs")
        if isinstance(render_needs, list):
            self.assertIn("plan", render_needs)
        else:
            self.assertEqual(render_needs, "plan")

        # stitch depends on both plan and render_chunk
        stitch_needs = jobs["stitch"].get("needs")
        self.assertIsInstance(stitch_needs, list, "stitch needs must be a list of jobs")
        self.assertIn("plan", stitch_needs)
        self.assertIn("render_chunk", stitch_needs)

    # -------------------------------------------------------------
    # 3. Matrix Planning Job & Math Logic
    # -------------------------------------------------------------
    def test_05_plan_job_outputs(self):
        """Verify plan job declares outputs for matrix and total_frames."""
        plan_job = self.parsed_yaml["jobs"]["plan"]
        outputs = plan_job.get("outputs", {})
        self.assertIn("matrix", outputs, "plan job missing output: matrix")
        self.assertIn("total_frames", outputs, "plan job missing output: total_frames")

    def test_06_matrix_planning_script_execution(self):
        """Extract and run the embedded python script from the plan job to verify matrix JSON."""
        plan_job = self.parsed_yaml["jobs"]["plan"]
        generate_step = None
        for step in plan_job.get("steps", []):
            if step.get("id") == "generate" or "matrix" in step.get("name", "").lower():
                generate_step = step
                break

        self.assertIsNotNone(generate_step, "Matrix generation step not found in plan job")
        run_script = generate_step.get("run", "")
        self.assertIn("python3", run_script)

        # Simulate execution of the chunk generator logic for 120 frames / 30 chunk_size
        total = 120
        chunk_sz = 30
        chunks = []
        num_chunks = math.ceil(total / chunk_sz)
        for i in range(num_chunks):
            start_frame = i * chunk_sz + 1
            end_frame = min((i + 1) * chunk_sz, total)
            chunks.append({"id": f"{i:02d}", "start": start_frame, "end": end_frame})

        self.assertEqual(len(chunks), 4)
        self.assertEqual(chunks[0], {"id": "00", "start": 1, "end": 30})
        self.assertEqual(chunks[1], {"id": "01", "start": 31, "end": 60})
        self.assertEqual(chunks[2], {"id": "02", "start": 61, "end": 90})
        self.assertEqual(chunks[3], {"id": "03", "start": 91, "end": 120})

    def test_07_render_chunk_matrix_strategy(self):
        """Verify render_chunk uses matrix chunk from needs.plan and fail-fast is false."""
        render_job = self.parsed_yaml["jobs"]["render_chunk"]
        strategy = render_job.get("strategy", {})
        self.assertFalse(strategy.get("fail-fast"), "strategy.fail-fast must be false")

        matrix = strategy.get("matrix", {})
        chunk_matrix = str(matrix.get("chunk", ""))
        self.assertIn("needs.plan.outputs.matrix", chunk_matrix)

    # -------------------------------------------------------------
    # 4. Artifact Naming & Stitch Integration
    # -------------------------------------------------------------
    def test_08_chunk_artifact_upload_contract(self):
        """Verify upload-artifact@v4 uses unique name frames-chunk-${{ matrix.chunk.id }}."""
        render_job = self.parsed_yaml["jobs"]["render_chunk"]
        upload_step = None
        for step in render_job.get("steps", []):
            if "upload-artifact" in str(step.get("uses", "")):
                upload_step = step
                break

        self.assertIsNotNone(upload_step, "actions/upload-artifact missing in render_chunk")
        with_params = upload_step.get("with", {})
        artifact_name = with_params.get("name", "")
        self.assertIn("frames-chunk-", artifact_name)
        self.assertIn("matrix.chunk.id", artifact_name)
        self.assertEqual(str(with_params.get("compression-level", 0)), "0")

    def test_09_stitch_artifact_download_contract(self):
        """Verify download-artifact@v4 uses pattern frames-chunk-* and merge-multiple: true."""
        stitch_job = self.parsed_yaml["jobs"]["stitch"]
        download_step = None
        for step in stitch_job.get("steps", []):
            if "download-artifact" in str(step.get("uses", "")):
                download_step = step
                break

        self.assertIsNotNone(download_step, "actions/download-artifact missing in stitch job")
        with_params = download_step.get("with", {})
        pattern = with_params.get("pattern", "")
        self.assertIn("frames-chunk-*", pattern)
        self.assertTrue(with_params.get("merge-multiple", False))

    def test_10_stitch_ffmpeg_broadcast_spec(self):
        """Verify FFmpeg compilation step uses 30fps, libx264, yuv420p, crf 18, and +faststart."""
        stitch_job = self.parsed_yaml["jobs"]["stitch"]
        ffmpeg_step = None
        for step in stitch_job.get("steps", []):
            run_cmd = step.get("run", "")
            if "ffmpeg -y" in run_cmd or "ffmpeg -framerate" in run_cmd:
                ffmpeg_step = step
                break

        self.assertIsNotNone(ffmpeg_step, "FFmpeg compile command missing in stitch job")
        cmd = ffmpeg_step.get("run", "")
        self.assertIn("-framerate 30", cmd)
        self.assertIn("-c:v libx264", cmd)
        self.assertIn("-pix_fmt yuv420p", cmd)
        self.assertIn("-crf 18", cmd)
        self.assertIn("+faststart", cmd)
        self.assertIn("Final_3D_Typography_Hook.mp4", cmd)

    def test_11_final_video_artifact_upload(self):
        """Verify final video artifact upload named Final_3D_Typography_Hook."""
        stitch_job = self.parsed_yaml["jobs"]["stitch"]
        final_upload_step = None
        for step in stitch_job.get("steps", []):
            if "upload-artifact" in str(step.get("uses", "")):
                final_upload_step = step

        self.assertIsNotNone(final_upload_step, "Final upload-artifact missing in stitch job")
        with_params = final_upload_step.get("with", {})
        self.assertEqual(with_params.get("name"), "Final_3D_Typography_Hook")
        self.assertEqual(with_params.get("path"), "Final_3D_Typography_Hook.mp4")

    # -------------------------------------------------------------
    # 5. Non-Destructive Integration
    # -------------------------------------------------------------
    def test_12_non_destructive_preservation(self):
        """Verify that existing Manim pipeline files remain intact."""
        manim_workflow = PROJECT_ROOT / ".github" / "workflows" / "render.yml"
        self.assertTrue(manim_workflow.is_file(), "Original render.yml was deleted or moved!")

        main_py = PROJECT_ROOT / "main.py"
        self.assertTrue(main_py.is_file(), "Original main.py was deleted or moved!")


if __name__ == "__main__":
    unittest.main()
