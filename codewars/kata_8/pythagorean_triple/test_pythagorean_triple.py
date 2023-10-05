from pythagorean_triple import pythagorean_triple


def test_true_pythagorean():
    given = [3, 4, 5]
    assert pythagorean_triple(given) == 1


def test_pythagorean():
    given = [3, 4, 6]
    assert pythagorean_triple(given) == 0
