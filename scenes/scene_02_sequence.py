import numpy as np
from manim import *
from config.settings import COLORS
from utils.collatz_utils import collatz_sequence


class ExtremeSequenceScene(Scene):
    """Cinematic 9:16 step-by-step trace of number 42."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # -------------------------------------------------------------
        # 1. HEADER
        # -------------------------------------------------------------
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=5.6, height=0.68,
                fill_color=COLORS["secondary"], fill_opacity=0.15,
                stroke_color=COLORS["secondary"], stroke_width=2
            ),
            Text("STEP-BY-STEP TRACE", font_size=24, color=COLORS["secondary"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text("WATCH 42 COLLAPSE", font_size=62, color=COLORS["accent"], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.30)

        subtitle = Text(
            "Follow the halving and tripling down to 1:",
            font_size=28, color=COLORS["light"]
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
        # 2. SEQUENCE DATA
        # -------------------------------------------------------------
        start_num = 42
        sequence = collatz_sequence(start_num, max_iterations=20)
        # 42 -> 21 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1 (9 values, 8 steps)

        rows = []
        top_y = 6.8
        row_gap = 1.45

        for i in range(1, len(sequence)):
            prev = sequence[i - 1]
            curr = sequence[i]
            is_even = (prev % 2 == 0)
            op = "\u00f7 2" if is_even else "\u00d7 3 + 1"
            col = COLORS["secondary"] if is_even else COLORS["primary"]

            y = top_y - (i - 1) * row_gap

            # Step index
            step_bg = RoundedRectangle(
                corner_radius=0.15, width=1.1, height=0.55,
                fill_color="#101426", fill_opacity=0.9,
                stroke_color=COLORS["card_border"], stroke_width=1.5
            ).move_to([-4.8, y, 0])
            step_lbl = Text(f"#{i:02d}", font_size=19, color=COLORS["subtext"], weight=BOLD).move_to(step_bg)
            step_grp = VGroup(step_bg, step_lbl)

            # Left number badge
            left_circ = Circle(radius=0.48, fill_color="#101426", fill_opacity=0.95,
                               stroke_color=col if i == 1 else COLORS["subtext"], stroke_width=2.5).move_to([-2.8, y, 0])
            left_txt = Text(str(prev), font_size=26, color=COLORS["light"], weight=BOLD).move_to(left_circ)
            left_grp = VGroup(left_circ, left_txt)

            # Arrow & Operation pill
            op_box = RoundedRectangle(
                corner_radius=0.15, width=2.4, height=0.55,
                fill_color=col, fill_opacity=0.18,
                stroke_color=col, stroke_width=2
            ).move_to([0.0, y, 0])
            op_txt = Text(op, font_size=20, color=col, weight=BOLD).move_to(op_box)
            arrow_l = Line([-2.1, y, 0], [-1.3, y, 0], stroke_color=col, stroke_width=3)
            arrow_r = Line([1.3, y, 0], [2.1, y, 0], stroke_color=col, stroke_width=3)
            op_grp = VGroup(arrow_l, op_box, op_txt, arrow_r)

            # Right number badge
            is_final = (curr == 1)
            r_col = COLORS["highlight"] if is_final else col
            r_circ = Circle(radius=0.48, fill_color="#101426", fill_opacity=0.95,
                            stroke_color=r_col, stroke_width=3.2 if is_final else 2.5).move_to([2.8, y, 0])
            r_txt = Text(str(curr), font_size=26, color=COLORS["light"], weight=BOLD).move_to(r_circ)
            r_grp = VGroup(r_circ, r_txt)

            row_mobj = VGroup(step_grp, left_grp, op_grp, r_grp)

            if is_final:
                target_pill = VGroup(
                    RoundedRectangle(corner_radius=0.15, width=2.0, height=0.55,
                                     fill_color=COLORS["highlight"], fill_opacity=0.2,
                                     stroke_color=COLORS["highlight"], stroke_width=1.8),
                    Text("TARGET \u2713", font_size=16, color=COLORS["highlight"], weight=BOLD)
                ).move_to([4.8, y, 0])
                row_mobj.add(target_pill)

            rows.append(row_mobj)

        # Animate rows with crisp cadence
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=RIGHT * 0.25), run_time=0.22)

        self.wait(0.4)

        # -------------------------------------------------------------
        # 3. FOOTER INSIGHT CARD
        # -------------------------------------------------------------
        footer_card = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.2,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["highlight"], stroke_width=3
        ).move_to([0, -9.8, 0])

        f_tag = Text("THE COLLATZ TRAP", font_size=20, color=COLORS["accent"], weight=BOLD)
        f_title = Text("Spikes to 64, then crashes down to 1 in 8 steps.", font_size=28, color=COLORS["highlight"], weight=BOLD)
        f_sub = Text("Once it touches a power of 2, the fall to 1 is unstoppable.", font_size=21, color=COLORS["light"])
        f_txt = VGroup(f_tag, f_title, f_sub).arrange(DOWN, buff=0.12).move_to(footer_card.get_center())
        footer = VGroup(footer_card, f_txt)

        self.play(FadeIn(footer, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # -------------------------------------------------------------
        # 4. OUTRO
        # -------------------------------------------------------------
        self.play(
            FadeOut(badge),
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(footer),
            *[FadeOut(r) for r in rows],
            run_time=0.6
        )


class SequenceVisualization(ExtremeSequenceScene):
    """Alias for backwards compatibility."""
    pass
