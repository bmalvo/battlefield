from unexpected_parsing import get_status


def test_get_status_busy():
    assert get_status(True) == {'status':'busy'} 


def test_get_status_available():
    assert get_status(False) == {'status':'available'}
