"""This is the test file for valid_parentheses.py."""

import pytest

parameters = [
    ("  (", False),
    (")test", False),
    ("", True),
    ("hi())(", False),
    ("hi(hi)()", True),
    ("()()()(", False),
    (")()()()()()", False),
    ("()()()()()(())", True),
    ("()()()((()))()(())()", True)
]


@pytest.mark.parametrize('n, result', parameters)
def test_valid_parentheses(n, result):
    """Test for valid_parentheses function."""
    from valid_parentheses import valid_parentheses
    assert valid_parentheses(n) == result
