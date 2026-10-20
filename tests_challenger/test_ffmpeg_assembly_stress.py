"""Adversarial stress-test harness for FFmpeg video assembly and MP4 faststart moov atom verification.

Empirically tests:
1. Exact workflow FFmpeg command flags:
   -framerate 30 -start_number 1 -i "frame_%05d.png" -c:v libx264 -profile:v high -level:v 4.2 -pix_fmt yuv420p -preset slow -crf 18 -movflags +faststart
2. ffprobe metadata verification:
   - Codec: H.264 (AVC)
   - Profile: High
   - Level: 42 (4.2)
   - Pixel Format: yuv420p (8-bit 4:2:0 planar chroma subsampling)
   - Frame Rate: 30 fps
   - Frame Count: exactly 30 frames
   - Resolution: 1920x1080
   - Duration: 1.000s
3. Binary ISO-BMFF (MP4) box/atom parser:
   - Verifies `moov` atom offset < `mdat` atom offset when `+faststart` is used.
   - Negative control: compiles identical frames WITHOUT `+faststart` and confirms `mdat` appears before `moov`.
4. Boundary condition: 1-frame video compilation and ffprobe validation.
5. Missing frame behavior:
   - Tests FFmpeg sequence stopping behavior when a gap exists (e.g. frames 1..4, 6..10).
   - Verifies why frame completeness and contiguous numbering validation are critical.
"""

import json
import os
import shutil
import struct
import subprocess
import sys
import unittest

from PIL import Image, ImageDraw


TEST_OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_ffmpeg_scratch"))


def parse_mp4_atoms(file_path):
    """Parse top-level atoms/boxes of an MP4/MOV file.
    
    Returns a list of dicts: [{'type': 'ftyp', 'offset': 0, 'size': 32}, ...]
    """
    atoms = []
    with open(file_path, "rb") as f:
        file_size = os.path.getsize(file_path)
        offset = 0
        while offset < file_size:
            f.seek(offset)
            header = f.read(8)
            if len(header) < 8:
                break
            size = struct.unpack(">I", header[0:4])[0]
            atom_type = header[4:8].decode("ascii", errors="replace")

            if size == 1:
                # 64-bit extended size
                ext_header = f.read(8)
                if len(ext_header) < 8:
                    break
                size = struct.unpack(">Q", ext_header)[0]
            elif size == 0:
                # Atom extends to EOF
                size = file_size - offset

            atoms.append({"type": atom_type, "offset": offset, "size": size})
            if size <= 0:
                break
            offset += size
    return atoms


def generate_png_sequence(dir_path, count, width=1920, height=1080, start_number=1, skip_numbers=None):
    """Generate clean synthetic test PNG images with frame numbers drawn."""
    os.makedirs(dir_path, exist_ok=True)
    skip = set(skip_numbers or [])
    created = []
    for i in range(start_number, start_number + count):
        if i in skip:
            continue
        img = Image.new("RGBA", (width, height), color=(15, 20, 30, 255))
        draw = ImageDraw.Draw(img)
        # Draw frame number
        draw.text((100, 100), f"FRAME {i:05d}", fill=(255, 215, 0, 255))
        draw.rectangle([200, 200, 400, 400], fill=(0, 230, 255, 255))
        filepath = os.path.join(dir_path, f"frame_{i:05d}.png")
        img.save(filepath, format="PNG")
        created.append(filepath)
    return created


def run_ffmpeg(args):
    """Run ffmpeg subprocess and return CompletedProcess."""
    cmd = ["ffmpeg"] + args
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return res


def run_ffprobe(file_path):
    """Extract stream and format info as JSON using ffprobe."""
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "stream=codec_name,profile,level,width,height,pix_fmt,r_frame_rate,avg_frame_rate,nb_frames,duration",
        "-show_entries", "format=format_name,duration,size,bit_rate",
        "-of", "json",
        file_path,
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"ffprobe failed: {res.stderr}")
    return json.loads(res.stdout)


class FFmpegAssemblyStressTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_OUTPUT_DIR):
            shutil.rmtree(TEST_OUTPUT_DIR)
        os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        # Keep scratch or cleanup if needed
        pass

    def test_01_standard_30fps_broadcast_compilation(self):
        """Compile a 30-frame sequence (1.0 sec @ 30fps) with full broadcast flags."""
        seq_dir = os.path.join(TEST_OUTPUT_DIR, "seq_30")
        generate_png_sequence(seq_dir, count=30, start_number=1)

        out_mp4 = os.path.join(TEST_OUTPUT_DIR, "output_broadcast.mp4")
        ffmpeg_args = [
            "-y",
            "-framerate", "30",
            "-start_number", "1",
            "-i", os.path.join(seq_dir, "frame_%05d.png"),
            "-c:v", "libx264",
            "-profile:v", "high",
            "-level:v", "4.2",
            "-pix_fmt", "yuv420p",
            "-preset", "slow",
            "-crf", "18",
            "-movflags", "+faststart",
            out_mp4,
        ]
        res = run_ffmpeg(ffmpeg_args)
        self.assertEqual(res.returncode, 0, f"FFmpeg failed with error:\n{res.stderr}")
        self.assertTrue(os.path.exists(out_mp4), "Output MP4 was not created")

        # ffprobe inspection
        info = run_ffprobe(out_mp4)
        streams = info.get("streams", [])
        self.assertGreater(len(streams), 0, "No video stream found")
        v = streams[0]

        self.assertEqual(v.get("codec_name"), "h264", "Codec must be h264")
        self.assertEqual(v.get("profile"), "High", "Profile must be High")
        self.assertEqual(v.get("level"), 42, "Level must be 42 (4.2)")
        self.assertEqual(v.get("pix_fmt"), "yuv420p", "Pixel format must be yuv420p")
        self.assertEqual(v.get("width"), 1920, "Width must be 1920")
        self.assertEqual(v.get("height"), 1080, "Height must be 1080")
        self.assertEqual(v.get("r_frame_rate"), "30/1", "Frame rate must be 30 fps")
        self.assertEqual(v.get("nb_frames"), "30", "nb_frames must equal 30")

        dur = float(v.get("duration", 0))
        self.assertAlmostEqual(dur, 1.0, places=2, msg=f"Duration {dur}s not close to 1.0s")

    def test_02_moov_atom_faststart_binary_verification(self):
        """Binary inspection: verify moov atom is placed before mdat atom with +faststart."""
        out_faststart = os.path.join(TEST_OUTPUT_DIR, "output_broadcast.mp4")
        atoms_fs = parse_mp4_atoms(out_faststart)
        atom_names_fs = [a["type"] for a in atoms_fs]

        self.assertIn("moov", atom_names_fs, "moov atom not found in MP4")
        self.assertIn("mdat", atom_names_fs, "mdat atom not found in MP4")

        moov_idx_fs = atom_names_fs.index("moov")
        mdat_idx_fs = atom_names_fs.index("mdat")

        moov_offset_fs = atoms_fs[moov_idx_fs]["offset"]
        mdat_offset_fs = atoms_fs[mdat_idx_fs]["offset"]

        self.assertLess(
            moov_offset_fs,
            mdat_offset_fs,
            f"moov offset ({moov_offset_fs}) must be BEFORE mdat offset ({mdat_offset_fs}) for faststart!",
        )

        # Counter-verification: Compile identical video WITHOUT -movflags +faststart
        seq_dir = os.path.join(TEST_OUTPUT_DIR, "seq_30")
        out_no_faststart = os.path.join(TEST_OUTPUT_DIR, "output_no_faststart.mp4")
        ffmpeg_args_no_fs = [
            "-y",
            "-framerate", "30",
            "-start_number", "1",
            "-i", os.path.join(seq_dir, "frame_%05d.png"),
            "-c:v", "libx264",
            "-profile:v", "high",
            "-level:v", "4.2",
            "-pix_fmt", "yuv420p",
            "-preset", "slow",
            "-crf", "18",
            out_no_faststart,
        ]
        res = run_ffmpeg(ffmpeg_args_no_fs)
        self.assertEqual(res.returncode, 0, f"FFmpeg without faststart failed: {res.stderr}")

        atoms_no_fs = parse_mp4_atoms(out_no_faststart)
        atom_names_no_fs = [a["type"] for a in atoms_no_fs]
        moov_idx_no_fs = atom_names_no_fs.index("moov")
        mdat_idx_no_fs = atom_names_no_fs.index("mdat")

        moov_offset_no_fs = atoms_no_fs[moov_idx_no_fs]["offset"]
        mdat_offset_no_fs = atoms_no_fs[mdat_idx_no_fs]["offset"]

        # Without faststart, mdat comes BEFORE moov
        self.assertGreater(
            moov_offset_no_fs,
            mdat_offset_no_fs,
            f"Without +faststart, mdat ({mdat_offset_no_fs}) must precede moov ({moov_offset_no_fs})!",
        )

    def test_03_single_frame_video_boundary_case(self):
        """Boundary condition: compile a single frame into a valid MP4."""
        seq_dir = os.path.join(TEST_OUTPUT_DIR, "seq_single")
        generate_png_sequence(seq_dir, count=1, start_number=1)

        out_single = os.path.join(TEST_OUTPUT_DIR, "output_single_frame.mp4")
        ffmpeg_args = [
            "-y",
            "-framerate", "30",
            "-start_number", "1",
            "-i", os.path.join(seq_dir, "frame_%05d.png"),
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-crf", "18",
            "-movflags", "+faststart",
            out_single,
        ]
        res = run_ffmpeg(ffmpeg_args)
        self.assertEqual(res.returncode, 0, f"FFmpeg 1-frame failed: {res.stderr}")

        info = run_ffprobe(out_single)
        v = info["streams"][0]
        self.assertEqual(v["codec_name"], "h264")
        self.assertEqual(v["nb_frames"], "1")
        self.assertAlmostEqual(float(v["duration"]), 1.0 / 30.0, places=2)

    def test_04_missing_frame_sequence_behavior(self):
        """Adversarial scenario: a gap exists in the frame numbering (e.g. frame 5 missing in 10 frames)."""
        seq_dir = os.path.join(TEST_OUTPUT_DIR, "seq_gap")
        generate_png_sequence(seq_dir, count=10, start_number=1, skip_numbers=[5])

        out_gap = os.path.join(TEST_OUTPUT_DIR, "output_gap.mp4")
        ffmpeg_args = [
            "-y",
            "-framerate", "30",
            "-start_number", "1",
            "-i", os.path.join(seq_dir, "frame_%05d.png"),
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-crf", "18",
            "-movflags", "+faststart",
            out_gap,
        ]
        res = run_ffmpeg(ffmpeg_args)
        self.assertEqual(res.returncode, 0)

        # Inspect frames encoded
        info = run_ffprobe(out_gap)
        v = info["streams"][0]
        encoded_frames = int(v["nb_frames"])

        # FFmpeg image sequence pattern 'frame_%05d.png' STOPS encoding when a sequence number is missing!
        # Since frame 5 was missing, it only encoded frames 1, 2, 3, 4!
        self.assertEqual(
            encoded_frames,
            4,
            f"Expected FFmpeg to halt at missing frame 5 (encoding only 4 frames), got {encoded_frames}",
        )


if __name__ == "__main__":
    unittest.main()
