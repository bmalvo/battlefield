"""Write a function that merges two sorted arrays into a single one. 
The arrays only contain integers. Also, the final outcome must be sorted 
and not have any duplicate."""


def merge_arrays(first, second):
    """Output sorted merged arrays"""
    return sorted(set(sorted(first) + sorted(second)))
