"""
Kata: Round by 0.5.

Best Practice Solution:

def solution(n):
    return round(2 * n) / 2
"""


def round_by_half_step(n):
    """Return the number rounded to the nearest 0.5."""
    import math
    lower = math.floor(n)
    if n - lower < 0.25:
        return lower
    elif n - lower < 0.5 or n - lower < 0.75:
        return lower + 0.5
    else:
        return lower + 1
