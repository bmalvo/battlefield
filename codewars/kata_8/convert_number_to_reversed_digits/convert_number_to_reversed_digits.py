"""Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits
of this number within an array in reverse order."""


def digitize(num):
    """result is reversed array of number digits"""
    num = str(num)
    num = num[::-1]
    arr = []
    for i in range(len(str(num))):
        arr.append(int(num[i]))
    return arr
