"""
Manim Scenes for Episode 03: Boss Building Rents
72 programmatic math calculation clips — finance Stickman / Quiet Money POV

RENDERING STANDARD:
- CFR 25.0 FPS: manim -qm --fps 25 -r 1920,1080 --format=mp4
- Each scene's self.wait() is calibrated to real_duration + 0.47s handle
- Motion Immunity: NO slow push-in zoom applied in assemble_video.py
- Pure math/charts only: NO stickmen, NO character diffusion images
"""

from manim import *
import numpy as np

# ─────────────────────────── SHARED STYLE ──────────────────────────────────
BG       = "#0f172a"      # dark slate background
CREAM    = "#f4e9d0"      # text / axes
GREEN    = "#10b981"      # positive / growth
RED      = "#ef4444"      # debt / negative
GOLD     = "#f59e0b"      # wealth / milestone
GRAY     = "#64748b"      # neutral label

def _cfg():
    config.background_color = BG
    config.pixel_width  = 1920
    config.pixel_height = 1080
    config.frame_rate   = 25

def title_text(label, scale=1.1, color=CREAM):
    return Text(label, font="Helvetica Neue", weight=BOLD, color=color).scale(scale)

def label_text(label, scale=0.65, color=CREAM):
    return Text(label, font="Helvetica Neue", color=color).scale(scale)

# ─────── CUT 048  dur=4.36s  render=4.83s ──────────────────────────────────
class Anim048(Scene):
    """Condo cost build: price→down→P&I→all-in"""
    def construct(self):
        _cfg()
        items = [
            ("Condo Price",        "$189,000", CREAM),
            ("5% Down",            "−$9,450",  RED),
            ("P&I / month",        "$1,207",   RED),
            ("+ Tax/Ins/PMI",      "$353",     RED),
            ("All-In Monthly",     "$1,560",   RED),
        ]
        rows = VGroup()
        for label, val, col in items:
            row = VGroup(
                label_text(label, 0.65, CREAM),
                label_text(val,   0.65, col)
            ).arrange(RIGHT, buff=1.2)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        for row in rows:
            self.play(Write(row), run_time=0.65)
        self.wait(1.48)   # total≈4.83s

# ─────── CUT 049  dur=5.14s  render=5.61s ──────────────────────────────────
class Anim049(Scene):
    """Bar: take-home $2,680 with $1,560 shaded red = 58%"""
    def construct(self):
        _cfg()
        bar_w = 8
        full  = Rectangle(width=bar_w, height=1.0, fill_color=GREEN,
                          fill_opacity=0.3, stroke_color=GREEN, stroke_width=2)
        rent  = Rectangle(width=bar_w*0.582, height=1.0, fill_color=RED,
                          fill_opacity=0.85, stroke_width=0).align_to(full, LEFT)
        t_all = label_text("Take-Home: $2,680", color=CREAM).next_to(full, UP, buff=0.2)
        t_r   = label_text("Mortgage: $1,560 (58%)", color=RED).next_to(rent, DOWN, buff=0.2)
        grp   = VGroup(full, rent, t_all, t_r).center()
        self.play(Create(full), Write(t_all), run_time=0.9)
        self.play(Create(rent), run_time=1.0)
        self.play(Write(t_r),   run_time=0.7)
        self.wait(2.21)

# ─────── CUT 054  dur=3.82s  render=4.29s ──────────────────────────────────
class Anim054(Scene):
    """Odometer: $19.40/hr × 2,080 hrs = $40,350/yr"""
    def construct(self):
        _cfg()
        eq = VGroup(
            label_text("$19.40 / hr", color=GOLD),
            label_text("×  2,080 hours", color=CREAM),
            label_text("= $40,350 / year", color=GREEN).scale(1.3),
        ).arrange(DOWN, buff=0.5).center()
        for mob in eq:
            self.play(FadeIn(mob, shift=UP*0.2), run_time=0.8)
        self.wait(1.69)

# ─────── CUT 060  dur=4.28s  render=4.75s ──────────────────────────────────
class Anim060(Scene):
    """Runway countdown: 19 days punch"""
    def construct(self):
        _cfg()
        label = label_text("RUNWAY IF PAYCHECKS STOP", color=GRAY)
        days  = Text("19 DAYS", font="Helvetica Neue", weight=BOLD,
                     color=RED).scale(3.5)
        sub   = label_text("savings ÷ monthly expenses", color=GRAY)
        grp   = VGroup(label, days, sub).arrange(DOWN, buff=0.45).center()
        self.play(FadeIn(label), run_time=0.5)
        self.play(Write(days),   run_time=1.2)
        self.play(FadeIn(sub),   run_time=0.5)
        self.wait(2.1)

# ─────── CUT 069  dur=3.10s  render=3.57s ──────────────────────────────────
class Anim069(Scene):
    """Mortgage card: $560k price → 5% down → 7.1%"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("House Price",    color=CREAM), label_text("$560,000", color=CREAM)).arrange(RIGHT, buff=1.5),
            VGroup(label_text("5% Down",        color=CREAM), label_text("$28,000",  color=RED  )).arrange(RIGHT, buff=1.5),
            VGroup(label_text("Loan Amount",    color=CREAM), label_text("$532,000", color=RED  )).arrange(RIGHT, buff=1.5),
            VGroup(label_text("Interest Rate",  color=CREAM), label_text("7.1%",     color=RED  )).arrange(RIGHT, buff=1.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        for row in rows:
            self.play(FadeIn(row), run_time=0.55)
        self.wait(0.97)

# ─────── CUT 070  dur=5.00s  render=5.47s ──────────────────────────────────
class Anim070(Scene):
    """P&I bar rising to $3,575"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,1,1], y_range=[0,5000,1000],
                  x_length=4, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  y_axis_config={"include_numbers": False})
        bar = ax.get_riemann_rectangles(ax.plot(lambda x: 3575*x, x_range=[0,1]),
                                        x_range=[0,1], dx=1, color=RED, fill_opacity=0.85)
        label = label_text("P&I / month: $3,575", color=RED).next_to(ax, UP)
        self.play(Create(ax), Write(label), run_time=1.0)
        self.play(Create(bar), run_time=2.5)
        self.wait(1.47)

# ─────── CUT 072  dur=2.32s  render=2.79s ──────────────────────────────────
class Anim072(Scene):
    """Bar grows to ~$4,500 with tax/ins/PMI segments"""
    def construct(self):
        _cfg()
        items = [
            ("P&I",         3575, RED),
            ("Tax",          540, "#f97316"),
            ("Insurance",    220, GOLD),
            ("PMI",          165, "#a78bfa"),
        ]
        bars = VGroup()
        total = 0
        for label, amt, col in items:
            b = Rectangle(width=amt/600, height=0.8, fill_color=col,
                          fill_opacity=0.85, stroke_width=0)
            t = label_text(f"{label}: ${amt}", color=col, scale=0.55)
            g = VGroup(b, t).arrange(RIGHT, buff=0.15)
            bars.add(g)
            total += amt
        bars.arrange(DOWN, aligned_edge=LEFT, buff=0.2).center()
        grand = label_text(f"Total ≈ ${total:}/mo", color=CREAM).scale(1.2).next_to(bars, DOWN, buff=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.3), run_time=1.4)
        self.play(Write(grand), run_time=0.5)
        self.wait(0.59)

# ─────── CUT 082  dur=3.76s  render=4.23s ──────────────────────────────────
class Anim082(Scene):
    """Money in $10,400 vs money out $10,100 monthly"""
    def construct(self):
        _cfg()
        in_bar  = Rectangle(width=6.5, height=1.0, fill_color=GREEN, fill_opacity=0.8, stroke_width=0)
        out_bar = Rectangle(width=6.3, height=1.0, fill_color=RED,   fill_opacity=0.8, stroke_width=0)
        t_in  = label_text("IN:  $10,400 / month",  color=GREEN).next_to(in_bar,  RIGHT, buff=0.3)
        t_out = label_text("OUT: $10,100 / month",  color=RED  ).next_to(out_bar, RIGHT, buff=0.3)
        gap   = label_text("Gap: $300 / month", color=GOLD).scale(1.2)
        grp   = VGroup(VGroup(in_bar, t_in), VGroup(out_bar, t_out)).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        gap.next_to(grp, DOWN, buff=0.5)
        self.play(FadeIn(grp[0]), run_time=0.8)
        self.play(FadeIn(grp[1]), run_time=0.8)
        self.play(Write(gap),     run_time=0.7)
        self.wait(1.43)

