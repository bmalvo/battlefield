from skee_ball import gun_buy
import pytest


@pytest.mark.parametrize('given, expected',[((500, 40),'Buy it!'),
                                            ((100, 50), 'Try again'),
                                            ((10000, 600), 'Buy it!')])
def test_gun_buy(given, expected):
    assert gun_buy(given[0], given[1]) == expected
