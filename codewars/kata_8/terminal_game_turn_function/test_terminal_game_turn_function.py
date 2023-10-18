from terminal_game_turn_function import do_turn


def test_do_turn():
    assert do_turn() == ('rolling a dice', 'moving', 'combat', 'geting coins', 
                         'buying health', 'printing status')
    