# ─────── CUT 083  dur=4.13s  render=4.60s ──────────────────────────────────
class Anim083(Scene):
    """$300 gap sliver, checking balance $3,300"""
    def construct(self):
        _cfg()
        label_gap = label_text("Monthly Gap: $300", color=GOLD).scale(1.4)
        sliver    = Rectangle(width=0.25, height=1.5, fill_color=GOLD, fill_opacity=0.9, stroke_width=0)
        label_bal = label_text("Burke's Checking: $3,300", color=RED).scale(1.1)
        label_sub = label_text("≈ 10 days of expenses", color=GRAY)
        grp = VGroup(label_gap, sliver, label_bal, label_sub).arrange(DOWN, buff=0.45).center()
        for m in grp:
            self.play(FadeIn(m), run_time=0.75)
        self.wait(1.1)

# ─────── CUT 086  dur=1.34s  render=1.81s ──────────────────────────────────
class Anim086(Scene):
    """10 DAYS punch"""
    def construct(self):
        _cfg()
        days = Text("10 DAYS", font="Helvetica Neue", weight=BOLD, color=RED).scale(4.0)
        sub  = label_text("Burke's runway", color=GRAY)
        grp  = VGroup(days, sub).arrange(DOWN, buff=0.4).center()
        self.play(Write(days),  run_time=0.7)
        self.play(FadeIn(sub),  run_time=0.3)
        self.wait(0.51)

# ─────── CUT 087  dur=2.56s  render=3.03s ──────────────────────────────────
class Anim087(Scene):
    """Salary bars: Burke $128k vs You $40,350"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,3,1], y_range=[0,150000,50000],
                  x_length=5, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        b_burke = ax.get_riemann_rectangles(ax.plot(lambda x: 128000, x_range=[0.1,1.0]),
                                            x_range=[0.1,1.0], dx=0.9, color=RED, fill_opacity=0.8)
        b_you   = ax.get_riemann_rectangles(ax.plot(lambda x: 40350,  x_range=[1.5,2.4]),
                                            x_range=[1.5,2.4], dx=0.9, color=GREEN, fill_opacity=0.8)
        t_b = label_text("Burke\n$128k", color=RED,  scale=0.6).next_to(b_burke, UP, buff=0.1)
        t_y = label_text("You\n$40k",   color=GREEN, scale=0.6).next_to(b_you,   UP, buff=0.1)
        self.play(Create(ax), run_time=0.7)
        self.play(Create(b_burke), Write(t_b), Create(b_you), Write(t_y), run_time=1.4)
        self.wait(0.63)

# ─────── CUT 088  dur=3.06s  render=3.53s ──────────────────────────────────
class Anim088(Scene):
    """Runway flip: You 19 days vs Burke 10 days"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Your Runway:",   color=CREAM), label_text("19 DAYS", color=GREEN)).arrange(RIGHT, buff=1.5),
            VGroup(label_text("Burke's Runway:", color=CREAM), label_text("10 DAYS", color=RED  )).arrange(RIGHT, buff=1.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).center()
        sub = label_text("You earn ⅓ — but own nearly 2× the tomorrows", color=GOLD).next_to(rows, DOWN, buff=0.5)
        self.play(FadeIn(rows[0]), run_time=0.9)
        self.play(FadeIn(rows[1]), run_time=0.9)
        self.play(Write(sub),      run_time=0.7)
        self.wait(0.74)

# ─────── CUT 093  dur=3.20s  render=3.67s ──────────────────────────────────
class Anim093(Scene):
    """Burke's bottom line: $3,300 hair-thin bar"""
    def construct(self):
        _cfg()
        bar = Rectangle(width=0.4, height=0.18, fill_color=RED, fill_opacity=0.9, stroke_width=0).center()
        label = label_text("Burke's Bottom Line: $3,300 / month", color=RED).scale(1.1).next_to(bar, UP, buff=0.4)
        sub   = label_text("≈ 10 days if income stops", color=GRAY).next_to(bar, DOWN, buff=0.4)
        self.play(Create(bar), Write(label), run_time=1.4)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.07)

# ─────── CUT 107  dur=5.36s  render=5.83s ──────────────────────────────────
class Anim107(Scene):
    """Year-1 accumulation line climbing to $971"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[1,13,1], y_range=[0,1200,200],
                  x_length=9, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  x_axis_config={"include_numbers": False},
                  y_axis_config={"include_numbers": False})
        def growth(x):
            return max(0, 971*(x-1)/11)
        curve = ax.plot(growth, x_range=[1,12], color=GREEN, stroke_width=3)
        dot   = Dot(ax.c2p(12, 971), color=GREEN)
        lab   = label_text("$971", color=GREEN).next_to(dot, RIGHT)
        x_lab = label_text("Month", color=GRAY).next_to(ax.x_axis, DOWN)
        self.play(Create(ax), Write(x_lab), run_time=1.0)
        self.play(Create(curve), run_time=2.5)
        self.play(FadeIn(dot), Write(lab), run_time=0.7)
        self.wait(0.93)

# ─────── CUT 120  dur=4.38s  render=4.85s ──────────────────────────────────
class Anim120(Scene):
    """Raise split: $240 → $120 invest + $120 life"""
    def construct(self):
        _cfg()
        raise_label = label_text("New Raise: +$240/mo", color=GOLD).scale(1.2)
        arrow_l = Arrow(UP*0.5, LEFT*2+DOWN*0.5, color=GREEN,  stroke_width=4)
        arrow_r = Arrow(UP*0.5, RIGHT*2+DOWN*0.5, color=RED,   stroke_width=4)
        invest  = label_text("$120 → Investments", color=GREEN).next_to(arrow_l.get_end(), DOWN)
        life    = label_text("$120 → Life",         color=RED  ).next_to(arrow_r.get_end(), DOWN)
        grp = VGroup(raise_label).center().shift(UP*1.5)
        self.play(Write(raise_label), run_time=0.8)
        self.play(Create(arrow_l), Create(arrow_r), run_time=1.2)
        self.play(Write(invest), Write(life), run_time=1.0)
        self.wait(1.05)

# ─────── CUT 122  dur=4.26s  render=4.73s ──────────────────────────────────
class Anim122(Scene):
    """Calendar wheel: auto-transfer fires on the 2nd"""
    def construct(self):
        _cfg()
        circle = Circle(radius=2.2, color=GRAY, stroke_width=2)
        days = VGroup(*[
            label_text(str(d), scale=0.5, color=RED if d == 2 else GRAY)
                .move_to(circle.point_at_angle((90 - (d-1)*(360/30)) * DEGREES))
            for d in range(1, 31)
        ])
        marker = Dot(circle.point_at_angle((90-1*(360/30))*DEGREES), color=RED, radius=0.15)
        label  = label_text("AUTO-TRANSFER", color=GREEN).scale(1.2).move_to(ORIGIN)
        sub    = label_text("every 2nd of the month — no decision needed", color=GRAY).scale(0.7).next_to(circle, DOWN, buff=0.3)
        self.play(Create(circle), FadeIn(days), run_time=1.5)
        self.play(FadeIn(marker), Write(label), run_time=1.0)
        self.play(Write(sub), run_time=0.8)
        self.wait(0.93)

# ─────── CUT 123  dur=6.00s  render=6.47s ──────────────────────────────────
class Anim123(Scene):
    """401k escalator: 6% → 10% → 12% → 15%"""
    def construct(self):
        _cfg()
        steps = [(6, 0.9), (10, 1.5), (12, 1.8), (15, 2.25)]
        ax = Axes(x_range=[0,5,1], y_range=[0,20,5],
                  x_length=7, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  y_axis_config={"include_numbers": False})
        y_lab = label_text("401k Contribution %", color=GRAY).next_to(ax.y_axis, LEFT).scale(0.65)
        self.play(Create(ax), Write(y_lab), run_time=1.0)
        prev_x = 0.5
        for pct, x in steps:
            bar = ax.get_riemann_rectangles(ax.plot(lambda _: pct, x_range=[prev_x, x]),
                                            x_range=[prev_x, x], dx=(x-prev_x), color=GREEN, fill_opacity=0.8)
            lbl = label_text(f"{pct}%", color=GREEN, scale=0.7).move_to(ax.c2p((prev_x+x)/2, pct+1.5))
            self.play(Create(bar), Write(lbl), run_time=0.9)
            prev_x = x
        self.wait(1.07)

# ─────── CUT 124  dur=3.66s  render=4.13s ──────────────────────────────────
class Anim124(Scene):
    """Timeline: contribution bump before each raise"""
    def construct(self):
        _cfg()
        line = Line(LEFT*4, RIGHT*4, color=GRAY, stroke_width=2).center()
        events = [
            (-2.5, "Bump 401k\nto 10%",    GREEN, UP),
            (-1.5, "Raise\n+$240",          GOLD,  DOWN),
            ( 0.5, "Bump 401k\nto 12%",    GREEN, UP),
            ( 1.5, "Raise\n+$260",          GOLD,  DOWN),
            ( 3.0, "Bump 401k\nto 15%",    GREEN, UP),
        ]
        dots_labels = VGroup()
        for x, lbl, col, dir_ in events:
            pt  = line.get_start() + RIGHT*(x+4)*0.5
            dot = Dot(pt, color=col)
            txt = label_text(lbl, scale=0.55, color=col).next_to(dot, dir_, buff=0.2)
            dots_labels.add(VGroup(dot, txt))
        self.play(Create(line), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(g) for g in dots_labels], lag_ratio=0.4), run_time=2.5)
        self.wait(0.78)

# ─────── CUT 129  dur=5.45s  render=5.92s ──────────────────────────────────
class Anim129(Scene):
    """End of year 3: $28,700 invested + $11,000 cash"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Invested (Market):", color=CREAM), label_text("$28,700", color=GREEN)).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Cash Reserve:",      color=CREAM), label_text("$11,000", color=GOLD )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Total Net Worth:",   color=CREAM), label_text("$39,700", color=CREAM)).arrange(RIGHT, buff=1.0),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).center()
        head = label_text("— End of Year 3 —", color=GOLD).scale(1.1).next_to(rows, UP, buff=0.5)
        self.play(Write(head), run_time=0.6)
        for row in rows:
            self.play(FadeIn(row), run_time=1.0)
        self.wait(1.72)

