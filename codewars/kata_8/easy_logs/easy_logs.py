"""Given a logarithm base X and two values A and B, return a sum of logratihms
with the base X: 
log X A + log X B """

import math


def logs(x, a, b):
    """return log X A + log X B """
    ans = math.log(a, x) + math.log(b, x)
    return ans
