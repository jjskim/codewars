"""
Kata: Valid Parentheses.

Best Practice Solution:

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
"""


def valid_parentheses(string):
    """Return if string has valid parentheses."""
    open_count = 0
    closing_count = 0
    for i in range(len(string)):
        if string[i] == "(":
            open_count += 1
        elif string[i] == ")":
            closing_count += 1
        if closing_count > open_count:
            return False
    return open_count == closing_count
