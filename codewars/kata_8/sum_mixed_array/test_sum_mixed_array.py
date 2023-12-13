from sum_mixed_array import sum_mix


def test_sum_mix():
    give = [1, 2, '3', 4, '5']
    assert sum_mix(give) == 15
