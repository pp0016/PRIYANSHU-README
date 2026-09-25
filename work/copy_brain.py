import os
import glob
import shutil
import re
import json

brain_dir = r"C:\Users\renu5\.gemini\antigravity\brain"
target_dir = r"c:\Users\renu5\Downloads\priyanshu readme\archive\raw_brain_backup"

os.makedirs(target_dir, exist_ok=True)

def clean_secrets_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        if re.search(r'gsk_[a-zA-Z0-9]{40,}', content):
            content = re.sub(r'gsk_[a-zA-Z0-9]{40,}', '[REDACTED_GROQ]', content)
            modified = True
        if re.search(r'ghp_[a-zA-Z0-9]{30,}', content):
            content = re.sub(r'ghp_[a-zA-Z0-9]{30,}', '[REDACTED_GITHUB]', content)
            modified = True
        if re.search(r'github_pat_[a-zA-Z0-9_]{50,}', content):
            content = re.sub(r'github_pat_[a-zA-Z0-9_]{50,}', '[REDACTED_GITHUB_PAT]', content)
            modified = True
        if re.search(r'AIza[a-zA-Z0-9_\\-]{35}', content):
            content = re.sub(r'AIza[a-zA-Z0-9_\\-]{35}', '[REDACTED_GCP]', content)
            modified = True
        if re.search(r'AQ\.[A-Za-z0-9\-_]{40,}', content):
            content = re.sub(r'AQ\.[A-Za-z0-9\-_]{40,}', '[REDACTED_GCP_TOKEN]', content)
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(f"Failed to clean {filepath}: {e}")

def main():
    folders = glob.glob(os.path.join(brain_dir, "*", ".system_generated", "logs", "transcript.jsonl"))
    
    relevant_folders = []
    
    for path in folders:
        is_relevant = False
        try:
            with open(path, 'r', encoding='utf-8') as f:
                # read first 1000 lines to check relevance quickly
                count = 0
                for line in f:
                    if count > 1000: break
                    if "priyanshu readme" in line.lower() or "stickman" in line.lower():
                        is_relevant = True
                        break
                    count += 1
        except:
            pass
            
        if is_relevant:
            folder_path = os.path.dirname(os.path.dirname(os.path.dirname(path)))
            relevant_folders.append(folder_path)
            
    print(f"Found {len(relevant_folders)} relevant folders.")
    
    for folder in relevant_folders:
        folder_name = os.path.basename(folder)
        dest_folder = os.path.join(target_dir, folder_name)
        
        if not os.path.exists(dest_folder):
            shutil.copytree(folder, dest_folder, ignore=shutil.ignore_patterns('tempmediaStorage'))
            print(f"Copied {folder_name}")
            
            # Clean secrets in all files in the copied folder
            for root, dirs, files in os.walk(dest_folder):
                for file in files:
                    clean_secrets_in_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
