from grasshooper_check_for_factor import check_for_factor
import pytest


@pytest.mark.parametrize('given, expected',
                         [((9, 2), False), ((653, 7), False), ((24617, 3), False),((6,2), True),((391, 17), True)])
def test_check_for_factor(given, expected):
    assert check_for_factor(given[0], given[1]) == expected
