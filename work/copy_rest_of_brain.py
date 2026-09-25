import os
import glob
import shutil
import re

brain_dir = r"C:\Users\renu5\.gemini\antigravity\brain"
target_dir = r"c:\Users\renu5\Downloads\priyanshu readme\archive\raw_brain_backup"

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
        if re.search(r'cfut_[a-zA-Z0-9]{40,}', content):
            content = re.sub(r'cfut_[a-zA-Z0-9]{40,}', '[REDACTED_CLOUDFLARE]', content)
            modified = True
        if re.search(r'sk-or-v1-[a-zA-Z0-9]{64}', content):
            content = re.sub(r'sk-or-v1-[a-zA-Z0-9]{64}', '[REDACTED_OPENROUTER]', content)
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    except:
        pass

def main():
    folders = [f for f in os.listdir(brain_dir) if len(f) == 36]
    count = 0
    for folder_name in folders:
        src = os.path.join(brain_dir, folder_name)
        dst = os.path.join(target_dir, folder_name)
        if not os.path.exists(dst):
            try:
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns('tempmediaStorage'))
                print(f"Copied missing: {folder_name}")
                count += 1
                for root, dirs, files in os.walk(dst):
                    for file in files:
                        clean_secrets_in_file(os.path.join(root, file))
            except Exception as e:
                pass
    print(f"Copied {count} remaining folders.")

if __name__ == "__main__":
    main()
