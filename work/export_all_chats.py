import os
import json
import glob
import re

brain_dir = r"C:\Users\renu5\.gemini\antigravity\brain"
output_dir = r"c:\Users\renu5\Downloads\priyanshu readme\archive\past_chats"

os.makedirs(output_dir, exist_ok=True)

def clean_secrets(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'gsk_[a-zA-Z0-9]{40,}', '[REDACTED_GROQ_KEY]', text)
    text = re.sub(r'ghp_[a-zA-Z0-9]{30,}', '[REDACTED_GITHUB_KEY]', text)
    text = re.sub(r'github_pat_[a-zA-Z0-9_]{50,}', '[REDACTED_GITHUB_PAT]', text)
    return text

def extract_all_clean_conversations():
    folders = glob.glob(os.path.join(brain_dir, "*", ".system_generated", "logs", "transcript.jsonl"))
    
    count = 0
    for path in folders:
        session_id = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(path))))
        
        # Parse cleanly - NO TRUNCATION
        md_content = f"# Chat Session: {session_id}\n\n"
        has_content = False
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        step_type = data.get('type')
                        
                        if step_type == 'USER_INPUT':
                            text = clean_secrets(data.get('content', ''))
                            if text:
                                md_content += f"### 🧑 You\n{text}\n\n---\n\n"
                                has_content = True
                                
                        elif step_type == 'PLANNER_RESPONSE':
                            # Get the AI's visible response to the user, not its tool outputs
                            text = clean_secrets(data.get('content', ''))
                            if text and text.strip():
                                md_content += f"### 🤖 Antigravity\n{text}\n\n---\n\n"
                                has_content = True
                    except:
                        pass
        except:
            pass
            
        if has_content:
            out_file = os.path.join(output_dir, f"{session_id}.md")
            with open(out_file, 'w', encoding='utf-8') as out:
                out.write(md_content)
            count += 1
            
    print(f"Successfully exported {count} total chats.")

if __name__ == "__main__":
    extract_all_clean_conversations()
