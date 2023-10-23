from return_negative import make_negative
import pytest


@pytest.mark.parametrize('given, expect', [(42,-42), (-9,-9), (0,0)])
def test_make_negative(given, expect):
    assert make_negative(given) == expect
