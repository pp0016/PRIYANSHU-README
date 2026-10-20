"""
Central Test Runner: Manim 05-Cel-Boil Audiobook Summary Replication
Executes all 4 Tiers of Opaque-Box E2E Tests with ANSI Table & JSON Reporting.
"""

import os
import sys
import time
import json
import unittest
import argparse
from pathlib import Path

# Add tests directory to sys.path
TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

import test_tier1_feature_coverage
import test_tier2_boundary_cases
import test_tier3_integration
import test_tier4_acceptance


def run_tier_suite(tier_name: str, test_case_cls, verbosity: int = 1) -> dict:
    """Run an individual test suite and return structured metrics."""
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_case_cls)
    start_time = time.perf_counter()
    runner = unittest.TextTestRunner(verbosity=verbosity, stream=sys.stderr)
    result = runner.run(suite)
    elapsed = time.perf_counter() - start_time

    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    skipped = len(result.skipped)
    passed = total - (failures + errors + skipped)

    failure_details = []
    for test, traceback_str in result.failures:
        failure_details.append({"test": str(test), "type": "FAIL", "trace": traceback_str})
    for test, traceback_str in result.errors:
        failure_details.append({"test": str(test), "type": "ERROR", "trace": traceback_str})

    return {
        "tier_name": tier_name,
        "total": total,
        "passed": passed,
        "failed": failures,
        "errors": errors,
        "skipped": skipped,
        "elapsed": elapsed,
        "failure_details": failure_details,
    }


def main():
    parser = argparse.ArgumentParser(description="Run E2E Test Suite for Manim Cel-Boil")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4], help="Run only a specific tier (1-4)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose test execution")
    parser.add_argument("--json", type=str, default="test_results.json", help="Path to write JSON test report")
    args = parser.parse_args()

    verbosity = 2 if args.verbose else 0

    tier_configs = [
        (1, "Tier 1: Feature Coverage", test_tier1_feature_coverage.TestTier1FeatureCoverage),
        (2, "Tier 2: Boundary & Corner Cases", test_tier2_boundary_cases.TestTier2BoundaryCases),
        (3, "Tier 3: Cross-Feature Integration", test_tier3_integration.TestTier3Integration),
        (4, "Tier 4: Acceptance / Real-World", test_tier4_acceptance.TestTier4Acceptance),
    ]

    if args.tier:
        tier_configs = [c for c in tier_configs if c[0] == args.tier]

    print("\n" + "=" * 85)
    print("TEST SUITE EXECUTION: MANIM 05-CEL-BOIL AUDIOBOOK SUMMARY REPLICATION")
    print("=" * 85)

    tier_results = []
    total_tests = 0
    total_passed = 0
    total_failed = 0
    total_errors = 0
    total_skipped = 0
    total_time = 0.0

    for tier_num, tier_title, test_cls in tier_configs:
        res = run_tier_suite(tier_title, test_cls, verbosity=verbosity)
        tier_results.append(res)
        total_tests += res["total"]
        total_passed += res["passed"]
        total_failed += res["failed"]
        total_errors += res["errors"]
        total_skipped += res["skipped"]
        total_time += res["elapsed"]

    # Render ANSI summary table
    print("\n" + "-" * 85)
    print(f"{'Test Suite Tier':<36} | {'Total':<6} | {'Pass':<6} | {'Fail':<6} | {'Error':<6} | {'Skip':<6} | {'Time (s)':<8}")
    print("-" * 85)

    for r in tier_results:
        print(f"{r['tier_name']:<36} | {r['total']:<6} | {r['passed']:<6} | {r['failed']:<6} | {r['errors']:<6} | {r['skipped']:<6} | {r['elapsed']:<8.3f}")

    print("-" * 85)
    print(f"{'TOTAL':<36} | {total_tests:<6} | {total_passed:<6} | {total_failed:<6} | {total_errors:<6} | {total_skipped:<6} | {total_time:<8.3f}")
    print("=" * 85)

    effective_total = total_tests - total_skipped
    pass_rate = (total_passed / effective_total * 100.0) if effective_total > 0 else 100.0
    print(f"FINAL PASS RATE : {pass_rate:.1f}% ({total_passed}/{effective_total} active passed, {total_skipped} skipped)")
    print("=" * 85 + "\n")

    # Export structured JSON report
    report_data = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {
            "total": total_tests,
            "passed": total_passed,
            "failed": total_failed,
            "errors": total_errors,
            "skipped": total_skipped,
            "pass_rate_pct": round(pass_rate, 2),
            "total_elapsed_seconds": round(total_time, 3),
        },
        "tiers": tier_results,
    }

    # Save to requested JSON path and inside tests dir
    json_path = Path(args.json)
    if not json_path.is_absolute():
        json_path = Path(r"c:\Users\renu5\Downloads\priyanshu readme") / json_path
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)
    print(f"Report JSON exported to: {json_path}")

    # Also save to tests_cel_boil/test_results.json
    local_json = TESTS_DIR / "test_results.json"
    with open(local_json, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)

    # Print any failure details
    all_failures = []
    for r in tier_results:
        all_failures.extend(r["failure_details"])

    if all_failures:
        print("\nFAILURE TRACES:")
        for idx, f in enumerate(all_failures, 1):
            print(f"[{idx}] {f['type']}: {f['test']}")
            print(f['trace'])
            print("-" * 50)
        sys.exit(1)
    else:
        print("ALL TESTS PASSED WITH ZERO INTEGRITY DEFECTS.")
        sys.exit(0)


if __name__ == "__main__":
    main()
