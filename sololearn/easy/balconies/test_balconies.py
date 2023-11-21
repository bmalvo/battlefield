from balconies import balcony
import pytest


@pytest.mark.parametrize('given, expected', [(('16,10','17,10'), 'Apartment B'),
                                             (('5,5','3,10'), 'Apartment B')])
def test_balcony(given, expected):
    assert balcony(given[0], given[1]) == expected
