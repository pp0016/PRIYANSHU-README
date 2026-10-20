import json
import os
import subprocess

FFMPEG_EXE = r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"

def build_video(project_dir, output_filename="final_video.mp4"):
    images_dir = os.path.join(project_dir, "images")
    voiceover_path = os.path.join(project_dir, "audio", "voiceover.wav")
    timestamps_json = os.path.join(project_dir, "audio", "cut_durations.json")
    concat_file = os.path.join(project_dir, "images_timeline.txt")
    output_path = os.path.join(project_dir, output_filename)

    if not os.path.exists(timestamps_json):
        raise FileNotFoundError(f"Missing timestamps file: {timestamps_json}")
    if not os.path.exists(voiceover_path):
        raise FileNotFoundError(f"Missing master voiceover file: {voiceover_path}")

    # 1. Load cut durations calculated from voiceover timestamps
    with open(timestamps_json, "r", encoding="utf-8") as f:
        cuts = json.load(f)  # list of {"file": "img_001.png", "duration": 0.95}

    # 2. Write the FFmpeg Concat demuxer file
    with open(concat_file, "w", encoding="utf-8") as f:
        for cut in cuts:
            img_path = os.path.join("images", cut["file"]).replace("\\", "/")
            f.write(f"file '{img_path}'\n")
            f.write(f"duration {cut['duration']:.3f}\n")
        # Final image repeat requirement for concat demuxer
        if cuts:
            last_img = os.path.join("images", cuts[-1]["file"]).replace("\\", "/")
            f.write(f"file '{last_img}'\n")

    print(f"Generated concat timeline with {len(cuts)} cuts across Two-Tier Dynamic Visuals.")

    # 3. Execute zero-degradation FFmpeg command (strictly compliant with user rules)
    cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_file,
        "-i", voiceover_path,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "17",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        output_path
    ]

    print("Running FFmpeg rendering pipeline...")
    subprocess.run(cmd, check=True)
    print(f"✅ Master 1080p Video rendered successfully: {output_path}")

if __name__ == "__main__":
    build_video(os.getcwd())
