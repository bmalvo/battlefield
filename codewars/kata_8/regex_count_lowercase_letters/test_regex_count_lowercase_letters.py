import pytest
from regex_count_lowercase_letters import lowercase_count


@pytest.mark.parametrize('given, expected',[
    ("abc", 3),
    ("abcABC123", 3),
    ("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~", 3),
    ("", 0),
    ("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~", 0),
    ("abcdefghijklmnopqrstuvwxyz", 26)
])

def test_lowercase_count(given, expected):
    assert lowercase_count(given) == expected
