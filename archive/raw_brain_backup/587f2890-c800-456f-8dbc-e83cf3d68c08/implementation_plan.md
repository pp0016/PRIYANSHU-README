# Create `pdf-to-markdown` Skill

I converted your PDFs by using my built-in `view_file` tool (which renders PDFs as screenshots) and visually transcribing the text, tables, and links directly into markdown. While effective, it relies on my visual processing and takes a lot of tokens and time. 

To automate this so it takes seconds, we will create a dedicated `pdf-to-markdown` skill that uses Python's `pymupdf4llm` library. This library natively extracts text, formatting, tables, and clickable links from PDFs into perfect markdown.

## User Review Required

Please review the proposed skill design below. If this looks good, click **Proceed** and I will build the skill, write a test script, and we can test it out.

## Proposed Changes

### [NEW] `pdf-to-markdown` Skill

We will create a new skill in your Gemini config directory with the following structure:

#### `SKILL.md`
The core instructions for the skill. It will tell the AI to use the bundled Python script whenever you ask to convert a PDF to Markdown.

#### `scripts/convert.py`
A python script that will automatically install `pymupdf4llm` if it's missing, and run the conversion process instantly, saving the output to a `.md` file.

## Verification Plan

### Automated Tests
I will create a test case to convert one of your PDFs (`1 to 6.pdf`) using the new skill to ensure it works correctly and quickly.

### Manual Verification
You will be able to review the generated markdown from the test case to ensure the formatting and links are preserved perfectly.
