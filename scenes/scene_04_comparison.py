import math
import numpy as np
from manim import *
from config.settings import COLORS
from utils.collatz_utils import collatz_sequence


class ComparisonScene(Scene):
    """Full-screen 9:16 comparison of multiple starting numbers."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # Header
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=5.6, height=0.68,
                fill_color=COLORS["accent"], fill_opacity=0.15,
                stroke_color=COLORS["accent"], stroke_width=2
            ),
            Text("MASS BENCHMARK", font_size=24, color=COLORS["accent"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text("DO ALL NUMBERS FALL?", font_size=58, color=COLORS["accent"], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.30)

        subtitle = Text("Comparing 5 completely different starting seeds:",
                        font_size=28, color=COLORS["light"])
        subtitle.next_to(title, DOWN, buff=0.20)

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            Write(title),
            FadeIn(subtitle),
            run_time=0.8
        )
        self.wait(0.2)

        # Test numbers & data
        test_numbers = [5, 42, 100, 99, 27]
        item_colors = [COLORS["secondary"], COLORS["highlight"], COLORS["accent"], COLORS["warning"], COLORS["primary"]]

        data = []
        for num in test_numbers:
            seq = collatz_sequence(num, max_iterations=500)
            data.append({
                "start": num,
                "steps": len(seq) - 1,
                "peak": max(seq),
                "color": item_colors[test_numbers.index(num)]
            })

        max_steps = max(d["steps"] for d in data)  # 111

        cards = []
        top_y = 6.4
        card_gap = 2.45

        for i, info in enumerate(data):
            y = top_y - i * card_gap
            col = info["color"]

            card_box = RoundedRectangle(
                corner_radius=0.25, width=12.2, height=2.1,
                fill_color=COLORS["card_bg"], fill_opacity=0.92,
                stroke_color=COLORS["card_border"], stroke_width=2
            ).move_to([0, y, 0])

            # Seed pill
            seed_bg = RoundedRectangle(
                corner_radius=0.18, width=2.4, height=1.3,
                fill_color="#101426", fill_opacity=0.95,
                stroke_color=col, stroke_width=2.5
            ).move_to([-4.4, y, 0])
            seed_lbl = Text(f"n = {info['start']}", font_size=26, color=col, weight=BOLD).move_to(seed_bg)
            seed_grp = VGroup(seed_bg, seed_lbl)

            # Progress bar track
            track_w = 4.8
            track = RoundedRectangle(
                corner_radius=0.12, width=track_w, height=0.38,
                fill_color="#101426", fill_opacity=0.8,
                stroke_color=COLORS["card_border"], stroke_width=1.5
            ).move_to([-0.3, y, 0])

            # Fill bar
            fill_pct = max(0.1, info["steps"] / max_steps)
            fill_w = track_w * fill_pct
            bar_fill = RoundedRectangle(
                corner_radius=0.12, width=fill_w, height=0.38,
                fill_color=col, fill_opacity=0.9, stroke_width=0
            ).move_to([track.get_left()[0] + fill_w / 2, y, 0])

            # Stat text
            step_txt = Text(f"{info['steps']} steps", font_size=22, color=COLORS["light"], weight=BOLD)
            peak_txt = Text(f"Peak: {info['peak']:,}", font_size=18, color=COLORS["subtext"])
            stats_grp = VGroup(step_txt, peak_txt).arrange(DOWN, buff=0.10).move_to([3.4, y, 0])

            # Checkmark badge
            target_badge = VGroup(
                Circle(radius=0.38, fill_color="#101426", fill_opacity=0.95,
                       stroke_color=COLORS["highlight"], stroke_width=2.2),
                Text("1 \u2713", font_size=18, color=COLORS["highlight"], weight=BOLD)
            ).move_to([5.3, y, 0])

            card_full = VGroup(card_box, seed_grp, track, bar_fill, stats_grp, target_badge)
            cards.append(card_full)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.2), run_time=0.26)

        self.wait(0.4)

        # Footer
        footer_card = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.2,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["highlight"], stroke_width=3
        ).move_to([0, -9.8, 0])

        f_tag = Text("100% CONVERGENCE", font_size=20, color=COLORS["accent"], weight=BOLD)
        f_title = Text("From 5 steps to 111 steps: ALL hit 1.", font_size=28, color=COLORS["highlight"], weight=BOLD)
        f_sub = Text("No matter the starting seed, gravity always wins.", font_size=21, color=COLORS["light"])
        f_txt = VGroup(f_tag, f_title, f_sub).arrange(DOWN, buff=0.12).move_to(footer_card.get_center())
        footer = VGroup(footer_card, f_txt)

        self.play(FadeIn(footer, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # Outro
        self.play(
            FadeOut(badge), FadeOut(title), FadeOut(subtitle),
            *[FadeOut(c) for c in cards],
            FadeOut(footer),
            run_time=0.6
        )


class SpiralComparison(Scene):
    """Full-screen 9:16 polar spirals visualizing chaotic orbits."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # Header
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=5.6, height=0.68,
                fill_color=COLORS["secondary"], fill_opacity=0.15,
                stroke_color=COLORS["secondary"], stroke_width=2
            ),
            Text("POLAR ORBITS", font_size=24, color=COLORS["secondary"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text("ORBITAL SPIRALS", font_size=60, color=COLORS["accent"], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.30)

        subtitle = Text("Visualizing sequence flow as collapsing spirals:",
                        font_size=28, color=COLORS["light"])
        subtitle.next_to(title, DOWN, buff=0.20)

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            Write(title),
            FadeIn(subtitle),
            run_time=0.8
        )

        # 3 Spiral Cards stacked vertically
        numbers = [(7, "n = 7  (Fast Decay)", COLORS["secondary"]),
                   (27, "n = 27  (Violent Storm)", COLORS["warning"]),
                   (77, "n = 77  (High Resonance)", COLORS["accent"])]

        spiral_cards = []
        center_ys = [4.8, -0.4, -5.6]

        for (num, desc, col), cy in zip(numbers, center_ys):
            card_box = RoundedRectangle(
                corner_radius=0.3, width=12.2, height=4.2,
                fill_color=COLORS["card_bg"], fill_opacity=0.92,
                stroke_color=col, stroke_width=2
            ).move_to([0, cy, 0])

            tag = Text(desc, font_size=22, color=col, weight=BOLD).move_to([0, cy + 1.55, 0])

            # Build spiral
            seq = collatz_sequence(num, max_iterations=45)
            max_s = max(seq)
            pts = []
            for i, val in enumerate(seq):
                angle = i * 0.45
                r = 0.35 + 1.2 * (math.log1p(val) / math.log1p(max_s))
                x = 0.0 + r * math.cos(angle)
                y = cy - 0.2 + (r * 0.65) * math.sin(angle)
                pts.append([x, y, 0])

            spiral_path = VMobject()
            if len(pts) > 1:
                spiral_path.set_points_as_corners(pts)
                spiral_path.set_stroke(color=col, width=2.8, opacity=0.85)

            center_dot = Circle(radius=0.18, fill_color=COLORS["highlight"], fill_opacity=1,
                                stroke_color=COLORS["light"], stroke_width=1.5).move_to([0, cy - 0.2, 0])

            card_grp = VGroup(card_box, tag, spiral_path, center_dot)
            spiral_cards.append(card_grp)

        for sc in spiral_cards:
            self.play(FadeIn(sc, shift=RIGHT * 0.2), run_time=0.4)

        self.wait(0.4)

        # Footer
        footer_card = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.2,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["highlight"], stroke_width=3
        ).move_to([0, -9.8, 0])

        f_tag = Text("THE GRAVITATIONAL CORE", font_size=20, color=COLORS["accent"], weight=BOLD)
        f_title = Text("Different orbits, but 1 is always the center.", font_size=28, color=COLORS["highlight"], weight=BOLD)
        f_sub = Text("Every spiral collapses inward to the exact same singularity.", font_size=21, color=COLORS["light"])
        f_txt = VGroup(f_tag, f_title, f_sub).arrange(DOWN, buff=0.12).move_to(footer_card.get_center())
        footer = VGroup(footer_card, f_txt)

        self.play(FadeIn(footer, shift=UP * 0.3), run_time=0.6)
        self.wait(1.8)

        # Outro
        self.play(
            FadeOut(badge), FadeOut(title), FadeOut(subtitle),
            *[FadeOut(sc) for sc in spiral_cards],
            FadeOut(footer),
            run_time=0.6
        )