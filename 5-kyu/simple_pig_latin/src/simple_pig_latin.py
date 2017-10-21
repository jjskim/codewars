"""
Kata: Simple Pig Latin.

Best Practice Solution:

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""


def pig_it(text):
    """Return the string translated to Pig Latin."""
    words = text.split()
    for i in range(len(words)):
        pig_latin_word = words[i][1:]
        word_ending = words[i][0]
        if words[i].isalpha():
            word_ending += "ay"
        pig_latin_word += word_ending
        words[i] = pig_latin_word
    return " ".join(words)