# ─────── CUT 141  dur=4.06s  render=4.53s ──────────────────────────────────
class Anim141(Scene):
    """New raise splits again, 401k locks at 15%"""
    def construct(self):
        _cfg()
        label = label_text("401k LOCKED at 15%", color=GREEN).scale(1.4)
        bar   = Rectangle(width=5.5, height=1.2, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        pct   = label_text("15%", color=BG).scale(2.0).move_to(bar)
        split_label = label_text("New raise: $280/mo split → $140 invest  |  $140 life", color=CREAM).scale(0.75)
        grp = VGroup(label, VGroup(bar, pct), split_label).arrange(DOWN, buff=0.5).center()
        self.play(Write(label), run_time=0.7)
        self.play(Create(bar), Write(pct), run_time=1.0)
        self.play(Write(split_label), run_time=0.9)
        self.wait(1.33)

# ─────── CUT 146  dur=5.48s  render=5.95s ──────────────────────────────────
class Anim146(Scene):
    """Burke's debt stack: mortgage, equity line, truck, boat"""
    def construct(self):
        _cfg()
        debts = [
            ("Mortgage",    520000, RED),
            ("Equity Line",  85000, "#f97316"),
            ("Truck Lease",  48000, GOLD),
            ("Boat Loan",    32000, "#a78bfa"),
        ]
        bars = VGroup()
        for label, amt, col in debts:
            w = amt / 55000
            b = Rectangle(width=w, height=0.6, fill_color=col, fill_opacity=0.85, stroke_width=0)
            t = label_text(f"{label}: ${amt:}", color=col, scale=0.6).next_to(b, RIGHT, buff=0.2)
            bars.add(VGroup(b, t))
        bars.arrange(DOWN, aligned_edge=LEFT, buff=0.3).center()
        head = label_text("Burke's Liabilities", color=RED).scale(1.1).next_to(bars, UP, buff=0.4)
        self.play(Write(head), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.35), run_time=3.3)
        self.wait(1.35)

# ─────── CUT 165  dur=3.94s  render=4.41s ──────────────────────────────────
class Anim165(Scene):
    """Debt-to-income gauge past 50% into red"""
    def construct(self):
        _cfg()
        arc_bg   = Arc(radius=2.5, start_angle=PI, angle=-PI, color=GRAY, stroke_width=12)
        arc_ok   = Arc(radius=2.5, start_angle=PI, angle=-PI*0.5, color=GREEN, stroke_width=12)
        arc_warn = Arc(radius=2.5, start_angle=PI*0.5, angle=-PI*0.35, color=RED, stroke_width=12)
        needle_angle = -0.65*PI
        needle = Arrow(ORIGIN, 2.2*np.array([np.cos(needle_angle), np.sin(needle_angle), 0]),
                       color=RED, stroke_width=5, buff=0)
        label  = label_text("Debt-to-Income: 54%", color=RED).scale(1.2).shift(DOWN*2)
        safe   = label_text("Safe: <36%", color=GREEN).scale(0.65).shift(LEFT*2.5+DOWN*0.5)
        self.play(Create(arc_bg), Create(arc_ok), Create(arc_warn), run_time=1.5)
        self.play(Create(needle), Write(label), Write(safe), run_time=1.5)
        self.wait(0.91)

# ─────── CUT 170  dur=4.76s  render=5.23s ──────────────────────────────────
class Anim170(Scene):
    """$622/mo × 72 months financing"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Monthly Payment:", color=CREAM), label_text("$622",     color=RED )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Term:",            color=CREAM), label_text("72 months", color=RED )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Total Paid:",      color=CREAM), label_text("$44,784",  color=RED )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).center()
        head = label_text("Burke's Truck Financing", color=RED).scale(1.1).next_to(rows, UP, buff=0.5)
        self.play(Write(head), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row), run_time=1.0)
        self.wait(1.23)

# ─────── CUT 172  dur=1.97s  render=2.44s ──────────────────────────────────
class Anim172(Scene):
    """$622/mo invested at market average start"""
    def construct(self):
        _cfg()
        label = label_text("What if $622/mo was invested instead?", color=GOLD).scale(1.1).center()
        self.play(Write(label), run_time=1.2)
        self.wait(0.74)

# ─────── CUT 173  dur=4.08s  render=4.55s ──────────────────────────────────
class Anim173(Scene):
    """Curve bending upward over 15 years, real return 6.69%"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,15,5], y_range=[0,220000,50000],
                  x_length=9, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  x_axis_config={"include_numbers": False},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        def fv(x):
            r = 0.0669/12
            n = x*12
            return 622 * ((1+r)**n - 1) / r if x > 0 else 0
        curve = ax.plot(fv, x_range=[0,15], color=GREEN, stroke_width=3)
        x_lab = label_text("Years", color=GRAY).next_to(ax.x_axis, DOWN)
        y_lab = label_text("Portfolio Value", color=GRAY).next_to(ax.y_axis, LEFT).scale(0.65)
        self.play(Create(ax), Write(x_lab), Write(y_lab), run_time=1.0)
        self.play(Create(curve), run_time=2.3)
        self.wait(0.75)

