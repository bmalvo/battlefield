"""Given an array of 3 non-negative integers a, b and c, 
determine if they form a pythagorean triple.

A pythagorean triple is formed when:

c2 = a2 + b2
where c is the largest value of a, b, c.

For example: a = 3, b = 4, c = 5 forms a pythagorean triple, 
because 5 ** 2 = 3 ** 2 + 4 ** 2

Return Values
1 if a, b and c form a pythagorean triple
0 if a, b and c do not form a pythagorean triple
For Python: return True or False
For JavaScript: return true or false"""


def pythagorean_triple(integers):
    """determine if the integers form a pythagorean triple."""
    sides = sorted(integers)
    return sides[-1] ** 2 == (sides[-2] ** 2) + (sides[-3] ** 2)
