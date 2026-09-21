# Heat Transfer (BE05000291) — Mid-Sem Analysis (30 Marks)

**Exam Date:** 05/09/2026 | **College:** GEC Bharuch | **Coordinator:** Prof. D.A. Pandey

> [!WARNING]
> **Syllabus Code Mismatch:** Your new syllabus uses code **BE05000291** (AY 2026-27). All 9 PYQ papers use old code **3151909**. The syllabus has been restructured. Every mapping below is strictly against your new syllabus wording — not old unit numbers. Some high-frequency PYQ topics are **completely out of scope** under the new scheme.

---

## 1. Syllabus Boundary Verification

### What's IN Scope (Your 3 COs)

**CO-1 (Conduction + Fins):**
- Fourier's law
- Effect of temperature on thermal conductivity (solids, liquids, gases)
- Generalized heat equation in Cartesian, cylindrical, spherical coordinates + reduction to specific cases
- 1D steady-state conduction
- Plane walls, composite walls, cylinders, spheres
- Electrical analogy
- Critical radius of insulation (cylinder and sphere)
- Overall heat transfer coefficient
- Types of fin
- Fin heat flow: infinitely long fin, fin insulated at tip, fin losing heat at tip
- Fin efficiency and effectiveness

**CO-2 (Convection):**
- Newton's law of cooling
- Dimensional analysis (forced + free convection)
- Dimensionless numbers + physical significance
- Empirical correlations (free + forced convection)
- Continuity, momentum, energy equations
- Thermal and hydrodynamic boundary layer

**CO-3 (Radiation):**
- Absorptivity, reflectivity, transmissivity
- Black, white, grey body
- Emissive power, emissivity
- Kirchhoff's law, Planck's law, Rayleigh-Jeans' law, Wien's law, Wien's displacement law, Stefan-Boltzmann law
- Intensity of radiation
- Radiation heat exchange between black bodies
- Shape factor

---

### 🚫 DANGER ZONES — Topics That LOOK Relevant But Are OUT

> [!CAUTION]
> These topics appear heavily in PYQs (often 7-14 marks per paper) but are **NOT in your mid-sem syllabus**. Studying these is the single biggest time-waste risk.

#### ❌ DANGER ZONE 1: Transient Heat Conduction / Lumped System Analysis
**Appears in:** W25 Q1(b), W23 Q2(a), W24 Q4(b), S25 Q3(a), S26 Q3(a), S22 Q5(c), S23 Q2(c)
**Why it's tempting:** Biot number and Fourier number definitions look like they overlap with "dimensionless numbers" in CO-2. They don't. Bi and Fo are transient conduction concepts. Your syllabus's "dimensionless numbers" refers to convection numbers (Re, Nu, Pr, Gr, St, Pe).
**Verdict:** Skip entirely. Your syllabus covers only **steady-state** conduction.

#### ❌ DANGER ZONE 2: Heat Exchangers (LMTD, NTU, Effectiveness, Fouling, Classification)
**Appears in:** W25 Q5(c), W24 Q1(b)(c), W24 Q3(b), W24 Q4(c)OR, W23 Q3(c), W22 Q5, S26 Q5, S25 Q2(b)(c), S24 Q1(c), S24 Q3(b)OR, S23 Q4(b)OR/Q5, S22 Q3
**Why it's tempting:** "Overall heat transfer coefficient" IS in your syllabus — but in the context of conduction through walls/cylinders, not heat exchanger design. LMTD derivation, NTU-effectiveness method, fouling factors, HE classification are all out.
**Verdict:** Skip entirely. 14-21 marks per PYQ paper are from HE topics — none of that applies to you.

#### ❌ DANGER ZONE 3: Boiling and Condensation
**Appears in:** W25 Q5(a)(b), W24 Q3(c), W22 Q5(b)(c)OR, S26 Q5(a), S24 Q3(b)(c)OR, S23 Q5
**Why it's tempting:** Often mixed with convection questions. But boiling/condensation are a separate chapter.
**Verdict:** Skip entirely.

