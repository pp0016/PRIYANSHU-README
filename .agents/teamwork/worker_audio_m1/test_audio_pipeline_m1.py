"""
Unit and Verification Tests for Clean Audio Master Pipeline (Worker M1)
========================================================================
Validates audio_pipeline.py and the master output audio_clean_30s.wav.
"""

import unittest
import os
import wave
import numpy as np

MASTER_WAV = r"C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\audio_clean_30s.wav"
SFX_WAV = r"C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\clean_sfx_30s.wav"
PIPELINE_SCRIPT = r"C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\audio_pipeline.py"


class TestAudioPipelineM1(unittest.TestCase):
    def test_01_pipeline_script_exists(self):
        self.assertTrue(os.path.isfile(PIPELINE_SCRIPT), f"Missing script: {PIPELINE_SCRIPT}")
        self.assertGreater(os.path.getsize(PIPELINE_SCRIPT), 500, "Script file is unexpectedly small")

    def test_02_master_wav_exists_and_size(self):
        self.assertTrue(os.path.isfile(MASTER_WAV), f"Missing master WAV: {MASTER_WAV}")
        # 1,440,000 samples * 2 channels * 2 bytes/sample + 78 bytes header = 5,760,078 bytes
        expected_size = 5760078
        self.assertEqual(os.path.getsize(MASTER_WAV), expected_size, f"File size mismatch: {os.path.getsize(MASTER_WAV)} != {expected_size}")

    def test_03_master_wav_pcm_format(self):
        with wave.open(MASTER_WAV, "rb") as wf:
            self.assertEqual(wf.getnchannels(), 2, "Expected stereo (2 channels)")
            self.assertEqual(wf.getsampwidth(), 2, "Expected 16-bit PCM (sample width 2)")
            self.assertEqual(wf.getframerate(), 48000, "Expected 48,000 Hz sample rate")
            self.assertEqual(wf.getnframes(), 1440000, "Expected exactly 1,440,000 frames/samples")
            duration = wf.getnframes() / float(wf.getframerate())
            self.assertAlmostEqual(duration, 30.000000, places=6, msg="Expected precisely 30.000000s duration")

    def test_04_sfx_track_format(self):
        self.assertTrue(os.path.isfile(SFX_WAV), f"Missing SFX WAV: {SFX_WAV}")
        with wave.open(SFX_WAV, "rb") as wf:
            self.assertEqual(wf.getnchannels(), 2, "Expected stereo SFX")
            self.assertEqual(wf.getframerate(), 48000, "Expected 48,000 Hz SFX sample rate")
            self.assertEqual(wf.getnframes(), 1440000, "Expected 1,440,000 SFX frames")

    def test_05_siren_window_dead_silence_in_sfx(self):
        with wave.open(SFX_WAV, "rb") as wf:
            sr = wf.getframerate()
            start_frame = int(8.16 * sr)
            end_frame = int(9.56 * sr)
            wf.setpos(start_frame)
            raw = wf.readframes(end_frame - start_frame)
            sampwidth = wf.getsampwidth()
            if sampwidth == 3:
                raw_bytes_arr = np.frombuffer(raw, dtype=np.uint8)
                raw_24 = raw_bytes_arr.reshape(-1, 3)
                int_32 = (raw_24[:, 0].astype(np.int32) |
                          (raw_24[:, 1].astype(np.int32) << 8) |
                          (raw_24[:, 2].astype(np.int32) << 16))
                int_32[int_32 >= 0x800000] -= 0x1000000
                samples = int_32.astype(np.float32) / 8388608.0
            else:
                samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

            peak = np.max(np.abs(samples))
            rms = np.sqrt(np.mean(samples ** 2))
            # Peak must be strictly below 0.0001 (noise floor is ~0.000009)
            self.assertLess(peak, 0.0001, f"Unexpected energy in siren window [8.16s - 9.56s]: peak={peak}")
            self.assertLess(rms, 0.00001, f"Unexpected RMS energy in siren window [8.16s - 9.56s]: rms={rms}")

    def test_06_master_audio_siren_orthogonality(self):
        # Generate exact siren waveform reference
        sr = 48000
        dur = 1.4
        t = np.linspace(0, dur, int(sr * dur), False)
        f = 850 + 260 * np.sin(2 * np.pi * 1.5 * t)
        phase = 2 * np.pi * np.cumsum(f) / sr
        sig = 0.45 * np.sin(phase) + 0.2 * np.sin(2 * phase)
        env = np.minimum(t / 0.08, 1.0) * np.minimum((dur - t) / 0.15, 1.0)
        siren_ref = (sig * env).astype(np.float32)

        with wave.open(MASTER_WAV, "rb") as wf:
            wf.setpos(int(8.16 * 48000))
            raw = wf.readframes(len(siren_ref))
            samples = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
            mixed_mono = samples.reshape(-1, 2).mean(axis=1)

        dot = np.dot(mixed_mono, siren_ref)
        norm = np.linalg.norm(mixed_mono) * np.linalg.norm(siren_ref)
        correlation = abs(dot / (norm + 1e-12))
        self.assertLess(correlation, 0.02, f"Residual correlation with police siren: {correlation}")


if __name__ == "__main__":
    unittest.main()
