import pytest
from are_you_playing_banjo import are_you_playing_banjo


@pytest.mark.parametrize('given, expected', [
    ("martin", "martin does not play banjo"),
    ("Rikke", "Rikke plays banjo"),
    ("bravo", "bravo does not play banjo"),
    ("rolf", "rolf plays banjo")
])

def test_are_you_playing_bajno(given, expected):
    assert are_you_playing_banjo(given) == expected
