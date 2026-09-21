import json
import os

transcript_path = r"C:\Users\renu5\.gemini\antigravity\brain\3a554bb4-f603-4809-ac0c-73160e772bd3\.system_generated\logs\transcript_full.jsonl"
out_path = r"C:\Users\renu5\.gemini\antigravity\brain\3a554bb4-f603-4809-ac0c-73160e772bd3\conversation_archive.md"

lines = []
if os.path.exists(transcript_path):
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip(): continue
            try:
                d = json.loads(line)
                t = d.get("type")
                if t == "USER_INPUT":
                    time = d.get("created_at", "")
                    content = d.get("content", "")
                    lines.append(f"## 👤 User ({time})\n\n{content}\n\n---\n")
                elif t == "PLANNER_RESPONSE":
                    time = d.get("created_at", "")
                    lines.append(f"## 🤖 AI Assistant ({time})\n\n")
                    content = d.get("content")
                    if content:
                        lines.append(f"{content}\n\n")
                    tc_list = d.get("tool_calls")
                    if tc_list:
                        for tc in tc_list:
                            name = tc.get("name")
                            lines.append(f"**Action**: `{name}`\n")
                    lines.append("\n---\n")
            except Exception as e:
                pass

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("# Full Conversation Archive\n\n" + "\n".join(lines))
    print(f"Created {out_path} successfully.")
else:
    print(f"Transcript not found at {transcript_path}")
