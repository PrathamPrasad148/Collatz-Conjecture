# Windows startup

## Easiest way
Double-click **START_PROJECT.bat**.

The first run creates a local `.venv` and installs the Python dependencies. After that it gives you a menu:

1. **Quick preview** — renders the complete reel at 540×960 / 30 FPS.
2. **Final HD reel** — renders the complete reel at 1080×1920 / 60 FPS.
3. **One scene** — useful for testing a scene before doing the full render.
4. **Open project folder**.
5. **Setup / repair dependencies**.

The final video is written to `output\collatz_reel_final_hd.mp4`.

## FFmpeg
FFmpeg is required to combine the individual scenes. It must be installed and available as `ffmpeg` in PATH. If it is missing, `SETUP.bat` will tell you.

## Important fixes made
- Removed the hard-coded Linux path `/home/claude/collatz_reel` from the scene files.
- The renderer now invokes Manim through the virtual environment's Python, so Windows does not depend on a global `manim` command.
- The old renderer expected a `1080p60` output even when using Manim low-quality mode; this has been corrected.
- All 8 advertised scenes are now rendered and combined.
- The final combination re-encodes to a compatible H.264 MP4 instead of relying on `-c copy`, which can fail when scene encodings differ.
- Dependencies were updated from obsolete pinned versions to a modern Manim-compatible range.
