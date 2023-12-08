"""Task:
Write a function that accepts two integers and returns the remainder of 
dividing the larger value by the smaller value.

Division by zero should return an empty value.

result - division by zero (refer to the specifications on how to handle this 
in your language)"""


def remainder(nam_a, num_b):
    """output the remainder"""
    try:
        res = max(nam_a,num_b) % min(nam_a,num_b)
    except ZeroDivisionError:
        res = None
    return res
