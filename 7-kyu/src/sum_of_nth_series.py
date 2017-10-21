"""
Kata: Sum of Nth Term in Series.

Best Practice Solution:

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Return the nth term sum of the series 1 + 1/4 + 1/7 + ..."""
    sum = 0
    denominator = 1
    for i in range(n):
        sum += 1.0 / denominator
        denominator += 3
    return '%.2f' % sum
