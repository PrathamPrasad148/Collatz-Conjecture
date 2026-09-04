from manim import *
from config.settings import COLORS


def overshoot(t):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


class EnhancedIntroScene(Scene):
    """Cinematic, mobile-optimized 9:16 intro for the Collatz Reel."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # -------------------------------------------------------------
        # 1. HEADER & HOOK
        # -------------------------------------------------------------
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=6.4, height=0.72,
                fill_color=COLORS["secondary"], fill_opacity=0.15,
                stroke_color=COLORS["secondary"], stroke_width=2
            ),
            Text("MATH'S GREATEST MYSTERY", font_size=24, color=COLORS["secondary"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title_1 = Text("THE COLLATZ", font_size=68, color=COLORS["primary"], weight=BOLD)
        title_2 = Text("CONJECTURE", font_size=68, color=COLORS["accent"], weight=BOLD)
        titles = VGroup(title_1, title_2).arrange(DOWN, buff=0.15).move_to([0, 8.8, 0])

        subtitle = Text(
            "Pick any positive integer. Follow two simple rules:",
            font_size=26, color=COLORS["light"]
        ).move_to([0, 7.0, 0])

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            FadeIn(titles, scale=1.1, rate_func=overshoot),
            FadeIn(subtitle),
            run_time=0.9
        )
        self.wait(0.4)

        # -------------------------------------------------------------
        # 2. RULE 1 CARD: EVEN NUMBERS (n -> n / 2)
        # -------------------------------------------------------------
        rule1_card = RoundedRectangle(
            corner_radius=0.3, width=12.2, height=3.6,
            fill_color=COLORS["card_bg"], fill_opacity=0.95,
            stroke_color=COLORS["secondary"], stroke_width=3
        ).move_to([0, 3.2, 0])

        r1_tag = VGroup(
            RoundedRectangle(corner_radius=0.15, width=3.8, height=0.55,
                             fill_color=COLORS["secondary"], fill_opacity=0.2,
                             stroke_color=COLORS["secondary"], stroke_width=1.5),
            Text("RULE 1 : EVEN NUMBER", font_size=17, color=COLORS["secondary"], weight=BOLD)
        ).move_to([-3.6, 4.3, 0])

        r1_formula = Text("n  \u2192  n \u00f7 2", font_size=36, color=COLORS["light"], weight=BOLD).move_to([-3.6, 2.8, 0])
        r1_desc = Text("Cut the number in half", font_size=20, color=COLORS["subtext"]).move_to([-3.6, 2.0, 0])

        def make_pill_num(val, color, x, y):
            circ = Circle(radius=0.62, fill_color="#101426", fill_opacity=0.95,
                          stroke_color=color, stroke_width=3.5).move_to([x, y, 0])
            lbl = Text(str(val), font_size=36, color=COLORS["light"], weight=BOLD).move_to([x, y, 0])
            return VGroup(circ, lbl)

        num_50 = make_pill_num(50, COLORS["secondary"], 1.2, 2.8)
        arrow_r1 = VGroup(
            Line([2.2, 2.8, 0], [3.6, 2.8, 0], stroke_color=COLORS["secondary"], stroke_width=4),
            Text("\u00f7 2", font_size=20, color=COLORS["secondary"], weight=BOLD).move_to([2.9, 3.3, 0])
        )
        num_25 = make_pill_num(25, COLORS["highlight"], 4.6, 2.8)

        self.play(
            Create(rule1_card),
            FadeIn(r1_tag),
            Write(r1_formula),
            FadeIn(r1_desc),
            run_time=0.6
        )
        self.play(
            FadeIn(num_50, scale=0.7),
            Create(arrow_r1),
            FadeIn(num_25, scale=0.7),
            run_time=0.6
        )
        self.wait(0.5)

        # -------------------------------------------------------------
        # 3. RULE 2 CARD: ODD NUMBERS (n -> 3n + 1)
        # -------------------------------------------------------------
        rule2_card = RoundedRectangle(
            corner_radius=0.3, width=12.2, height=3.6,
            fill_color=COLORS["card_bg"], fill_opacity=0.95,
            stroke_color=COLORS["primary"], stroke_width=3
        ).move_to([0, -1.0, 0])

        r2_tag = VGroup(
            RoundedRectangle(corner_radius=0.15, width=3.8, height=0.55,
                             fill_color=COLORS["primary"], fill_opacity=0.2,
                             stroke_color=COLORS["primary"], stroke_width=1.5),
            Text("RULE 2 : ODD NUMBER", font_size=17, color=COLORS["primary"], weight=BOLD)
        ).move_to([-3.6, 0.1, 0])

        r2_formula = Text("n  \u2192  3n + 1", font_size=36, color=COLORS["light"], weight=BOLD).move_to([-3.6, -1.4, 0])
        r2_desc = Text("Triple and add 1", font_size=20, color=COLORS["subtext"]).move_to([-3.6, -2.2, 0])

        num_25_odd = make_pill_num(25, COLORS["primary"], 1.2, -1.4)
        arrow_r2 = VGroup(
            Line([2.2, -1.4, 0], [3.6, -1.4, 0], stroke_color=COLORS["primary"], stroke_width=4),
            Text("3(25)+1", font_size=18, color=COLORS["primary"], weight=BOLD).move_to([2.9, -0.9, 0])
        )
        num_76 = make_pill_num(76, COLORS["warning"], 4.6, -1.4)

        self.play(
            Create(rule2_card),
            FadeIn(r2_tag),
            Write(r2_formula),
            FadeIn(r2_desc),
            run_time=0.6
        )
        self.play(
            FadeIn(num_25_odd, scale=0.7),
            Create(arrow_r2),
            FadeIn(num_76, scale=0.7),
            run_time=0.6
        )
        self.wait(0.5)

        # -------------------------------------------------------------
        # 4. PUNCHLINE / CHALLENGE CARD
        # -------------------------------------------------------------
        punchline_card = RoundedRectangle(
            corner_radius=0.3, width=12.2, height=3.6,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["accent"], stroke_width=3
        ).move_to([0, -5.6, 0])

        p_tag = Text("THE MYSTERY", font_size=20, color=COLORS["accent"], weight=BOLD)
        p_main = Text("Keep repeating until you hit  1.", font_size=30, color=COLORS["light"], weight=BOLD)
        p_sub = Text("Does EVERY number in the universe reach 1?", font_size=24, color=COLORS["highlight"], weight=BOLD)
        p_txt = VGroup(p_tag, p_main, p_sub).arrange(DOWN, buff=0.18).move_to(punchline_card.get_center())

        self.play(
            FadeIn(punchline_card, shift=UP * 0.4),
            FadeIn(p_txt),
            run_time=0.7
        )
        self.wait(2.0)

        # -------------------------------------------------------------
        # 5. OUTRO
        # -------------------------------------------------------------
        self.play(
            FadeOut(badge),
            FadeOut(titles),
            FadeOut(subtitle),
            FadeOut(rule1_card), FadeOut(r1_tag), FadeOut(r1_formula), FadeOut(r1_desc),
            FadeOut(num_50), FadeOut(arrow_r1), FadeOut(num_25),
            FadeOut(rule2_card), FadeOut(r2_tag), FadeOut(r2_formula), FadeOut(r2_desc),
            FadeOut(num_25_odd), FadeOut(arrow_r2), FadeOut(num_76),
            FadeOut(punchline_card), FadeOut(p_txt),
            run_time=0.6
        )