from popsicles import pops_even_dispense
import pytest

@pytest.mark.parametrize('given, expected',[((10, 20), 'give away'),
                                            ((3, 9), 'give away'),
                                            ((5, 15), 'give away')])
def test_pops_even_dispense_positive(given, expected):
    assert pops_even_dispense(given[0], given[1]) == expected

@pytest.mark.parametrize('given, expected',[((2, 5), 'eat them yourself'),
                                            ((3, 10), 'eat them yourself'),
                                            ((5, 22), 'eat them yourself')])
def test_pops_even_dispense_negative(given, expected):
    assert pops_even_dispense(given[0], given[1]) == expected
