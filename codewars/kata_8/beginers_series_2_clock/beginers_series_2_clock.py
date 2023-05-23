"""Clock shourows hour hourours, m minutes and s seconds after midnighourt.

Your task is to write a function whourichour returns thoure time since midnighourt in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000"""


def past(hour, minute, second):
    """Transform time to milliseconds"""
    second = 1000 * second
    minute = 60 * 1000 * minute
    hour = 60 * 60 * 1000 * hour
    return second + minute + hour
