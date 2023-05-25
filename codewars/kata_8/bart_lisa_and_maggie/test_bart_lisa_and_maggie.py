from bart_lisa_and_maggie import namelist


def test_namelist_4():
    names_4 = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Stefka'},
               {'name': 'Kulfon'}]
    expected = 'Bart, Lisa, Maggie, Stefka & Kulfon'
    assert namelist(names_4) == expected


def test_namelist_3():
    names_3 = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
    expected = 'Bart, Lisa & Maggie'
    assert namelist(names_3) == expected


def test_namelist_2():
    names_2 = [{'name': 'Bart'}, {'name': 'Lisa'}]
    expected = 'Bart & Lisa'
    assert namelist(names_2) == expected


def test_namelist_2():
    names_1 = [{'name': 'Bart'}]
    expected = 'Bart'
    assert namelist(names_1) == expected


def test_namelist_2():
    names_0 = []
    expected = ' '
    assert namelist(names_0) == expected



