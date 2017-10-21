"""This is the test file for find_the_odd_int.py."""

import pytest

numbers = [
    ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
    ([1, 1, 1, 2], 1),
    ([2, 2, 3, 3, 3, 4], 3),
    ([3, 3, 1, 3, 1, 3, 1], 1),
    ([22, 2, 22, 2, 22, 1, 1], 22)
]


@pytest.mark.parametrize('n, result', numbers)
def test_find_the_odd_int(n, result):
    """Test for nth_even function."""
    from find_the_odd_int import find_the_odd_int
    assert find_the_odd_int(n) == result
