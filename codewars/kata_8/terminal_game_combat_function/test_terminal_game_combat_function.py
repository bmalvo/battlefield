import pytest
from terminal_game_combat_function import combat


@pytest.mark.parametrize('given, expected', [((100, 5), 95),
                                             ((83, 16), 67),
                                             ((20, 30), 0)])

def test_combat(given, expected):
    health, damage = given
    assert combat(health, damage) == expected