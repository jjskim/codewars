"""This is the test file for valid_parentheses.py."""

import pytest

parameters = [
    (1, "1.00"),
    (2, "1.25"),
    (3, "1.39"),
    (4, "1.49"),
    (5, "1.57"),
    (6, "1.63"),
    (7, "1.68")
]


@pytest.mark.parametrize('n, result', parameters)
def test_series_sum(n, result):
    """Test for series_sum function."""
    from sum_of_nth_series import series_sum
    assert series_sum(n) == result
