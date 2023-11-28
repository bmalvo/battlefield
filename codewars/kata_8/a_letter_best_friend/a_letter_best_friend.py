"""Given a string, return if a given letter always appears immediately before 
another given letter.

Worked Example
("he headed to the store", "h", "e") ➞ True

# All occurences of "h": ["he", "headed", "the"]
# All occurences of "h" have an "e" after it.
# Return True

('abcdee', 'e', 'e') ➞ False

# For first "e" we can get "ee"
# For second "e" we cannot have "ee"
# Return False
Examples
("i found an ounce with my hound", "o", "u") ➞ True

("we found your dynamite", "d", "y") ➞ False"""


def best_friend(txt, letter_a, letter_b):
    """check if always apear together"""
    for index, char in enumerate(txt):
        if char == letter_a:
            try:
                char2 = txt[index+1]
                if char2 != letter_b:
                    return False
            except IndexError:
                return False
    return True