# ─────── CUT 174  dur=4.84s  render=5.31s ──────────────────────────────────
class Anim174(Scene):
    """Curve lands at ~$192,000 — odometer"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,15,5], y_range=[0,220000,50000],
                  x_length=9, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  x_axis_config={"include_numbers": False},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        def fv(x):
            r = 0.0669/12
            n = x*12
            return 622 * ((1+r)**n - 1) / r if x > 0 else 0
        curve = ax.plot(fv, x_range=[0,15], color=GREEN, stroke_width=3)
        dot   = Dot(ax.c2p(15, fv(15)), color=GOLD, radius=0.12)
        val   = Text("$192,000", font="Helvetica Neue", weight=BOLD, color=GOLD).scale(1.4).next_to(dot, UP+RIGHT)
        self.add(ax, curve)
        self.play(FadeIn(dot), Write(val), run_time=1.5)
        self.wait(3.06)

# ─────── CUT 177  dur=3.08s  render=3.55s ──────────────────────────────────
class Anim177(Scene):
    """$192k truck money vs $189k condo"""
    def construct(self):
        _cfg()
        b1 = Rectangle(width=5.0, height=1.0, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        b2 = Rectangle(width=4.95, height=1.0, fill_color=GOLD,  fill_opacity=0.85, stroke_width=0)
        t1 = label_text("$622/mo Invested → $192,000", color=GREEN).next_to(b1, RIGHT, buff=0.2)
        t2 = label_text("Cedar St Condo: $189,000",    color=GOLD ).next_to(b2, RIGHT, buff=0.2)
        grp = VGroup(VGroup(b1,t1), VGroup(b2,t2)).arrange(DOWN, buff=0.4).center()
        self.play(FadeIn(grp[0]), run_time=0.9)
        self.play(FadeIn(grp[1]), run_time=0.9)
        self.wait(0.95)

# ─────── CUT 181  dur=5.61s  render=6.08s ──────────────────────────────────
class Anim181(Scene):
    """End of Year 5: $66k invested + $20,700 cash"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Invested (Market):", color=CREAM), label_text("$66,000", color=GREEN)).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Cash Reserve:",      color=CREAM), label_text("$20,700", color=GOLD )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Runway:",            color=CREAM), label_text("≈ 9 months", color=GREEN)).arrange(RIGHT, buff=1.0),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).center()
        head = label_text("— End of Year 5 —", color=GOLD).scale(1.1).next_to(rows, UP, buff=0.5)
        self.play(Write(head), run_time=0.6)
        for row in rows:
            self.play(FadeIn(row), run_time=1.2)
        self.wait(1.48)

# ─────── CUT 182  dur=4.04s  render=4.51s ──────────────────────────────────
class Anim182(Scene):
    """Runway bars: Burke 10 days vs You ~9 months"""
    def construct(self):
        _cfg()
        b_you   = Rectangle(width=7.0, height=0.9, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        b_burke = Rectangle(width=0.35, height=0.9, fill_color=RED,   fill_opacity=0.85, stroke_width=0)
        t_y = label_text("Your Runway:   ≈ 9 months", color=GREEN).next_to(b_you,   RIGHT, buff=0.2)
        t_b = label_text("Burke Runway: 10 days",     color=RED  ).next_to(b_burke, RIGHT, buff=0.2)
        grp = VGroup(VGroup(b_you,t_y), VGroup(b_burke,t_b)).arrange(DOWN, aligned_edge=LEFT, buff=0.5).center()
        self.play(FadeIn(grp[0]), run_time=1.1)
        self.play(FadeIn(grp[1]), run_time=1.1)
        self.wait(1.61)

# ─────── CUT 196  dur=3.73s  render=4.20s ──────────────────────────────────
class Anim196(Scene):
    """Purchase split: $58k → loan $46,400 (80%) + your $11,600 (20%)"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Duplex Purchase Price:", color=CREAM), label_text("$58,000", color=CREAM)).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Bank Loan (80%):",       color=CREAM), label_text("$46,400", color=RED  )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Your Cash (20%):",       color=CREAM), label_text("$11,600", color=GREEN)).arrange(RIGHT, buff=1.0),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.5), run_time=2.5)
        self.wait(0.95)

# ─────── CUT 197  dur=1.90s  render=2.37s ──────────────────────────────────
class Anim197(Scene):
    """+ Rehab $22,000 = $33,600 of your cash"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Your Down:",    color=CREAM), label_text("$11,600", color=GREEN)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("+ Rehab:",      color=CREAM), label_text("$22,000", color=GOLD )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("= Your Total:", color=CREAM), label_text("$33,600", color=GOLD )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.4), run_time=1.4)
        self.wait(0.57)

