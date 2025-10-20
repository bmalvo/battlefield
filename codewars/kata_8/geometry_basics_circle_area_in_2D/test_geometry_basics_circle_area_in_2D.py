import pytest
from geometry_basics_circle_area_in_2D import Circle, circle_area


@pytest.mark.parametrize('given, expected', [
    (Circle(1, 30), 2827.4333882308138),
    (Circle(1, 30), 2827.4333882308138),
    (Circle(1, 0), 0.0),
    (Circle(1, 12.5), 490.8738521234052),
])

def test_circle_area(given, expected):
    assert circle_area(given) == expected