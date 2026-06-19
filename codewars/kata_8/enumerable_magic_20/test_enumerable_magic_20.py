from enumerable_magic_20 import each_cons
import pytest


lst = [3, 5, 8, 13]

@pytest.mark.parametrize('given, expected', [
         
    ((lst, 1), [[3], [5], [8], [13]]),    
    ((lst, 2), [[3, 5], [5, 8], [8, 13]]),
    ((lst, 3), [[3, 5, 8], [5, 8, 13]]),
    (([],3), [])
])

def test_each_cons(given, expected):
    assert each_cons(given[0], given[1]) == expected
