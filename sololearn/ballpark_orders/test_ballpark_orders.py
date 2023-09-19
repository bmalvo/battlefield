import pytest
from ballpark_orders import cost


@pytest.mark.parametrize('given, expected', [('Coke', 5.35),('Pizza', 6.42),
                                ('Nachos Pizza Cheeseburger Water', 27.82),
                                ('Cheeseburger Cheeseburger Pizza Oak',33.17),
                                ('Water Water Water Water', 17.12),
                                ('Cheeseburger Cheeseburger Coke Water', 31.03)])
def test_cost(given, expected):
    assert cost(given) == expected