#### ⚠️ DANGER ZONE 4: Radiation Shields
**Appears in:** W24 Q4(c), W22 Q4(c)OR, S25 Q4(a), S24 Q2(a), S26 Q4(b)
**Why it's borderline:** Your syllabus mentions grey body and emissivity, but "radiation shields" as a concept (inserting plates between parallel surfaces) is NOT explicitly listed. The derivations involve grey body exchange, which is also not listed — your syllabus only says "radiation heat exchange between **black** bodies."
**Verdict:** Low priority. If you have spare time after everything else, know the basic concept. Don't learn the derivation.

#### ⚠️ DANGER ZONE 5: Blasius Solution / Von Karman Integral
**Appears in:** W23 Q4(c)OR, S25 Q4(b)
**Why it's borderline:** Your syllabus says "continuity, momentum and energy equations" and "boundary layer" — which is broad. Blasius is a specific solution technique for boundary layer equations.
**Verdict:** Low priority. Know what Blasius method is (1-2 lines) but don't learn the full derivation.

#### ❌ DANGER ZONE 6: Thermometer Well / Thermometric Pocket
**Appears in:** S22 Q2(c)OR, S25 Q3(b)OR
**Verdict:** Skip. This is a transient conduction application.

---

## 2. PYQ Papers Used

| # | Paper | Season | Date | Code |
|---|-------|--------|------|------|
| 1 | Winter 2022 | W22 | 06-01-2023 | 3151909 |
| 2 | Summer 2022 | S22 | 04-06-2022 | 3151909 |
| 3 | Winter 2023 | W23 | 07-12-2023 | 3151909 |
| 4 | Summer 2023 | S23 | 26-06-2023 | 3151909 |
| 5 | Winter 2024 | W24 | 28-11-2024 | 3151909 |
| 6 | Summer 2024 | S24 | 18-05-2024 | 3151909 |
| 7 | Winter 2025 | W25 | 19-11-2025 | 3151909 |
| 8 | Summer 2025 | S25 | 15-05-2025 | 3151909 |
| 9 | Summer 2026 | S26 | 25-05-2026 | 3151909 |

**Total questions analyzed:** ~180 (including OR options)
**In-scope questions:** ~105 | **Out-of-scope:** ~75

---

## 3. Topic Frequency Analysis

### CO-1: Conduction + Fins

| Topic | Papers (out of 9) | Typical Marks | Question Type | Tier |
|-------|:---:|:---:|---|:---:|
| General heat conduction eq. (Cartesian) + Laplace/Poisson/Fourier | 6 (W24, W22, S26, S25, S24, S22) | 7 | Derivation | 🔴 T1 |
| Fourier's law / thermal conductivity / thermal diffusivity definitions | 7 (W25, W22, W23, S25, S24, S23, S22) | 3-4 | Theory/Define | 🔴 T1 |
| Composite wall (derivation + numerical) | 6 (W25, W23, W24, S26, S24, S23) | 4-7 | Derivation + Numerical | 🔴 T1 |
| Critical radius of insulation (cylinder + sphere) | 5 (W24, W23, S26, S25, S24) | 3-7 | Theory + Derivation | 🔴 T1 |
| Fin numerical (heat dissipation, tip temperature) | 7 (W22, W24, W23, S26, S24, S22, S23) | 7 | Numerical | 🔴 T1 |
| Fin theory (types, selection, when not useful, advantages) | 7 (W25, W24×2, S25, S26, S24, S22) | 3-4 | Theory | 🔴 T1 |
| Fin efficiency + effectiveness (definition/theory) | 4 (W25, W22, W23, S26) | 3-7 | Theory/Explain | 🟡 T2 |
| Modes of heat transfer (define/compare conduction, convection, radiation) | 4 (W25, W24, W22, S26) | 3 | Theory/Define | 🟡 T2 |
| General heat conduction eq. (Cylindrical coordinates) | 3 (W23, W22, S23) | 4-7 | Derivation | 🟡 T2 |
| 1D steady-state plane wall derivation | 1 (W25) | 7 | Derivation | 🟢 T3 |
| General heat conduction eq. (Spherical coordinates) | 2 (S25, S23) | 4-7 | Derivation | 🟢 T3 |
| Electrical analogy / thermal circuit | 1 (S22) | 3 | Theory | 🟢 T3 |
| Overall HTC (standalone question) | 1 (S26) | 7 | Numerical | 🟢 T3 |
| Conduction through cylinders/spheres (numerical) | 2 (S26, S23) | 3-7 | Numerical | 🟢 T3 |
| Fin temperature distribution derivation (insulated tip) | 1 (S25) | 7 | Derivation | 🟢 T3 |

