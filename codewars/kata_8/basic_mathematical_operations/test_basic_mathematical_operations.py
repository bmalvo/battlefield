import pytest
from basic_mathematical_operations import basic_op


@pytest.mark.parametrize('given, expected', [

    (('+', 4, 7), 11),
    (('-', 15, 18), -3),
    (('*', 5, 5), 25),
    (('/', 49, 7), 7)
])

def test_basic_op(given, expected):
    operator, value1, value2 = given
    assert basic_op(operator, value1, value2) == expected