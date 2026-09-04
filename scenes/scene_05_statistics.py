import numpy as np
from manim import *
from config.settings import COLORS
from utils.collatz_utils import collatz_sequence


class DataVisualization(Scene):
    """Full-screen 9:16 statistical records for Collatz numbers."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # Header
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=5.6, height=0.68,
                fill_color=COLORS["accent"], fill_opacity=0.15,
                stroke_color=COLORS["accent"], stroke_width=2
            ),
            Text("BIG DATA INSIGHTS", font_size=24, color=COLORS["accent"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text("FASCINATING RECORDS", font_size=58, color=COLORS["accent"], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.30)

        subtitle = Text("Scanning all starting numbers up to 100:",
                        font_size=28, color=COLORS["light"])
        subtitle.next_to(title, DOWN, buff=0.20)

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            Write(title),
            FadeIn(subtitle),
            run_time=0.8
        )
        self.wait(0.2)

        # 3 Hero Cards
        def make_metric_card(tag_text, big_num, label_text, sub_text, color, y):
            box = RoundedRectangle(
                corner_radius=0.3, width=12.2, height=3.8,
                fill_color=COLORS["card_bg"], fill_opacity=0.94,
                stroke_color=color, stroke_width=2.5
            ).move_to([0, y, 0])

            tag = VGroup(
                RoundedRectangle(corner_radius=0.15, width=4.2, height=0.55,
                                 fill_color=color, fill_opacity=0.18,
                                 stroke_color=color, stroke_width=1.5),
                Text(tag_text, font_size=17, color=color, weight=BOLD)
            ).move_to([-3.4, y + 1.25, 0])

            val = Text(big_num, font_size=44, color=COLORS["light"], weight=BOLD).move_to([0, y + 0.2, 0])
            lbl = Text(label_text, font_size=24, color=color, weight=BOLD).move_to([0, y - 0.55, 0])
            sub = Text(sub_text, font_size=18, color=COLORS["subtext"]).move_to([0, y - 1.2, 0])

            return VGroup(box, tag, val, lbl, sub)

        card1 = make_metric_card("LONGEST MARATHON", "n = 97  \u2192  118 STEPS",
                                 "Under 100, 97 reigns supreme", "Takes over 100 iterations to reach 1",
                                 COLORS["secondary"], 4.8)

        card2 = make_metric_card("HIGHEST SUMMIT", "n = 27  \u2192  9,232 PEAK",
                                 "A 341\u00d7 explosive surge", "Reaches astronomical heights before dropping",
                                 COLORS["primary"], 0.2)

        card3 = make_metric_card("EMPIRICAL TEST", "2^68 NUMBERS CHECKED",
                                 "Zero counterexamples found", "Trillions of trillions tested by supercomputers",
                                 COLORS["highlight"], -4.4)

        cards = [card1, card2, card3]
        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.25), run_time=0.45)

        self.wait(0.4)

        # Footer
        footer_card = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.2,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["highlight"], stroke_width=3
        ).move_to([0, -9.8, 0])

        f_tag = Text("THE VERDICT", font_size=20, color=COLORS["accent"], weight=BOLD)
        f_title = Text("Every single tested number reaches 1.", font_size=28, color=COLORS["highlight"], weight=BOLD)
        f_sub = Text("Yet no mathematician on Earth can prove why.", font_size=21, color=COLORS["light"])
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


class StatisticsScene(DataVisualization):
    """Alias for backwards compatibility."""
    pass


class ConclusionScene(Scene):
    """Grand finale 9:16 climax for the Collatz Reel."""

    def construct(self):
        self.camera.background_color = COLORS["dark"]

        # Header
        badge = VGroup(
            RoundedRectangle(
                corner_radius=0.25, width=6.2, height=0.68,
                fill_color=COLORS["accent"], fill_opacity=0.15,
                stroke_color=COLORS["accent"], stroke_width=2
            ),
            Text("THE UNSOLVED RIDDLE", font_size=24, color=COLORS["accent"], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text("COLLATZ CONJECTURE", font_size=64, color=COLORS["primary"], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.30)

        subtitle = Text("The simplest math puzzle no one can solve.",
                        font_size=28, color=COLORS["light"])
        subtitle.next_to(title, DOWN, buff=0.20)

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            Write(title),
            FadeIn(subtitle),
            run_time=0.8
        )
        self.wait(0.2)

        # Central Singularity of 1
        center_y = 3.2
        glow_ring3 = Circle(radius=2.2, stroke_color=COLORS["accent"], stroke_width=1.5, stroke_opacity=0.25).move_to([0, center_y, 0])
        glow_ring2 = Circle(radius=1.6, stroke_color=COLORS["secondary"], stroke_width=2, stroke_opacity=0.45).move_to([0, center_y, 0])
        glow_ring1 = Circle(radius=1.0, stroke_color=COLORS["primary"], stroke_width=2.5, stroke_opacity=0.75).move_to([0, center_y, 0])
        center_disk = Circle(radius=0.72, fill_color=COLORS["accent"], fill_opacity=1,
                             stroke_color=COLORS["light"], stroke_width=3).move_to([0, center_y, 0])
        one_txt = Text("1", font_size=58, color=COLORS["dark"], weight=BOLD).move_to(center_disk)

        core = VGroup(glow_ring3, glow_ring2, glow_ring1, center_disk, one_txt)

        self.play(FadeIn(core, scale=0.7), run_time=0.7)

        # 3 Pillar Summary Cards
        def make_pillar_card(title_txt, sub_txt, color, y):
            box = RoundedRectangle(
                corner_radius=0.25, width=12.2, height=2.2,
                fill_color=COLORS["card_bg"], fill_opacity=0.94,
                stroke_color=color, stroke_width=2.5
            ).move_to([0, y, 0])
            t = Text(title_txt, font_size=26, color=color, weight=BOLD)
            s = Text(sub_txt, font_size=20, color=COLORS["light"])
            txt = VGroup(t, s).arrange(DOWN, buff=0.15).move_to(box.get_center())
            return VGroup(box, txt)

        card_a = make_pillar_card("SIMPLE RULES", "Only basic halving and tripling", COLORS["secondary"], -0.8)
        card_b = make_pillar_card("INFINITE COMPLEXITY", "Unpredictable chaotic trajectories", COLORS["primary"], -3.4)
        card_c = make_pillar_card("A $1,000,000 BOUNTY", "Unproven after nearly 100 years", COLORS["accent"], -6.0)

        pillars = [card_a, card_b, card_c]
        for p in pillars:
            self.play(FadeIn(p, shift=UP * 0.25), run_time=0.35)

        # Final Call to Action
        cta_card = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.4,
            fill_color="#101426", fill_opacity=0.98,
            stroke_color=COLORS["highlight"], stroke_width=3
        ).move_to([0, -9.6, 0])

        cta_t = Text("CAN YOU PROVE IT?", font_size=32, color=COLORS["highlight"], weight=BOLD)
        cta_s = Text("Share your thoughts in the comments below \u2193", font_size=22, color=COLORS["light"])
        cta_txt = VGroup(cta_t, cta_s).arrange(DOWN, buff=0.15).move_to(cta_card.get_center())
        cta = VGroup(cta_card, cta_txt)

        self.play(FadeIn(cta, shift=UP * 0.3), run_time=0.6)
        self.wait(2.2)

        # Fade out
        self.play(
            FadeOut(badge), FadeOut(title), FadeOut(subtitle),
            FadeOut(core),
            *[FadeOut(p) for p in pillars],
            FadeOut(cta),
            run_time=0.8
        )