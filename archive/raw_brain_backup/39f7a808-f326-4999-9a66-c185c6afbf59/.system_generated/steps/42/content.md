Title: Live Content

Description: Fetched live

Source: https://raw.githubusercontent.com/VjiaoBlack/layercake/main/README.md

---

# layercake

Cut a photo into depth-ordered transparent PNG layers with [Meta's
Segment Anything 2](https://github.com/facebookresearch/sam2). Every output
PNG is the source image's exact dimensions, so layers stack cleanly under
CSS `object-fit: cover; object-position: center`.

PSD is for Photoshop. **layercake is for CSS.**

Built for layered hero composites on the web — the kind where text weaves
between a foreground object and the subject, or where parallax layers
separate fore/mid/background. Click a few points per layer, optionally draw
a bounding box, pick edge quality, save. Source dimensions guaranteed.

## Why this and not something else

| Tool | Click-prompted | N layers | Source-dim PNG stack | Local & free |
|---|:-:|:-:|:-:|:-:|
| Photoshop "Select Subject" | ✕ | ✕ | N/A | Paid |
| remove.bg / Photoroom / Clipdrop | ✕ | Fg/bg only | ✕ | Cloud |
| iOS "Lift Subject" | ✕ | Subject only | ✕ | Local |
| [jhj0517/sam2-playground](https://github.com/jhj0517/sam2-playground) | ✓ | PSD | ✕ | Local |
| 10b.ai RGBA Layers | ✕ | ✓ | ✓ | Cloud, paid |
| **layercake** | **✓** | **✓** | **✓** | **✓** |

## Install

Requires Python 3.10+. Recommended via [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/<you>/layercake.git
cd layercake
uv venv --python 3.13 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

First run downloads SAM 2 weights (~900 MB for `sam2-hiera-large`). Cached
under `~/.cache/huggingface/`. Device auto-detects MPS (Apple silicon),
CUDA, or CPU.

## SAM 3 text prompts (optional)

The Gradio UI includes an opt-in **"Segment by concept"** section powered by
[SAM 3](https://github.com/facebookresearch/sam3) (Nov 2025). Type a short
noun phrase (`rope`, `face`, `hand`, `leaves`) and SAM 3 segments **every
instance** of the concept, creating one layer per instance.

This is genuinely additive to SAM 2 — SAM 2 needs you to know where to click;
SAM 3 takes the concept name and finds it for you. Especially useful for
scenes where the same thing repeats (multiple rope strands, a crowd, a shelf
of objects).

**One-time setup (weights are gated):**

1. Visit [huggingface.co/facebook/sam3](https://huggingface.co/facebook/sam3)
   and click *Agree and access repository*.
2. Create a read-scope token at
   [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
3. `export HF_TOKEN=hf_...` in your shell, or run `huggingface-cli login`.

Then relaunch layercake. The first concept segmentation downloads the model
(~3 GB) and caches it under `~/.cache/huggingface/`.

**Reading the scores:** SAM 3 multiplies each instance's confidence by an
image-level "is this concept present at all" confidence, so final scores run
lower than you'd expect — a clearly-visible concept can land at 0.1–0.3 when
the presence head is conservative (thin structures like rope especially).
If a concept you can plainly see returns nothing, lower the score threshold
before rewording the phrase; the default of 0.4 suits prominent subjects,
not fine ones.

## Interactive UI (recommended)

```bash
python layers_app.py
```

Opens at `http://127.0.0.1:7860`. Workflow:

1. Upload a source image.
2. Name a layer (order = depth; **first layer = nearest**) and hit **Add layer**.
3. With the layer active, click the image. Modes:
   - **include** — positive click: "this pixel belongs to the layer."
   - **exclude** — negative click: "this pixel does NOT."
   - **move** — 1st click picks up the nearest point, 2nd drops it.
   - **box** — 2 clicks mark opposite corners of an axis-aligned bounding box.
   - **erase** — click near a point (or inside the box) to remove it.
4. Repeat for each layer. Edit points directly in the dataframe (move by
   changing x/y, delete by removing rows).
5. Hit **Save layers**.

Output directory gets:

- `<name>.png` per layer, all source-dim RGBA
- `bg.png` — the inverse of the union of all your layers
- `points.json` — the full spec, for replay via the CLI
- `snippet.html` — ready-to-paste HTML + CSS that stacks the layers

## Headless CLI

Same engine, no UI. Useful in build scripts.

```bash
python layers.py input.jpg \
  --layers '[
    {"name": "foreground",  "points": [[1200, 300], [850, 250]]},
    {"name": "subject",     "points": [[420, 400]], "box": [300, 200, 600, 900]},
    {"name": "midground",   "points": [[1100, 800]], "labels": [1]}
  ]' \
  --out out/ \
  --edges matting \
  --preview
```

Each layer entry supports:

- `name` (required)
- `points` — list of `[x, y]` in source-image pixel space
- `labels` — per-point include/exclude: `1` or `0` (default all 1)
- `box` — optional axis-aligned `[x1, y1, x2, y2]`
- `concept` — SAM 3 text prompt (`"rope"`, `"face"`); requires SAM 3 access
  (see above). A concept-only layer expands to one layer per found instance
  (capped at the 10 best after dropping near-duplicates — SAM 3 often
  returns several overlapping instances of the same object, so an instance
  mostly covered by better-scoring ones is skipped),
  named `{name}-1`, `{name}-2`, … best-score-first,
  and the SAM 3 masks are used as-is. A concept **combined with** points/box
  takes the best instance as a warm-start prior an

