"""You meet a group of aliens, and their language is just like English except
that they say every word backwards. How will you learn to communicate with 
them?
Take a word in English that you would like to say, and tun it into language
that these aliens will understand.

Input:
A string of a word in English.

Output:
A string of the reversed word that represents the original word translated 
into alien language."""


def alien_translator(eng_word:str):
    """Translate word"""
    return eng_word[::-1]
