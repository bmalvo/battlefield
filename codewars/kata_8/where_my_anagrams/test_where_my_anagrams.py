from where_my_anagrams_at import anagrams


def test_anagrams1():
    anagrams1 = ('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
    expected = ['aabb', 'bbaa']
    assert anagrams(anagrams1, anagrams1[1]) == expected


def test_anagrams2():
    anagrams2 = ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
    expected = ['carer', 'racer']
    assert anagrams(anagrams2, anagrams2[1]) == expected


def test_anagrams3():
    anagrams3 = ('laser', ['lazing', 'lazy', 'lacer'])
    expected = []
    assert anagrams(anagrams3, anagrams3[1]) == expected
