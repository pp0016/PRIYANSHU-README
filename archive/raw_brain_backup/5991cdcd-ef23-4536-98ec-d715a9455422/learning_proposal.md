# Learning Proposal: Gemini Watermark Remover

## Classification
**Type:** New Skill
**Name:** `gemini-watermark-remover`
**Trigger:** Whenever the user asks to "remove watermark", "clean video", or specifically mentions removing the Gemini/Flow sparkle watermark from an image or video.

## Rationale
The tool `@pilio/gemini-watermark-remover` (`gwr`) has two specific quirks we discovered:
1. It frequently stops at ~12% on videos due to low confidence. It requires the undocumented `--allow-low-confidence` flag to force processing.
2. It re-encodes videos at a low default bitrate, ruining quality. It requires `--video-bitrate-mbps 30` (or similar) to maintain 1080p quality.

Creating a skill ensures any future AI agent in a new conversation will automatically know to use these flags when you ask it to remove a watermark.

## Proposed SKILL.md Content

**Path:** `C:\Users\renu5\.gemini\config\skills\gemini-watermark-remover\SKILL.md`

```markdown
---
name: gemini-watermark-remover
description: >
  Expert instructions for removing Google Flow, Gemini, and Veo "sparkle" watermarks from images and videos using the `gwr` CLI tool.
---

# Gemini Watermark Remover Skill

This skill teaches how to use the `@pilio/gemini-watermark-remover` CLI tool (`gwr`) correctly, specifically addressing its hidden flags and quality issues on Windows.

## Core Rules

1. **Always Force Low Confidence:** The `gwr` tool often fails video processing around 12% with a Chinese error about low confidence. You MUST append the hidden flag `--allow-low-confidence` to bypass this error on all video requests.
2. **Always Force High Quality:** By default, `gwr` compresses re-encoded video output heavily, causing noticeable quality loss. You MUST append `--video-bitrate-mbps 30` to preserve the original 1080p fidelity.
3. **Overwrite:** Use `--overwrite` to automatically replace existing files and prevent the tool from pausing to prompt the user.

## Command Template

To remove a watermark from a single video/image:
```powershell
gwr remove "C:\path\to\input.mp4" --output "C:\path\to\output_clean.mp4" --allow-low-confidence --video-bitrate-mbps 30 --overwrite
```

To remove watermarks from a whole directory:
```powershell
gwr remove "C:\path\to\input_dir" --out-dir "C:\path\to\output_dir" --allow-low-confidence --video-bitrate-mbps 30 --overwrite
```

## Troubleshooting
- If `gwr` throws a `playwright` browser executable error, run `npx playwright install chromium` first.
```
