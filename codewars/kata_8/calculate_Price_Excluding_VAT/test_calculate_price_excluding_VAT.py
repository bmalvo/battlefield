from calculate_price_excluding_vat import excluding_vat_price
import pytest

@pytest.mark.parametrize('given, expected',[(115, 100.00),(190, 165.22),
                                            (None, -1), (230, 200.00)])
def test_excluding_vat_price(given, expected):
    assert excluding_vat_price(given) == expected
