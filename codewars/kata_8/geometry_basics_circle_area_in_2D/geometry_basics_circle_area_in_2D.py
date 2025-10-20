"""This series of katas will introduce you to basics of doing geometry with 
computers.

Write the function circleArea/CircleArea which takes in a Circle object and 
calculates the area of that circle."""

from math import pi

# The Circle class can be seen below:

class Circle:
    """class Circle"""
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


# And the Point class can be seen below:

class Point:
    """class Point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


def circle_area(circle):
    """Count circle area"""
    return pi * circle.radius ** 2
