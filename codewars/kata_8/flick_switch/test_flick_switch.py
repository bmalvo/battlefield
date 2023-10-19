from flick_switch import flick_switch
import pytest


@pytest.mark.parametrize('given, expect', 
                         [((['codewars', 'flick', 'code', 'wars']),
                           [True, False, False, False]),
                           ((['flick', 'chocolate', 'adventure', 'sunshine']),
                            [False, False, False, False]),
                            ((['bicycle', 'jarmony', 'flick', 'sheep', 'flick']),
                             [True, True, False, False, True])])
def test_flick_switch(given, expect):
    assert flick_switch(given) == expect
