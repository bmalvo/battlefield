from izzy_the_iguana import snack_points_counter
import pytest


@pytest.mark.parametrize('given, expected', [
    ('Mango Cheeseburger Carrot', 'Come on Down!')])
def test_snack_point_counter(given, expected):
    assert snack_points_counter(given) == expected
