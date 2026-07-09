from create_the_rooms import rooms


def test_len():
    assert len(rooms.keys()) >= 3

def test_is_a_dict():
    assert isinstance(rooms, dict)
