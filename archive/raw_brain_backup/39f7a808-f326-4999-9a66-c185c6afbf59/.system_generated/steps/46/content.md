Title: Live Content

Description: Fetched live

Source: https://raw.githubusercontent.com/geekyutao/Inpaint-Anything/main/README.md

---

<p align="center">
  <img src="./example/IAM.png">
</p>

# Inpaint Anything: Segment Anything Meets Image Inpainting
Inpaint Anything can inpaint anything in **images**, **videos** and **3D scenes**!
- Authors: Tao Yu, Runseng Feng, Ruoyu Feng, Jinming Liu, Xin Jin, Wenjun Zeng and Zhibo Chen.
- Institutes: University of Science and Technology of China; Eastern Institute for Advanced Study.
- [[Paper](https://arxiv.org/abs/2304.06790)] [[Website](https://huggingface.co/spaces/InpaintAI/Inpaint-Anything)] [[Hugging Face Homepage](https://huggingface.co/InpaintAI)]
<p align="center">
  <img src="./example/MainFramework.png" width="100%">
</p>

TL; DR: Users can select any object in an image by clicking on it. With powerful vision models, e.g., [SAM](https://arxiv.org/abs/2304.02643), [LaMa](https://arxiv.org/abs/2109.07161) and [Stable Diffusion (SD)](https://arxiv.org/abs/2112.10752), **Inpaint Anything** is able to remove the object smoothly (i.e., *Remove Anything*). Further, prompted by user input text, Inpaint Anything can fill the object with any desired content (i.e., *Fill Anything*) or replace the background of it arbitrarily (i.e., *Replace Anything*).

---

## 🚧 New: [`main_2026`](https://github.com/geekyutao/Inpaint-Anything/tree/main_2026) branch — modernized stack + robotics support (beta)

The [**`main_2026`**](https://github.com/geekyutao/Inpaint-Anything/tree/main_2026)
branch brings Inpaint Anything up to date with the 2026 model landscape, and adds
a new direction: **data engineering for robotics**.

| | `main` (this branch) | [`main_2026`](https://github.com/geekyutao/Inpaint-Anything/tree/main_2026) |
| --- | --- | --- |
| Segmentation | SAM 1 | **SAM 3** — plus open-vocabulary *text* prompts |
| Video / 3D tracking | OSTrack | **SAM 3 video predictor** — one less model and checkpoint |
| Video inpainting | STTN | **ProPainter** |
| Text-guided fill / replace | SD 2 *(no longer downloadable)* | **SDXL**, optional **FLUX.1-Fill** |
| Robotics | — | **`remove_hands.py`** — batch hand removal for Human-to-Robot pipelines |

Two things you can do there that you cannot do here:

- **Name the object instead of clicking it.** `--text_select "dog"` finds every match, which also means the pipelines can run unattended over a whole dataset.
- **Prepare egocentric data for robot learning.** `remove_hands.py` erases human hands from egocentric video and exports the masks — the *hand removal and inpainting* stage of Human-to-Robot synthesis pipelines such as [Qwen-RobotManip](https://github.com/QwenLM/Qwen-RobotManip) and [EgoEngine](https://egoengine.github.io/). On EgoMimic footage it matches human annotation at IoU 0.96, and it reconstructs the background rather than blacking the arm out.

```bash
git checkout main_2026
# then follow the Quick start in that branch's README
```

> ⚠️ **`main_2026` is in beta.** It needs Python ≥ 3.12, PyTorch ≥ 2.7 and
> CUDA ≥ 12.6 (SAM 3's floor), and the NeRF-based 3D path has not been
> end-to-end verified on that stack yet. Every legacy backend
> (SAM 1 / MobileSAM, OSTrack, STTN) is still selectable by flag, so you can fall
> back per stage.
>
> 🤝 **Contributions very welcome** — especially on the robotics side. Issues and
> PRs against `main_2026` are appreciated: more egocentric datasets, action
> retargeting, robot rendering and compositing, or newer inpainting backends.
> Please open an issue if you hit anything.

---

## 📜 News
[2026/7/28] <span style="color:red">🔥NEW</span> [**`main_2026`**](https://github.com/geekyutao/Inpaint-Anything/tree/main_2026) **branch (beta):** upgraded to [SAM 3](https://github.com/facebookresearch/sam3) with text prompts, [ProPainter](https://github.com/sczhou/ProPainter) for video, SDXL/FLUX for text-guided editing, and **robotics support** via `remove_hands.py`. OSTrack is no longer needed. Contributions welcome!\
[2023/9/15] [Remove Anything 3D](#remove-anything-3d) code is available!\
[2023/4/30] [Remove Anything Video](#remove-anything-video) available! You can remove any object from a video!\
[2023/4/24] [Local web UI](./app) supported! You can run the demo website locally!\
[2023/4/22] [Website](https://huggingface.co/spaces/InpaintAI/Inpaint-Anything) available! You can experience Inpaint Anything through the interface!\
[2023/4/22] [Remove Anything 3D](#remove-anything-3d) available! You can remove any 3D object from a 3D scene!\
[2023/4/13] [Technical report on arXiv](https://arxiv.org/abs/2304.06790) available!

## 🌟 Features
- [x] [**Remove** Anything](#remove-anything)
- [x] [**Fill** Anything](#fill-anything)
- [x] [**Replace** Anything](#replace-anything)
- [x] [Remove Anything **3D**](#remove-anything-3d) (<span style="color:red">🔥NEW</span>)
- [ ] Fill Anything **3D**
- [ ] Replace Anything **3D**
- [x] [Remove Anything **Video**](#remove-anything-video) (<span style="color:red">🔥NEW</span>)
- [ ] Fill Anything **Video**
- [ ] Replace Anything **Video**


## 💡 Highlights
- [x] Any aspect ratio supported
- [x] 2K resolution supported
- [x] [Technical report on arXiv](https://arxiv.org/abs/2304.06790) available (<span style="color:red">🔥NEW</span>)
- [x] [Website](https://huggingface.co/spaces/InpaintAI/Inpaint-Anything) available (<span style="color:red">🔥NEW</span>)
- [x] [Local web UI](./app) available (<span style="color:red">🔥NEW</span>)
- [x] Multiple modalities (i.e., image, video and 3D scene) supported (<span style="color:red">🔥NEW</span>)

<!-- ## Updates
| Date | News |
| ------ | --------
| 2023-04-12 | Release the Fill Anything feature | 
| 2023-04-10 | Release the Remove Anything feature |
| 2023-04-10 | Release the first version of Inpaint Anything | -->

## <span id="remove-anything">📌 Remove Anything</span>


<!-- <table>
  <tr>
    <td><img src="./example/remove-anything/dog/with_points.png" width="100%"></td>
    <td><img src="./example/remove-anything/dog/with_mask.png" width="100%"></td>
    <td><img src="./example/remove-anything/dog/inpainted_with_mask.png" width="100%"></td>
  </tr>
</table> -->

<p align="center">
    <img src="./example/GIF/Remove-dog.gif"  alt="image" style="width:40

