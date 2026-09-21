import json
import os
import glob
from datetime import datetime, timedelta

brain_dirs = [
    r"C:\Users\renu5\.gemini\antigravity\brain",
    r"C:\Users\renu5\.gemini\antigravity-ide\brain"
]
output_md = r"C:\Users\renu5\.gemini\antigravity\brain\1682ac12-05ba-422a-a04c-f2d378a84e1d\scratch\stickman_history.md"

os.makedirs(os.path.dirname(output_md), exist_ok=True)

ten_days_ago = datetime.now() - timedelta(days=10)
ten_days_ago_ts = ten_days_ago.timestamp()

md_lines = ["# Stickman Conversation & Grill-Me Responses (Last 10 Days)\n\n"]
md_lines.append("> **Note:** This report includes the exact prompts you used, your responses to AI questions, and the surrounding context (the exchange before and after) to ensure no 'Grill Me' responses were missed even if they didn't explicitly contain the word 'stickman'.\n\n")

def process_transcript(path, conv_id):
    try:
        if os.path.getmtime(path) < ten_days_ago_ts:
            return
    except:
        return
    
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    content_lower = "".join(lines).lower()
    if 'stikman' not in content_lower and 'stickman' not in content_lower:
        return
        
    conversation_pairs = []
    current_user_prompt = None
    current_agent_response = None
    
    for line in lines:
        try:
            step = json.loads(line)
            step_type = step.get('type')
            content = step.get('content', '')
            
            if step_type == 'USER_INPUT':
                if current_user_prompt is not None:
                    conversation_pairs.append({'user': current_user_prompt, 'agent': current_agent_response})
                current_user_prompt = content
                current_agent_response = ""
            elif step_type in ['PLANNER_RESPONSE', 'MODEL_RESPONSE']:
                if current_user_prompt is not None:
                    current_agent_response += content + "\n"
        except Exception as e:
            continue
            
    if current_user_prompt is not None:
        conversation_pairs.append({'user': current_user_prompt, 'agent': current_agent_response})
        
    relevant_indices = set()
    for i, pair in enumerate(conversation_pairs):
        user_lower = pair['user'].lower()
        agent_lower = (pair['agent'] or "").lower()
        
        if 'stikman' in user_lower or 'stickman' in user_lower or 'stikman' in agent_lower or 'stickman' in agent_lower:
            relevant_indices.add(i)
            # Add context: the user's response to an AI question might be in i+1
            if i < len(conversation_pairs) - 1:
                relevant_indices.add(i + 1)
            # The AI's question that the user responded to might be in i-1
            if i > 0:
                relevant_indices.add(i - 1)
                
    if relevant_indices:
        source = "Antigravity IDE" if "antigravity-ide" in path else "Antigravity 2.0"
        md_lines.append(f"## {source} - Conversation ID: `{conv_id}`\n")
        
        sorted_indices = sorted(list(relevant_indices))
        
        for i in sorted_indices:
            pair = conversation_pairs[i]
            md_lines.append(f"### Exchange {i+1}\n")
            
            # Identify if this looks like a Grill Me response
            is_grill = 'grill' in pair['user'].lower() or 'grill' in (pair['agent'] or "").lower()
            if is_grill:
                md_lines.append("🔥 **[GRILL ME SESSION DETECTED]**\n\n")
                
            md_lines.append("**Your Prompt / Response:**\n")
            user_text = pair['user'].strip().replace(chr(10), chr(10)+'> ')
            md_lines.append(f"> {user_text}\n\n")
            
            md_lines.append("<details>\n<summary><b>Click to expand AI Response / Questions</b></summary>\n\n")
            agent_text = (pair['agent'] or "").strip()
            md_lines.append(f"{agent_text}\n\n</details>\n\n")
            
        md_lines.append("---\n\n")

for brain_dir in brain_dirs:
    pattern = os.path.join(brain_dir, "*", ".system_generated", "logs", "transcript.jsonl")
    for path in glob.glob(pattern):
        conv_id = path.split(os.sep)[-4]
        process_transcript(path, conv_id)
    
with open(output_md, 'w', encoding='utf-8') as f:
    f.writelines(md_lines)
    
print(f"Wrote {output_md}")
