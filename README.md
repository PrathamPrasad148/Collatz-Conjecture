# COLLATZ CONJECTURE - INSTAGRAM REEL MANIM PROJECT

Beautiful, extreme animations visualizing the Collatz Conjecture for Instagram Reels. No audio needed—pure visual storytelling.

## 📋 Project Overview

This Manim project generates a complete Instagram Reel (9:16 aspect ratio) explaining the Collatz Conjecture through mesmerizing animations:

- **Simple Rules**: Shows the two rules (even: divide by 2, odd: 3n+1)
- **Sequence Tracking**: Visualize how numbers flow through the sequence
- **Trajectory Plots**: See the height/magnitude journey of each number
- **Comparisons**: Test multiple numbers and compare their paths
- **Statistics**: Display fascinating patterns and facts
- **All Visual**: No audio explanations needed

## 📁 Project Structure

```
collatz_reel/
├── config/
│   └── settings.py              # Manim configuration, colors, animation speeds
├── scenes/
│   ├── scene_01_intro.py        # Introduction to Collatz rules
│   ├── scene_02_sequence.py     # Step-by-step sequence visualization
│   ├── scene_03_trajectory.py   # Height/trajectory plots and bar charts
│   ├── scene_04_comparison.py   # Multiple numbers comparison
│   └── scene_05_statistics.py   # Stats and conclusions
├── utils/
│   └── collatz_utils.py         # Collatz math functions
├── output/                       # Final rendered videos
├── requirements.txt             # Python dependencies
├── main.py                      # Main entry point
├── quick_render.py              # Quick render individual scenes
├── render_all.py                # Render all scenes and combine
└── README.md                    # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Install FFmpeg (for video combining)
# On Ubuntu/Debian:
sudo apt-get install ffmpeg

# On macOS:
brew install ffmpeg

# On Windows:
# Download from https://ffmpeg.org/download.html
```

### 2. Render Individual Scenes (Testing)

Test a single scene quickly:

```bash
python quick_render.py intro          # Introduction
python quick_render.py sequence       # Sequence visualization
python quick_render.py trajectory     # Trajectory plots
python quick_render.py bars           # Bar chart
python quick_render.py comparison     # Multi-number comparison
python quick_render.py spiral         # Spiral visualization
python quick_render.py stats          # Statistics
python quick_render.py conclusion     # Final message
```

### 3. Render All Scenes (Full Project)

Render all scenes and combine into one video:

```bash
python render_all.py
```

This will:
- Render each scene individually
- Combine all videos into `output/collatz_reel_final.mp4`
- Output ready for Instagram Reels upload

## 🎬 Available Scenes

| Scene | File | Duration | Content |
|-------|------|----------|---------|
| **Intro** | `scene_01_intro.py` | ~4s | Explains the two rules with animations |
| **Sequence** | `scene_02_sequence.py` | ~6s | Traces a number through step-by-step |
| **Trajectory** | `scene_03_trajectory.py` | ~8s | Plot the journey as a line graph |
| **Bars** | `scene_03_trajectory.py` | ~7s | Bar chart showing magnitude changes |
| **Comparison** | `scene_04_comparison.py` | ~8s | Compare multiple numbers |
| **Spiral** | `scene_04_comparison.py` | ~6s | Spiral visualization of sequences |
| **Statistics** | `scene_05_statistics.py` | ~7s | Interesting facts and patterns |
| **Conclusion** | `scene_05_statistics.py` | ~5s | Final message |

**Total video length: ~45-50 seconds** (perfect for Instagram Reels)

## 🎨 Customization

### Change Colors

Edit `config/settings.py`:

```python
COLORS = {
    "primary": "#FF6B6B",      # Red
    "secondary": "#4ECDC4",    # Teal
    "accent": "#FFE66D",       # Yellow
    "dark": "#1A1A2E",         # Dark
    "light": "#FFFFFF",        # White
    # ... add/modify colors
}
```

