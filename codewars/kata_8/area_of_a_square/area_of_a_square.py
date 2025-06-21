"""Complete the function that calculates the area of the red square 
(file red_square.png in this folder), when the  length of the circular arc A 
is given as the input. Return the result rounded 
to two decimals.
Note: use the π value provided in your language 
(Math::PI, M_PI, math.pi, etc)"""

from math import pi


def square_area(circular_arc):
    """calculate area of a square"""

    r = (4 * circular_arc) / (2 * pi)

    return round(r * r, 2)
