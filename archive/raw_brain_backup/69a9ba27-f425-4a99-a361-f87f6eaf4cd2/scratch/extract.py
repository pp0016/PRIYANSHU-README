import email
import sys
from bs4 import BeautifulSoup

def mhtml_to_text(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f)
    
    html_content = ""
    # MHTML is structured like an email
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            html_content += part.get_payload(decode=True).decode('utf-8', errors='ignore')
            
    if html_content:
        # Extract just the readable text
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text(separator='\n\n', strip=True)
        return text
    return ""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide file path")
        sys.exit(1)
        
    mhtml_path = sys.argv[1]
    text = mhtml_to_text(mhtml_path)
    
    md_path = r'C:\Users\renu5\.gemini\antigravity\brain\69a9ba27-f425-4a99-a361-f87f6eaf4cd2\scratch\chat.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(text)
        
    print(f"Extracted Text Length (chars): {len(text)}")
