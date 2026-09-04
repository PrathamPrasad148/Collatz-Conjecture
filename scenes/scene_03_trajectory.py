import math
import numpy as np
from manim import *
from config.settings import COLORS
from utils.collatz_utils import collatz_sequence


class TrajectoryScene(Scene):
    """Full-screen 9:16 mountain trajectory of number 27."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # -------------------------------------------------------------
        # 1. HEADER
        # -------------------------------------------------------------
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=5.6, height=0.68,
                fill_color=COLORS["warning"], fill_opacity=0.15,
                stroke_color=COLORS["warning"], stroke_width=2
            ),
            Text("THE ROLLERCOASTER", font_size=24, color=COLORS["warning"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text("THE JOURNEY OF 27", font_size=62, color=COLORS["accent"], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.30)

        subtitle = Text(
            "Starts humble. Skyrockets to 9,232. Crashes to 1.",
            font_size=27, color=COLORS["light"]
        )
        subtitle.next_to(title, DOWN, buff=0.20)

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            Write(title),
            FadeIn(subtitle),
            run_time=0.8
        )
        self.wait(0.2)

        # -------------------------------------------------------------
        # 2. CHART FRAME & DATA
        # -------------------------------------------------------------
        start_num = 27
        sequence = collatz_sequence(start_num, max_iterations=120)
        max_val = max(sequence)
        n = len(sequence)

        chart_w, chart_h = 12.2, 11.4
        chart_center = np.array([0.0, 0.6, 0.0])
        plot_left = chart_center[0] - chart_w / 2 + 0.6
        plot_right = chart_center[0] + chart_w / 2 - 0.6
        plot_bottom = chart_center[1] - chart_h / 2 + 0.8
        plot_top = chart_center[1] + chart_h / 2 - 0.8

        frame_box = RoundedRectangle(
            corner_radius=0.3, width=chart_w, height=chart_h,
            fill_color=COLORS["card_bg"], fill_opacity=0.92,
            stroke_color=COLORS["card_border"], stroke_width=2.5
        ).move_to(chart_center)

        # Subtle tier gridlines
        grid_lines = VGroup()
        tier_labels = VGroup()
        tiers = [(1, "1"), (10, "10"), (100, "100"), (1000, "1K"), (9232, "9.2K")]
        for val, lbl_str in tiers:
            log_pos = math.log10(max(1, val)) / math.log10(max_val)
            y_pos = plot_bottom + (plot_top - plot_bottom) * log_pos
            line = DashedLine([plot_left, y_pos, 0], [plot_right, y_pos, 0],
                              dash_length=0.15, dashed_ratio=0.5,
                              stroke_color=COLORS["card_border"], stroke_width=1.5)
            lbl = Text(lbl_str, font_size=16, color=COLORS["subtext"]).move_to([plot_left - 0.45, y_pos, 0])
            grid_lines.add(line)
            tier_labels.add(lbl)

        self.play(Create(frame_box), Create(grid_lines), FadeIn(tier_labels), run_time=0.6)

        # Calculate trajectory points
        coords = []
        for i, val in enumerate(sequence):
            x = plot_left + (plot_right - plot_left) * (i / (n - 1))
            log_val = math.log10(max(1, val)) / math.log10(max_val)
            y = plot_bottom + (plot_top - plot_bottom) * log_val
            coords.append(np.array([x, y, 0.0]))

        # Smooth curved path
        path = VMobject()
        path.set_points_as_corners(coords)
        path.set_stroke(color=COLORS["secondary"], width=3.5, opacity=0.85)

        # Area under curve
        fill_pts = [np.array([coords[0][0], plot_bottom, 0])] + coords + [np.array([coords[-1][0], plot_bottom, 0])]
        fill_poly = Polygon(*fill_pts, fill_color=COLORS["secondary"], fill_opacity=0.12, stroke_width=0)

        self.play(Create(path), FadeIn(fill_poly), run_time=1.1)

        # -------------------------------------------------------------
        # 3. PEAK & LANDING HIGHLIGHTS
        # -------------------------------------------------------------
        peak_idx = sequence.index(max_val)
        peak_pt = coords[peak_idx]

        peak_ring = Circle(radius=0.35, stroke_color=COLORS["warning"], stroke_width=3).move_to(peak_pt)
        peak_badge = VGroup(
            RoundedRectangle(corner_radius=0.15, width=3.6, height=0.65,
                             fill_color="#101426", fill_opacity=0.95,
                             stroke_color=COLORS["warning"], stroke_width=2),
            Text(f"PEAK: {max_val:,} (Step {peak_idx})", font_size=18, color=COLORS["warning"], weight=BOLD)
        ).next_to(peak_ring, UP, buff=0.25)

        end_pt = coords[-1]
        end_ring = Circle(radius=0.35, stroke_color=COLORS["highlight"], stroke_width=3).move_to(end_pt)
        end_badge = VGroup(
            RoundedRectangle(corner_radius=0.15, width=2.4, height=0.65,
                             fill_color="#101426", fill_opacity=0.95,
                             stroke_color=COLORS["highlight"], stroke_width=2),
            Text("TARGET: 1 \u2713", font_size=18, color=COLORS["highlight"], weight=BOLD)
        ).next_to(end_ring, UP, buff=0.25)

        self.play(
            Create(peak_ring),
            FadeIn(peak_badge, scale=0.8),
            run_time=0.6
        )
        self.play(
            Create(end_ring),
            FadeIn(end_badge, scale=0.8),
            run_time=0.5
        )
        self.wait(0.3)

        # -------------------------------------------------------------
        # 4. FOOTER STATS CARD
        # -------------------------------------------------------------
        footer_card = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.2,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["highlight"], stroke_width=3
        ).move_to([0, -9.8, 0])

        f_tag = Text("111 STEPS OF CHAOS", font_size=20, color=COLORS["accent"], weight=BOLD)
        f_title = Text("From 27 to 9,232... then down to 1.", font_size=28, color=COLORS["highlight"], weight=BOLD)
        f_sub = Text("No matter how high a number flies, the rules pull it home.", font_size=21, color=COLORS["light"])
        f_txt = VGroup(f_tag, f_title, f_sub).arrange(DOWN, buff=0.12).move_to(footer_card.get_center())
        footer = VGroup(footer_card, f_txt)

        self.play(FadeIn(footer, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # -------------------------------------------------------------
        # 5. OUTRO
        # -------------------------------------------------------------
        self.play(
            FadeOut(badge),
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(frame_box),
            FadeOut(grid_lines),
            FadeOut(tier_labels),
            FadeOut(path),
            FadeOut(fill_poly),
            FadeOut(peak_ring), FadeOut(peak_badge),
            FadeOut(end_ring), FadeOut(end_badge),
            FadeOut(footer),
            run_time=0.6
        )


class BarChartTrajectory(Scene):
    """Full-screen 9:16 equalizer bar spectrum for number 15."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # Header
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=5.6, height=0.68,
                fill_color=COLORS["secondary"], fill_opacity=0.15,
                stroke_color=COLORS["secondary"], stroke_width=2
            ),
            Text("HARMONIC SPECTRUM", font_size=24, color=COLORS["secondary"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text("THE COLLATZ EQUALIZER", font_size=58, color=COLORS["accent"], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.30)

        subtitle = Text("Step-by-step heights for starting seed n = 15:",
                        font_size=28, color=COLORS["light"])
        subtitle.next_to(title, DOWN, buff=0.20)

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            Write(title),
            FadeIn(subtitle),
            run_time=0.8
        )

        # Sequence of 15
        sequence = collatz_sequence(15, max_iterations=25)
        max_v = max(sequence)
        n_bars = len(sequence)

        chart_w, chart_h = 12.2, 10.5
        chart_box = RoundedRectangle(
            corner_radius=0.3, width=chart_w, height=chart_h,
            fill_color=COLORS["card_bg"], fill_opacity=0.92,
            stroke_color=COLORS["card_border"], stroke_width=2.5
        ).move_to([0, 0.8, 0])

        self.play(Create(chart_box), run_time=0.4)

        bar_baseline = chart_box.get_bottom()[1] + 1.2
        bar_avail_h = chart_h - 2.4
        bar_w = (chart_w - 2.0) / n_bars

        bars = []
        bar_labels = []
        start_x = chart_box.get_left()[0] + 1.0 + bar_w / 2

        for i, val in enumerate(sequence):
            is_final = (val == 1)
            is_even = (val % 2 == 0)
            col = COLORS["highlight"] if is_final else (COLORS["secondary"] if is_even else COLORS["primary"])

            # Log-proportional height
            norm_h = max(0.4, (math.log10(max(1, val)) / math.log10(max_v)) * bar_avail_h)
            x = start_x + i * bar_w

            bar = RoundedRectangle(
                corner_radius=min(0.12, bar_w * 0.3),
                width=bar_w * 0.82, height=norm_h,
                fill_color=col, fill_opacity=0.85,
                stroke_color=col, stroke_width=1.5
            )
            bar.move_to([x, bar_baseline + norm_h / 2, 0])

            lbl = Text(str(val), font_size=min(18, int(bar_w * 22)), color=COLORS["light"], weight=BOLD)
            lbl.next_to(bar, UP, buff=0.12)

            bars.append(bar)
            bar_labels.append(lbl)

        # Reveal bars like an equalizer
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.3) for b in bars], lag_ratio=0.08),
            LaggedStart(*[FadeIn(l) for l in bar_labels], lag_ratio=0.08),
            run_time=1.0
        )
        self.wait(0.4)

        # Highlight the peak bar
        peak_idx = sequence.index(max_v)
        self.play(
            bars[peak_idx].animate.set_fill(COLORS["warning"], opacity=1.0),
            run_time=0.4
        )

        # Footer card
        footer_card = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.2,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["highlight"], stroke_width=3
        ).move_to([0, -9.8, 0])

        f_tag = Text("17 STEPS TO HARMONY", font_size=20, color=COLORS["accent"], weight=BOLD)
        f_title = Text("15 peaks at 160 before settling down to 1.", font_size=28, color=COLORS["highlight"], weight=BOLD)
        f_sub = Text("Cyan = Even (\u00f72)  |  Coral = Odd (3n+1)", font_size=21, color=COLORS["light"])
        f_txt = VGroup(f_tag, f_title, f_sub).arrange(DOWN, buff=0.12).move_to(footer_card.get_center())
        footer = VGroup(footer_card, f_txt)

        self.play(FadeIn(footer, shift=UP * 0.3), run_time=0.6)
        self.wait(1.8)

        # Outro
        self.play(
            FadeOut(badge), FadeOut(title), FadeOut(subtitle),
            FadeOut(chart_box),
            *[FadeOut(b) for b in bars],
            *[FadeOut(l) for l in bar_labels],
            FadeOut(footer),
            run_time=0.6
        )