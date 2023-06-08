""" Create a function that returns the CSV representation of a two-dimensional numeric array.

Example:

input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]

output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34' """

exampel = [[0, 1, 2, 3, 4],
           [10, 11, 12, 13, 14],
           [20, 21, 22, 23, 24],
           [30, 31, 32, 33, 34]]


def to_csv_text(array):
    """returns the CSV representation of a two-dimensional numeric array"""
    final = ''
    for line, row in enumerate(array):
        count = 0
        for item in row:
            final += str(item)
            count += 1
            if count < len(row):
                final += ','
        if line + 1 != len(array):
            final += '\n'
    return final


print(to_csv_text(exampel))
