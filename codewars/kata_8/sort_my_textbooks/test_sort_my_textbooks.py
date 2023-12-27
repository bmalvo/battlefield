import pytest
from sort_my_textbooks import sorter


@pytest.mark.parametrize('given, expected', [
                            (['Algebra', 'History', 'Geometry', 'English'],
                             ['Algebra', 'English', 'Geometry', 'History']),
                            (['Algebra', 'history', 'Geometry', 'english'],
                             ['Algebra', 'english', 'Geometry', 'history']),
                            (['Alg#bra', '$istory', 'Geom^try', '**english'],
                             ['$istory', '**english', 'Alg#bra', 'Geom^try'])])
def test_sorter(given, expected):
    assert sorter(given) == expected
