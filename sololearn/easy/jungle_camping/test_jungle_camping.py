from jungle_camping import sounds_translator
import pytest


@pytest.mark.parametrize('given, expected', [
    ('Rawr Chirp Ssss', 'Tiger Bird Snake'),
    ('Grr Grr', 'Lion Lion'),
    ('Ssss', 'Snake')
    ])
def test_sounds_translator(given, expected):
    assert sounds_translator(given) == expected
