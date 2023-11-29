from string_templates_bug_fixes_5 import build_string
import pytest


@pytest.mark.parametrize('given, expected', [(
        ('Cheese','Milk','Chocolate'), 'I like Cheese, Milk, Chocolate!'),
        (('Cheese','Milk'), 'I like Cheese, Milk!'),
        (('Chocolate',), 'I like Chocolate!')])
def test_buil_string(given, expected):
    assert build_string(*given) == expected
