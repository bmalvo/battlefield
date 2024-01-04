"""Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son 
(or in how many years he will be twice as old). The answer is always greater 
or equal to 0, no matter if it was in the past or it is in the future."""


def twice_as_old(dad_years_old, son_years_old):
    """Check how many years ago or will be in future
    father doubled years_old of son"""
    years_old = (dad_years_old, son_years_old*2)
    return max(years_old) - min(years_old)
