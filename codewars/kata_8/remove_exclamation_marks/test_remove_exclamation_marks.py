from remove_exclamation_marks import remove_exclamation_marks


def test_remove_exclamation_marks():
    assert remove_exclamation_marks('test!') == 'test'
    