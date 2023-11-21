from neverland import age_counter
import pytest


@pytest.mark.parametrize('given, expected', [
    ((10, 8),'My twin is 18 years old and they are 8 years older than me'),
    ((19, 2), 'My twin is 21 years old and they are 2 years older than me'),
    ((8, 4), 'My twin is 12 years old and they are 4 years older than me')])
def test_age_counter(given, expected):
    assert age_counter(given[0], given[1]) == expected
