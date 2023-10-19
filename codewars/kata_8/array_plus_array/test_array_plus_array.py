from array_plus_array import array_plus_array
import pytest


@pytest.mark.parametrize('given, expect',[(([1, 2, 3], [4, 5, 6]), 21),
                                          (([-1, -2, -3], [-4, -5, -6]), -21),
                                          (([0, 0, 0], [4, 5, 6]), 15),
                                          (([100, 200, 300], [400, 500, 600]), 2100)])
def test_array_plus_array(given, expect):
    assert array_plus_array(given[0], given[1]) == expect
