import pytest
from will_you_make_it import zero_fuel


@pytest.mark.parametrize('given, expected', [((50, 25, 2), True), ((100, 50, 1), False)])
def test_zero_fuel(given, expected):
    assert zero_fuel(given[0], given[1], given[2]) == expected
