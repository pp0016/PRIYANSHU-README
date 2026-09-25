import os
import json
import glob
from datetime import datetime

brain_dir = r"C:\Users\renu5\.gemini\antigravity\brain"
output_file = r"c:\Users\renu5\Downloads\priyanshu readme\work\backfilled_chats_summary.md"

def extract_chats():
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("# Backfilled Chat History\n\n")
        out.write("This file contains the extracted history from all other chat sessions related to `priyanshu readme`.\n\n")
        
        folders = glob.glob(os.path.join(brain_dir, "*", ".system_generated", "logs", "transcript.jsonl"))
        
        relevant_chats = []
        for path in folders:
            is_relevant = False
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if "priyanshu readme" in content.lower() or "stickman" in content.lower():
                        is_relevant = True
            except:
                continue
                
            if not is_relevant:
                continue
                
            # If relevant, parse it
            out.write(f"## Session: {os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(path))))}\n")
            
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    for line in f:
                        data = json.loads(line)
                        if data.get('type') == 'USER_INPUT':
                            time = data.get('created_at', 'Unknown time')
                            text = data.get('content', '')
                            out.write(f"**[{time}] USER:** {text[:500]}...\n\n")
            except Exception as e:
                out.write(f"Error parsing: {str(e)}\n\n")
                
            out.write("---\n\n")
            
    print(f"Extraction complete! Saved to {output_file}")

if __name__ == "__main__":
    extract_chats()