### CO-2: Convection

| Topic | Papers (out of 9) | Typical Marks | Question Type | Tier |
|-------|:---:|:---:|---|:---:|
| Dimensionless numbers (Re, Nu, Pr, Gr) — definitions + significance | 7 (W25, W22×2, S25, S24×2, S23) | 3-7 | Theory/Define | 🔴 T1 |
| Free vs forced convection (comparison) | 6 (W25×2, W22, W23, S24, S23) | 3-4 | Theory | 🔴 T1 |
| Free convection numerical (using empirical correlations) | 4 (W22, W24, S22×2) | 4-7 | Numerical | 🟡 T2 |
| Buckingham π: Nu = f(Gr, Pr) for free convection | 3 (W22, S26, S23) | 7 | Derivation | 🟡 T2 |
| Thermal + hydrodynamic boundary layer (concept/definition) | 4 (W22, S26, S25, S23) | 3-7 | Theory | 🟡 T2 |
| Newton's law of cooling / convection HTC | 2 (W25, S24) | 4 | Theory | 🟢 T3 |
| Buckingham π: Nu = f(Re, Pr) for forced convection | 2 (W25, S24) | 7 | Derivation | 🟢 T3 |
| Energy equation for boundary layer (derivation) | 1 (W25) | 7 | Derivation | 🟢 T3 |
| Forced convection numerical | 1 (W23) | 7 | Numerical | 🟢 T3 |
| Dimensional analysis method (Rayleigh's limitations) | 1 (S24) | 7 | Theory | 🟢 T3 |

### CO-3: Radiation

| Topic | Papers (out of 9) | Typical Marks | Question Type | Tier |
|-------|:---:|:---:|---|:---:|
| Absorptivity, reflectivity, transmissivity (definition) | 4 (W25, W23, W22, S23) | 3 | Define | 🟡 T2 |
| Black/white/grey body (definition) | 4 (W25, S26, S24, S22) | 3-4 | Define | 🟡 T2 |
| Kirchhoff's law (state + prove) | 4 (W25, W23, S23, S22) | 3-7 | Theory + Proof | 🟡 T2 |
| Stefan-Boltzmann / emissive power / radiation numerical | 4 (W25×2, S22, S23) | 4-7 | Numerical | 🟡 T2 |
| Intensity of radiation / Eb = πIb proof | 3 (W22, S26, S23) | 7 | Derivation | 🟡 T2 |
| Shape factor (definition + properties/features) | 4 (W22, W23, S26, S25) | 3-4 | Theory | 🟡 T2 |
| Shape factor numerical | 2 (S26, S23) | 3-7 | Numerical | 🟢 T3 |
| Radiation heat exchange between black bodies (derivation) | 2 (S25, W23) | 7 | Derivation | 🟢 T3 |
| Wien's displacement law (state + explain) | 1 (W25) | 4 | Theory | 🟢 T3 |
| Planck's law numerical | 1 (S22) | 7 | Numerical | 🟢 T3 |
| Practical radiation concepts (polished surfaces, white vs black) | 2 (W24, W22) | 3 | Theory | 🟢 T3 |

---

## 4. 🎯 Strategy A: 20/30 Marks (~6-8 hours)

> [!IMPORTANT]
> This strategy targets only 🔴 Tier 1 theory questions + one numerical type. It's designed for minimum effort, maximum marks.

**Study order (follow this sequence):**

### Hour 1-2: Quick-Win Definitions (Target: 6-10 marks)

1. **Fourier's law + thermal conductivity + thermal diffusivity** (30 min)
   - Write: Q = -kA(dT/dx), define each symbol
   - α = k/(ρcp) — what it means physically
   - Temperature effect on k: solids ↓, liquids ↓ (except water ↑), gases ↑
   - *Asked in 7/9 papers, always 3-4 marks*

2. **Dimensionless numbers: Re, Nu, Pr, Gr** (30 min)
   - Formula + physical meaning of each (ratio of what to what)
   - Re = inertia/viscous, Nu = convective/conductive, Pr = momentum diffusivity/thermal diffusivity, Gr = buoyancy/viscous
   - *Asked in 7/9 papers, 3-7 marks*

3. **Free vs forced convection — comparison table** (20 min)
   - Driving force, flow mechanism, h values, examples
   - *Asked in 6/9 papers, always 3 marks*

4. **Modes of heat transfer — conduction vs convection vs radiation** (15 min)
   - One-line definition + example each
   - *Asked in 4/9 papers, always 3 marks*

5. **Fin theory — types, selection criteria, when fins hurt** (25 min)
   - Types: straight rectangular, triangular, pin, annular
   - Selection: high k material, thin + long, high h surface
   - When fins decrease HT: when Bi (hAc/kP) > 1, adding fins to an already high-h surface
   - *Asked in 7/9 papers, 3-4 marks*

### Hour 2-4: The Big Derivation (Target: 7 marks)

6. **General heat conduction equation (Cartesian) + Laplace/Poisson/Fourier** (1.5 hours)
   - This is the single highest-frequency 7-mark question in the entire subject
   - Derive from energy balance on infinitesimal element
   - Reduce to: Laplace (steady, no qg → ∇²T = 0), Poisson (steady + qg → ∇²T + qg/k = 0), Fourier (no qg → ∇²T = (1/α)∂T/∂τ)
   - *Asked in 6/9 papers, always 7 marks*

### Hour 4-6: Critical Radius + Composite Wall (Target: 7-11 marks)

7. **Critical radius of insulation** (1 hour)
   - Cylinder: rc = k/h (derivation from dQ/dr = 0)
   - Sphere: rc = 2k/h
   - Physical significance: below rc, adding insulation increases heat loss
   - *Asked in 5/9 papers, 3-7 marks*

8. **Composite wall — thermal resistance + numerical** (1.5 hours)
   - Series resistance: Rtotal = R1 + R2 + ... + Rconv
   - Q = ΔT/Rtotal
   - Practice one plane wall numerical with convection on both sides
   - *Asked in 6/9 papers, 4-7 marks*

### DO NOT STUDY (Strategy A)
- ❌ Heat exchangers, LMTD, NTU, effectiveness, fouling
- ❌ Boiling, condensation
- ❌ Lumped system analysis, Biot/Fourier in transient context
- ❌ Radiation shields derivation
- ❌ Blasius solution
- ❌ Thermometer well
- ❌ Fin numericals (save for Strategy B)
- ❌ Buckingham π derivations
- ❌ General equation in cylindrical/spherical coordinates

**Expected marks: 20-24/30**

---

## 5. 🎯 Strategy B: 25/30 Marks (~12-15 hours)

Everything from Strategy A, plus the following in order:

### Hours 7-9: Fin Mastery (Target: +7-11 marks)

9. **Fin numerical — insulated tip** (2 hours)
   - Learn: m = √(hP/kAc)
   - Insulated tip: θ(x) = θb × cosh[m(L-x)] / cosh(mL)
   - Q = √(hPkAc) × θb × tanh(mL)
   - Infinite fin: Q = √(hPkAc) × θb
   - Practice 3 numericals: rectangular fin, equilateral triangle cross-section, cylindrical rod
   - For triangular cross section: A = (√3/4)a², P = 3a
   - *Asked in 7/9 papers, always 7 marks — this is the most repeated numerical*

10. **Fin efficiency + effectiveness definitions with formulas** (30 min)
    - η = Qactual/Qmax = tanh(mL)/(mL) [insulated tip]
    - ε = Qwith fin/Qwithout fin = √(kP/hAc) × tanh(mL)
    - ε > 1 means fin is useful; ε < 1 means fin actually hurts
    - *Asked in 4/9 papers, 3-7 marks*

### Hours 9-10.5: Convection Depth (Target: +7 marks)

11. **Buckingham π: Nu = f(Gr, Pr) for free convection** (1.5 hours)
    - Variables: h, L, k, μ, ρ, Cp, βgΔT
    - Step-by-step π-theorem application
    - Final: Nu = C(Gr)^m(Pr)^n
    - *Asked in 3/9 papers, always 7 marks*

12. **Thermal + hydrodynamic boundary layer** (30 min)
    - Definitions with diagrams
    - Velocity BL: region where u < 0.99U∞
    - Thermal BL: region where (T-Ts)/(T∞-Ts) < 0.99
    - Effect of Pr: Pr > 1 → thermal BL thinner than velocity BL
    - *Asked in 4/9 papers, 3-7 marks*

### Hours 10.5-13: Radiation Coverage (Target: +7-10 marks)

13. **Kirchhoff's law — state + prove** (30 min)
    - At thermal equilibrium: ε = α (emissivity equals absorptivity)
    - Proof using cavity argument
    - *Asked in 4/9 papers, 3-7 marks*

14. **Absorptivity, reflectivity, transmissivity** (15 min)
    - Definitions + α + ρ + τ = 1
    - *Asked in 4/9 papers, always 3 marks*

15. **Black body, white body, grey body definitions** (15 min)
    - Black: α = 1, White: ρ = 1, Grey: ε constant (independent of λ)
    - *Asked in 4/9 papers, 3-4 marks*

16. **Intensity of radiation + Eb = πIb proof** (1 hour)
    - Define intensity, derive using solid angle integration
    - *Asked in 3/9 papers, always 7 marks*

17. **Shape factor — definition + properties** (30 min)
    - Reciprocity: A1F12 = A2F21
    - Summation: ΣFij = 1
    - For convex surface: Fii = 0
    - *Asked in 4/9 papers, 3-4 marks*

18. **Stefan-Boltzmann law + radiation numerical** (1 hour)
    - Eb = σT⁴ where σ = 5.67×10⁻⁸ W/m²K⁴
    - Practice: total energy emitted, intensity, Wien's displacement (λmax·T = 2898 μm·K)
    - *Asked in 4/9 papers, 4-7 marks*

### Hours 13-14: Additional Coverage

19. **General heat conduction in cylindrical coordinates** (1 hour)
    - Derivation from energy balance on cylindrical element
    - *Asked in 3/9 papers, 4-7 marks*

20. **Free convection numerical using correlation** (1 hour)
    - Practice: vertical plate or horizontal cylinder
    - Use Nu = C(Gr·Pr)^n, find h, then Q = hA(Ts - T∞)
    - *Asked in 4/9 papers, 4-7 marks*

### DO NOT STUDY (Strategy B)
- ❌ Heat exchangers, LMTD, NTU, effectiveness, fouling — 0 marks on your exam
- ❌ Boiling, condensation — 0 marks on your exam
- ❌ Lumped system analysis, transient conduction — 0 marks on your exam
- ❌ Radiation shields derivation — not explicitly in syllabus
- ❌ Blasius solution full derivation — borderline, low frequency
- ❌ Thermometer well — transient conduction application
- ❌ Heat pipe — not in syllabus
- ❌ TEMA charts — not in syllabus

**Expected marks: 25-28/30**

---

## 6. Key Formulas to Memorize

### CO-1: Conduction + Fins

| # | Formula | When to Use |
|---|---------|-------------|
| 1 | $Q = -kA\frac{dT}{dx}$ | Fourier's law |
| 2 | $\alpha = \frac{k}{\rho c_p}$ | Thermal diffusivity definition |
| 3 | $\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} + \frac{\partial^2 T}{\partial z^2} + \frac{q_g}{k} = \frac{1}{\alpha}\frac{\partial T}{\partial \tau}$ | General Cartesian equation |
| 4 | Laplace: $\nabla^2 T = 0$ | Steady, no heat generation |
| 5 | Poisson: $\nabla^2 T + \frac{q_g}{k} = 0$ | Steady + heat generation |
| 6 | Fourier: $\nabla^2 T = \frac{1}{\alpha}\frac{\partial T}{\partial \tau}$ | Transient, no heat generation |
| 7 | $Q = \frac{\Delta T}{\sum R}$ where $R_{wall} = \frac{L}{kA}$, $R_{conv} = \frac{1}{hA}$ | Composite wall |
| 8 | $r_c = \frac{k}{h}$ (cylinder), $r_c = \frac{2k}{h}$ (sphere) | Critical radius |
| 9 | $m = \sqrt{\frac{hP}{kA_c}}$ | Fin parameter |
| 10 | $Q_{fin} = \sqrt{hPkA_c} \cdot \theta_b \cdot \tanh(mL)$ | Fin insulated at tip |
| 11 | $Q_{fin} = \sqrt{hPkA_c} \cdot \theta_b$ | Infinitely long fin |
| 12 | $\eta = \frac{\tanh(mL)}{mL}$ | Fin efficiency (insulated tip) |
| 13 | $\varepsilon = \frac{Q_{with\ fin}}{Q_{without\ fin}}$ | Fin effectiveness |
| 14 | $\frac{1}{U} = \frac{1}{h_i} + \frac{L}{k} + \frac{1}{h_o}$ | Overall HTC (plane wall) |

