#!/usr/bin/env python3
"""Render one scene quickly on Windows/macOS/Linux."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCENES = {
    "intro": ("scenes/scene_01_intro.py", "EnhancedIntroScene"),
    "sequence": ("scenes/scene_02_sequence.py", "ExtremeSequenceScene"),
    "trajectory": ("scenes/scene_03_trajectory.py", "TrajectoryScene"),
    "bars": ("scenes/scene_03_trajectory.py", "BarChartTrajectory"),
    "comparison": ("scenes/scene_04_comparison.py", "ComparisonScene"),
    "spiral": ("scenes/scene_04_comparison.py", "SpiralComparison"),
    "stats": ("scenes/scene_05_statistics.py", "DataVisualization"),
    "conclusion": ("scenes/scene_05_statistics.py", "ConclusionScene"),
}

parser = argparse.ArgumentParser()
parser.add_argument("scene", choices=SCENES)
args = parser.parse_args()
source, scene_class = SCENES[args.scene]

cmd = [
    sys.executable, "-m", "manim", "-ql",
    "--disable_caching", "--format", "mp4",
    "--resolution", "540,960", "--fps", "30",
    "--output_file", f"{args.scene}.mp4",
    source, scene_class,
]
print("Running:", " ".join(cmd))
subprocess.run(cmd, cwd=ROOT, check=False)
