"""The goal is to create a function of two inputs number and power, that 
"raises" the number up to power (ie multiplies number by itself power times).

Examples
number_to_pwr(3, 2)  # -> 9 ( = 3 * 3 )
number_to_pwr(2, 3)  # -> 8 ( = 2 * 2 * 2 )
number_to_pwr(10, 6) # -> 1000000

Note: math.pow and some others math functions are disabled on final tests."""


def number_to_pwr(number, p):
    """count number raised to proper power"""
    if p == 0:
        return 1
    while p > 0:
        number = number * number
        p -= p
    return number

print(number_to_pwr(2, 9))
