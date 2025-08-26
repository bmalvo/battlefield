import pytest
from thinkful_dictionary_drills_order_filler import fillable


stock = {
    'football': 4,
    'boardgame': 10,
    'leggos': 1,
    'doll': 5}

@pytest.mark.parametrize('given, expected', [((stock, 'football', 3), True),
                                             ((stock, 'leggos', 2), False),
                                             ((stock, 'action figure', 1), False)])
def test_fillable(given, expected):
    assert fillable(given[0], given[1], given[2]) == expected
