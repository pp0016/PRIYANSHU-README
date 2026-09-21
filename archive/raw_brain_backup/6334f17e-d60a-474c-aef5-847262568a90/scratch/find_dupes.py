import os
import hashlib
from collections import defaultdict
import json

def get_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096 * 1024), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def find_duplicate_videos(directory):
    video_exts = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm', '.m4v', '.3gp', '.ts', '.m2ts'}
    
    size_map = defaultdict(list)
    
    print(f"Scanning {directory} for videos...")
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} does not exist.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in video_exts:
                full_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(full_path)
                    size_map[size].append(full_path)
                except Exception as e:
                    pass

    hash_map = defaultdict(list)
    
    potential_dupes = {size: paths for size, paths in size_map.items() if len(paths) > 1}
    total_potential = sum(len(paths) for paths in potential_dupes.values())
    print(f"Found {total_potential} files to hash (grouped by identical sizes)...")
    
    processed = 0
    for size, paths in potential_dupes.items():
        for path in paths:
            h = get_hash(path)
            if h:
                hash_map[h].append(path)
            processed += 1
            if processed % 50 == 0:
                print(f"Hashed {processed}/{total_potential} files")
                
    duplicate_groups = [paths for paths in hash_map.values() if len(paths) > 1]
    
    # Sort groups by file size (descending) so we see largest duplicates first
    duplicate_groups.sort(key=lambda paths: os.path.getsize(paths[0]) if paths else 0, reverse=True)
    
    with open('duplicates.json', 'w', encoding='utf-8') as f:
        json.dump(duplicate_groups, f, indent=2, ensure_ascii=False)
        
    print(f"Found {len(duplicate_groups)} duplicate groups.")

if __name__ == '__main__':
    find_duplicate_videos(r"C:\All phones data\mom phone storage")
