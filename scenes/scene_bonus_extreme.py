from manim import *
from config.settings import COLORS
from utils.collatz_utils import collatz_sequence

class ExtremeParticleScene(Scene):
    """Ultra-extreme particle explosion visualization"""
    def construct(self):
        self.camera.background_color = COLORS["dark"]
        
        title = Text("COLLATZ EXPLOSION", font_size=64, color=COLORS["warning"], weight=BOLD)
        title.move_to(UP * 3.5)
        
        self.play(Write(title), run_time=0.6)
        
        # Starting number
        start_num = 99
        sequence = collatz_sequence(start_num, max_iterations=80)
        
        # Create particle burst at origin
        particles = []
        
        for i in range(min(len(sequence), 30)):
            # Random spread
            angle = (i / 30) * TAU
            distance = 2 + (i * 0.15)
            
            x = distance * np.cos(angle)
            y = distance * np.sin(angle)
            
            # Particle
            particle = Circle(
                radius=0.15,
                color=COLORS["primary"] if sequence[i] % 2 == 0 else COLORS["accent"],
                fill_opacity=0.8
            )
            particle.move_to([x, y, 0])
            
            # Number label
            label = Text(str(sequence[i]), font_size=16, color=COLORS["light"])
            label.move_to([x, y, 0])
            
            particles.append((particle, label, sequence[i]))
        
        # Burst animation
        for i, (particle, label, val) in enumerate(particles):
            self.add(particle, label)
            
            if i % 3 == 0:
                self.wait(0.05)
        
        self.wait(1)
        
        # Converge to center
        center_circle = Circle(
            radius=0.5,
            color=COLORS["highlight"],
            fill_opacity=1
        )
        center_circle.move_to(ORIGIN)
        
        center_label = Text("1", font_size=48, color=COLORS["dark"], weight=BOLD)
        center_label.move_to(ORIGIN)
        
        self.play(
            *[p.animate.move_to(ORIGIN) for p, _, _ in particles],
            FadeIn(center_circle),
            FadeIn(center_label),
            run_time=1
        )
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(center_circle), FadeOut(center_label), run_time=0.5)
        self.play(*[FadeOut(p) for p, _, _ in particles], run_time=0.3)


class RippleEffectScene(Scene):
    """Ripple/wave effect showing sequence propagation"""
    def construct(self):
        self.camera.background_color = COLORS["dark"]
        
        title = Text("SEQUENCE RIPPLE", font_size=56, color=COLORS["accent"], weight=BOLD)
        title.move_to(UP * 3.5)
        
        self.play(Write(title), run_time=0.6)
        
        start_num = 50
        sequence = collatz_sequence(start_num, max_iterations=60)
        
        # Create ripples at center spreading outward
        ripples = []
        
        for i in range(0, min(len(sequence), 25)):
            val = sequence[i]
            
            # Create ripple circle with opacity based on value
            circle = Circle(
                radius=0.3 + (val / max(sequence)) * 0.7,
                stroke_color=COLORS["secondary"],
                stroke_width=2,
                fill_opacity=0.1 * (1 - i / 25),
                fill_color=COLORS["primary"]
            )
            
            # Position radially outward
            distance = i * 0.5
            angle = 0
            x = distance * np.cos(angle)
            y = distance * np.sin(angle)
            
            circle.move_to([x, y, 0])
            ripples.append(circle)
        
        # Animate ripples emanating
        for i, ripple in enumerate(ripples):
            self.add(ripple)
            self.play(
                ripple.animate.set_stroke(opacity=0),
                ripple.animate.scale(1.5),
                run_time=0.2
            )
        
        self.wait(1.5)
        self.play(FadeOut(title), *[FadeOut(r) for r in ripples], run_time=0.6)


