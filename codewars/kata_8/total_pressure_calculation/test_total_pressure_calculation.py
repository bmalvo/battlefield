import pytest
from total_pressure_calculation import solution


@pytest.mark.parametrize('given, expected', [
    ((44, 30, 3, 2, 5, 50), 0.7146511212121212),
    ((60, 20, 10, 30, 10, 100), 5.099716666666667)])
def test_solution(given, expected):
    assert solution(
        given[0],given[1],given[2],given[3],given[4],given[5]) == round(expected,15)