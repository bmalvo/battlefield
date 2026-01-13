"""Make a function that returns the value multiplied by 50 and increased by 6. 
If the value entered is a string it should return "Error"."""


def problem(a: int) -> int:
    """multiply argument 50 times and increase it by 6"""
    return round(a * 50 + 6) if isinstance(a, (int, float))  else 'Error'
