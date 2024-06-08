""" Task:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Finish the solution so that it returns the sum of all the
multiples of 3 or 5 below the number passed in. Additionally, if the number is negative,
return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
"""
# Solution:


def solution(number):
    """Getting list of numbers in range multiplied by
    3 or 5 and sum this list"""
    lst = list(range(number))
    lst2 = set()
    for num in lst:
        if num % 3 == 0:
            lst2.add(num)
        if num % 5 == 0:
            lst2.add(num)
    return sum(lst2)


print(solution(16))
