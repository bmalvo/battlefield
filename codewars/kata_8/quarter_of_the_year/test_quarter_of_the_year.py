from quarter_of_the_year import quarter_of
import pytest


@pytest.mark.parametrize('given, expected', [(1, 1), (4, 2), (7, 3), (12, 4)])
def test_quarter_of(given, expected):
    assert quarter_of(given) == expected
