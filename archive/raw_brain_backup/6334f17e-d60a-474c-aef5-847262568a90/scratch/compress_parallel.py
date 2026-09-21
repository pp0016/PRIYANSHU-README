import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def compress_single_video(original_path):
    dir_name, file_name = os.path.split(original_path)
    base, ext = os.path.splitext(file_name)
    temp_path = os.path.join(dir_name, f"{base}_temp_compressed_parallel{ext}")
    
    file_size = os.path.getsize(original_path)
    print(f"[AGENT START] Worker assigned to: {file_name} ({file_size / (1024*1024):.2f} MB)", flush=True)
    
    cmd = [
        'ffmpeg', '-y', '-i', original_path,
        '-c:v', 'libx264', '-crf', '28', '-preset', 'fast',
        '-c:a', 'aac', '-b:a', '128k',
        temp_path
    ]
    
    start_time = time.time()
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    elapsed = time.time() - start_time
    
    if process.returncode == 0 and os.path.exists(temp_path):
        new_size = os.path.getsize(temp_path)
        if new_size < file_size:
            os.replace(temp_path, original_path)
            saved_mb = (file_size - new_size) / (1024*1024)
            print(f"[AGENT DONE] {file_name} -> {new_size / (1024*1024):.2f} MB (Saved {saved_mb:.2f} MB) in {elapsed:.1f}s", flush=True)
            return file_size, new_size
        else:
            os.remove(temp_path)
            print(f"[AGENT SKIPPED] {file_name} was larger after compression. Kept original.", flush=True)
            return file_size, file_size
    else:
        print(f"[AGENT ERROR] {file_name} failed. Return code: {process.returncode}", flush=True)
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return file_size, file_size

def compress_videos_parallel(directory, max_workers=3):
    video_exts = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.3gp', '.ts', '.m2ts'}
    
    videos = []
    for root, _, files in os.walk(directory):
        for file in files:
            if '_temp_compressed' not in file and os.path.splitext(file)[1].lower() in video_exts:
                videos.append(os.path.join(root, file))

    print(f"Starting Multi-Agent Parallel Compression on {len(videos)} videos with {max_workers} concurrent agents...", flush=True)
    
    total_original = 0
    total_new = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(compress_single_video, v): v for v in videos}
        for future in as_completed(futures):
            orig_sz, new_sz = future.result()
            total_original += orig_sz
            total_new += new_sz
            
    print("\n--- All Agents Finished ---", flush=True)
    print(f"Total Space Saved: {(total_original - total_new) / (1024*1024):.2f} MB", flush=True)

if __name__ == '__main__':
    compress_videos_parallel(r"C:\All phones data\Left5", max_workers=3)
