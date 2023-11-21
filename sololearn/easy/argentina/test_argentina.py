from argentina import check_exchange
import pytest


@pytest.mark.parametrize('given, expected', [((400, 10), 'Pesos'),
                                             ((1000, 10), 'Dollars')])
def test_check_exchange(given, expected):
    assert check_exchange(given[0], given[1]) == expected
