from extra_terrestrials import alien_translator
import pytest

@pytest.mark.parametrize('given, expected', [('bathroom', 'moorhtab'), 
                                             ('garbage', 'egabrag'),
                                             ('canada', 'adanac')])
def test_alien_translator(given, expected):
    assert alien_translator(given) == expected
