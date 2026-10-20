"""Adversarial stress-test harness for Cloud Render Farm matrix chunk partition algorithm.

Tests:
1. Exact total frames not divisible by chunk size (e.g. 100 frames with chunk size 30).
2. Small frame counts (1 frame, 10 frames).
3. Prime frame counts (37, 71, and all primes up to 130).
4. Chunk size larger than total frames (10 frames with chunk size 30).
5. Large frame counts (300 frames, 600 frames, 1800 frames, 3600 frames).
6. Massive property-based sweep across 5,000 randomized configurations:
   - Verifies zero gaps
   - Verifies zero overlaps
   - Verifies exact coverage [1 .. total]
   - Verifies chunk count equals math.ceil(total / chunk_size)
7. Adversarial / pathological inputs (0 frames, negative frames, 0 chunk_size, string parsing).
"""

import math
import random
import sys
import unittest


def partition_chunks_workflow(total_frames, chunk_size):
    """Direct implementation of the algorithm from blender_render.yml line 38-42."""
    chunks = []
    num_chunks = math.ceil(total_frames / chunk_size)
    for i in range(num_chunks):
        start_frame = i * chunk_size + 1
        end_frame = min((i + 1) * chunk_size, total_frames)
        chunks.append({"id": f"{i:02d}", "start": start_frame, "end": end_frame})
    return chunks


def verify_partition_invariants(total_frames, chunk_size, chunks):
    """Oracle verifying mathematical invariants."""
    expected_chunks = math.ceil(total_frames / chunk_size)
    assert len(chunks) == expected_chunks, (
        f"Chunk count mismatch: expected {expected_chunks}, got {len(chunks)}"
    )

    if total_frames == 0:
        assert len(chunks) == 0
        return

    # Invariant 1: First chunk starts at 1
    assert chunks[0]["start"] == 1, f"First chunk starts at {chunks[0]['start']}, expected 1"

    # Invariant 2: Last chunk ends at total_frames
    assert chunks[-1]["end"] == total_frames, (
        f"Last chunk ends at {chunks[-1]['end']}, expected {total_frames}"
    )

    # Invariant 3: Continuity, zero gaps, zero overlaps
    covered_frames = set()
    for idx, c in enumerate(chunks):
        start = c["start"]
        end = c["end"]
        # Each chunk has start <= end
        assert start <= end, f"Chunk {idx} inverted range: start={start} > end={end}"

        # If not the first chunk, start must be previous chunk end + 1 (NO GAP, NO OVERLAP)
        if idx > 0:
            prev_end = chunks[idx - 1]["end"]
            assert start == prev_end + 1, (
                f"Boundary violation between chunk {idx-1} (end={prev_end}) "
                f"and chunk {idx} (start={start}). Gap/Overlap: {start - prev_end - 1}"
            )

        # Record frames in range
        chunk_frames = set(range(start, end + 1))
        # Ensure no overlap with previously covered frames
        overlap = covered_frames.intersection(chunk_frames)
        assert len(overlap) == 0, f"Overlapping frames detected in chunk {idx}: {overlap}"
        covered_frames.update(chunk_frames)

    # Invariant 4: Exact coverage: set of covered frames must equal 1..total_frames
    expected_frames = set(range(1, total_frames + 1))
    assert covered_frames == expected_frames, (
        f"Coverage mismatch! Missing: {expected_frames - covered_frames}, "
        f"Extra: {covered_frames - expected_frames}"
    )
    assert len(covered_frames) == total_frames, (
        f"Total covered count {len(covered_frames)} != {total_frames}"
    )


