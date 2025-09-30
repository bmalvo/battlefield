"""Given a non-negative integer b, write a function which returns an integer 
d such that the binary representation of b is the same as the decimal 
representation of d."""


def to_binary(n:int) -> str:
    "Output binary representation of number n"
    return int(bin(n)[2:])
