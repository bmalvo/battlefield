from csv_representation import to_csv_text

exampel = [[0, 1, 2, 3, 4],
           [10, 11, 12, 13, 14],
           [20, 21, 22, 23, 24],
           [30, 31, 32, 33, 34]]


def test_to_csv_text():
    assert to_csv_text(exampel) == \
           "0,1,2,3,4\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34"
