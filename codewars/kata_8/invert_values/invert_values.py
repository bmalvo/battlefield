"""Given a set of numbers, return the additive inverse of each. 
Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []"""


def invert(lst):
    """return the additive inverse of each numbers"""
    return [abs(x) if x < 0 else x - (2 * x) for x in lst]
