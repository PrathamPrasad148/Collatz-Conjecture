from manim import *
from scenes.scene_01_intro import EnhancedIntroScene
from scenes.scene_02_sequence import ExtremeSequenceScene
from scenes.scene_03_trajectory import TrajectoryScene, BarChartTrajectory
from scenes.scene_04_comparison import ComparisonScene, SpiralComparison
from scenes.scene_05_statistics import StatisticsScene, DataVisualization, ConclusionScene

# Configuration
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_rate = 60
config.quality = "high_quality"

# All scenes in sequence
all_scenes = [
    ("Intro", EnhancedIntroScene),
    ("Sequence", ExtremeSequenceScene),
    ("Trajectory", TrajectoryScene),
    ("Bars", BarChartTrajectory),
    ("Comparison", ComparisonScene),
    ("Spiral", SpiralComparison),
    ("Statistics", DataVisualization),
    ("Conclusion", ConclusionScene),
]

if __name__ == "__main__":
    print("Collatz Conjecture Manim Project")
    print("=" * 50)
    print("\nAvailable scenes:")
    for name, scene_class in all_scenes:
        print(f"  - {name}: {scene_class.__name__}")
    
    print("\n" + "=" * 50)
    print("\nTo render individual scenes, use:")
    print("  manim -pql main.py <SceneClassName>")
    print("\nTo render all scenes:")
    print("  python render_all.py")
    print("\n" + "=" * 50)