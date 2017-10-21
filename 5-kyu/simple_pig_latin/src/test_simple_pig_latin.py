"""This is the test file for simple_pig_latin.py."""

import pytest

numbers = [
    ("Pig latin is cool", "igPay atinlay siay oolcay"),
    ("This is my string", "hisTay siay ymay tringsay"),
    ("What is life", "hatWay siay ifelay"),
    ("Why you do this to me", "hyWay ouyay oday histay otay emay"),
    ("Codefellows why", "odefellowsCay hyway"),
    ("My weekend", "yMay eekendway"),
    ("Do you guys even read this", "oDay ouyay uysgay veneay eadray histay")
]


@pytest.mark.parametrize('n, result', numbers)
def test_simple_pig_latin(n, result):
    """Test for pig_it function."""
    from simple_pig_latin import pig_it
    assert pig_it(n) == result
