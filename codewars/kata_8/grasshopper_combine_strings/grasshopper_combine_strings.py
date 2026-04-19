"""
Create a function named combineNames/combine_names/CombineNames that 
accepts two parameters (first and last name). The function should return 
the full name.

Example:

With "James" as the first name and "Stevens" as the last name should return 
"James Stevens" 
"""


def combine_names(first_name: str, last_name: str) -> str:
    """combine names"""
    return f'{first_name} {last_name}'
