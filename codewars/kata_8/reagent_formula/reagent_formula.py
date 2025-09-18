"""Now we will confect a reagent. There are eight materials to choose from, 
numbered 1,2,..., 8 respectively.

We know the rules of confect:

material1 and material2 cannot be selected at the same time
material3 and material4 cannot be selected at the same time
material5 and material6 must be selected at the same time
material7 or  material8 must be selected(at least one, or both)
Task
You are given a integer array formula. Array contains only digits 1-8 that 
represents material 1-8. Your task is to determine if the formula is valid. 
Returns true if it's valid, false otherwise.

Example
For formula = [1,3,7], The output should be true.

For formula = [7,1,2,3], The output should be false.

For formula = [1,3,5,7], The output should be false.

For formula = [1,5,6,7,3], The output should be true.

For formula = [5,6,7], The output should be true.

For formula = [5,6,7,8], The output should be true.

For formula = [6,7,8], The output should be false.

For formula = [7,8], The output should be true.

Note
All inputs are valid. Array contains at least 1 digit. Each digit appears at 
most once.

Happy Coding ^_^ """


def is_valid(formula):
    """checking if the formula obey the rules"""
    rule1 = not ((1 in formula) and (2 in formula))
    rule2 = not ((3 in formula) and (4 in formula))
    rule3 = (5 in formula and (6 in formula)) or (5 not in formula) and (6 not in formula)
    rule4 = 7 in formula or 8 in formula
    return rule1 and rule2 and rule3 and rule4
