import pytest
from if_else_and_tenary_operator import sale_hotdogs


@pytest.mark.parametrize('given, expected',
                         [(0, 0), (1, 100), (2, 200), (3, 300), (4, 400), 
                          (5, 475), (9, 855), (10, 900), (11, 990), 
                          (100, 9000)])
def test_sale_hotdogs(given, expected):
    assert sale_hotdogs(given) == expected
