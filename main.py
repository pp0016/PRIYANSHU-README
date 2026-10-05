from manim import *
import numpy as np

# =============================================================================
# VARIATION 1: Kinetic Typography + Minimalist Icons
# =============================================================================
class KineticTypographyHookScene(Scene):
    def construct(self):
        self.camera.background_color = "#121212"

        # Beat 01.1: Hook Question & Eye Aperture (0:00 - 0:02)
        eye_pupil = Dot(color="#00D4FF", radius=0.15)
        eye_upper = Arc(radius=0.9, start_angle=0.2, angle=2.74, color="#F8F9FA", stroke_width=3.5)
        eye_lower = Arc(radius=0.9, start_angle=3.34, angle=2.74, color="#F8F9FA", stroke_width=3.5)
        eye_icon = VGroup(eye_upper, eye_lower, eye_pupil).move_to(DOWN * 0.4)
        text_01 = Text("KABHI NOTICE KIYA?", font_size=46, weight=BOLD, color="#F8F9FA").move_to(UP * 1.3)

        self.play(FadeIn(eye_icon, scale=0.6), FadeIn(text_01, shift=UP * 0.3), run_time=0.6)
        self.play(Indicate(text_01, scale_factor=1.12, color="#FFB800"), Flash(eye_pupil, color="#00D4FF", num_lines=8, line_length=0.25), run_time=0.6)
        self.wait(0.8)

        # Beat 01.2: Minimalist Horseshoe Magnet & Inward Nodes (0:02 - 0:04)
        magnet_arc = Arc(radius=0.55, start_angle=PI, angle=PI, color="#FF2A6D", stroke_width=7)
        pole_left = Line(start=[-0.55, 0, 0], end=[-0.55, 0.65, 0], color="#00D4FF", stroke_width=7)
        pole_right = Line(start=[0.55, 0, 0], end=[0.55, 0.65, 0], color="#FF2A6D", stroke_width=7)
        magnet_icon = VGroup(magnet_arc, pole_left, pole_right).move_to(DOWN * 0.4)

        text_02 = Text("EFFORTLESS TRUST & RESPECT", font_size=40, weight=BOLD, t2c={"TRUST": "#FFB800", "RESPECT": "#00D4FF"}).move_to(UP * 1.3)

        nodes = VGroup(*[
            Dot(point=[np.cos(a) * 2.8, np.sin(a) * 2.8 + magnet_icon.get_center()[1], 0], color="#FFB800", radius=0.07)
            for a in np.linspace(0, TAU, 10, endpoint=False)
        ])

        self.play(ReplacementTransform(eye_icon, magnet_icon), ReplacementTransform(text_01, text_02), LaggedStart(*[FadeIn(d, scale=0.5) for d in nodes], lag_ratio=0.05), run_time=0.9)
        self.play(LaggedStart(*[d.animate.move_to(magnet_icon.get_center()) for d in nodes], lag_ratio=0.05), run_time=0.8)
        self.wait(0.3)

        # Beat 01.3: Split-Screen Comparison & Sharp Friction (0:04 - 0:06)
        divider = Line(start=[0, 3.5, 0], end=[0, -3.5, 0], color="#64748B", stroke_width=2.5)
        text_03 = Text("DOOSRE: STRUGGLE & REJECTED!", font_size=36, weight=BOLD, color="#FF2A6D").move_to(RIGHT * 3.2 + UP * 0.6)
        warning_box = SurroundingRectangle(text_03, color="#FF2A6D", buff=0.25, corner_radius=0.1)

        self.play(
            FadeOut(nodes),
            magnet_icon.animate.shift(LEFT * 3.0),
            text_02.animate.shift(LEFT * 3.0).scale(0.8),
            Create(divider),
            FadeIn(text_03, shift=LEFT * 0.4),
            run_time=0.7
        )
        self.play(Create(warning_box), Wiggle(text_03, scale_value=1.1, rotation_angle=0.03 * TAU), run_time=0.7)
        self.wait(0.6)


