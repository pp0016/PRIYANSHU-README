import email
import sys
import markdownify

def mhtml_to_md(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f)
    
    html_content = ""
    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            html_content += part.get_payload(decode=True).decode('utf-8', errors='ignore')
            
    if html_content:
        # Convert HTML to Markdown preserving links
        md_text = markdownify.markdownify(html_content, heading_style="ATX", strip=['script', 'style'])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_text.strip())
        print(f"Successfully converted to {output_path}")
    else:
        print("No HTML content found.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python mhtml_to_md.py <input> <output>")
        sys.exit(1)
    mhtml_to_md(sys.argv[1], sys.argv[2])
