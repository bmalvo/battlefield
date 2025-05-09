"""Task:

Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, how many 
cakes he could bake considering his recipes? Write a function cakes(), which 
takes the recipe (object) and the available ingredients (also an object) and 
returns the maximum number of cakes Pete can bake (integer). For simplicity
there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are 
simply 1 or 200). Ingredients that are not present in the objects, can be 
considered as 0.
"""

# Solution:


def cakes(recipe, available):
    """Counting how many cakes We can make"""
    many = []
    for key in recipe:
        if key not in available or recipe[key] > available[key]:
            return 0
    for key in available:
        if key in recipe:
            many.append(available[key] / recipe[key])
    return int(min(many))
