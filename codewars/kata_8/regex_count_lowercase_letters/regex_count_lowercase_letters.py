"""Your task is simply to count the total number of lowercase letters in 
a string."""


def lowercase_count(strng: str) -> int:
    """count lowercase letter"""
    lower_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                      'o','p','r','s','t','u','v','w','q', 'x','y','z']
    counter = 0
    for letter in strng:
        if letter in lower_alphabet:
            counter += 1
    return counter