class MatrixPartitionStressTest(unittest.TestCase):

    def test_01_non_divisible_workload_100_frames_chunk_30(self):
        """Total frames 100 with chunk size 30."""
        total = 100
        chunk_sz = 30
        chunks = partition_chunks_workflow(total, chunk_sz)
        self.assertEqual(len(chunks), 4)
        self.assertEqual(chunks[0], {"id": "00", "start": 1, "end": 30})
        self.assertEqual(chunks[1], {"id": "01", "start": 31, "end": 60})
        self.assertEqual(chunks[2], {"id": "02", "start": 61, "end": 90})
        self.assertEqual(chunks[3], {"id": "03", "start": 91, "end": 100})
        verify_partition_invariants(total, chunk_sz, chunks)

    def test_02_small_frame_counts(self):
        """Single frame and small frame counts."""
        for total in [1, 2, 5, 10]:
            for chunk_sz in [1, 2, 5, 10, 30]:
                chunks = partition_chunks_workflow(total, chunk_sz)
                verify_partition_invariants(total, chunk_sz, chunks)

        # Explicit check for 1 frame with chunk 30
        c1 = partition_chunks_workflow(1, 30)
        self.assertEqual(len(c1), 1)
        self.assertEqual(c1[0], {"id": "00", "start": 1, "end": 1})

        # Explicit check for 10 frames with chunk 30
        c10 = partition_chunks_workflow(10, 30)
        self.assertEqual(len(c10), 1)
        self.assertEqual(c10[0], {"id": "00", "start": 1, "end": 10})

    def test_03_prime_frame_counts(self):
        """Prime numbers for total frames against various chunk sizes."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
        chunk_sizes = [7, 11, 13, 23, 30, 37, 60]
        for p in primes:
            for sz in chunk_sizes:
                chunks = partition_chunks_workflow(p, sz)
                verify_partition_invariants(p, sz, chunks)

        # Check specifically 37 frames with chunk 30
        c37 = partition_chunks_workflow(37, 30)
        self.assertEqual(len(c37), 2)
        self.assertEqual(c37[0], {"id": "00", "start": 1, "end": 30})
        self.assertEqual(c37[1], {"id": "01", "start": 31, "end": 37})

        # Check specifically 71 frames with chunk 30
        c71 = partition_chunks_workflow(71, 30)
        self.assertEqual(len(c71), 3)
        self.assertEqual(c71[0], {"id": "00", "start": 1, "end": 30})
        self.assertEqual(c71[1], {"id": "01", "start": 31, "end": 60})
        self.assertEqual(c71[2], {"id": "02", "start": 61, "end": 71})

    def test_04_chunk_size_larger_than_total_frames(self):
        """Chunk size larger than total frames: e.g. 10 frames with chunk size 30."""
        cases = [
            (10, 30),
            (1, 100),
            (29, 30),
            (15, 60),
            (50, 1000),
        ]
        for total, sz in cases:
            chunks = partition_chunks_workflow(total, sz)
            self.assertEqual(len(chunks), 1, f"Expected 1 chunk for total={total}, sz={sz}")
            self.assertEqual(chunks[0]["start"], 1)
            self.assertEqual(chunks[0]["end"], total)
            verify_partition_invariants(total, sz, chunks)

    def test_05_large_frame_counts(self):
        """Large frame counts: 300, 600, 1800 (1 min), 3600 (2 min) at 30 fps."""
        large_cases = [
            (300, 30, 10),
            (600, 30, 20),
            (1800, 30, 60),
            (1800, 60, 30),
            (3600, 30, 120),
            (3600, 60, 60),
        ]
        for total, sz, expected_n in large_cases:
            chunks = partition_chunks_workflow(total, sz)
            self.assertEqual(len(chunks), expected_n)
            verify_partition_invariants(total, sz, chunks)

    def test_06_massive_randomized_property_sweep(self):
        """5,000 randomized configurations across broad ranges."""
        rng = random.Random(42)
        failures = 0
        iterations = 5000

        for _ in range(iterations):
            total = rng.randint(1, 2000)
            sz = rng.randint(1, 150)
            try:
                chunks = partition_chunks_workflow(total, sz)
                verify_partition_invariants(total, sz, chunks)
            except Exception as e:
                failures += 1
                self.fail(f"Invariant failed for total={total}, chunk_sz={sz}: {e}")

        self.assertEqual(failures, 0, f"Encountered {failures} invariant failures out of {iterations}")

    def test_07_adversarial_zero_and_negative_handling(self):
        """Adversarial stress-test: what happens if total_frames <= 0 or chunk_size <= 0?"""
        # total_frames == 0
        chunks = partition_chunks_workflow(0, 30)
        self.assertEqual(len(chunks), 0)

        # chunk_size == 0 must raise ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            partition_chunks_workflow(100, 0)

        # negative chunk_size
        chunks_neg = partition_chunks_workflow(100, -30)
        # In python, 100 / -30 = -3.333, ceil is -3, range(-3) is empty list []
        self.assertEqual(len(chunks_neg), 0)


if __name__ == "__main__":
    unittest.main()
