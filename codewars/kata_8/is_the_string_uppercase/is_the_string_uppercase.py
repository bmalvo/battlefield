"""Task:
Create a method to see whether the string is ALL CAPS."""


def is_uppercase(inp: str):
    """Check if the string is all uppercase"""
    for i in inp:
        if i.islower():
            return False
    return True
