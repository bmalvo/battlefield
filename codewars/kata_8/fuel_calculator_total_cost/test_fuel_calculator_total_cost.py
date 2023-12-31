import pytest
from fuel_calculator_total_cost import fuel_price


@pytest.mark.parametrize('litres, price, cost',[(10, 21.5, 212.5),
                                                (40, 10, 390),
                                                (15, 5.83, 83.7)])
def test_fuel_price(litres, price, cost):
    assert fuel_price(litres, price) == cost
