import pytest
from function_syntax_debugging import main


@pytest.mark.parametrize('given, expected', [(('take ', 'item'), 'take item'),
                                             (('use ', 'sword'), 'use sword')])

def test_main(given, expected):
    word1, word2 = given
    assert main(word1, word2) == expected
