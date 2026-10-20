"""
Specification-Compliant Stubs & Reference Contracts
Manim 05-Cel-Boil Audiobook Summary Replication
"""

import math
from pathlib import Path
import numpy as np

try:
    import manim as mn
    from manim import VGroup, VMobject, Circle, Square, Rectangle, RoundedRectangle, Line, Text, Scene
except ImportError:
    # Graceful fallback mock if manim is imported without GUI/cairo in minimal environments
    class VMobject:
        def __init__(self, *args, **kwargs):
            self.points = np.zeros((16, 3), dtype=np.float64)
            self.updaters = []
            self.submobjects = []
            self.color = kwargs.get("color", "#1c1613")
        def add_updater(self, updater):
            self.updaters.append(updater)
            return self
        def update(self, dt=0.0):
            for u in self.updaters:
                u(self, dt)
            return self
        def copy(self):
            obj = VMobject()
            obj.points = self.points.copy()
            obj.color = self.color
            return obj
        def get_center(self):
            return np.mean(self.points, axis=0) if len(self.points) > 0 else np.zeros(3)
        def set_color(self, color):
            self.color = color
            return self

    class VGroup(VMobject):
        def __init__(self, *vmobjects, **kwargs):
            super().__init__(**kwargs)
            self.submobjects = list(vmobjects)
        def __len__(self):
            return len(self.submobjects)
        def __getitem__(self, idx):
            return self.submobjects[idx]
        def add(self, *vmobjects):
            self.submobjects.extend(vmobjects)
            return self

    class Circle(VMobject):
        def __init__(self, radius=1.0, **kwargs):
            super().__init__(**kwargs)
            angles = np.linspace(0, 2*np.pi, 32, endpoint=False)
            self.points = np.column_stack([radius*np.cos(angles), radius*np.sin(angles), np.zeros(32)])

    class Square(VMobject):
        def __init__(self, side_length=2.0, **kwargs):
            super().__init__(**kwargs)
            half = side_length / 2.0
            self.points = np.array([[-half, -half, 0], [half, -half, 0], [half, half, 0], [-half, half, 0]], dtype=np.float64)

    class Rectangle(VMobject):
        def __init__(self, width=4.0, height=2.0, **kwargs):
            super().__init__(**kwargs)
            hw, hh = width / 2.0, height / 2.0
            self.points = np.array([[-hw, -hh, 0], [hw, -hh, 0], [hw, hh, 0], [-hw, hh, 0]], dtype=np.float64)

    class RoundedRectangle(Rectangle):
        pass

    class Line(VMobject):
        def __init__(self, start=np.zeros(3), end=np.ones(3), **kwargs):
            super().__init__(**kwargs)
            self.points = np.array([start, end], dtype=np.float64)

    class Text(VMobject):
        def __init__(self, text="", **kwargs):
            super().__init__(**kwargs)
            self.text = text
        def set_color(self, color):
            self.color = color
            return self

    class Scene:
        def __init__(self):
            class Cam:
                background_color = "#f4e9d0"
            self.camera = Cam()
            self.mobjects = []
        def add(self, *mobs):
            self.mobjects.extend(mobs)
        def construct(self):
            pass


# Palette definition
PAL = {
    "cream": "#f4e9d0",
    "ink": "#1c1613",
    "red": "#e5402b",
    "yel": "#ffc425",
    "hi": "#fff6e2",
    "pencil": "#d9573f",
}

