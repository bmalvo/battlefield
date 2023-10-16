from simple_fun_whose_move import whose_move
import pytest

@pytest.mark.parametrize('given, expected',[(('white',True), 'white'),
                                            (('white', False), 'black'),
                                            (('black', True), 'black'),
                                            (('black', False), 'white')])
def test_whose_move(given, expected):
    assert whose_move(given[0], given[1]) == expected
