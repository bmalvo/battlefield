"""Implement String#digit?, which should return true if given object is 
a digit (0-9), false otherwise."""


def is_digit(num):
    """check if input is a digit"""
    digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    return num in digits
