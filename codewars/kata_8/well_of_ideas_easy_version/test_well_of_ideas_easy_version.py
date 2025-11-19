import pytest
from well_of_ideas_easy_version import well


@pytest.mark.parametrize('given, expected', [
    (['bad', 'bad', 'bad'], 'Fail!'),
    (['good', 'bad', 'bad', 'bad', 'bad'], 'Publish!'),
    (['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good'], 
        'I smell a series!'),
])

def test_well(given, expected):
    assert well(given) == expected
