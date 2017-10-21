"""This is the test file for even_or_odd.py."""

import pytest

numbers = [
    (2, "Even"), (0, "Even"), (7, "Odd"), (1, "Odd"), (10, "Even"),
    (20, "Even"), (10, "Even"), (21, "Odd"), (13, "Odd"), (-1, "Odd")
]


@pytest.mark.parametrize('n, result', numbers)
def test_even_or_odd(n, result):
    """Test for even_or_odd function."""
    from even_or_odd import even_or_odd
    assert even_or_odd(n) == result
