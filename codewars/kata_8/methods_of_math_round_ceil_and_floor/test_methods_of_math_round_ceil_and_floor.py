import pytest
from methods_of_math_round_ceil_and_floor import round_it

def test_les_number_before_point():
    assert round_it(3.45) == 4

def test_more_number_before_point():
    assert round_it(34.5) == 34

def test_equal_number_among_point():
    assert round_it(34.56) == 35
