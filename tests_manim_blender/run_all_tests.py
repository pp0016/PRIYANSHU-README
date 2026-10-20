"""Central Automated Test Runner for Blender 3D Motion Graphics & Cloud Render Farm.

Discovers and executes:
- Tier 1: Feature Coverage (Headless execution, typography curves, PBR materials, lights, camera, Cycles CPU)
- Tier 2: Boundary Cases (Single-frame, extreme strings, unicode Hindi, sampling limits, path formats, chunk math)
- Tier 3: Workflow Integration (GitHub Actions YAML schema, DAG dependencies, matrix planning, artifacts, FFmpeg)
- Tier 4: Real-World Scenarios (Binary PNG inspection, PIL validation, FFmpeg broadcast stitching, ffprobe verification)

Produces structured ANSI console reports and machine-readable JSON artifacts.
"""

import os
import sys
import time
import json
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
    find_blender_binary,
    get_blender_version,
    find_ffmpeg_binary,
    find_ffprobe_binary,
)

import test_tier1_feature_coverage
import test_tier2_boundary_cases
import test_tier3_workflow_integration
import test_tier4_real_world_scenarios


class StructuredTestResult(unittest.TestResult):
    """Custom test result collector capturing timing, descriptions, and statuses."""

    def __init__(self):
        super().__init__()
        self.test_records = []
        self._test_start = None

    def startTest(self, test):
        super().startTest(test)
        self._test_start = time.perf_counter()

    def addSuccess(self, test):
        super().addSuccess(test)
        elapsed = time.perf_counter() - self._test_start
        self._record(test, "PASSED", elapsed)

    def addError(self, test, err):
        super().addError(test, err)
        elapsed = time.perf_counter() - self._test_start
        self._record(test, "ERROR", elapsed, str(err[1]))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        elapsed = time.perf_counter() - self._test_start
        self._record(test, "FAILED", elapsed, str(err[1]))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        elapsed = time.perf_counter() - self._test_start
        self._record(test, "SKIPPED", elapsed, reason)

    def _record(self, test, status, elapsed, message=None):
        doc = test.shortDescription() or ""
        self.test_records.append({
            "id": test.id(),
            "name": test._testMethodName,
            "description": doc.strip(),
            "status": status,
            "duration_seconds": round(elapsed, 4),
            "message": message,
        })


def run_suite(json_output_path="test_results.json"):
    """Execute all test tiers, display structured console report, and save JSON artifact."""
    print("=" * 80)
    print("3D MOTION GRAPHICS PIPELINE & CLOUD RENDER FARM: E2E TEST SUITE")
    print("=" * 80)

    # 1. Environment Banner
    blender_bin = find_blender_binary()
    blender_ver = get_blender_version(blender_bin) if blender_bin else "NOT FOUND"
    ffmpeg_bin = find_ffmpeg_binary()
    ffprobe_bin = find_ffprobe_binary()

    print(f"Blender Executable : {blender_bin} ({blender_ver})")
    print(f"FFmpeg Executable  : {ffmpeg_bin}")
    print(f"FFprobe Executable : {ffprobe_bin}")
    print(f"Python Version     : {sys.version.split()[0]}")
    print(f"Repository Root    : {PROJECT_ROOT}")
    print("-" * 80)

    # 2. Test Suite Setup
    tiers = [
        ("Tier 1: Feature Coverage", test_tier1_feature_coverage),
        ("Tier 2: Boundary & Corner Cases", test_tier2_boundary_cases),
        ("Tier 3: Workflow Integration", test_tier3_workflow_integration),
        ("Tier 4: Real-World Scenarios", test_tier4_real_world_scenarios),
    ]

    tier_summaries = []
    all_records = []
    overall_start = time.perf_counter()

    for tier_name, module in tiers:
        print(f"\n[RUNNING] {tier_name}...")
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(module)
        result = StructuredTestResult()

        t_start = time.perf_counter()
        suite.run(result)
        t_elapsed = time.perf_counter() - t_start

        passed = len([r for r in result.test_records if r["status"] == "PASSED"])
        failed = len(result.failures)
        errored = len(result.errors)
        skipped = len(result.skipped)
        total = result.testsRun

        tier_summaries.append({
            "tier": tier_name,
            "total": total,
            "passed": passed,
            "failed": failed,
            "errored": errored,
            "skipped": skipped,
            "duration_seconds": round(t_elapsed, 3),
        })
        all_records.extend(result.test_records)

        # Print per-test execution status
        for r in result.test_records:
            status_tag = f"[{r['status']}]"
            padding = " " * (9 - len(r['status']))
            print(f"  {status_tag}{padding} {r['name']} ({r['duration_seconds']}s) - {r['description']}")

    overall_elapsed = time.perf_counter() - overall_start

    # 3. Formatted Summary Table
    print("\n" + "=" * 80)
    print("EXECUTION SUMMARY")
    print("=" * 80)
    header = f"{'Test Suite Tier':<36} | {'Total':<6} | {'Pass':<6} | {'Fail':<6} | {'Error':<6} | {'Time (s)':<8}"
    print(header)
    print("-" * len(header))

    total_tests = sum(s["total"] for s in tier_summaries)
    total_passed = sum(s["passed"] for s in tier_summaries)
    total_failed = sum(s["failed"] for s in tier_summaries)
    total_errored = sum(s["errored"] for s in tier_summaries)

    for s in tier_summaries:
        print(
            f"{s['tier']:<36} | {s['total']:<6} | {s['passed']:<6} | {s['failed']:<6} | "
            f"{s['errored']:<6} | {s['duration_seconds']:<8.3f}"
        )

    print("-" * len(header))
    print(
        f"{'TOTAL':<36} | {total_tests:<6} | {total_passed:<6} | {total_failed:<6} | "
        f"{total_errored:<6} | {round(overall_elapsed, 3):<8.3f}"
    )
    print("=" * 80)

    pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0.0
    print(f"FINAL PASS RATE : {pass_rate:.1f}% ({total_passed}/{total_tests} passed)")

    # 4. Export JSON Report
    report_data = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "environment": {
            "blender_path": blender_bin,
            "blender_version": blender_ver,
            "ffmpeg_path": ffmpeg_bin,
            "ffprobe_path": ffprobe_bin,
            "python_version": sys.version,
            "target_repository": str(PROJECT_ROOT),
        },
        "summary": {
            "total": total_tests,
            "passed": total_passed,
            "failed": total_failed,
            "errored": total_errored,
            "pass_rate_percent": round(pass_rate, 2),
            "duration_seconds": round(overall_elapsed, 3),
        },
        "tier_summaries": tier_summaries,
        "test_cases": all_records,
    }

    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)

    print(f"Structured JSON report exported to: {json_output_path}")

    if total_failed == 0 and total_errored == 0:
        print("\n>>> ALL TESTS PASSED SUCCESSFULLY! SUITE VERIFICATION COMPLETE. <<<\n")
        return 0
    else:
        print("\n>>> TEST SUITE FAILED. DEFECTS DETECTED. <<<\n")
        return 1


if __name__ == "__main__":
    exit_code = run_suite("test_results.json")
    sys.exit(exit_code)
