"""Create a function that checks if a number n is divisible by two numbers 
   x AND y. All inputs are strictly positive numbers."""


def is_divisible(first, second, third):
    """Checking if n is divisible by x and y"""
    return first % second == 0 and first % third == 0
