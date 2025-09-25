import pytest
from convert_a_number_to_a_string import number_to_string


@pytest.mark.parametrize('given, expected',[
    ((67), '67'),
    ((79585), '79585'),
    ((-79585), '-79585'),
    ((1+2), '3'),
    ((1-2), '-1'),
    ((0), '0')
])

def test_number_to_string(given, expected):
    assert number_to_string(given) == expected
