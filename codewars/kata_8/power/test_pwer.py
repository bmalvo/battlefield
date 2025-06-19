import pytest
from power import number_to_pwr


@pytest.mark.parametrize('given, expected', [
    ((1,1), 1),
    ((3, 2), 9),
    ((2, 3), 8),
    ((10, 6), 1000000),
    ((4, 2), 16),
    ((10, 4), 10000),
    ((10, 0), 1)
    ])
def test_number_to_pwr(given, expected):
    assert number_to_pwr(given[0], given[1]) == expected

# assert number_to_pwr(1,1) == 1