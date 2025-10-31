import pytest
from calculate_bmi import bmi


@pytest.mark.parametrize('given, expected', [
    ((50, 1.80), "Underweight",),
    ((80, 1.80), "Normal",),
    ((90, 1.80), "Overweight",),
    ((100, 1.80), "Obese",)
])

def test_bmi(given, expected):
    weight, height = given
    assert bmi(weight, height) == expected
