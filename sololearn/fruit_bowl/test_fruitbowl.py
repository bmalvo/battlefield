from fruitbowl import pie_counter
import pytest


@pytest.mark.parametrize('given, expected',[(4, 0), (12, 2), (20, 3)])
def test_pie_counter(given, expected):
    assert pie_counter(given) == expected
