import pytest
from index_of_an_element_in_an_array import find
from math import pi


array = [2, 3, 5, 7, 11]
array2 = [True, 'Hello World', False, 'Lorem Ipsum', 6, pi]


@pytest.mark.parametrize('given, expected', [((array, 5), 2),
                                             ((array, 11), 4),
                                             ((array, 3), 1),
                                             ((array, 2), 0),
                                             ((array, 7), 3),
                                             ((array, 1), 'Not found'),
                                             ((array, 8), 'Not found'),
                                             ((array2, 'Hello World'), 1),
                                             ((array2, 'lorem ipsum'), 'Not found'),
                                             ((array2, 'Lorem Ipsum'), 3),
                                             ((array2, False), 2),
                                             ((array2, True), 0),
                                             ((array2, pi), 5),
                                             ((array2, 3.14), 'Not found')])

def test_find(given, expected):
    array, element = given
    assert find(array, element) == expected
