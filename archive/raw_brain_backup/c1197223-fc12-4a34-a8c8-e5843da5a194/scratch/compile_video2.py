import cv2
import glob
import os
import re

render_dir = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\scratch\frames2"
output_video_path = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\stickman_pro.mp4"

def get_frame_num(path):
    m = re.search(r'frame_(\d+)', path)
    return int(m.group(1)) if m else 0

frames = sorted(glob.glob(os.path.join(render_dir, "*.png")), key=get_frame_num)

if not frames:
    print("No frames found!")
    exit(1)
    
img = cv2.imread(frames[0])
height, width, layers = img.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

for frame in frames:
    video.write(cv2.imread(frame))

video.release()
print(f"Video saved to {output_video_path}")
