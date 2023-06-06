from count_pos_sum_negative import count_positives_sum_negatives


def test_count_positives_sum_negatives():
    testing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    assert count_positives_sum_negatives(testing_list) == [10, -65]


def test_count_positives_sum_negatives_if_zer_zero():
    testing_list = [0, 0]
    assert count_positives_sum_negatives(testing_list) == [0, 0]


def test_count_positives_sum_negatives_if_null():
    testing_list = []
    assert count_positives_sum_negatives(testing_list) == []
