# 🎬 Episode Production Checklist & Requirements: 01_kept_car_20_years

> **Video Title:** POV: You Kept the Same Car for 20 Years — Here's What It Built  
> **vidIQ Title Score:** **99/100** (Highest in research pass)  
> **Formula:** Hybrid H01 (Time Capsule × Vehicle Debt × Cognitive Dissonance)  
> **Target Runtime:** 20–25 Minutes (3,800–4,700 words @ 180–195 WPM)  
> **Visual Assets:** 550–700 Sequential PNGs (Two-Tier Dynamic Pacing: 0.8s–1.2s hook; 1.8s–2.5s body)  
> **Status:** [ ] Scripted | [ ] Audio Rendered | [ ] Images Generated | [ ] Video Compiled | [ ] Scheduled

---

## 📂 Subfolder Asset Checklist: What Goes Where

| Subfolder | Required Assets | Forbidden / Banned Assets |
|---|---|---|
| **`/dossier`** | `script_intake.md` (intake parameters), `quality_gate_audit.md` (Gemini 3.8 Flash audit), `math_model.md` (7–8% S&P math), source URLs | Inflated 12%+ compound math, unsourced claims |
| **`/transcripts`** | 3–5 competitor transcripts on this exact topic, `gap_analysis.md` (40% gap rule) | Saturated advice copied verbatim |
| **`/audio`** | `voiceover.wav` (ElevenLabs v3), `cut_durations.json` (timestamps), 4-act background music beds (-16dB ducked), SFX tracks | Unedited takes, non-normalized audio |
| **`/images`** | 550–700 sequential PNGs (`img_001.png` to `img_700.png`), 16:9 1080p, neutral stoic stickman hero, warm American environments | Floating headline text overlays, 3D uncanny styles, dark void backgrounds |
| **`/thumbnails`** | `thumbnail_final.png` (1280x720, 8 laws verified, bottom-right 180x40px safe zone clear) | Emotional protagonist, floating "POV" text, red clickbait arrows |

---

## ⚡ 1-Click Compilation
Run the local assembly script once all assets are populated:
```powershell
python assemble_video.py
```
Outputs: `final_video.mp4` (20–25 min 1080p master render) in root of this episode folder in under 2 minutes.
