import os
import subprocess
import shutil
import time

def compress_videos(directory):
    video_exts = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.3gp', '.ts', '.m2ts'}
    
    videos = []
    for root, _, files in os.walk(directory):
        for file in files:
            if '_temp_compressed' not in file and os.path.splitext(file)[1].lower() in video_exts:
                videos.append(os.path.join(root, file))
                
    total_original_size = 0
    total_compressed_size = 0
    success_count = 0
    
    print(f"Found {len(videos)} videos to compress in {directory}", flush=True)
    
    for i, original_path in enumerate(videos, 1):
        file_size = os.path.getsize(original_path)
        total_original_size += file_size
        
        dir_name, file_name = os.path.split(original_path)
        base, ext = os.path.splitext(file_name)
        temp_path = os.path.join(dir_name, f"{base}_temp_compressed{ext}")
        
        print(f"\n[{i}/{len(videos)}] Compressing: {file_name} ({file_size / (1024*1024):.2f} MB)", flush=True)
        
        # -crf 28 as per the standard video-compressor skill (15% quality drop, massive size reduction)
        cmd = [
            'ffmpeg', '-y', '-i', original_path,
            '-c:v', 'libx264', '-crf', '28', '-preset', 'fast',
            '-c:a', 'aac', '-b:a', '128k',
            temp_path
        ]
        
        try:
            start_time = time.time()
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            elapsed = time.time() - start_time
            
            if process.returncode == 0 and os.path.exists(temp_path):
                new_size = os.path.getsize(temp_path)
                
                if new_size < file_size:
                    os.replace(temp_path, original_path)
                    total_compressed_size += new_size
                    success_count += 1
                    saved_mb = (file_size - new_size) / (1024*1024)
                    print(f"  -> Success! Compressed to {new_size / (1024*1024):.2f} MB. Saved {saved_mb:.2f} MB. Took {elapsed:.1f}s.", flush=True)
                else:
                    os.remove(temp_path)
                    total_compressed_size += file_size
                    print(f"  -> Skipped. Compressed file was larger ({new_size / (1024*1024):.2f} MB). Kept original.", flush=True)
            else:
                print(f"  -> FFmpeg failed with return code {process.returncode}", flush=True)
                total_compressed_size += file_size
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
        except Exception as e:
            print(f"  -> Error processing {file_name}: {e}", flush=True)
            total_compressed_size += file_size
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
    saved_total = total_original_size - total_compressed_size
    print(f"\n--- Compression Complete ---", flush=True)
    print(f"Processed {len(videos)} videos.", flush=True)
    print(f"Original Size: {total_original_size / (1024*1024):.2f} MB", flush=True)
    print(f"New Size: {total_compressed_size / (1024*1024):.2f} MB", flush=True)
    print(f"Total Space Saved: {saved_total / (1024*1024):.2f} MB", flush=True)

if __name__ == '__main__':
    compress_videos(r"C:\All phones data\Left5")
