"""Task:
Count the number of ones in the binary representation of a given integer.

Input Format:
An integer.

Output Format: 
An integer representing the count of ones in the binary representation of 
the input.

Sample Input:
9

Sample Output:
2"""


def ones_counter(integer):
    """counts amount of ones in binary representation of integer"""
    return len([x for x in ''.join(str(bin(integer))) if x =='1'])
