from easter_eggs import egg_counter
import pytest


@pytest.mark.parametrize('given, expected',[((20, 5, 8), 'Keep Hunting'),
                                            ((30, 15, 15),'Candy Time')])
def test_egg_counter(given, expected):
    assert egg_counter(given[0], given[1], given[2]) == expected
