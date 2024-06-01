"""Write a function which calculates the average of the numbers in a given list.

Empty arrays should return 0."""


def find_average(numbers):
    """Output average from given list"""
    return sum(numbers)/len(numbers) if numbers else 0
