import pytest
from a_wolf_in_sheeps_clothing import warn_the_sheep


@pytest.mark.parametrize('given, expected', [
    (['wolf'],'Pls go away and stop eating my sheep'),
    (['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep'],
     'Oi! Sheep number 2! You are about to be eaten by a wolf!'),
    (['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep'], 
     'Oi! Sheep number 5! You are about to be eaten by a wolf!'),
    (['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep'], 
     'Oi! Sheep number 6! You are about to be eaten by a wolf!'),
    (['sheep', 'wolf', 'sheep'], 
     'Oi! Sheep number 1! You are about to be eaten by a wolf!'),
    (['sheep', 'sheep', 'wolf'], 'Pls go away and stop eating my sheep'),
    ])

def test_warn_the_sheep(given, expected):
    assert warn_the_sheep(given) == expected