# =============================================================================
# VARIATION 2: Geometric Scenes (Abstract Vector Metaphors & Tactical Standoff)
# =============================================================================
class PoliceStandoffGeometricScene(Scene):
    def construct(self):
        self.camera.background_color = "#050814"

        b_width = 3.2
        b_height = 4.6
        b_center = ORIGIN

        building_frame = Rectangle(height=b_height, width=b_width, color="#64748B", stroke_width=2.5).move_to(b_center)
        floor_lines = VGroup(*[
            Line(start=[-b_width / 2, -b_height / 2 + (i + 1) * (b_height / 5), 0],
                 end=[b_width / 2, -b_height / 2 + (i + 1) * (b_height / 5), 0],
                 color="#64748B", stroke_width=1.5)
            for i in range(4)
        ])
        building = VGroup(building_frame, floor_lines)

        top_floor_y = b_height / 2 - (b_height / 10)
        top_floor_box = Rectangle(
            height=b_height / 5, width=b_width,
            fill_color="#FF2A6D", fill_opacity=0.25,
            stroke_color="#FF2A6D", stroke_width=2
        ).move_to([0, top_floor_y, 0])

        crowley_dot = Dot(point=[0, top_floor_y, 0], radius=0.15, color="#FF2A6D")
        crowley_shield = Annulus(inner_radius=0.25, outer_radius=0.28, color="#FF2A6D", fill_opacity=0.4).move_to(crowley_dot.get_center())
        crowley_group = VGroup(crowley_dot, crowley_shield)

        title_text = Text("MAY 1931: 150 NYPD vs TWO-GUN CROWLEY", font_size=32, weight=BOLD, color="#F8F9FA").to_edge(UP, buff=0.4)

        self.play(Create(building), FadeIn(top_floor_box), FadeIn(crowley_group, scale=0.5), Write(title_text), run_time=1.2)

        cordon_radii = [2.2, 2.9, 3.6, 4.3]
        dots_per_ring = [25, 35, 42, 48]
        police_dots = VGroup()
        for r, count in zip(cordon_radii, dots_per_ring):
            for i in range(count):
                angle = (i / count) * TAU + np.random.uniform(-0.03, 0.03)
                p_x = np.cos(angle) * (r * 1.35)
                p_y = np.sin(angle) * (r * 0.95)
                dot = Dot(point=[p_x, p_y, 0], radius=0.06, color="#00D4FF")
                police_dots.add(dot)

        cordon_rings = VGroup(*[
            DashedVMobject(Circle(radius=r, color="#00D4FF", stroke_width=1.5).scale([1.35, 0.95, 1]), num_dashes=36)
            for r in cordon_radii
        ])

        police_badge = Text("150 POLICE OFFICERS ASSEMBLE", font_size=24, weight=BOLD, color="#00D4FF").next_to(building, DOWN, buff=0.3)

        self.play(
            Create(cordon_rings),
            LaggedStartMap(FadeIn, police_dots, lag_ratio=0.005),
            FadeIn(police_badge, shift=UP * 0.2),
            crowley_shield.animate.scale(1.25),
            run_time=1.8
        )

        tear_gas_clouds = VGroup(*[
            Circle(radius=0.45 + i * 0.1, color="#2DFDC4", fill_color="#2DFDC4", fill_opacity=0.22, stroke_width=1)
            .move_to(crowley_dot.get_center() + np.array([np.cos(i * 1.25) * 0.35, np.sin(i * 1.25) * 0.25, 0]))
            for i in range(5)
        ])
        gas_label = Text("TEAR GAS INFILTRATION", font_size=20, weight=BOLD, color="#2DFDC4").next_to(top_floor_box, RIGHT, buff=0.4)

        self.play(FadeIn(tear_gas_clouds, scale=0.2), FadeIn(gas_label), run_time=0.8)
        self.play(
            tear_gas_clouds.animate.scale(2.2),
            crowley_dot.animate.set_color("#FF8C00"),
            run_time=1.0
        )

        tracers = VGroup()
        for i in range(16):
            start_p = police_dots[i * 9].get_center()
            end_p = crowley_dot.get_center() + np.random.uniform(-0.25, 0.25, 3)
            tracers.add(Line(start_p, end_p, stroke_width=2.5, color=interpolate_color(ManimColor("#FFB800"), ManimColor("#FF2A6D"), i / 16)))

        self.play(LaggedStart(*[ShowPassingFlash(line, time_width=0.35) for line in tracers], lag_ratio=0.04), run_time=1.2)

        containment_box = SurroundingRectangle(crowley_dot, color="#FF2A6D", stroke_width=3, buff=0.25)
        surrender_text = Text("AFTER 1 HOUR... HEAVY CAPTURE!", font_size=28, weight=BOLD, color="#FF2A6D").to_edge(DOWN, buff=0.4)

        self.play(
            FadeOut(tear_gas_clouds),
            FadeOut(gas_label),
            FadeOut(police_badge),
            Create(containment_box),
            ReplacementTransform(title_text, surrender_text),
            run_time=1.0
        )
        self.play(Indicate(containment_box, color="#FFFFFF", scale_factor=1.1), run_time=0.5)
        self.wait(0.5)


