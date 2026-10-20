## 2026-10-10T18:18:53Z
You are Worker M2: Cel-Boil Vector Perturbation Engine (teamwork_preview_worker).
Your working directory is: `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\worker_cel_m2`
MANDATORY: Read `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\ORIGINAL_REQUEST.md` before starting work.
Also read `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\orchestrator_4\PROJECT.md`.
Reference Explorer 1 & 3 analysis at `c:\Users\renu5\Downloads\priyanshu readme\.agents\teamwork\explorer_survey_1\analysis.md` and `explorer_survey_3\analysis.md`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Your exclusive write ownership:
- `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\cel_boil.py`
- `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\test_cel_boil_local.py`

Tasks:
1. Implement `cel_boil.py` in `C:\Users\renu5\Downloads\mg-styles-15-test\manim-port\`:
   - Build a robust, authentic vector perturbation engine for Python Manim Community edition (`VMobject`).
   - Implement continuous 2D/3D spatial noise displacement:
     x' = x + amp * N(x/scale, y/scale, z)
     y' = y + amp * N(x/scale + 41.3, y/scale - 17.9, z)
     where z = seed * 2.371 + 0.5.
   - Provide two boil rates:
     - `fps=12` ("on twos") for active scenes (Beats 1-9)
     - `fps=8` ("on threes") for holds/outro (Beat 10)
   - Implement Bézier curve continuity preservation: perturb anchors and control handles coherently using continuous spatial noise field so curve continuity is preserved and no curve cracking occurs.
   - Implement the differential jitter subtraction algorithm (`points -= m.last_jitter; points += new_jitter`) or reference point anchoring so that animated transforms (scaling, shifting, rotating) can occur naturally without point explosion or positional drift over 720 frames.
   - Provide helper functions:
     - `apply_cel_boil(vmobject, amp=0.035, scale=1.2, fps=12, seed_offset=0)`
     - `remove_cel_boil(vmobject)`
2. Implement and execute `test_cel_boil_local.py` using `C:\Users\renu5\Downloads\manim_video_repo\venv\Scripts\python.exe` to test:
   - Applying cel boil to `Circle`, `Square`, `Text`, `VGroup`.
   - Running updater across 100 simulated frames: verify points jitter, no NaN/inf, mean coordinate drift is near 0.
3. Write `handoff.md` with verification outputs and send a message.