### CO-2: Convection

| # | Formula | When to Use |
|---|---------|-------------|
| 15 | $Q = hA(T_s - T_\infty)$ | Newton's law of cooling |
| 16 | $Re = \frac{\rho V L}{\mu} = \frac{VL}{\nu}$ | Reynolds number |
| 17 | $Nu = \frac{hL}{k}$ | Nusselt number |
| 18 | $Pr = \frac{\mu c_p}{k} = \frac{\nu}{\alpha}$ | Prandtl number |
| 19 | $Gr = \frac{g\beta \Delta T L^3}{\nu^2}$ | Grashof number |

### CO-3: Radiation

| # | Formula | When to Use |
|---|---------|-------------|
| 20 | $\alpha + \rho + \tau = 1$ | Absorptivity + reflectivity + transmissivity |
| 21 | $E_b = \sigma T^4$ where $\sigma = 5.67 \times 10^{-8}$ W/m²K⁴ | Stefan-Boltzmann law |
| 22 | $\lambda_{max} \cdot T = 2898\ \mu m \cdot K$ | Wien's displacement law |
| 23 | $E_{b\lambda} = \frac{C_1 \lambda^{-5}}{e^{C_2/\lambda T} - 1}$ | Planck's law |
| 24 | $I_b = \frac{E_b}{\pi}$ | Intensity of normal radiation |
| 25 | $\varepsilon = \alpha$ (at thermal equilibrium) | Kirchhoff's law |
| 26 | $A_1 F_{12} = A_2 F_{21}$ | Reciprocity rule |
| 27 | $\sum_{j=1}^{n} F_{ij} = 1$ | Summation rule |

