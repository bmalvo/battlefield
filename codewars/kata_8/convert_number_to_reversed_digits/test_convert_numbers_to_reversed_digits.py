from convert_number_to_reversed_digits import digitize
import pytest


@pytest.mark.parametrize('given, expected', [(35231, [1, 3, 2, 5, 3]), 
                            (0, [0]), (23582357, [7, 5, 3, 2, 8, 5, 3, 2]), (984764738, [8, 3, 7, 4, 6, 7, 4, 8, 9]), (45762893920, [0, 2, 9, 3, 9, 8, 2, 6, 7, 5, 4])])
def test_digitize(given, expected):
    assert digitize(given) == expected
