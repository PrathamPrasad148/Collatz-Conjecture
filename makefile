.PHONY: install setup clean test render-all render-intro render-seq render-traj quick help

help:
	@echo "Collatz Conjecture Manim Project"
	@echo "================================="
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install       Install all dependencies"
	@echo "  setup         Create necessary directories"
	@echo "  test          Test a quick render (intro scene)"
	@echo "  render-intro  Render introduction scene"
	@echo "  render-seq    Render sequence scene"
	@echo "  render-traj   Render trajectory scene"
	@echo "  render-all    Render all scenes and combine"
	@echo "  clean         Clean output directories"
	@echo "  help          Show this help message"
	@echo ""

install:
	@echo "📦 Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "✅ Python packages installed"
	@echo ""
	@echo "📦 Installing FFmpeg..."
	@echo "   On Ubuntu/Debian: sudo apt-get install ffmpeg"
	@echo "   On macOS: brew install ffmpeg"
	@echo "   On Windows: Download from https://ffmpeg.org/download.html"

setup:
	@echo "📁 Creating directories..."
	mkdir -p output
	mkdir -p media
	@echo "✅ Directories created"

test: setup
	@echo "🧪 Testing quick render..."
	python quick_render.py intro

render-intro: setup
	@echo "🎬 Rendering intro scene..."
	python quick_render.py intro

render-seq: setup
	@echo "🎬 Rendering sequence scene..."
	python quick_render.py sequence

render-traj: setup
	@echo "🎬 Rendering trajectory scene..."
	python quick_render.py trajectory

render-all: setup
	@echo "🎬 Rendering all scenes..."
	python render_all.py

clean:
	@echo "🧹 Cleaning output directories..."
	rm -rf media/
	rm -rf output/*.mp4
	@echo "✅ Cleaned"

show-config:
	@echo "Current Configuration:"
	@grep -E "^[A-Z_]+ =" config/settings.py

.DEFAULT_GOAL := help