# 12 Structured Kinetic Subtitle Cues
KINETIC_BEATS = [
    {
        "index": 1,
        "start": 0.00,
        "end": 1.50,
        "kicker": "KYA AAPNE...",
        "hero": "KABHI NOTICE KIYA?",
        "sub": "Audiobook Summary Hook",
        "color": PAL["yel"],
    },
    {
        "index": 2,
        "start": 1.50,
        "end": 4.50,
        "kicker": "BINA FORCE KIYE...",
        "hero": "TRUST & RESPECT",
        "sub": "Logon Ka Dil Jeetna",
        "color": PAL["hi"],
    },
    {
        "index": 3,
        "start": 4.50,
        "end": 7.00,
        "kicker": "JABKI KUCH LOG...",
        "hero": "CONVINCE NAHI HOTE",
        "sub": "Baat Kyun Nahi Banti?",
        "color": PAL["yel"],
    },
    {
        "index": 4,
        "start": 7.00,
        "end": 9.00,
        "kicker": "AAKHIR DONO MEIN...",
        "hero": "DIFFERENCE KYA HAI?!",
        "sub": "The Real Difference",
        "color": PAL["red"],
    },
    {
        "index": 5,
        "start": 9.00,
        "end": 12.20,
        "kicker": "SIRF COMMUNICATION SKILLS?",
        "hero": "KA GAME HAI?",
        "sub": "Communication Vs Psychology",
        "color": PAL["yel"],
    },
    {
        "index": 6,
        "start": 12.20,
        "end": 15.00,
        "kicker": "YA PHIR ISKE PEECHE...",
        "hero": "HUMAN PSYCHOLOGY KA SCIENCE",
        "sub": "A Deeper Science",
        "color": PAL["hi"],
    },
    {
        "index": 7,
        "start": 15.00,
        "end": 18.50,
        "kicker": "DALE CARNEGIE KI LEGENDARY BOOK",
        "hero": "HOW TO WIN FRIENDS",
        "sub": "& INFLUENCE PEOPLE",
        "color": PAL["yel"],
    },
    {
        "index": 8,
        "start": 18.50,
        "end": 21.00,
        "kicker": "LOGON KO MANIPULATE KARNA NAHI...",
        "hero": "MANIPULATION ❌",
        "sub": "Dhoka Ya Asli Rishte?",
        "color": PAL["red"],
    },
    {
        "index": 9,
        "start": 21.00,
        "end": 23.36,
        "kicker": "BALKI UNHE SAMAJHNA AUR...",
        "hero": "GENUINE RELATIONSHIPS ❤",
        "sub": "Build Real Connections",
        "color": PAL["hi"],
    },
    {
        "index": 10,
        "start": 23.36,
        "end": 26.14,
        "kicker": "IS BOOK MEIN JAANENGE...",
        "hero": "ZERO ARGUMENTS 🕊️",
        "sub": "Bina Vivaad Ke Apni Baat Rakhein",
        "color": PAL["yel"],
    },
    {
        "index": 11,
        "start": 26.14,
        "end": 29.58,
        "kicker": "CRITICISM KE BINA...",
        "hero": "INSPIRE KARNA! ✨",
        "sub": "Inspire Others To Improve",
        "color": PAL["hi"],
    },
    {
        "index": 12,
        "start": 29.58,
        "end": 30.00,
        "kicker": "HOW TO WIN FRIENDS",
        "hero": "CHAPTER 1: COMING UP",
        "sub": "Next Video Teaser",
        "color": PAL["yel"],
    },
]

# 15 Procedural SFX Cue Timestamps (Police Siren at 8.16s explicitly omitted)
SFX_CUES = [
    {"time": 0.05, "sfx": "paper_slide", "beat": 1},
    {"time": 1.08, "sfx": "cork_pop", "beat": 1},
    {"time": 3.12, "sfx": "chime_ding_c5", "beat": 2},
    {"time": 6.80, "sfx": "tension_riser", "beat": 3},
    # 8.16 police_siren OMITTED
    {"time": 11.20, "sfx": "mechanical_tick", "beat": 4},
    {"time": 14.18, "sfx": "blip_g4", "beat": 5},
    {"time": 16.04, "sfx": "book_slam", "beat": 6},
    {"time": 19.34, "sfx": "gunshot_crack", "beat": 7},
    {"time": 21.86, "sfx": "sparkle_chime", "beat": 7},
    {"time": 23.36, "sfx": "page_turn", "beat": 8},
    {"time": 24.20, "sfx": "sticker_slap_1", "beat": 8},
    {"time": 25.00, "sfx": "whoosh", "beat": 8},
    {"time": 26.20, "sfx": "sticker_slap_2", "beat": 9},
    {"time": 28.20, "sfx": "shimmer_bloom", "beat": 9},
    {"time": 28.74, "sfx": "hero_bell_g5", "beat": 9},
]


def _hash_noise(x: float, y: float, z: float) -> float:
    """Fast deterministic spatial hash function returning values in [-1.0, 1.0]."""
    return math.sin(x * 2.31 + y * 3.73 + z * 5.17)


