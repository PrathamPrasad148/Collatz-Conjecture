import numpy as np
from manim import *
from config.settings import COLORS

class ReverseCollatzTreeScene(Scene):
    def construct(self):
        self.camera.background_color = COLORS['dark']

        # -------------------------------------------------------------
        # 1. HEADER & INTRO
        # -------------------------------------------------------------
        badge = VGroup(
            RoundedRectangle(corner_radius=0.25, width=4.6, height=0.68,
                             fill_color=COLORS['secondary'], fill_opacity=0.15,
                             stroke_color=COLORS['secondary'], stroke_width=2),
            Text('REVERSE COLLATZ', font_size=24, color=COLORS['secondary'], weight=BOLD)
        ).move_to([0, 10.8, 0])

        title = Text('THE HIDDEN TREE', font_size=64, color=COLORS['accent'], weight=BOLD)
        title.next_to(badge, DOWN, buff=0.32)

        subtitle = Text('Run the rules backwards from 1: who can reach it?',
                        font_size=28, color=COLORS['light'])
        subtitle.next_to(title, DOWN, buff=0.22)

        # Bottom Rule Cards
        def make_rule_card(badge_text, formula, sub, color, width=5.7):
            box = RoundedRectangle(corner_radius=0.25, width=width, height=2.0,
                                   fill_color='#12162a', fill_opacity=0.95,
                                   stroke_color=color, stroke_width=2.5)
            lbl = Text(badge_text, font_size=19, color=color, weight=BOLD)
            form = Text(formula, font_size=32, color=COLORS['light'], weight=BOLD)
            subt = Text(sub, font_size=18, color=color)
            txt = VGroup(lbl, form, subt).arrange(DOWN, buff=0.12)
            return VGroup(box, txt)

        card_even = make_rule_card('ALWAYS DOUBLE', 'n  \u2192  2n', 'Reverse of  \u00f72  (\u00d72)', COLORS['secondary'])
        card_odd = make_rule_card('ODD BRANCH', 'n  \u2192  (n\u22121)\u00f73', 'Only when result is odd', COLORS['primary'])
        rule_cards = VGroup(card_even, card_odd).arrange(RIGHT, buff=0.6).move_to([0, -10.4, 0])

        self.play(
            FadeIn(badge, shift=DOWN * 0.4),
            Write(title),
            FadeIn(subtitle),
            FadeIn(rule_cards, shift=UP * 0.4),
            run_time=0.9
        )
        self.wait(0.3)

        # -------------------------------------------------------------
        # 2. TREE DATA & COORDINATES
        # -------------------------------------------------------------
        coords = {
            1: (0.0, 7.2),
            2: (0.0, 5.4),
            4: (0.0, 3.6),
            8: (0.0, 1.8),
            16: (0.0, 0.0),
            32: (-2.8, -2.2),
            5: (2.8, -2.2),
            64: (-3.8, -4.6),
            10: (3.8, -4.6),
            128: (-5.2, -7.0),
            21: (-2.4, -7.0),
            20: (2.4, -7.0),
            3: (5.2, -7.0),
        }

        def make_node(val):
            is_root = (val == 1)
            is_odd = val in [5, 21, 3]
            col = COLORS['accent'] if is_root else (COLORS['primary'] if is_odd else COLORS['secondary'])
            rad = 0.68 if is_root else 0.58

            glow = Circle(radius=rad + 0.14, stroke_color=col, stroke_width=1.8,
                          stroke_opacity=0.35).move_to([coords[val][0], coords[val][1], 0])
            circ = Circle(radius=rad, fill_color='#101426', fill_opacity=0.96,
                          stroke_color=col, stroke_width=3.8).move_to([coords[val][0], coords[val][1], 0])
            lbl = Text(str(val), font_size=38 if len(str(val)) <= 2 else 32,
                       color=COLORS['light'], weight=BOLD).move_to([coords[val][0], coords[val][1], 0])

            return VGroup(glow, circ, lbl), col

        def make_edge(p, c, typ, tag=None):
            col = COLORS['primary'] if typ == 'odd' else COLORS['secondary']
            p_pos = np.array([coords[p][0], coords[p][1], 0])
            c_pos = np.array([coords[c][0], coords[c][1], 0])
            dir_v = c_pos - p_pos
            length = np.linalg.norm(dir_v)
            u = dir_v / length
            start = p_pos + u * 0.65
            end = c_pos - u * 0.65
            line = Line(start, end, stroke_color=col, stroke_width=4.5, stroke_opacity=0.85)

            tag_grp = None
            if tag:
                mid = (start + end) / 2
                offset = (RIGHT if mid[0] < 0 else LEFT) * 0.45
                tag_bg = RoundedRectangle(corner_radius=0.15, width=1.9, height=0.48,
                                          fill_color='#101426', fill_opacity=0.95,
                                          stroke_color=col, stroke_width=1.5)
                tag_txt = Text(tag, font_size=15, color=col, weight=BOLD)
                tag_grp = VGroup(tag_bg, tag_txt).move_to(mid + offset)

            return line, tag_grp

        nodes = {}
        node_colors = {}
        for v in coords:
            nodes[v], node_colors[v] = make_node(v)

        root_badge = VGroup(
            RoundedRectangle(corner_radius=0.15, width=1.5, height=0.45,
                             fill_color='#101426', fill_opacity=0.95,
                             stroke_color=COLORS['accent'], stroke_width=1.5),
            Text('ROOT', font_size=15, color=COLORS['accent'], weight=BOLD)
        ).next_to(nodes[1], RIGHT, buff=0.2)

        # -------------------------------------------------------------
        # 3. ACT 1: TRUNK EMERGENCE (1 -> 2 -> 4 -> 8 -> 16)
        # -------------------------------------------------------------
        self.play(FadeIn(nodes[1], scale=0.6), FadeIn(root_badge), run_time=0.5)

        trunk_edges = []
        trunk_steps = [(1, 2), (2, 4), (4, 8), (8, 16)]
        for p, c in trunk_steps:
            edge, _ = make_edge(p, c, 'even')
            trunk_edges.append(edge)
            self.play(
                Create(edge),
                FadeIn(nodes[c], scale=0.7),
                run_time=0.25
            )
        
        trunk_tag = Text('The 1 \u2192 2 \u2192 4 \u2192 8 \u2192 16 trunk', font_size=20,
                         color=COLORS['highlight'], weight=BOLD).next_to(nodes[8], RIGHT, buff=0.5)
        self.play(FadeIn(trunk_tag), run_time=0.3)
        self.wait(0.4)

        # -------------------------------------------------------------
        # 4. ACT 2: THE FIRST FORK AT 16!
        # -------------------------------------------------------------
        pulse_16 = Circle(radius=0.9, stroke_color=COLORS['accent'], stroke_width=4, stroke_opacity=0.9).move_to(nodes[16].get_center())
        fork_callout = Text('At 16: (16\u22121)\u00f73 = 5! A branch is born!', font_size=22,
                            color=COLORS['accent'], weight=BOLD).move_to([0, -1.0, 0])

        self.play(
            FadeOut(trunk_tag),
            nodes[16][1].animate.set_stroke(COLORS['accent'], width=5),
            FadeIn(pulse_16, scale=0.5),
            FadeIn(fork_callout),
            run_time=0.4
        )
        self.play(FadeOut(pulse_16), run_time=0.2)

        edge_16_32, _ = make_edge(16, 32, 'even')
        edge_16_5, tag_16_5 = make_edge(16, 5, 'odd', '(16\u22121)\u00f73')

        self.play(
            Create(edge_16_32),
            FadeIn(nodes[32], scale=0.7),
            Create(edge_16_5),
            FadeIn(tag_16_5),
            FadeIn(nodes[5], scale=0.7),
            FadeOut(fork_callout),
            run_time=0.65
        )
        self.wait(0.3)

        # -------------------------------------------------------------
        # 5. ACT 3: SPREADING TO GENERATIONS 2 & 3
        # -------------------------------------------------------------
        edge_32_64, _ = make_edge(32, 64, 'even')
        edge_5_10, _ = make_edge(5, 10, 'even')

        self.play(
            Create(edge_32_64),
            FadeIn(nodes[64], scale=0.7),
            Create(edge_5_10),
            FadeIn(nodes[10], scale=0.7),
            run_time=0.45
        )

        edge_64_128, _ = make_edge(64, 128, 'even')
        edge_64_21, tag_64_21 = make_edge(64, 21, 'odd', '(64\u22121)\u00f73')
        edge_10_20, _ = make_edge(10, 20, 'even')
        edge_10_3, tag_10_3 = make_edge(10, 3, 'odd', '(10\u22121)\u00f73')

        self.play(
            Create(edge_64_128),
            FadeIn(nodes[128], scale=0.7),
            Create(edge_64_21),
            FadeIn(tag_64_21),
            FadeIn(nodes[21], scale=0.7),
            Create(edge_10_20),
            FadeIn(nodes[20], scale=0.7),
            Create(edge_10_3),
            FadeIn(tag_10_3),
            FadeIn(nodes[3], scale=0.7),
            run_time=0.7
        )
        self.wait(0.5)

        # -------------------------------------------------------------
        # 6. ACT 4: CANOPY EXPANSION & GRAND CONCLUSION
        # -------------------------------------------------------------
        # Smoothly replace bottom rule cards with the grand conclusion card!
        conclusion_box = RoundedRectangle(
            corner_radius=0.25, width=12.2, height=2.2,
            fill_color='#101426', fill_opacity=0.98,
            stroke_color=COLORS['highlight'], stroke_width=3
        ).move_to([0, -10.4, 0])

        c_tag = Text('THE COLLATZ CONJECTURE', font_size=20, color=COLORS['accent'], weight=BOLD)
        c_title = Text('Every single number lives in this infinite tree.', font_size=30, color=COLORS['highlight'], weight=BOLD)
        c_sub = Text('All numbers in the universe connect back to 1.', font_size=22, color=COLORS['light'])
        c_text = VGroup(c_tag, c_title, c_sub).arrange(DOWN, buff=0.12).move_to(conclusion_box.get_center())
        conclusion_card = VGroup(conclusion_box, c_text)

        # Sprout delicate glowing branches from the leaf nodes
        canopy_branches = VGroup()
        canopy_dots = VGroup()

        sub_branches = [
            # from 128: 256
            ((-5.2, -7.0), (-6.0, -8.3), COLORS['secondary']),
            ((-5.2, -7.0), (-4.7, -8.3), COLORS['secondary']),
            # from 21: 42
            ((-2.4, -7.0), (-2.9, -8.3), COLORS['secondary']),
            ((-2.4, -7.0), (-1.9, -8.3), COLORS['secondary']),
            # from 20: 40 and 13
            ((2.4, -7.0), (1.9, -8.3), COLORS['secondary']),
            ((2.4, -7.0), (2.9, -8.3), COLORS['primary']),
            # from 3: 6
            ((5.2, -7.0), (4.7, -8.3), COLORS['secondary']),
            ((5.2, -7.0), (6.0, -8.3), COLORS['secondary']),
        ]

        for (sx, sy), (ex, ey), c_col in sub_branches:
            l = Line([sx, sy - 0.65, 0], [ex, ey, 0], stroke_color=c_col, stroke_width=2.5, stroke_opacity=0.6)
            d = Dot([ex, ey, 0], radius=0.10, color=c_col)
            canopy_branches.add(l)
            canopy_dots.add(d)

        self.play(
            FadeOut(rule_cards, shift=DOWN * 0.3),
            FadeIn(conclusion_card, shift=UP * 0.3),
            Create(canopy_branches),
            FadeIn(canopy_dots),
            # Pulse the trunk nodes
            *[nodes[v][0].animate.set_stroke(COLORS['highlight'], width=3, opacity=0.8) for v in [1, 2, 4, 8, 16]],
            run_time=0.9
        )
        self.wait(2.0)

        # -------------------------------------------------------------
        # 7. CLEAN OUTRO
        # -------------------------------------------------------------
        self.play(
            FadeOut(badge),
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(conclusion_card),
            FadeOut(canopy_branches),
            FadeOut(canopy_dots),
            *[FadeOut(nodes[v]) for v in nodes],
            FadeOut(root_badge),
            *[FadeOut(e) for e in trunk_edges],
            FadeOut(edge_16_32), FadeOut(edge_16_5), FadeOut(tag_16_5),
            FadeOut(edge_32_64), FadeOut(edge_5_10),
            FadeOut(edge_64_128), FadeOut(edge_64_21), FadeOut(tag_64_21),
            FadeOut(edge_10_20), FadeOut(edge_10_3), FadeOut(tag_10_3),
            run_time=0.6
        )
