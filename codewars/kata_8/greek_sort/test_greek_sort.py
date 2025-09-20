import pytest
from greek_sort import greek_comparator


@pytest.mark.parametrize('given, expected', [
    (('alpha', 'beta'), -1),
    (('psi', 'psi'), 0),
    (('upsilon', 'rho'), 1)
])

def test_greek_comparator(given, expected):
    lhs, rhs = given
    assert greek_comparator(lhs, rhs) == expected
