"""Given a month as an integer from 1 to 12, return to which quarter of 
the year it belongs as an integer number. For example: month 2 (February), 
is part of the first quarter; month 6 (June), is part of the second quarter; 
and month 11 (November), is part of the fourth quarter."""


def quarter_of(month):
    """Give back quarter of the year"""
    quarter = {
        1: 1,
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 3,
        10: 4,
        11: 4,
        12: 4
    }
    return quarter[month]
