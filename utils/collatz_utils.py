import numpy as np
from typing import List, Tuple

def collatz_sequence(n: int, max_iterations: int = 500) -> List[int]:
    """
    Generate Collatz sequence for a given number.
    
    Rules:
    - If n is even: n = n / 2
    - If n is odd: n = 3n + 1
    - Stop when reaching 1
    """
    sequence = [n]
    iterations = 0
    
    while n != 1 and iterations < max_iterations:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        iterations += 1
    
    return sequence


def get_collatz_statistics(numbers: List[int]) -> dict:
    """Get statistics about Collatz sequences for multiple numbers."""
    stats = {
        "sequences": {},
        "max_length": 0,
        "max_value": 0,
        "avg_length": 0
    }
    
    total_length = 0
    
    for num in numbers:
        seq = collatz_sequence(num)
        stats["sequences"][num] = seq
        stats["max_length"] = max(stats["max_length"], len(seq))
        stats["max_value"] = max(stats["max_value"], max(seq))
        total_length += len(seq)
    
    stats["avg_length"] = total_length / len(numbers) if numbers else 0
    
    return stats


def normalize_sequence(sequence: List[int], target_height: float = 8) -> List[Tuple[float, float]]:
    """
    Normalize sequence to coordinates for plotting.
    Returns list of (x, y) coordinates.
    """
    if not sequence:
        return []
    
    max_val = max(sequence)
    coordinates = []
    
    for i, val in enumerate(sequence):
        x = i * 0.3  # Horizontal spacing
        y = (val / max_val) * target_height  # Normalized height
        coordinates.append((x, y))
    
    return coordinates


def get_sequence_color_map(sequence: List[int]) -> List[str]:
    """
    Get color for each step in sequence based on operation.
    Red for odd (3n+1), Blue for even (n/2)
    """
    colors = []
    for i in range(len(sequence) - 1):
        current = sequence[i]
        if current % 2 == 0:
            colors.append("#4ECDC4")  # Teal for divide
        else:
            colors.append("#FF6B6B")  # Red for multiply
    
    colors.append("#FFE66D")  # Yellow for final 1
    return colors


def is_interesting_number(n: int) -> bool:
    """Determine if a number produces an interesting Collatz sequence."""
    seq = collatz_sequence(n)
    
    # Interesting if:
    # - Long sequence
    # - High peak value
    # - Multiple operations
    conditions = [
        len(seq) > 20,
        max(seq) > n * 10,
        len(seq) > 15
    ]
    
    return sum(conditions) >= 2


def get_tree_structure(n: int, depth: int = 3) -> dict:
    """
    Build tree structure of Collatz sequence.
    Useful for network visualization.
    """
    seq = collatz_sequence(n, max_iterations=depth)
    tree = {"value": seq[0], "children": []}
    
    current = tree
    for val in seq[1:]:
        child = {"value": val, "children": []}
        current["children"].append(child)
        current = child
    
    return tree