import pytest
from exclamation_marks_series_6 import remove


@pytest.mark.parametrize('text, number, output', [("Hi!", 1, "Hi"),
                                ("Hi!",100, "Hi"),
                                ("Hi!!!", 1, "Hi!!"),
                                ("Hi!!!",100, "Hi"),
                                ("!Hi", 1, "Hi"),
                                ("!Hi!", 1, "Hi!"),
                                ("!Hi!", 100, "Hi"),
                                ("!!!Hi !!hi!!! !hi", 1,"!!Hi !!hi!!! !hi"),
                                ("!!!Hi !!hi!!! !hi", 3,"Hi !!hi!!! !hi"),
                                ("!!!Hi !!hi!!! !hi", 5, "Hi hi!!! !hi"),
                                ("!!!Hi !!hi!!! !hi", 100, "Hi hi hi")])
def test_remove(text, number, output):
    assert remove(text, number) == output
