"""You are the owner of a box making company.

Your company can produce any equal sided polygon box, but plenty of your 
customers want to transport circular objects in these boxes. Circles are 
a very common shape in the consumer industry. Tin cans, glasses, tyres 
and CD's are a few examples of these.

As a result you decide to add this information on your boxes: The largest 
(diameter) circular object that can fit into a given box."""
import math


def circle_diameter(sides, side_length):
    """Calculate the largest diameter using the formula"""
    if sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")

    diameter = side_length * (1 / math.tan(math.pi / sides))

    return round(diameter, 3)