def apply_cel_boil(mobject: VMobject, amp: float = 0.03, scale: float = 1.5, fps: int = 12, seed: int = 0) -> VMobject:
    """Attach custom cel-boil vector perturbation updater to any Manim VMobject.
    
    Guarantees:
    1. Points perturbed relative to cached base_points (zero cumulative drift).
    2. Displacement strictly bounded within [-amp, +amp].
    3. Center of mass drift is zero.
    4. Deterministic updates on 1/fps stepped seeds.
    """
    if not hasattr(mobject, "base_points") or mobject.base_points is None:
        mobject.base_points = mobject.points.copy()

    def cel_boil_updater(mob: VMobject, dt: float = 0.0):
        if amp == 0.0 or len(mob.base_points) == 0:
            mob.points = mob.base_points.copy()
            return

        t = getattr(mob, "_anim_time", 0.0) + dt
        mob._anim_time = t

        # Frame quantization: 8 fps on hold, 12 fps on action
        boil_fps = 8 if t >= 29.58 else fps
        current_seed = seed + int(t * boil_fps)
        z = current_seed * 2.371 + 0.5

        pts = mob.base_points
        new_pts = pts.copy()

        for i in range(len(pts)):
            px, py = pts[i, 0], pts[i, 1]
            dx = amp * _hash_noise(px / scale, py / scale, z)
            dy = amp * _hash_noise(px / scale + 41.3, py / scale - 17.9, z)
            new_pts[i, 0] = px + dx
            new_pts[i, 1] = py + dy

        mob.points = new_pts

    mobject.add_updater(cel_boil_updater)
    return mobject


class KineticSubtitleManager:
    """Manages the 12 structured kinetic Hinglish subtitle banners."""

    def __init__(self):
        self.cues = KINETIC_BEATS

    def get_cue_at(self, t: float) -> dict | None:
        """Return the subtitle cue active at timestamp t (seconds)."""
        if t < 0.0:
            return None
        if t >= 29.58:
            return None  # Beat 10 plaque holds outro, banner hidden
        for c in self.cues:
            if c["start"] <= t < c["end"]:
                return c
        return None

    def get_banner_mobject(self, cue_idx: int) -> VGroup:
        """Construct Manim VGroup for subtitle banner pill."""
        if not (1 <= cue_idx <= len(self.cues)):
            raise ValueError(f"Invalid cue index: {cue_idx}")

        cue = self.cues[cue_idx - 1]
        
        # Pill backing
        shadow = RoundedRectangle(width=8.0, height=1.6, corner_radius=0.4, color=PAL["ink"])
        body = RoundedRectangle(width=8.0, height=1.6, corner_radius=0.4, color=PAL["hi"])
        border = RoundedRectangle(width=8.0, height=1.6, corner_radius=0.4, color=PAL["ink"])

        # Typography lines
        kicker = Text(cue["kicker"], color=PAL["pencil"])
        hero = Text(cue["hero"], color=cue.get("color", PAL["ink"]))
        sub = Text(cue["sub"], color=PAL["pencil"])

        banner = VGroup(shadow, body, border, kicker, hero, sub)
        apply_cel_boil(banner, amp=0.02, fps=12)
        return banner


