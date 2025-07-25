import pytest
from freudian_translator import to_freud


@pytest.mark.parametrize('given, expected', [("test", "sex"),
                                             ("sexy sex", "sex sex"),
                                             ("This is a test", "sex sex sex sex"),
                                             ("This is a longer test", "sex sex sex sex sex"),
                                             ("You're becoming a true freudian expert", "sex sex sex sex sex sex"),
                                             (' ', '')])

def test_to_freud(given, expected):
    assert to_freud(given) == expected