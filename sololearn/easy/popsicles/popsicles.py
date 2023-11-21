"""You have a box of popsicles and you want to give them all away to a group
of brothers and sisters. If you have enough left in the box to give them each
an even amount you should go for it! If not, they will fight over them, and 
you should eat them yourself later.

Given the number of siblings that you are giving popsicles to, determine if 
you can give them each an even amount or if you shouldn't mention the 
popsicles at all.

Input: 
Two integer values, the first one represents the number of siblings, and the 
second one represents the number of popsicles that you have left in the box.

Output:
A string that says 'give away' if you are giving them away, or 'eat them 
yourself' if you will be eating them yourself"""


def pops_even_dispense(siblings:int, popsicles:int):
    """Check can you split up pops even or not"""
    if popsicles % siblings == 0:
        res = 'give away'
    else:
        res = 'eat them yourself'
    return res
