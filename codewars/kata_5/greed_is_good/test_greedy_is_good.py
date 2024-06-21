import pytest
from greed_is_good import score


@pytest.mark.parametrize("given_value,expected_value", [([2, 4, 4, 5, 4], 450),
                                                        ([5, 1, 3, 4, 1], 250),
                                                        ([1, 1, 1, 3, 1], 1100)])
def test_score(given_value, expected_value):
    assert score(given_value) == expected_value
