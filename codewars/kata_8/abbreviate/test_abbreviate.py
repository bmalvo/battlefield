from abbreviate import abbrev_name


def test_abbrev_name():
    assert abbrev_name('john wick') == 'J.W'


def test2_abbrev_name():
    assert abbrev_name('john snow') == 'J.S'
