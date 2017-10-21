"""
Kata: Find the odd int.

Best Practice Solution:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""


def find_the_odd_int(seq):
    """Return the number in list that appears an odd number of times."""
    num_appearances = {}
    for num in seq:
        if num not in num_appearances.keys():
            num_appearances[num] = 1
        else:
            num_appearances[num] += 1
    for key in num_appearances.keys():
        if num_appearances[key] % 2 == 1:
            return key
