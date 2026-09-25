import os
import json
import glob

brain_dir = r"C:\Users\renu5\.gemini\antigravity\brain"
pushed_dir = r"c:\Users\renu5\Downloads\priyanshu readme\archive\past_chats"
output_report = r"c:\Users\renu5\Downloads\priyanshu readme\work\chat_backup_status.md"

def get_chat_preview(session_id):
    path = os.path.join(brain_dir, session_id, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(path):
        return "No transcript found"
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get('type') == 'USER_INPUT':
                        text = data.get('content', '').replace('\n', ' ')
                        return text[:80] + "..." if len(text) > 80 else text
                except:
                    pass
    except:
        pass
    return "Unknown topic"

def generate_report():
    pushed_files = glob.glob(os.path.join(pushed_dir, "*.md"))
    pushed_ids = set([os.path.basename(f).replace('.md', '') for f in pushed_files])
    
    all_folders = [f for f in os.listdir(brain_dir) if os.path.isdir(os.path.join(brain_dir, f))]
    
    # Filter out non-UUID folders like tempmediaStorage
    all_ids = set([f for f in all_folders if len(f) == 36 and '-' in f])
    
    not_pushed_ids = all_ids - pushed_ids
    
    with open(output_report, 'w', encoding='utf-8') as out:
        out.write(f"# Chat Backup Status Report\n\n")
        out.write(f"**Total Chats in Brain:** {len(all_ids)}\n")
        out.write(f"**Pushed to GitHub:** {len(pushed_ids)}\n")
        out.write(f"**Not Pushed to GitHub:** {len(not_pushed_ids)}\n\n")
        
        out.write(f"## 🟢 Pushed to GitHub ({len(pushed_ids)})\n")
        out.write("These chats contained references to 'priyanshu readme' or 'stickman'.\n\n")
        for sid in list(pushed_ids)[:50]: # List first 50 to avoid massive file
            out.write(f"- `{sid}`: {get_chat_preview(sid)}\n")
        if len(pushed_ids) > 50:
            out.write(f"- ... and {len(pushed_ids) - 50} more.\n")
            
        out.write(f"\n## 🔴 Not Pushed to GitHub ({len(not_pushed_ids)})\n")
        out.write("These chats did not match the project keywords, so they were left out of the GitHub repo (but are safely inside your Desktop ZIP backups).\n\n")
        for sid in list(not_pushed_ids)[:50]: # List first 50
            out.write(f"- `{sid}`: {get_chat_preview(sid)}\n")
        if len(not_pushed_ids) > 50:
            out.write(f"- ... and {len(not_pushed_ids) - 50} more.\n")
            
    print(f"Report generated: {len(pushed_ids)} pushed, {len(not_pushed_ids)} not pushed.")

if __name__ == "__main__":
    generate_report()