### Adjust Animation Speed

Lower values = faster animations:

```python
ANIMATION_SPEED = 0.3  # Default
ANIMATION_SPEED = 0.1  # Very fast
ANIMATION_SPEED = 0.5  # Slower
```

### Change Test Numbers

In individual scene files or `config/settings.py`:

```python
SAMPLE_NUMBERS = [27, 42, 15, 99, 100]  # Numbers to test
```

### Modify Output Resolution

Edit `main.py`:

```python
config.pixel_height = 1920    # Instagram Reel height
config.pixel_width = 1080     # Instagram Reel width
config.frame_rate = 60        # 60 FPS
config.quality = "high_quality"  # Quality setting
```

## 🛠️ Development

### Add a New Scene

1. Create file in `scenes/` folder:

```python
from manim import *
from config.settings import COLORS

class MyNewScene(Scene):
    def construct(self):
        self.camera.background_color = COLORS["dark"]
        # Your animations here
```

2. Add to `main.py`:

```python
from scenes.my_new_scene import MyNewScene

all_scenes = [
    # ... existing scenes
    ("MyScene", MyNewScene),
]
```

3. Render:

```bash
python quick_render.py my_new_scene
```

### Use Collatz Math Functions

```python
from utils.collatz_utils import (
    collatz_sequence,           # Get sequence for a number
    get_collatz_statistics,     # Get stats for multiple numbers
    normalize_sequence,         # Convert to coordinates
    get_sequence_color_map,     # Get colors based on operations
)

# Example
seq = collatz_sequence(27, max_iterations=100)
print(seq)  # [27, 82, 41, 124, 62, 31, 94, ...]
```

## 💡 Tips for Instagram Reels

1. **Aspect Ratio**: Project is already 9:16 (1080x1920) ✓
2. **Duration**: 45-50 seconds is ideal for Reels ✓
3. **No Audio**: All visual—viewers understand without sound ✓
4. **Captions**: Add these in Instagram's editor:
   - "If n is even: divide by 2"
   - "If n is odd: multiply by 3, add 1"
   - "Repeat until you reach 1"
   - "Does it ALWAYS work?"
   - "No one has proven it yet!"

5. **Music**: Add trending audio in Instagram editor for engagement

## 🔧 Rendering Options

### Quick Testing (Low Quality, Fast)
```bash
manim -pql -o output.mp4 scenes/scene_01_intro.py EnhancedIntroScene
```

### High Quality (Slow)
```bash
manim -pqh -o output.mp4 scenes/scene_01_intro.py EnhancedIntroScene
```

### Full HD (2K)
```bash
manim -pqk -o output.mp4 scenes/scene_01_intro.py EnhancedIntroScene
```

## 📊 Performance

| Quality | Time (1 scene) | File Size |
|---------|---|---|
| Low (-pql) | 30-60s | 5-10 MB |
| Medium (-pqm) | 2-5 min | 20-30 MB |
| High (-pqh) | 5-15 min | 50-100 MB |

## ❓ Troubleshooting

### Manim not found
```bash
pip install --upgrade manim
```

### FFmpeg not found
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### Video quality is poor
```bash
# Use high quality rendering
manim -pqh -o output.mp4 your_scene.py YourScene
```

### Videos not combining
```bash
# Check FFmpeg is installed
ffmpeg -version

# Render individual videos again
python render_all.py
```

## 📚 Learning Resources

- [Manim Documentation](https://docs.manim.community/)
- [Manim Community Discord](https://discord.gg/mMRrZQW)
- [Collatz Conjecture on Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)

## 📄 License

Free to use and modify for educational purposes.

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Test individual scenes: `python quick_render.py intro`
3. ✅ Render full project: `python render_all.py`
4. ✅ Edit output video in Instagram app (add music, captions)
5. ✅ Upload as Reel!

---

**Happy rendering!** 🚀✨

Questions? Check the individual scene files for detailed comments!