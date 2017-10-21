"""
Kata: Even or Odd.

Best Practice Solution:

def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'
"""


def even_or_odd(number):
    """Return if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
