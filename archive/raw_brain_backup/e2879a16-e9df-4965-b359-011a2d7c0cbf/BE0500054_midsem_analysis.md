# Fundamental of Power Electronics (BE0500054) — Mid-Sem Analysis (30 Marks)

> [!IMPORTANT]
> **No PYQs exist** — brand new subject. This analysis is built from: GTU exam pattern norms, syllabus weight distribution (4 units for 30 marks), and power electronics exam conventions across Indian universities.

---

## 1. Syllabus Scope — What's IN

| Unit | Title | Key Sub-Topics |
|:----:|-------|----------------|
| 1 | Introduction & Devices | Basics, PE systems, applications, control vs power circuits, device classification (Diode, SCR, TRIAC, DIAC, BJT, MOSFET, IGBT), structure & operation (conceptual), ratings, switching frequency, thermal considerations |
| 2 | Power Rectifiers | Half/full wave diode rectifiers, bridge rectifier, controlled rectifiers (half/fully controlled), firing angle, R & RL loads, applications (power supplies, battery charging) |
| 3 | Inverters | DC–AC conversion need, VSI & CSI, square wave inverter, intro to PWM, 3-phase inverter basics, applications (UPS, EV drives, solar inverters, motor drives) |
| 4 | DC–DC Converters | DC supply basics, linear vs switching supply, duty cycle & switching principles, Buck/Boost/Buck-Boost, Flyback & Forward converter basics, isolated vs non-isolated, applications (SMPS, EV, battery chargers) |

