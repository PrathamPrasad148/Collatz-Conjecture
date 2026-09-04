#!/usr/bin/env python3
"""Render the Collatz Reel scenes and combine them into one MP4.

Examples:
    python render_all.py                 # fast preview, 540x960
    python render_all.py --quality high  # final reel, 1080x1920 @ 60fps
    python render_all.py --scene intro   # render only one scene
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output"
MEDIA_DIR = ROOT / "media"
TEMP_DIR = ROOT / "temp_renders"

SCENES = [
    ("intro", "scenes/scene_01_intro.py", "EnhancedIntroScene"),
    ("sequence", "scenes/scene_02_sequence.py", "ExtremeSequenceScene"),
    ("tree", "scenes/scene_06_tree.py", "ReverseCollatzTreeScene"),
    ("trajectory", "scenes/scene_03_trajectory.py", "TrajectoryScene"),
    ("bars", "scenes/scene_03_trajectory.py", "BarChartTrajectory"),
    ("comparison", "scenes/scene_04_comparison.py", "ComparisonScene"),
    ("spiral", "scenes/scene_04_comparison.py", "SpiralComparison"),
    ("stats", "scenes/scene_05_statistics.py", "DataVisualization"),
    ("conclusion", "scenes/scene_05_statistics.py", "ConclusionScene"),
]


def run(cmd: list[str], *, cwd: Path = ROOT) -> None:
    print("\n> " + " ".join(map(str, cmd)))
    subprocess.run(cmd, cwd=cwd, check=True)


def check_dependencies() -> None:
    try:
        run([sys.executable, "-m", "manim", "--version"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nERROR: Manim is not installed in this environment.")
        print("Run SETUP.bat first.")
        raise SystemExit(1)

    if shutil.which("ffmpeg") is None:
        print("\nERROR: FFmpeg was not found on PATH.")
        print("Install FFmpeg and reopen the terminal, then run this again.")
        raise SystemExit(1)


def find_rendered_video(scene_name: str) -> Path | None:
    candidates = list(MEDIA_DIR.rglob(f"{scene_name}.mp4"))
    if not candidates:
        return None
    return max(candidates, key=lambda p: p.stat().st_mtime)


def render_scene(key: str, source: str, scene_class: str, quality: str) -> Path:
    print(f"\n{'=' * 70}\nRendering {key}: {scene_class}\n{'=' * 70}")

    if quality == "high":
        width, height, fps, quality_flag = 1080, 1920, 60, "-qh"
    else:
        width, height, fps, quality_flag = 540, 960, 30, "-ql"

    # Use Python's module invocation so Windows PATH does not need a global 'manim.exe'.
    cmd = [
        sys.executable, "-m", "manim", quality_flag,
        "--disable_caching",
        "--format", "mp4",
        "--resolution", f"{width},{height}",
        "--fps", str(fps),
        "--output_file", f"{key}.mp4",
        source,
        scene_class,
    ]
    run(cmd)

    video = find_rendered_video(key)
    if video is None:
        raise RuntimeError(f"Manim finished but no MP4 was found for {scene_class}.")

    return video


def combine_videos(videos: list[Path], output: Path) -> None:
    TEMP_DIR.mkdir(exist_ok=True)
    concat = TEMP_DIR / "concat.txt"
    with concat.open("w", encoding="utf-8") as f:
        for video in videos:
            # FFmpeg concat demuxer accepts absolute paths when -safe 0 is used.
            f.write("file '" + video.resolve().as_posix().replace("'", "'\\''") + "'\n")

    output.parent.mkdir(exist_ok=True)
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "warning",
        "-f", "concat", "-safe", "0", "-i", str(concat),
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-an", "-movflags", "+faststart",
        "-y", str(output),
    ]
    run(cmd)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render the Collatz Instagram Reel")
    parser.add_argument("--quality", choices=["low", "high"], default="low")
    parser.add_argument("--scene", choices=[x[0] for x in SCENES], help="Render one scene only")
    args = parser.parse_args()

    print("\nCOLLATZ CONJECTURE — MANIM REEL")
    print("Project folder:", ROOT)
    check_dependencies()

    selected = [x for x in SCENES if x[0] == args.scene] if args.scene else SCENES
    rendered: list[Path] = []

    for key, source, scene_class in selected:
        rendered.append(render_scene(key, source, scene_class, args.quality))

    if len(rendered) > 1:
        final_name = "collatz_reel_final_hd.mp4" if args.quality == "high" else "collatz_reel_preview.mp4"
        final = OUTPUT_DIR / final_name
        combine_videos(rendered, final)
        print(f"\nSUCCESS! Final video:\n{final}")
    else:
        print(f"\nSUCCESS! Rendered video:\n{rendered[0]}")


if __name__ == "__main__":
    main()
