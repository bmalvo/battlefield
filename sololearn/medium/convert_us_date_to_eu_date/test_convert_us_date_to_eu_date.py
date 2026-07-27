import pytest
from convert_us_date_to_eu_date import date_converter


@pytest.mark.parametrize('given, expected', [
    ('7/26/2019', '26/7/2019')
])

def test_date_converter(given, expected):
    assert date_converter(given) == expected