> [!WARNING]
> **Danger Zones — Do NOT Study These:**
> - Advanced IGBT/MOSFET fabrication processes (only conceptual structure is in scope)
> - Multi-pulse rectifiers (12-pulse, 24-pulse) — NOT mentioned
> - Space vector modulation / advanced PWM — only "introductory PWM" is in scope
> - Resonant converters, soft switching — NOT mentioned
> - Cycloconverters, matrix converters — NOT in scope
> - Detailed thermal design / heatsink calculations — only "thermal considerations" conceptually
> - Choppers (the word "chopper" is not used — it's called DC-DC converters here)

---

## 2. Predicted Marks Distribution (30 Marks Mid-Sem)

GTU mid-sem = typically 6 questions × 5 marks each, or a mix of 3-mark + 4-mark + 7-mark. Expected split:

| Unit | Expected Marks | Why |
|:----:|:--------------:|-----|
| 1 | ~7-8 marks | Theory-heavy, definitions + device comparison — easiest to ask |
| 2 | ~8-9 marks | Numericals (rectifier output, firing angle) + theory — heaviest unit |
| 3 | ~6-7 marks | Theory + basic waveform sketches |
| 4 | ~7-8 marks | Numericals (duty cycle, Buck/Boost) + theory |

---

## 3. Topic Priority Table (No PYQ Data — Based on Exam Probability)

### Unit 1: Introduction & Devices

| Topic | Priority | Expected Marks | Question Type |
|-------|:--------:|:--------------:|---------------|
| Comparison table: SCR vs MOSFET vs IGBT | 🔴 Tier 1 | 3-5 | Table/theory — **almost guaranteed** |
| Advantages & applications of Power Electronics | 🔴 Tier 1 | 3-4 | List/short answer |
| Control circuit vs Power circuit (difference) | 🔴 Tier 1 | 3 | Table or short note |
| V-I characteristics of SCR with diagram | 🔴 Tier 1 | 4-5 | Diagram + explanation |
| Device classification (uncontrolled/semi/fully) | 🟡 Tier 2 | 3-4 | Classification chart |
| TRIAC & DIAC structure + operation | 🟡 Tier 2 | 3-4 | Diagram + short note |
| Switching frequency & thermal considerations | 🟢 Tier 3 | 3 | Short note |

### Unit 2: Power Rectifiers

| Topic | Priority | Expected Marks | Question Type |
|-------|:--------:|:--------------:|---------------|
| Full wave bridge rectifier — waveform + Vdc formula (R load) | 🔴 Tier 1 | 5-7 | **Numerical + diagram** |
| Fully controlled rectifier — firing angle α, Vdc = (Vm/π)(1+cosα) | 🔴 Tier 1 | 5-7 | **Numerical — highest priority** |
| Half wave rectifier — waveform + Vdc, Vrms | 🔴 Tier 1 | 3-5 | Numerical/diagram |
| Half controlled vs fully controlled rectifier comparison | 🟡 Tier 2 | 3-4 | Table |
| Effect of RL load on rectifier (freewheeling diode concept) | 🟡 Tier 2 | 3-4 | Waveform sketch + explanation |
| Applications of rectifiers | 🟢 Tier 3 | 2-3 | List |

### Unit 3: Inverters

| Topic | Priority | Expected Marks | Question Type |
|-------|:--------:|:--------------:|---------------|
| VSI vs CSI comparison | 🔴 Tier 1 | 3-4 | **Table — very likely** |
| Single-phase square wave inverter — output waveform + working | 🔴 Tier 1 | 5-7 | Diagram + explanation |
| Need for DC-AC conversion + applications | 🔴 Tier 1 | 3-4 | Short note |
| Basic concept of PWM (what it does, why it's used) | 🟡 Tier 2 | 3 | Short note |
| 3-phase inverter basics (120° / 180° conduction) | 🟡 Tier 2 | 3-5 | Waveform/diagram |
| Applications: UPS, solar, EV | 🟢 Tier 3 | 2-3 | List |

### Unit 4: DC-DC Converters

| Topic | Priority | Expected Marks | Question Type |
|-------|:--------:|:--------------:|---------------|
| Buck converter — circuit, waveform, Vo = D × Vin | 🔴 Tier 1 | 5-7 | **Numerical + diagram — top priority** |
| Boost converter — circuit, waveform, Vo = Vin/(1-D) | 🔴 Tier 1 | 5-7 | **Numerical + diagram** |
| Buck-Boost converter — Vo = -D×Vin/(1-D) | 🔴 Tier 1 | 4-5 | Numerical |
| Linear vs Switching power supply comparison | 🔴 Tier 1 | 3-4 | **Table — very likely** |
| Duty cycle concept + switching principle | 🟡 Tier 2 | 3 | Short note |
| Flyback vs Forward converter (basic difference) | 🟡 Tier 2 | 3-4 | Comparison |
| Isolated vs non-isolated supply | 🟡 Tier 2 | 3 | Short note |
| Applications: SMPS, EV subsystems | 🟢 Tier 3 | 2-3 | List |

---

## 4. 🎯 Strategy A: 20/30 Marks (~4-5 hours)

Study ONLY these, in this order:

| # | What to Study | Time | Expected Marks |
|:-:|---------------|:----:|:--------------:|
| 1 | **Comparison table: SCR vs MOSFET vs IGBT** — memorize 6-7 parameters (voltage, current, speed, gate drive, conduction drop, cost, application) | 20 min | 3-5 |
| 2 | **SCR V-I characteristics diagram** — draw from memory, label holding current, latching current, breakover voltage, forward/reverse blocking | 20 min | 3-4 |
| 3 | **Control vs Power circuit** — 5 differences table | 10 min | 3 |
| 4 | **Full wave bridge rectifier** — draw circuit, draw waveform for R load, formula: Vdc = 2Vm/π, Vrms = Vm/√2 | 30 min | 4-5 |
| 5 | **Controlled rectifier firing angle** — Vdc = (Vm/π)(1+cosα) for full wave, Vdc = (Vm/2π)(1+cosα) for half wave. Practice 2 numericals | 45 min | 5-7 |
| 6 | **Buck converter** — circuit diagram, Vo = D×Vin, practice 2 numericals (given Vin, D, find Vo and vice versa) | 30 min | 4-5 |
| 7 | **Boost converter** — circuit diagram, Vo = Vin/(1-D), practice 2 numericals | 30 min | 4-5 |
| 8 | **VSI vs CSI table** — 5-6 comparison points | 15 min | 3 |
| 9 | **Linear vs Switching power supply table** — 5-6 points (efficiency, size, regulation, cost, ripple, complexity) | 15 min | 3 |
| 10 | **Square wave inverter** — basic working + output waveform sketch | 20 min | 3-4 |

**Total: ~4 hours | Expected: 20-24 marks**

> [!TIP]
> **DO NOT WASTE TIME ON:**
> - Reading full device fabrication details
> - Deriving rectifier formulas from scratch
> - PWM mathematics
> - 3-phase inverter switching tables
> - Flyback/Forward converter internal working

---

## 5. 🎯 Strategy B: 25/30 Marks (~8-10 hours)

Everything from Strategy A **PLUS**:

| # | What to Add | Time | Extra Marks |
|:-:|-------------|:----:|:-----------:|
| 11 | **TRIAC & DIAC** — structure diagram + how they work (both direction conduction) | 25 min | 3 |
| 12 | **Device classification chart** — uncontrolled (diode), semi-controlled (SCR), fully controlled (GTO, IGBT, MOSFET) — draw a tree diagram | 15 min | 2-3 |
| 13 | **RL load effect on rectifier** — waveform changes, freewheeling diode, discontinuous vs continuous conduction | 30 min | 3-4 |
| 14 | **Half controlled vs fully controlled rectifier** — comparison + circuit diagrams | 25 min | 3 |
| 15 | **Buck-Boost converter** — circuit + formula Vo = D×Vin/(1-D), 2 numericals | 30 min | 3-4 |
| 16 | **PWM concept** — why sinusoidal PWM reduces harmonics, basic idea only | 20 min | 2-3 |
| 17 | **3-phase inverter** — 180° conduction mode, switching sequence (conceptual) | 30 min | 3 |
| 18 | **Flyback vs Forward converter** — comparison table + basic circuit | 25 min | 3 |
| 19 | **Applications** — make ONE combined list of all applications across units (UPS, SMPS, EV, solar, battery charging, motor drives) | 15 min | 2-3 |
| 20 | **Isolated vs Non-isolated supply** — difference + examples | 10 min | 2 |

**Total: ~8 hours | Expected: 25-28 marks**

---

## 6. Key Formulas to Memorize

### Rectifiers
| Circuit | Vdc | Vrms |
|---------|-----|------|
| Half wave (uncontrolled, R load) | Vm/π | Vm/2 |
| Full wave (uncontrolled, R load) | 2Vm/π | Vm/√2 |
| Half wave (controlled) | (Vm/2π)(1 + cosα) | — |
| Full wave (controlled) | (Vm/π)(1 + cosα) | — |

Where Vm = √2 × Vrms(supply), α = firing angle

### DC-DC Converters
| Converter | Output Voltage | Duty Cycle Range |
|-----------|---------------|:----------------:|
| Buck (step-down) | Vo = D × Vin | 0 < D < 1 |
| Boost (step-up) | Vo = Vin / (1 − D) | 0 < D < 1 |
| Buck-Boost | Vo = D × Vin / (1 − D) | 0 < D < 1 |

Where D = Ton / T (duty cycle), T = switching period

### Inverter
- Square wave inverter RMS output = Vdc (for ideal single-phase)
- Fundamental component of square wave = (4Vdc) / π

### Quick Numbers to Remember
- Power diode: forward drop ~0.7-1.2V
- SCR: forward drop ~1.5-2.5V
- MOSFET: RDS(on) based (resistive drop)
- IGBT: forward drop ~2-3V

---

## 7. Exam Day Cheat Sheet — What to Write for Maximum Marks

### Theory Questions — Use This Format:
1. **Definition** (1 line) → 1 mark
2. **Diagram** (neat, labeled) → 1-2 marks
3. **Working/Explanation** (3-4 bullet points) → 1-2 marks
4. **Advantages OR Applications** (3-4 points) → 1 mark

### Numerical Questions — Use This Format:
1. **Given/Find** → write clearly
2. **Formula** → write the formula, get 1 mark even if calculation wrong
3. **Substitution** → show step by step
4. **Answer with unit** → box it

> [!CAUTION]
> **Golden Rule for New Subject Exams:** When there are no PYQs, professors pull directly from the textbook examples and end-of-chapter problems. The first mid-sem of a new subject is usually **easier** than subsequent years — they test definitions, comparisons, basic diagrams, and straightforward numericals. **Do NOT overcomplicate your preparation.**

---

## 8. ✅ Analysis Complete — Ready to Start Coaching?

Your study map is above. Since this is a new subject with no PYQs, your edge comes from:
1. **Nailing comparison tables** (SCR/MOSFET/IGBT, VSI/CSI, Linear/SMPS) — these are almost guaranteed 
2. **Mastering 3 numerical types** — controlled rectifier (firing angle), Buck converter, Boost converter
3. **Drawing neat diagrams** — SCR V-I curve, bridge rectifier, Buck/Boost circuits

I'll default to **Mode 2 (Deep practice)** — one GTU-format question at a time, graded with specific point breakdowns.

**Which topic do you want to start drilling?**
- Unit 1 (Devices — comparison tables, SCR characteristics)
- Unit 2 (Rectifiers — firing angle numericals)
- Unit 3 (Inverters — VSI/CSI, square wave)
- Unit 4 (DC-DC — Buck/Boost numericals)
