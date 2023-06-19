"""Given a string, you have to return a string
 in which each character (case-sensitive) is repeated once."""


def double_char(text):
    """return string with
    doubled charts"""
    result = ''
    for char in text:
        result += char * 2
    return result
