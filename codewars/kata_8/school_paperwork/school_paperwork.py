"""Your classmates asked you to copy some paperwork for them. You know 
that there are 'n'
classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. 
If n < 0 or m < 0 return 0."""


def paperwork(classmates, pages):
    """Return how many pages are need to copy paperwork"""
    return  pages * classmates if classmates > 0 and pages > 0 else 0
