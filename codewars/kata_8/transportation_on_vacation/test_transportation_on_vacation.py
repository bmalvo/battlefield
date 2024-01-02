from transportation_on_vacation import rental_car_cost
import pytest


@pytest.mark.parametrize('given, expected', [(1, 40), (4, 140), (7, 230), (8, 270)])
def test_rental_car_cost(given, expected):
    assert rental_car_cost(given) == expected
