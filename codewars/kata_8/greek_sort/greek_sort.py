"""Write a comparator for a list of phonetic words for the letters of the 
greek alphabet.

A comparator is:

a custom comparison function of two arguments (iterable elements) which should 
return a negative, zero or positive number depending on whether the first 
argument is considered smaller than, equal to, or larger than the second 
argument"""


greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    """compare indexes of two letters in greek alphabet"""
    lhs = greek_alphabet.index(lhs)
    rhs = greek_alphabet.index(rhs)
    return [1, -1][lhs < rhs] if lhs != rhs else 0
