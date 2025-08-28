import pytest
from datetime import datetime
from is_the_date_today import is_today


@pytest.mark.parametrize('given, expected', [
    ((2020, 10, 1, 1, 1, 1, 1), False),
    ((2080, 10, 1, 1, 1, 1, 1), False),
    ((datetime.today()), True)])
def test_is_today(given, expected):
    assert is_today(given) == expected
