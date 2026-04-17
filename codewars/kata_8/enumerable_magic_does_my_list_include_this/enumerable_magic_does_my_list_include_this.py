"""Create a method that accepts a list and an item, and returns true if the 
item belongs to the list, otherwise false."""


def include(arr: list, item: any) -> bool:
    """checks if an item belongs to list"""
    return arr.count(item) > 0
