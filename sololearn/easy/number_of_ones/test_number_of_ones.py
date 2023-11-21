from number_of_ones import ones_counter
import pytest


@pytest.mark.parametrize('given, expected',[(9, 2), (99, 4), (79, 5)])
def test_ones_counter(given, expected):
    assert ones_counter(given) == expected
