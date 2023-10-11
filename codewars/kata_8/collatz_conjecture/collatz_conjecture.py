"""The Collatz conjecture (also known as 3n+1 conjecture) is a conjecture that 
applying the following algorithm to any number we will always eventually 
reach one:

[This is writen in pseudocode]
if(number is even) number = number / 2
if(number is odd) number = 3*number + 1

Your task is to make a function hotpo that takes a positive n as input and 
returns the number of times you need to perform this algorithm to get n = 1.

example: hotpo(6) returns 8
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1"""

def hotpo(numb):
    """Count Collatz Conjecture"""
    res = 0
    while numb != 1:
        if numb % 2 == 0:
            numb = numb/2
            res += 1
            if numb ==1:
                break
        if numb % 2 != 0:
            numb = 3 * numb + 1
            res += 1
            if numb ==1:
                break
    return res
