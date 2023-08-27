"""Write a function that checks if a given string (case insensitive)
   is a palindrome."""


def is_palindrome(string):
    """check if string is a palindrome"""
    return string.lower() == string[::-1].lower()
