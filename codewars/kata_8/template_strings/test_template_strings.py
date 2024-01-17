import pytest
from template_strings import template_strings


@pytest.mark.parametrize('given, expected',[
    (("Animals","Good"), 'Animals are Good'),
    (("Animals","Good"), 'Animals are Good'),
    (("You","Special"), 'You are Special'),
    (("lives","frozen"), 'lives are frozen')])
def test_template_strings(given, expected):
    assert template_strings(given[0], given[1]) == expected
