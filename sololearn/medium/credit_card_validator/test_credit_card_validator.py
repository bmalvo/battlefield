import pytest
from credit_card_validator import credit_card_validator


@pytest.mark.parametrize('given, expected', [
    ('4091131560563988', 'valid')
])

def test_credit_card_validator(given, expected):
    assert credit_card_validator(given) == expected
