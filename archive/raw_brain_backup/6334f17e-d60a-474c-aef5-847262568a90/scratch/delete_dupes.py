import json
import os

with open('duplicates.json', 'r', encoding='utf-8') as f:
    duplicates = json.load(f)

total_bytes_cleared = 0
deleted_files = []

for group in duplicates:
    for file_path in group:
        if 'for laptop' in file_path:
            try:
                size = os.path.getsize(file_path)
                os.remove(file_path)
                total_bytes_cleared += size
                deleted_files.append(file_path)
                print(f"Deleted: {file_path} ({size / (1024*1024):.2f} MB)")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

total_mb = total_bytes_cleared / (1024 * 1024)
print(f"\nSuccessfully deleted {len(deleted_files)} duplicate files from the 'for laptop' folder.")
print(f"Total space cleared: {total_mb:.2f} MB")