class NetworkVisualization(Scene):
    """Show Collatz sequence as network nodes"""
    def construct(self):
        self.camera.background_color = COLORS["dark"]
        
        title = Text("NUMBER NETWORK", font_size=56, color=COLORS["accent"], weight=BOLD)
        title.move_to(UP * 3.5)
        
        self.play(Write(title), run_time=0.6)
        
        # Multiple numbers converging to 1
        numbers = [7, 15, 27, 31]
        sequences = {n: collatz_sequence(n, max_iterations=30) for n in numbers}
        
        # Common center point (1)
        center = Circle(
            radius=0.6,
            color=COLORS["highlight"],
            fill_opacity=1
        )
        center.move_to(ORIGIN)
        
        center_text = Text("1", font_size=48, color=COLORS["dark"], weight=BOLD)
        center_text.move_to(ORIGIN)
        
        self.add(center, center_text)
        
        # Draw paths from each number to center
        colors_for_num = [COLORS["primary"], COLORS["secondary"], COLORS["accent"], COLORS["warning"]]
        
        for idx, start_num in enumerate(numbers):
            seq = sequences[start_num]
            
            # Starting circle
            start_circle = Circle(
                radius=0.4,
                color=colors_for_num[idx],
                fill_opacity=0.8
            )
            
            angle = (idx / len(numbers)) * TAU
            distance = 4
            x = distance * np.cos(angle)
            y = distance * np.sin(angle)
            start_circle.move_to([x, y, 0])
            
            # Connection line
            line = Line(start_circle.get_center(), center.get_center())
            line.set_stroke(colors_for_num[idx], width=2, opacity=0.5)
            
            # Label
            label = Text(str(start_num), font_size=28, color=colors_for_num[idx], weight=BOLD)
            label.move_to([x, y, 0])
            
            self.play(
                FadeIn(start_circle),
                FadeIn(label),
                run_time=0.5
            )
            
            self.play(Create(line), run_time=0.8)
            
            self.wait(0.2)
        
        # Pulsing center
        self.play(
            center.animate.scale(1.3),
            center_text.animate.scale(1.3),
            run_time=0.5
        )
        
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)


class HypnoticSpiral(Scene):
    """Hypnotic spiral convergence effect"""
    def construct(self):
        self.camera.background_color = COLORS["dark"]
        
        title = Text("THE SPIRAL", font_size=56, color=COLORS["accent"], weight=BOLD)
        title.move_to(UP * 3.5)
        
        self.play(Write(title), run_time=0.6)
        
        start_num = 73
        sequence = collatz_sequence(start_num, max_iterations=100)
        
        # Create hypnotic spiral
        points = []
        max_val = max(sequence)
        
        for i, val in enumerate(sequence[:80]):
            # Logarithmic spiral
            angle = i * 0.5
            radius = 0.1 + (i * 0.03) * (1 - i / 80)  # Decreasing as we approach center
            
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            points.append([x, y, 0])
        
        # Create spiral line
        spiral = VMobject()
        spiral.set_points_as_corners(points)
        spiral.set_stroke(
            color=COLORS["primary"],
            width=4,
            opacity=0.8
        )
        
        self.play(Create(spiral), run_time=2)
        
        # End point highlight
        end_circle = Circle(
            radius=0.3,
            color=COLORS["highlight"],
            fill_opacity=1
        )
        end_circle.move_to(points[-1])
        
        self.play(FadeIn(end_circle), run_time=0.5)
        
        # Spiral color gradient animation
        self.play(
            spiral.animate.set_stroke(color=COLORS["warning"]),
            spiral.animate.set_stroke(width=5),
            run_time=0.8
        )
        
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)


class MatrixRain(Scene):
    """Matrix-style falling numbers converging to 1"""
    def construct(self):
        self.camera.background_color = COLORS["dark"]
        
        title = Text("MATRIX MODE", font_size=56, color=COLORS["accent"], weight=BOLD)
        title.move_to(UP * 3.5)
        
        self.play(Write(title), run_time=0.6)
        
        # Multiple columns of numbers falling
        columns = 8
        numbers_per_column = 20
        
        all_numbers = []
        
        for col in range(columns):
            x = -3 + col * 1
            
            for row in range(numbers_per_column):
                y = 3 - row * 0.6
                
                num = Text(
                    str(np.random.randint(1, 100)),
                    font_size=20,
                    color=COLORS["secondary"],
                    opacity=1 - (row / numbers_per_column) * 0.5
                )
                num.move_to([x, y, 0])
                all_numbers.append((num, x, y))
        
        # Show all numbers
        for num, _, _ in all_numbers:
            self.add(num)
        
        self.wait(0.5)
        
        # Animate all falling to center with value 1
        self.play(
            *[num.animate.move_to(ORIGIN) for num, _, _ in all_numbers],
            *[num.animate.set_color(COLORS["highlight"]) for num, _, _ in all_numbers],
            run_time=1.5
        )
        
        # Final 1
        final = Circle(
            radius=0.8,
            color=COLORS["highlight"],
            fill_opacity=1
        )
        final.move_to(ORIGIN)
        
        final_text = Text("1", font_size=64, color=COLORS["dark"], weight=BOLD)
        final_text.move_to(ORIGIN)
        
        self.play(FadeIn(final), FadeIn(final_text), run_time=0.6)
        
        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)