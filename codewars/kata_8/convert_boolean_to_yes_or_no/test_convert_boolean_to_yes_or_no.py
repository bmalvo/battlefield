from convert_boolean_to_yes_or_no import bool_to_word


def test_bool_to_word_if_true():
    boolean = True
    assert bool_to_word(boolean) == 'Yes'


def test_bool_to_word_if_false():
    boolean = False
    assert bool_to_word(boolean) == 'No'
    