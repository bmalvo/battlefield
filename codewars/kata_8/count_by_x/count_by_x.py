"""Create a function with two arguments that will return an array of the first (n) multiples of (x).

Assume both the given number and the number of times to count will be positive numbers greater

than 0. Return the results as an array (or list in Python, Haskell or Elixir)."""


def count_by(mul, timez):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    arr = [i*mul for i in range(1, timez+1)]
    return arr


print(count_by(2, 3))