# ─────── CUT 199  dur=3.24s  render=3.71s ──────────────────────────────────
class Anim199(Scene):
    """Cash bar emptying to $0"""
    def construct(self):
        _cfg()
        label = label_text("Your Liquid Cash", color=CREAM).scale(1.1)
        bar   = Rectangle(width=6.5, height=1.0, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        self.add(label.next_to(bar, UP, buff=0.3), bar)
        bar.center()
        label.next_to(bar, UP, buff=0.3)
        empty = Rectangle(width=0.01, height=1.0, fill_color=RED, fill_opacity=0.85, stroke_width=0).align_to(bar, LEFT)
        zero  = label_text("$0", color=RED).scale(2.0).next_to(bar, DOWN, buff=0.5)
        self.play(Create(bar), Write(label), run_time=0.5)
        self.play(Transform(bar, empty), run_time=1.5)
        self.play(Write(zero), run_time=0.5)
        self.wait(0.71)

# ─────── CUT 200  dur=4.64s  render=5.11s ──────────────────────────────────
class Anim200(Scene):
    """Runway gauge to 0 — bone-crack punch"""
    def construct(self):
        _cfg()
        label = Text("0 DAYS", font="Helvetica Neue", weight=BOLD, color=RED).scale(4.5)
        sub   = label_text("6 months — no emergency runway", color=GRAY).scale(0.9)
        sub2  = label_text("The person who built their life around runway has none.", color=CREAM).scale(0.75)
        grp   = VGroup(label, sub, sub2).arrange(DOWN, buff=0.5).center()
        self.play(Write(label),   run_time=1.2)
        self.play(FadeIn(sub),    run_time=0.8)
        self.play(FadeIn(sub2),   run_time=0.8)
        self.wait(2.01)

# ─────── CUT 215  dur=3.09s  render=3.56s ──────────────────────────────────
class Anim215(Scene):
    """BRRRR step: appraisal $105k × 75% = new loan $78,750"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("New Appraisal:",  color=CREAM), label_text("$105,000", color=GOLD  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("× 75% LTV:",      color=CREAM), label_text("",         color=CREAM )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("New Loan:",        color=CREAM), label_text("$78,750",  color=GREEN )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        head = label_text("BRRRR Refinance", color=GOLD).scale(1.1).next_to(rows, UP, buff=0.4)
        self.play(Write(head), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row), run_time=0.65)
        self.wait(0.96)

# ─────── CUT 216  dur=1.85s  render=2.32s ──────────────────────────────────
class Anim216(Scene):
    """New loan $78,750 pays off old loan $46,190"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("New Loan:",     color=CREAM), label_text("$78,750", color=GREEN)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Old Loan Paid:", color=CREAM), label_text("−$46,190", color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Cash Returned:", color=CREAM), label_text("$32,560", color=GOLD )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.4), run_time=1.4)
        self.wait(0.52)

# ─────── CUT 219  dur=4.33s  render=4.80s ──────────────────────────────────
class Anim219(Scene):
    """$33,600 in − $30,160 back = $3,440 still inside"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Cash Invested:",  color=CREAM), label_text("$33,600", color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Cash Returned:",  color=CREAM), label_text("$30,160", color=GREEN)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Still In Deal:",  color=CREAM), label_text("$3,440",  color=GOLD )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        head = label_text("BRRRR Result — Delmar Duplex", color=GOLD).scale(1.1).next_to(rows, UP, buff=0.4)
        self.play(Write(head), run_time=0.6)
        for row in rows:
            self.play(FadeIn(row), run_time=0.9)
        self.wait(1.1)

# ─────── CUT 221  dur=4.36s  render=4.83s ──────────────────────────────────
class Anim221(Scene):
    """Rent $1,200 − mortgage/tax/ins $729 − reserve $120 = $351"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Tenant Rent:",         color=CREAM), label_text("$1,200", color=GREEN)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("− Mortgage/Tax/Ins:",  color=CREAM), label_text("$729",   color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("− Reserve:",           color=CREAM), label_text("$120",   color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("= Net Cash Flow:",     color=CREAM), label_text("$351",   color=GREEN)).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        for row in rows:
            self.play(FadeIn(row), run_time=0.75)
        self.wait(0.83)

# ─────── CUT 225  dur=2.79s  render=3.26s ──────────────────────────────────
class Anim225(Scene):
    """Monthly gap the building doesn't cover: ~$700"""
    def construct(self):
        _cfg()
        label = label_text("Monthly costs building doesn't cover:", color=CREAM).scale(0.9)
        amt   = Text("≈ $700", font="Helvetica Neue", weight=BOLD, color=RED).scale(2.5)
        grp   = VGroup(label, amt).arrange(DOWN, buff=0.5).center()
        self.play(Write(label), run_time=0.8)
        self.play(Write(amt),   run_time=0.8)
        self.wait(0.96)

# ─────── CUT 227  dur=4.92s  render=5.39s ──────────────────────────────────
class Anim227(Scene):
    """$28,000 / $700 = 40 months odometer"""
    def construct(self):
        _cfg()
        eq = VGroup(
            label_text("Remaining Cash Gap to Cover:", color=CREAM),
            label_text("$28,000 ÷ $700/mo",            color=GOLD).scale(1.2),
            Text("= 40 MONTHS", font="Helvetica Neue", weight=BOLD, color=GREEN).scale(1.8),
        ).arrange(DOWN, buff=0.5).center()
        for mob in eq:
            self.play(FadeIn(mob, shift=UP*0.2), run_time=1.0)
        self.wait(1.69)

# ─────── CUT 229  dur=2.46s  render=2.93s ──────────────────────────────────
class Anim229(Scene):
    """Runway bars: Burke 10 days vs You 40 months"""
    def construct(self):
        _cfg()
        b_you   = Rectangle(width=7.5, height=0.9, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        b_burke = Rectangle(width=0.35, height=0.9, fill_color=RED,   fill_opacity=0.85, stroke_width=0)
        t_y = label_text("Your Runway:  40 months", color=GREEN).next_to(b_you,   RIGHT, buff=0.2)
        t_b = label_text("Burke Runway: 10 days",   color=RED  ).next_to(b_burke, RIGHT, buff=0.2)
        grp = VGroup(VGroup(b_you,t_y), VGroup(b_burke,t_b)).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        self.play(FadeIn(grp[0]), run_time=0.8)
        self.play(FadeIn(grp[1]), run_time=0.8)
        self.wait(0.63)

# ─────── CUT 237  dur=4.84s  render=5.31s ──────────────────────────────────
class Anim237(Scene):
    """Account balance line plateaus at $81k — year 6 march"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,8,2], y_range=[0,100000,20000],
                  x_length=9, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  x_axis_config={"include_numbers": False},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        curve = ax.plot(lambda x: min(81000, 12000*x**0.9), x_range=[0,6.5], color=GREEN, stroke_width=3)
        plateau = ax.plot(lambda x: 81000, x_range=[6.5,7.5], color=GOLD, stroke_width=3)
        dot     = Dot(ax.c2p(6.5, 81000), color=GOLD)
        lab     = label_text("$81,000", color=GOLD).next_to(dot, UP)
        self.play(Create(ax), run_time=0.8)
        self.play(Create(curve), run_time=2.5)
        self.play(Create(plateau), FadeIn(dot), Write(lab), run_time=0.8)
        self.wait(0.73)

# ─────── CUT 238  dur=5.28s  render=5.75s ──────────────────────────────────
class Anim238(Scene):
    """Line falls for 7 months"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,9,1], y_range=[50000,90000,10000],
                  x_length=9, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  x_axis_config={"include_numbers": False},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        plateau = ax.plot(lambda x: 81000, x_range=[0,1.5], color=GOLD, stroke_width=3)
        fall    = ax.plot(lambda x: 81000 - (x-1.5)*2571, x_range=[1.5,8.5], color=RED, stroke_width=3)
        dot_end = Dot(ax.c2p(8.5, 63000), color=RED)
        lab     = label_text("$63,000", color=RED).next_to(dot_end, DOWN)
        x_lab   = label_text("Month", color=GRAY).next_to(ax.x_axis, DOWN)
        self.play(Create(ax), Write(x_lab), run_time=0.8)
        self.play(Create(plateau), run_time=0.8)
        self.play(Create(fall), run_time=2.8)
        self.play(FadeIn(dot_end), Write(lab), run_time=0.5)
        self.wait(0.65)

# ─────── CUT 241  dur=5.86s  render=6.33s ──────────────────────────────────
class Anim241(Scene):
    """$81k plunging to $63k — odometer"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("7 months ago:", color=CREAM), label_text("$81,000", color=GOLD)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Today:",        color=CREAM), label_text("$63,000", color=RED )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).center()
        delta = Text("−$18,000", font="Helvetica Neue", weight=BOLD, color=RED).scale(2.0).next_to(rows, DOWN, buff=0.6)
        self.play(FadeIn(rows[0]), run_time=1.0)
        self.play(FadeIn(rows[1]), run_time=1.0)
        self.play(Write(delta),    run_time=1.5)
        self.wait(2.03)

# ─────── CUT 242  dur=2.50s  render=2.97s ──────────────────────────────────
class Anim242(Scene):
    """Red drop −$18,000 punch"""
    def construct(self):
        _cfg()
        label = Text("−$18,000", font="Helvetica Neue", weight=BOLD, color=RED).scale(3.5)
        sub   = label_text("gone in 7 months", color=GRAY)
        grp   = VGroup(label, sub).arrange(DOWN, buff=0.4).center()
        self.play(Write(label), run_time=1.2)
        self.play(FadeIn(sub),  run_time=0.5)
        self.wait(0.77)

# ─────── CUT 251  dur=6.67s  render=7.14s ──────────────────────────────────
class Anim251(Scene):
    """Burke: 401k zeroed + HELOC $85k added"""
    def construct(self):
        _cfg()
        rows_before = VGroup(
            VGroup(label_text("401k Contribution:", color=CREAM), label_text("15%",    color=GREEN)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("HELOC Balance:",     color=CREAM), label_text("$0",     color=CREAM)).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rows_after = VGroup(
            VGroup(label_text("401k Contribution:", color=CREAM), label_text("STOPPED", color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("HELOC Balance:",     color=CREAM), label_text("$85,000", color=RED  )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        head_b = label_text("Burke — Before", color=GRAY).scale(0.9).next_to(rows_before, UP)
        head_a = label_text("Burke — After",  color=RED ).scale(0.9).next_to(rows_after,  UP)
        pair   = VGroup(VGroup(head_b, rows_before), VGroup(head_a, rows_after)).arrange(RIGHT, buff=1.5).center()
        self.play(FadeIn(pair[0]), run_time=1.5)
        self.play(FadeIn(pair[1]), run_time=1.5)
        self.wait(3.44)

# ─────── CUT 256  dur=3.78s  render=4.25s ──────────────────────────────────
class Anim256(Scene):
    """Falling price vs rising share count — DCA"""
    def construct(self):
        _cfg()
        months = list(range(1,8))
        prices = [100, 92, 83, 75, 70, 72, 70]
        shares = [10, 10.9, 12.0, 13.3, 14.3, 13.9, 14.3]
        ax = Axes(x_range=[0,8,1], y_range=[0,120,20],
                  x_length=7, y_length=4,
                  axis_config={"color": GRAY, "stroke_width": 1})
        price_curve = ax.plot_line_graph(months, prices, line_color=RED,  add_vertex_dots=False, stroke_width=3)
        share_curve = ax.plot_line_graph(months, shares, line_color=GREEN, add_vertex_dots=False, stroke_width=3)
        p_lab = label_text("Price (↓)", color=RED,   scale=0.65).to_edge(RIGHT).shift(UP*0.5)
        s_lab = label_text("Shares (↑)", color=GREEN, scale=0.65).to_edge(RIGHT).shift(DOWN*0.5)
        self.play(Create(ax), run_time=0.8)
        self.play(Create(price_curve), Write(p_lab), run_time=1.2)
        self.play(Create(share_curve), Write(s_lab), run_time=1.2)
        self.wait(0.75)

# ─────── CUT 257  dur=3.36s  render=3.83s ──────────────────────────────────
class Anim257(Scene):
    """Fixed $1,000 buys larger blocks as price falls — DCA visual"""
    def construct(self):
        _cfg()
        prices = [100, 85, 70]
        blocks = [10, 11.8, 14.3]
        rows = VGroup()
        for p, s in zip(prices, blocks):
            b = Rectangle(width=s*0.4, height=0.65, fill_color=GREEN, fill_opacity=0.8, stroke_width=0)
            t = label_text(f"$1,000 @ ${p} = {s:.1f} shares", color=CREAM, scale=0.65).next_to(b, RIGHT, buff=0.2)
            rows.add(VGroup(b, t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        head = label_text("Same Dollar — More Shares at Lower Prices", color=GOLD).scale(0.9).next_to(rows, UP, buff=0.4)
        self.play(Write(head), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.4), run_time=1.9)
        self.wait(0.83)

# ─────── CUT 264  dur=5.70s  render=6.17s ──────────────────────────────────
class Anim264(Scene):
    """Garnet BRRRR: $64k+$19k = $83k → refi 75%×$110k = $82,500 out"""
    def construct(self):
        _cfg()
        in_rows = VGroup(
            VGroup(label_text("Buy Price:",   color=CREAM), label_text("$64,000", color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("+ Rehab:",     color=CREAM), label_text("$19,000", color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("= In Deal:",   color=CREAM), label_text("$83,000", color=RED  )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        refi_rows = VGroup(
            VGroup(label_text("New Appraisal:",    color=CREAM), label_text("$110,000", color=GOLD  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("× 75% LTV Refi:",   color=CREAM), label_text("$82,500",  color=GREEN )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Still In Deal:",    color=CREAM), label_text("$500",     color=CREAM )).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        pair = VGroup(in_rows, refi_rows).arrange(RIGHT, buff=1.5).center()
        head = label_text("Garnet Ave — BRRRR #2", color=GOLD).scale(1.1).next_to(pair, UP, buff=0.4)
        self.play(Write(head), run_time=0.5)
        self.play(FadeIn(in_rows),   run_time=2.0)
        self.play(FadeIn(refi_rows), run_time=2.0)
        self.wait(0.87)

# ─────── CUT 287  dur=2.88s  render=3.35s ──────────────────────────────────
class Anim287(Scene):
    """12 apartments × $900/mo = $10,800/mo"""
    def construct(self):
        _cfg()
        eq = VGroup(
            label_text("12 Apartments  ×  $900/mo", color=CREAM).scale(1.2),
            Text("= $10,800/mo", font="Helvetica Neue", weight=BOLD, color=GREEN).scale(1.6),
        ).arrange(DOWN, buff=0.5).center()
        self.play(Write(eq[0]), run_time=1.0)
        self.play(Write(eq[1]), run_time=1.0)
        self.wait(0.65)

# ─────── CUT 288  dur=3.64s  render=4.11s ──────────────────────────────────
class Anim288(Scene):
    """Adding 2 storefronts: $1,900 corner + $1,400 dry cleaner = $14,100 gross"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("12 Apartments:",   color=CREAM), label_text("$10,800/mo", color=GREEN)).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Corner Store:",    color=CREAM), label_text("$1,900/mo",  color=GOLD )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Dry Cleaner:",     color=CREAM), label_text("$1,400/mo",  color=GOLD )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Gross Total:",     color=CREAM), label_text("$14,100/mo", color=GREEN)).arrange(RIGHT, buff=1.0),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        for row in rows:
            self.play(FadeIn(row), run_time=0.65)
        self.wait(0.96)

