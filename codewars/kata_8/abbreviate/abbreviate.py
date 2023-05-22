"""DESCRIPTION:
Write a function to convert a name into initials.

This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F"""


def abbrev_name(name):
    """return initials"""
    initials = name.title().split(" ")
    return f'{initials[0][0]}.{initials[1][0]}'