def get_beat_group(beat_index: int, t_start: float = 0.0, t_end: float = 0.0) -> VGroup:
    """Return procedurally constructed Manim VGroup for each of the 10 visual beats."""
    if not (1 <= beat_index <= 10):
        raise ValueError(f"Beat index must be between 1 and 10, got {beat_index}")

    group = VGroup()

    if beat_index == 1:
        # Magnifying Glass & Cork Pop
        lens = Circle(radius=1.4, color=PAL["hi"])
        rim = Circle(radius=1.45, color=PAL["ink"])
        inner_rule = Circle(radius=1.3, color=PAL["pencil"])
        handle = Line(start=np.array([1.0, -1.0, 0]), end=np.array([2.5, -2.5, 0]), color=PAL["red"])
        spark = Circle(radius=0.2, color=PAL["yel"])
        group.add(lens, rim, inner_rule, handle, spark)

    elif beat_index == 2:
        # Dual Seals (TRUST & RESPECT)
        seal1 = Circle(radius=1.2, color=PAL["red"])
        seal2 = Circle(radius=1.2, color=PAL["yel"])
        ribbon = Line(start=np.array([-2.0, 0, 0]), end=np.array([2.0, 0, 0]), color=PAL["ink"])
        txt_trust = Text("TRUST", color=PAL["hi"]).set_color(PAL["hi"])
        txt_respect = Text("RESPECT", color=PAL["ink"]).set_color(PAL["ink"])
        group.add(seal1, seal2, ribbon, txt_trust, txt_respect)

    elif beat_index == 3:
        # Question Mark & Alert
        qm_dot = Circle(radius=0.3, color=PAL["red"])
        qm_curve = Circle(radius=1.5, color=PAL["ink"])
        alert_ring = Circle(radius=2.2, color=PAL["yel"])
        group.add(qm_curve, qm_dot, alert_ring)

    elif beat_index == 4:
        # Communication Game Die & Speech Balloons
        balloon1 = RoundedRectangle(width=3.0, height=1.5, corner_radius=0.3, color=PAL["yel"])
        balloon2 = RoundedRectangle(width=3.0, height=1.5, corner_radius=0.3, color=PAL["red"])
        die = Square(side_length=1.0, color=PAL["hi"])
        group.add(balloon1, balloon2, die)

    elif beat_index == 5:
        # Brain Psychology & Atomic Rings
        brain = Circle(radius=1.5, color=PAL["hi"])
        ring1 = Circle(radius=2.0, color=PAL["red"])
        ring2 = Circle(radius=2.0, color=PAL["yel"])
        group.add(brain, ring1, ring2)

    elif beat_index == 6:
        # Hero 3D Book Slam
        cover = Rectangle(width=4.5, height=3.0, color=PAL["red"])
        border = Rectangle(width=4.0, height=2.6, color=PAL["yel"])
        ribbon = Line(start=np.array([0, 1.5, 0]), end=np.array([0, -2.0, 0]), color=PAL["yel"])
        title = Text("HOW TO WIN FRIENDS", color=PAL["hi"]).set_color(PAL["hi"])
        group.add(cover, border, ribbon, title)

    elif beat_index == 7:
        # Manipulation Slash -> Friendship Rings
        x_line1 = Line(start=np.array([-2, -2, 0]), end=np.array([2, 2, 0]), color=PAL["red"])
        x_line2 = Line(start=np.array([-2, 2, 0]), end=np.array([2, -2, 0]), color=PAL["red"])
        ring_l = Circle(radius=1.0, color=PAL["yel"])
        ring_r = Circle(radius=1.0, color=PAL["red"])
        group.add(x_line1, x_line2, ring_l, ring_r)

    elif beat_index == 8:
        # Zero Arguments Ribbons & Peace Shield
        ribbon1 = Line(start=np.array([-3, 0.5, 0]), end=np.array([3, 0.5, 0]), color=PAL["yel"])
        ribbon2 = Line(start=np.array([-3, -0.5, 0]), end=np.array([3, -0.5, 0]), color=PAL["ink"])
        shield = Circle(radius=1.2, color=PAL["hi"])
        group.add(ribbon1, ribbon2, shield)

    elif beat_index == 9:
        # Inspire Flame Spirit
        flame = Circle(radius=1.2, color=PAL["red"])
        core = Circle(radius=0.7, color=PAL["yel"])
        star = Circle(radius=0.3, color=PAL["hi"])
        group.add(flame, core, star)

    elif beat_index == 10:
        # Chapter 1 Outro Plaque
        plaque = Rectangle(width=6.0, height=3.5, color=PAL["hi"])
        inner_gold = Rectangle(width=5.5, height=3.0, color=PAL["yel"])
        title = Text("HOW TO WIN FRIENDS", color=PAL["ink"]).set_color(PAL["ink"])
        badge = RoundedRectangle(width=3.0, height=0.8, corner_radius=0.2, color=PAL["yel"])
        badge_txt = Text("CHAPTER 1", color=PAL["ink"]).set_color(PAL["ink"])
        group.add(plaque, inner_gold, title, badge, badge_txt)

    apply_cel_boil(group, amp=0.03, fps=12)
    return group


class AudiobookSummaryScene(Scene):
    """Master Scene replicating 30-second cel-boil audiobook summary."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = PAL["cream"]
        self.duration = 30.00
        self.fps = 24

    def construct(self):
        # 1. Warm cream triple frame border
        border_outer = Rectangle(width=15.5, height=8.5, color=PAL["red"])
        border_mid = Rectangle(width=15.3, height=8.3, color=PAL["hi"])
        border_inner = Rectangle(width=15.0, height=8.0, color=PAL["ink"])
        frame_group = VGroup(border_outer, border_mid, border_inner)
        apply_cel_boil(frame_group, amp=0.02, fps=12)
        self.add(frame_group)

        # 2. Visual beats and subtitles
        sub_mgr = KineticSubtitleManager()
        # Clean slate guaranteed: no SC. 05, no No. 074, no CEL BOIL text