# =============================================================================
# VARIATION 3: Agent's Choice Hybrid (Tactical HUD & SWAT Radar)
# =============================================================================
class Variation3TacticalHUDAndSWATRadar(Scene):
    def construct(self):
        self.camera.background_color = "#020617"

        # 1. Background Coordinate Grid
        grid_lines = VGroup()
        for x in np.linspace(-7, 7, 15):
            grid_lines.add(Line([x, -4, 0], [x, 4, 0], stroke_width=0.5, stroke_opacity=0.12, color="#06b6d4"))
        for y in np.linspace(-4, 4, 9):
            grid_lines.add(Line([-7, y, 0], [7, y, 0], stroke_width=0.5, stroke_opacity=0.12, color="#06b6d4"))
        self.add(grid_lines)

        # 2. Header Telemetry Bar
        header_bar = RoundedRectangle(corner_radius=0.08, height=0.55, width=13.6, color="#1e293b", fill_color="#0f172a", fill_opacity=0.85, stroke_width=1.5).to_edge(UP, buff=0.2)
        header_title = Text("NEURO-METRICS // INFLUENCE TELEMETRY // DALE CARNEGIE PROTOCOL", font_size=16, weight=BOLD, color="#06b6d4").move_to(header_bar)
        coord_badge = Text("SYS.VER: 1936-2026 // GRID: 40.7831° N, 73.9712° W", font_size=11, color="#94a3b8").to_corner(UR, buff=0.32)

        self.play(Create(header_bar), Write(header_title), FadeIn(coord_badge), run_time=0.8)

        # 3. Telemetry Split Cards
        card_a = RoundedRectangle(corner_radius=0.12, height=4.4, width=5.8, color="#10b981", stroke_width=1.5, fill_color="#1e293b", fill_opacity=0.4).shift(LEFT * 3.2 + DOWN * 0.3)
        title_a = Text("PERSON A: EFFORTLESS MAGNETISM", font_size=17, weight=BOLD, color="#10b981").next_to(card_a.get_top(), DOWN, buff=0.25)
        gauge_bg_a = Arc(radius=0.85, start_angle=0, angle=TAU, stroke_width=6, stroke_color="#334155").move_to(card_a.get_center() + DOWN * 0.5)
        gauge_fill_a = Arc(radius=0.85, start_angle=PI/2, angle=-TAU * 0.98, stroke_width=6, stroke_color="#10b981").move_to(card_a.get_center() + DOWN * 0.5)
        pct_label_a = Text("TRUST: 98%", font_size=22, weight=BOLD, color="#10b981").move_to(gauge_bg_a)

        card_b = RoundedRectangle(corner_radius=0.12, height=4.4, width=5.8, color="#ef4444", stroke_width=1.5, fill_color="#1e293b", fill_opacity=0.4).shift(RIGHT * 3.2 + DOWN * 0.3)
        title_b = Text("PERSON B: REJECTED & ISOLATED", font_size=17, weight=BOLD, color="#ef4444").next_to(card_b.get_top(), DOWN, buff=0.25)
        gauge_bg_b = Arc(radius=0.85, start_angle=0, angle=TAU, stroke_width=6, stroke_color="#334155").move_to(card_b.get_center() + DOWN * 0.5)
        gauge_fill_b = Arc(radius=0.85, start_angle=PI/2, angle=-TAU * 0.12, stroke_width=6, stroke_color="#ef4444").move_to(card_b.get_center() + DOWN * 0.5)
        pct_label_b = Text("TRUST: 12%", font_size=22, weight=BOLD, color="#ef4444").move_to(gauge_bg_b)

        group_a = VGroup(card_a, title_a, gauge_bg_a, gauge_fill_a, pct_label_a)
        group_b = VGroup(card_b, title_b, gauge_bg_b, gauge_fill_b, pct_label_b)

        self.play(FadeIn(group_a, shift=RIGHT * 0.5), FadeIn(group_b, shift=LEFT * 0.5), run_time=1.2)
        self.play(Flash(pct_label_a, color="#10b981"), Wiggle(group_b, scale_value=1.05), run_time=0.8)
        self.wait(0.5)

        # 4. Transition into 1931 NYPD Tactical SWAT Radar
        radar_circle_1 = Circle(radius=1.5, color="#06b6d4", stroke_width=1.5, stroke_opacity=0.5)
        radar_circle_2 = Circle(radius=2.7, color="#06b6d4", stroke_width=1.5, stroke_opacity=0.35)
        radar_circle_3 = DashedVMobject(Circle(radius=3.8, color="#06b6d4", stroke_width=1.2, stroke_opacity=0.25), num_dashes=48)
        radar_cross_h = Line([-4.2, 0, 0], [4.2, 0, 0], color="#06b6d4", stroke_width=0.8, stroke_opacity=0.3)
        radar_cross_v = Line([0, -3.2, 0], [0, 3.2, 0], color="#06b6d4", stroke_width=0.8, stroke_opacity=0.3)
        radar_rig = VGroup(radar_circle_1, radar_circle_2, radar_circle_3, radar_cross_h, radar_cross_v).shift(DOWN * 0.2)

        target_dot = Dot(point=radar_rig.get_center(), radius=0.18, color="#ef4444")
        target_reticle = Square(side_length=0.6, color="#ef4444", stroke_width=2).move_to(target_dot)
        target_label = Text("TARGET: TWO-GUN CROWLEY", font_size=16, weight=BOLD, color="#ef4444").next_to(target_reticle, UP, buff=0.2)

        self.play(FadeOut(group_a), FadeOut(group_b), run_time=0.6)
        self.play(Create(radar_rig), FadeIn(target_dot, scale=0.5), Create(target_reticle), Write(target_label), run_time=1.0)

        # 150 NYPD Dots in Tactical Perimeter
        swat_dots = VGroup()
        for i in range(150):
            r = np.random.uniform(2.8, 3.9)
            theta = np.random.uniform(0, TAU)
            pos = radar_rig.get_center() + np.array([r * np.cos(theta), r * np.sin(theta) * 0.8, 0])
            swat_dots.add(Dot(point=pos, radius=0.05, color="#06b6d4", fill_opacity=0.85))

        status_badge = Text("150 OFFICERS // SIEGE ACTIVE", font_size=18, weight=BOLD, color="#06b6d4").to_edge(DOWN, buff=0.35)

        self.play(LaggedStartMap(FadeIn, swat_dots, lag_ratio=0.005), Write(status_badge), run_time=1.2)

        # Ballistic Tracer Barrage
        tracers = VGroup()
        for i in range(14):
            idx = int(np.random.uniform(0, len(swat_dots)))
            origin = swat_dots[idx].get_center()
            end = target_dot.get_center() + np.array([np.random.uniform(-0.25, 0.25), np.random.uniform(-0.25, 0.25), 0])
            tracers.add(Line(origin, end, color="#f59e0b", stroke_width=2.5))

        self.play(LaggedStart(*[ShowPassingFlash(t, time_width=0.25) for t in tracers], lag_ratio=0.04), run_time=0.8)
        self.play(Flash(target_dot, color="#ef4444", num_lines=12), run_time=0.5)
        self.wait(0.5)


# =============================================================================
# DEFAULT SCENE FOR GITHUB ACTIONS RENDER FARM
# =============================================================================
# Set default scene to render. You can change this to KineticTypographyHookScene
# or PoliceStandoffGeometricScene at any time.
class MainScene(Variation3TacticalHUDAndSWATRadar):
    pass