---

## 7. Honest Risk Assessment

> [!IMPORTANT]
> **What could go wrong with this analysis:**
>
> 1. **New syllabus = new professor = new question style.** These PYQs are from old code 3151909. Prof. Pandey may set questions differently — especially theory questions that don't match old patterns. The frequency data is the best predictor available, but it's not a guarantee.
>
> 2. **Radiation section has no Tier 1 topics.** Every radiation topic sits at Tier 2 or below. This means radiation questions are less predictable from PYQ patterns. If the exam has 10 marks from radiation, you need broad Tier 2 coverage — not deep mastery of one topic.
>
> 3. **The "Cartesian general equation" derivation is so dominant (6/9) that if they DON'T ask it, Strategy A loses 7 marks immediately.** Hedge by also knowing composite wall derivation.
>
> 4. **Fin numericals are the safest bet for 7 marks** — asked in 7/9 papers. If you can do only ONE numerical type, do fins (insulated tip).

---

## 8. Coaching Transition

---

### ✅ Analysis Complete — Ready to Start Coaching?

Your study map is above. Now we move into active recall mode.

**If you have your coaching prompt file**, say:
> "Start coaching. Prompt file: [path to your gtu_midsem_prompt.md]"

I will read the coaching prompt, adopt that role, and begin drilling you using the study priorities above — starting with Tier 1 topics in the recommended order.

**If you don't have the coaching prompt**, I'll default to Mode 2 (Deep practice) — one GTU-format question at a time, graded with specific point breakdowns.

Which topic do you want to start with?