# ─────── CUT 289  dur=3.54s  render=4.01s ──────────────────────────────────
class Anim289(Scene):
    """Expense waterfall: tax, ins, maintenance, utilities"""
    def construct(self):
        _cfg()
        items = [("Property Tax", 2800), ("Insurance", 1400), ("Maintenance Reserve", 1800), ("Utilities", 1500)]
        bars  = VGroup()
        for label, amt in items:
            w = amt / 1000 * 1.2
            b = Rectangle(width=w, height=0.6, fill_color=RED, fill_opacity=0.8, stroke_width=0)
            t = label_text(f"{label}: ${amt:}/yr", color=RED, scale=0.6).next_to(b, RIGHT, buff=0.15)
            bars.add(VGroup(b, t))
        bars.arrange(DOWN, aligned_edge=LEFT, buff=0.3).center()
        head = label_text("Annual Expenses", color=GRAY).scale(0.9).next_to(bars, UP, buff=0.4)
        self.play(Write(head), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.35), run_time=2.3)
        self.wait(0.81)

# ─────── CUT 290  dur=2.96s  render=3.43s ──────────────────────────────────
class Anim290(Scene):
    """NOI bottom line locks at $90,000/yr"""
    def construct(self):
        _cfg()
        label = label_text("Net Operating Income (NOI):", color=CREAM).scale(1.0)
        amt   = Text("$90,000/yr", font="Helvetica Neue", weight=BOLD, color=GREEN).scale(2.5)
        grp   = VGroup(label, amt).arrange(DOWN, buff=0.5).center()
        self.play(Write(label), run_time=0.8)
        self.play(Write(amt),   run_time=1.2)
        self.wait(0.73)

# ─────── CUT 292  dur=4.50s  render=4.97s ──────────────────────────────────
class Anim292(Scene):
    """Installment sale: spike vs smooth bars"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,22,5], y_range=[0,120000,30000],
                  x_length=9, y_length=4,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  y_axis_config={"decimal_number_config": {"num_decimal_places": 0}})
        # lump sum spike
        spike = ax.get_riemann_rectangles(ax.plot(lambda x: 100000 if 0.5<x<1.5 else 0, x_range=[0,22]),
                                          x_range=[0,22], dx=1, color=RED, fill_opacity=0.8)
        # installment bars (20 years)
        install = ax.get_riemann_rectangles(ax.plot(lambda x: 5000 if 1<x<21 else 0, x_range=[0,22]),
                                            x_range=[0,22], dx=1, color=GREEN, fill_opacity=0.7)
        lab_s = label_text("Lump-Sum Tax: $100k now",    color=RED,   scale=0.7).to_edge(UP).shift(LEFT*2)
        lab_i = label_text("Installment: $5k/yr × 20y", color=GREEN, scale=0.7).to_edge(UP).shift(RIGHT*2)
        self.play(Create(ax), run_time=0.8)
        self.play(Create(spike),   Write(lab_s), run_time=1.3)
        self.play(Create(install), Write(lab_i), run_time=1.3)
        self.wait(0.87)

# ─────── CUT 294  dur=3.33s  render=3.80s ──────────────────────────────────
class Anim294(Scene):
    """Seller finance terms: 6%, $95k down"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Deal Type:",    color=CREAM), label_text("Seller Financing Note", color=GOLD  )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Interest Rate:", color=CREAM), label_text("6.00%",               color=RED   )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Down Payment:", color=CREAM), label_text("$95,000",              color=GREEN )).arrange(RIGHT, buff=1.0),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        head = label_text("Harlan's Terms — Mercer Building", color=GOLD).scale(1.1).next_to(rows, UP, buff=0.4)
        self.play(Write(head), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row), run_time=0.75)
        self.wait(0.8)

