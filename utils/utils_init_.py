# Utilities package for Collatz Conjecture Manim project
from .collatz_utils import (
    collatz_sequence,
    get_collatz_statistics,
    normalize_sequence,
    get_sequence_color_map,
    is_interesting_number,
    get_tree_structure
)

__all__ = [
    'collatz_sequence',
    'get_collatz_statistics',
    'normalize_sequence',
    'get_sequence_color_map',
    'is_interesting_number',
    'get_tree_structure'
]