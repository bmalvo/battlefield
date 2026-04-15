import pytest
from simple_fun_seats_in_theater import seats_in_theater


@pytest.mark.parametrize('given, expected',[
    ((16, 11, 5, 3), 96),
    ((1, 1, 1, 1), 0),
    ((13, 6, 8, 3), 18),
    ((60, 100, 60, 1), 99),
    ((1000, 1000, 1000, 1000), 0)
])

def test_seats_in_theater(given, expected):
    tot_cols, tot_rows, col, row = given[0], given[1], given[2], given[3]
    assert seats_in_theater(tot_cols, tot_rows, col, row) == expected
