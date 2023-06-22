from exclamation_marks_series_1 import remove
import pytest


@pytest.mark.parametrize('given, expected',
                         [("Hi!", "Hi"), ("Hi!!!", "Hi!!"), ("!Hi", "!Hi"), ("!Hi!", "!Hi"),
                          ("Hi! Hi!", "Hi! Hi"), ("Hi", "Hi")])
def test_remove(given, expected):
    assert remove(given) == expected
