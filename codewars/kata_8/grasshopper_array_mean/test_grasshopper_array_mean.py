from grasshopper_array_mean import mean_counter
import pytest


@pytest.mark.parametrize('given, expected', [
                                             ((1, 3, 5, 7), 4), 
                                             ((1, 5), 3), 
                                             ((1,), 1), 
                                             ((1, 3, 5, 7), 4), 
                                             ((-1, 3, 5, -7), 0), 
                                             ((5, 7, 3, 7), 5.5), 
                                             ((0,), 0)
                                             ])
def test_mean_array(given, expected):
    assert mean_counter(given) == expected
