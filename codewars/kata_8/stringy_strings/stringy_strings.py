"""write me a function stringy that takes a size and returns a string 
of alternating 1s and 0s.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers."""


def stringy(size):
    """return ones and zeros of proper size"""
    res_size =  [ i + 1 for i in range(size)]
    res = ['1' if res_size.index(num) % 2 == 0 else '0' for num in res_size]
    return "".join(res)
