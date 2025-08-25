import pytest
from simple_change_machine import change_me


@pytest.mark.parametrize('given, expected', [(("£1"), "20p 20p 20p 20p 20p"),
                                             (("Money"), "Money")])
def test_change_me(given, expected):
    assert change_me(given) == expected