# ─────── CUT 295  dur=3.75s  render=4.22s ──────────────────────────────────
class Anim295(Scene):
    """Down payment source 1: brokerage $41k"""
    def construct(self):
        _cfg()
        bar = Rectangle(width=4.1, height=1.0, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        t   = label_text("Secret Brokerage Account: $41,000", color=GREEN).next_to(bar, RIGHT, buff=0.2)
        tot = label_text("Building toward $95,000 Down", color=CREAM).scale(0.85)
        grp = VGroup(VGroup(bar, t), tot).arrange(DOWN, buff=0.6).center()
        self.play(Create(bar), Write(t), run_time=1.5)
        self.play(Write(tot), run_time=0.8)
        self.wait(1.22)

# ─────── CUT 296  dur=6.05s  render=6.52s ──────────────────────────────────
class Anim296(Scene):
    """Down payment stack: $41k + $33k + $21k = $95k"""
    def construct(self):
        _cfg()
        sources = [
            ("Brokerage Account", 41000, GREEN),
            ("Duplex Refinances", 33000, GOLD),
            ("Saved Rents",       21000, "#60a5fa"),
        ]
        bars = VGroup()
        total = 0
        for label, amt, col in sources:
            w = amt / 10000 * 0.9
            b = Rectangle(width=w, height=0.75, fill_color=col, fill_opacity=0.85, stroke_width=0)
            t = label_text(f"{label}: ${amt:}", color=col, scale=0.65).next_to(b, RIGHT, buff=0.15)
            bars.add(VGroup(b, t))
            total += amt
        bars.arrange(DOWN, aligned_edge=LEFT, buff=0.3).center()
        total_lab = Text(f"Total: ${total:}", font="Helvetica Neue", weight=BOLD, color=GOLD).scale(1.4).next_to(bars, DOWN, buff=0.5)
        for b in bars:
            self.play(FadeIn(b), run_time=1.2)
        self.play(Write(total_lab), run_time=1.0)
        self.wait(1.52)

# ─────── CUT 307  dur=4.88s  render=5.35s ──────────────────────────────────
class Anim307(Scene):
    """Monthly note to Harlan: $6,797/mo"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Mercer Building Purchase Price:", color=CREAM), label_text("$1,580,000",  color=CREAM)).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Down Payment:",                   color=CREAM), label_text("$95,000",     color=GREEN)).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Note Balance:",                   color=CREAM), label_text("$1,485,000",  color=RED  )).arrange(RIGHT, buff=1.0),
            VGroup(label_text("Monthly Payment to Harlan:",      color=CREAM), label_text("$6,797/mo",   color=RED  )).arrange(RIGHT, buff=1.0),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        for row in rows:
            self.play(FadeIn(row), run_time=0.9)
        self.wait(0.95)

# ─────── CUT 308  dur=4.01s  render=4.48s ──────────────────────────────────
class Anim308(Scene):
    """Net monthly cash flow: $14,100 − $6,797 − $6,574 = $729"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Gross Rents:",          color=CREAM), label_text("$14,100", color=GREEN)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("− Debt Service:",       color=CREAM), label_text("$6,797",  color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("− Operations:",         color=CREAM), label_text("$6,574",  color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("= Net Monthly CF:",     color=CREAM), label_text("+$729",   color=GREEN)).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        for row in rows:
            self.play(FadeIn(row), run_time=0.7)
        self.wait(0.78)

# ─────── CUT 312  dur=4.28s  render=4.75s ──────────────────────────────────
class Anim312(Scene):
    """$6,797 payment split: interest vs principal wedge"""
    def construct(self):
        _cfg()
        total = 6797
        interest   = 7425 * 0.0669 / 12 * 1485000 / 1000  # approx
        interest   = round(total * 0.84)
        principal  = total - interest
        pie = VGroup(
            Rectangle(width=interest/900,  height=1.2, fill_color=RED,   fill_opacity=0.85, stroke_width=0),
            Rectangle(width=principal/900, height=1.2, fill_color=GREEN, fill_opacity=0.85, stroke_width=0),
        ).arrange(RIGHT, buff=0).center()
        t_int = label_text(f"Interest: ${interest:}", color=RED,   scale=0.75).next_to(pie[0], DOWN, buff=0.15)
        t_pri = label_text(f"Principal: ${principal:}", color=GREEN, scale=0.75).next_to(pie[1], DOWN, buff=0.15)
        head  = label_text("Monthly Payment: $6,797", color=CREAM).scale(1.0).next_to(pie, UP, buff=0.4)
        self.play(Write(head), run_time=0.5)
        self.play(Create(pie), run_time=1.5)
        self.play(Write(t_int), Write(t_pri), run_time=1.0)
        self.wait(1.0)

# ─────── CUT 313  dur=2.85s  render=3.32s ──────────────────────────────────
class Anim313(Scene):
    """Green principal paydown expanding each month"""
    def construct(self):
        _cfg()
        label = label_text("Every month, part of the $6,797 payment\npays down your loan balance.", color=CREAM).scale(0.85)
        bar   = Rectangle(width=0.5, height=1.0, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        bar_full = Rectangle(width=4.5, height=1.0, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        lab_b = label_text("Principal Paydown (growing each month →)", color=GREEN, scale=0.65).next_to(bar_full, DOWN)
        grp   = VGroup(label, bar, lab_b).arrange(DOWN, buff=0.4).center()
        self.play(Write(label), run_time=0.8)
        bar.center().shift(DOWN*0.5)
        lab_b.next_to(bar, DOWN)
        self.play(Create(bar), run_time=0.5)
        self.play(Transform(bar, bar_full.center().shift(DOWN*0.5)), run_time=1.2)
        self.wait(0.52)

# ─────── CUT 314  dur=4.62s  render=5.09s ──────────────────────────────────
class Anim314(Scene):
    """12-month cumulative paydown counter → $18,779"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,13,1], y_range=[0,22000,5000],
                  x_length=9, y_length=4.5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  x_axis_config={"include_numbers": False},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        def paydown(x):
            return 18779 * (x / 12) if x <= 12 else 18779
        curve = ax.plot(paydown, x_range=[0,12], color=GREEN, stroke_width=3)
        dot   = Dot(ax.c2p(12, 18779), color=GOLD)
        lab   = label_text("$18,779 Paydown (Yr 1)", color=GOLD).next_to(dot, RIGHT)
        x_lab = label_text("Month", color=GRAY).next_to(ax.x_axis, DOWN)
        self.play(Create(ax), Write(x_lab), run_time=0.9)
        self.play(Create(curve), run_time=2.3)
        self.play(FadeIn(dot), Write(lab), run_time=0.7)
        self.wait(0.69)

# ─────── CUT 318  dur=5.20s  render=5.67s ──────────────────────────────────
class Anim318(Scene):
    """Engine 1: W-2 Take-Home $39,600"""
    def construct(self):
        _cfg()
        label = label_text("Engine 1 — W-2 Job (Kessler)", color=GRAY).scale(0.9)
        amt   = Text("$39,600", font="Helvetica Neue", weight=BOLD, color=CREAM).scale(2.8)
        sub   = label_text("annual take-home after tax", color=GRAY).scale(0.8)
        grp   = VGroup(label, amt, sub).arrange(DOWN, buff=0.4).center()
        self.play(Write(label), run_time=0.7)
        self.play(Write(amt),   run_time=1.5)
        self.play(FadeIn(sub),  run_time=0.7)
        self.wait(2.0)

# ─────── CUT 320  dur=3.03s  render=3.50s ──────────────────────────────────
class Anim320(Scene):
    """Engine 2 builds: component 1 market growth +$7,700"""
    def construct(self):
        _cfg()
        label = label_text("Engine 2 — The Asset Stack", color=GOLD).scale(1.0)
        bar1  = Rectangle(width=1.5, height=0.75, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        t1    = label_text("Market Growth:  +$7,700", color=GREEN, scale=0.75).next_to(bar1, RIGHT, buff=0.2)
        grp   = VGroup(label, VGroup(bar1, t1)).arrange(DOWN, aligned_edge=LEFT, buff=0.5).center()
        self.play(Write(label), run_time=0.6)
        self.play(Create(bar1), Write(t1), run_time=1.4)
        self.wait(0.7)

# ─────── CUT 321  dur=4.55s  render=5.02s ──────────────────────────────────
class Anim321(Scene):
    """Engine 2 adds: loan paydown +$18,779"""
    def construct(self):
        _cfg()
        bar1 = Rectangle(width=1.5, height=0.75, fill_color=GREEN, fill_opacity=0.85, stroke_width=0)
        t1   = label_text("Market Growth:  +$7,700",        color=GREEN, scale=0.65).next_to(bar1, RIGHT, buff=0.2)
        bar2 = Rectangle(width=3.75, height=0.75, fill_color=GOLD, fill_opacity=0.85, stroke_width=0)
        t2   = label_text("Mercer Loan Paydown: +$18,779",  color=GOLD,  scale=0.65).next_to(bar2, RIGHT, buff=0.2)
        grp  = VGroup(VGroup(bar1, t1), VGroup(bar2, t2)).arrange(DOWN, aligned_edge=LEFT, buff=0.35).center()
        self.play(FadeIn(grp[0]), run_time=0.8)
        self.play(FadeIn(grp[1]), run_time=1.5)
        self.wait(2.02)

# ─────── CUT 322  dur=2.40s  render=2.87s ──────────────────────────────────
class Anim322(Scene):
    """Engine 2 adds: Mercer cash flow +$8,700"""
    def construct(self):
        _cfg()
        bar = Rectangle(width=1.74, height=0.75, fill_color="#60a5fa", fill_opacity=0.85, stroke_width=0)
        t   = label_text("Mercer Cash Flow:  +$8,700", color="#60a5fa", scale=0.75).next_to(bar, RIGHT, buff=0.2)
        grp = VGroup(bar, t).center()
        self.play(Create(bar), Write(t), run_time=1.4)
        self.wait(0.67)

# ─────── CUT 323  dur=3.48s  render=3.95s ──────────────────────────────────
class Anim323(Scene):
    """Engine 2 adds: duplex net flow +$8,000"""
    def construct(self):
        _cfg()
        bar = Rectangle(width=1.6, height=0.75, fill_color="#a78bfa", fill_opacity=0.85, stroke_width=0)
        t   = label_text("Delmar & Garnet Duplex Flow:  +$8,000", color="#a78bfa", scale=0.75).next_to(bar, RIGHT, buff=0.2)
        grp = VGroup(bar, t).center()
        self.play(Create(bar), Write(t), run_time=1.4)
        self.wait(1.75)

# ─────── CUT 324  dur=2.14s  render=2.61s ──────────────────────────────────
class Anim324(Scene):
    """Engine 2 total slams: $43,179"""
    def construct(self):
        _cfg()
        label = label_text("Engine 2 Total:", color=GOLD)
        amt   = Text("$43,179", font="Helvetica Neue", weight=BOLD, color=GOLD).scale(3.0)
        grp   = VGroup(label, amt).arrange(DOWN, buff=0.4).center()
        self.play(Write(label), run_time=0.4)
        self.play(Write(amt),   run_time=0.9)
        self.wait(0.61)

# ─────── CUT 325  dur=5.02s  render=5.49s ──────────────────────────────────
class Anim325(Scene):
    """Crossover chart: Engine 2 $43,179 surpasses Engine 1 $39,600 (+$3,579)"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,3,1], y_range=[0,50000,10000],
                  x_length=5, y_length=5,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        b1 = ax.get_riemann_rectangles(ax.plot(lambda x: 39600, x_range=[0.2,1.1]),
                                       x_range=[0.2,1.1], dx=0.9, color=GRAY, fill_opacity=0.7)
        b2 = ax.get_riemann_rectangles(ax.plot(lambda x: 43179, x_range=[1.5,2.4]),
                                       x_range=[1.5,2.4], dx=0.9, color=GOLD, fill_opacity=0.85)
        t1 = label_text("Engine 1\n$39,600", color=GRAY, scale=0.6).next_to(b1, UP, buff=0.1)
        t2 = label_text("Engine 2\n$43,179", color=GOLD, scale=0.6).next_to(b2, UP, buff=0.1)
        delta = label_text("+$3,579", color=GREEN).scale(1.3).next_to(b2, RIGHT)
        self.play(Create(ax), run_time=0.8)
        self.play(Create(b1), Write(t1), run_time=1.0)
        self.play(Create(b2), Write(t2), run_time=1.0)
        self.play(Write(delta), run_time=0.7)
        self.wait(1.19)

# ─────── CUT 330  dur=2.96s  render=3.43s ──────────────────────────────────
class Anim330(Scene):
    """Depreciation shielding: non-cash write-off vs taxable income"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Net Cash Flow:",         color=CREAM), label_text("$8,748",   color=GREEN)).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Depreciation Deduction:", color=CREAM), label_text("−$57,455", color=GOLD )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Taxable Income:",        color=CREAM), label_text("$0",       color=GREEN)).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center()
        head = label_text("Real Estate Depreciation Shield", color=GOLD).scale(1.0).next_to(rows, UP, buff=0.4)
        self.play(Write(head), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row), run_time=0.65)
        self.wait(0.78)

# ─────── CUT 351  dur=3.50s  render=3.97s ──────────────────────────────────
class Anim351(Scene):
    """Beach trip $650 split vs Mercer monthly CF $729"""
    def construct(self):
        _cfg()
        rows = VGroup(
            VGroup(label_text("Beach Trip (your share):", color=CREAM), label_text("$650",  color=RED  )).arrange(RIGHT, buff=1.2),
            VGroup(label_text("Mercer Monthly Cash Flow:", color=CREAM), label_text("+$729", color=GREEN)).arrange(RIGHT, buff=1.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).center()
        sub = label_text("Building paid for the trip — with $79 to spare.", color=GOLD).scale(0.85).next_to(rows, DOWN, buff=0.5)
        self.play(FadeIn(rows[0]), run_time=1.0)
        self.play(FadeIn(rows[1]), run_time=1.0)
        self.play(Write(sub),      run_time=0.9)
        self.wait(0.77)

# ─────── CUT 372  dur=2.86s  render=3.33s ──────────────────────────────────
class Anim372(Scene):
    """Burke salary drop: $128k → $84k"""
    def construct(self):
        _cfg()
        ax = Axes(x_range=[0,3,1], y_range=[0,160000,40000],
                  x_length=4, y_length=4,
                  axis_config={"color": GRAY, "stroke_width": 1},
                  y_axis_config={"include_numbers": False,
                                 "decimal_number_config": {"num_decimal_places": 0}})
        b1 = ax.get_riemann_rectangles(ax.plot(lambda x: 128000, x_range=[0.2,1.1]),
                                       x_range=[0.2,1.1], dx=0.9, color=GRAY, fill_opacity=0.7)
        b2 = ax.get_riemann_rectangles(ax.plot(lambda x: 84000,  x_range=[1.5,2.4]),
                                       x_range=[1.5,2.4], dx=0.9, color=RED, fill_opacity=0.85)
        t1 = label_text("Before\n$128k", color=GRAY, scale=0.6).next_to(b1, UP, buff=0.1)
        t2 = label_text("After\n$84k",   color=RED,  scale=0.6).next_to(b2, UP, buff=0.1)
        self.play(Create(ax), run_time=0.5)
        self.play(Create(b1), Write(t1), run_time=0.8)
        self.play(Create(b2), Write(t2), run_time=0.8)
        self.wait(0.73)

# ─────── CUT 412  dur=5.64s  render=6.11s ──────────────────────────────────
class Anim412(Scene):
    """Burke's full debt waterfall: truck, boat, HELOC, 401k loans"""
    def construct(self):
        _cfg()
        debts = [
            ("Silverado Lease",  "$48,000",  RED),
            ("Boat Loan",        "$32,000",  "#f97316"),
            ("HELOC",            "$85,000",  "#a78bfa"),
            ("401(k) Loans",     "$38,000",  GOLD),
        ]
        rows = VGroup()
        for label, amt, col in debts:
            row = VGroup(
                label_text(label, color=col,  scale=0.75),
                label_text(amt,   color=col,  scale=0.75),
            ).arrange(RIGHT, buff=1.5)
            rows.add(row)
        total = label_text("Total Liabilities: $203,000", color=RED).scale(1.1)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        total.next_to(rows, DOWN, buff=0.5)
        VGroup(rows, total).center()
        head = label_text("Burke's Debt Ledger", color=RED).scale(1.1).next_to(rows, UP, buff=0.4)
        self.play(Write(head), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(r) for r in rows], lag_ratio=0.4), run_time=3.0)
        self.play(Write(total), run_time=0.9)
        self.wait(0.91)
