"""Create a function that takes an integer as an argument and returns "Even" for even numbers
or "Odd" for odd numbers."""


def even_or_odd(number):
    """Check if number is Even or Odd"""
    if number % 2 == 0:
        res = 'Even'
    else:
        res = 'Odd'
    return res

# Best from site:
# def even_or_odd(number):
#     return 'Odd' if number % 2 else 'Even'
