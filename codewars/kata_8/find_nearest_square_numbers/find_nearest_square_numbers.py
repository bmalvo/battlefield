"""Your task is to find the nearest square number, nearest_sq(n), of a positive integer n."""
import math


def nearest_sq(num):
    """Returns nearest sqruared number arg n"""
    sqr = math.isqrt(num)
    sqr_next = sqr + 1
    if (num - (sqr*sqr)) < ((sqr_next*sqr_next) - num):
        return sqr * sqr
    return sqr_next * sqr_next
