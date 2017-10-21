"""This is the test file for nth_even.py."""

import pytest

numbers = [
    (1, 0), (2, 2), (3, 4), (100, 198), (1298734, 2597466), (24, 46),
    (20, 38), (5, 8), (21, 40), (13, 24), (15, 28)
]


@pytest.mark.parametrize('n, result', numbers)
def test_nth_even(n, result):
    """Test for nth_even function."""
    from nth_even import nth_even
    assert nth_even(n) == result
