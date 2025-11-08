"""Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty 
( zero length )."""


def solution(a, b):
    """pack given str in order: short->long->short"""
    return [f'{a}{b}{a}', f'{b}{a}{b}'][len(a) > len(b)]
