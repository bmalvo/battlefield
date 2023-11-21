"""You need to calculate the sum of all the multiples of 3 or 5 below a given 
number.

Task: 
Given an integer number, output the sum of all the multiples of 3 and 5 below 
that number. 
If a number is a multiple of both, 3 and 5, it should appear in the sum only 
once.

Input Format: 
An integer.

Output Format: 
An integer, representing the sum of all the multiples of 3 and 5 below the 
given input.

Sample Input: 
10

Sample Output:
23"""


def calc_multiples(number):
    """output sum all multiples of 3 and 5 in certain range"""
    multiples_3 = [num for num in range(number) if num % 3 == 0]
    multiples_5 = [num for num in range(number) if num % 5 == 0]
    return sum(set(multiples_5 + multiples_3))
