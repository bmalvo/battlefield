"""Task:

Welcome.
In this kata you are required to, given a string, replace every letter with 
its position in the alphabet. If anything in the text isn't a letter, ignore 
it and don't return it.
"a" = 1, "b" = 2, etc."""

# Solution:

alphabet = {chr(i+96): i for i in range(1, 27)}


def alphabet_position(text):
    """Give You position in alphabet any character in string"""
    text = text.lower()
    text = list(text)
    new_text = []
    for char in text:
        if char in alphabet:
            new_text.append(alphabet[char])
    result = " ".join(str(x) for x in new_text)
    return result
