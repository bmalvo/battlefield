"""This is: Format a string of names like 'Bart, Lisa & Maggie'"""
# Task:
# Format a string of names like 'Bart, Lisa & Maggie'.
# Examples:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'coverage report -m
#
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

# Solution:

def namelist(names):
    """Made a list of names"""
    names = [x['name'] for x in names]
    if len(names) == 0:
        names = ' '
        return names
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        names.insert(-1, '&')
        names = ' '.join(names)
        return names
    if len(names) == 3:
        names.insert(-1, '&')
        names_first = [names[0], names[1]]
        names_second = [names[2], names[3]]
        names_first = ', '.join(names_first)
        names_second = ' '.join(names_second)
        names = names_first + ' ' + names_second
        return names
    if len(names) > 3:
        names.insert(-1, '&')
        names_first = names[:-2]
        names_second = names[-2:]
        names_first = ', '.join(names_first)
        names_second = ' '.join(names_second)
        names = names_first + ' ' + names_second
        return names
    return None


# Best solution from site:

# def namelist1(names):
#     """Make a list of names"""
#     return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ", 1)[::-1]
#
#
# namelist1(names_3)
