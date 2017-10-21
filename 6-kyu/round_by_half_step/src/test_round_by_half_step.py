"""This is the test file for round_by_half_step.py."""

import pytest

numbers = [
    (4.2, 4),
    (4.25, 4.5),
    (4.4, 4.5),
    (4.6, 4.5),
    (4.75, 5),
    (4.8, 5),
    (5.5, 5.5),
    (5.8, 6),
    (1.3, 1.5),
    (3.4, 3.5)
]


@pytest.mark.parametrize('n, result', numbers)
def test_round_by_half_step(n, result):
    """Test for round_by_half_step function."""
    from round_by_half_step import round_by_half_step
    assert round_by_half_step(n) == result
