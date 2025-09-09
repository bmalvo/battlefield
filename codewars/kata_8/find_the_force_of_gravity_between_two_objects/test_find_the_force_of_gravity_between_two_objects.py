import pytest
from find_the_force_of_gravity_between_two_objects import solution


@pytest.mark.parametrize('given, expected', [
    (([1000, 1000, 100], ["g", "kg", "m"]), 6.67e-12),
    (([1000, 1000, 100], ["kg", "kg", "m"]), 6.667e-9),
    (([1000, 1000, 100], ["kg", "kg", "cm"]), 0.0000667)
                                            ])

def test_solution(given, expected):
    arr_val, arr_unit = given
    assert solution(arr_val, arr_unit) == expected
