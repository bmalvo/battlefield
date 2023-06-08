"""Given an array of integers. Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative. If the input is an empty array or is null, return an empty array. 

Example: 
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]."""  # pylint: disable=line-too-long


def count_positives_sum_negatives(arr):
    """Like in description above"""
    if not arr:
        result = []
    else:
        result = []
        result.append(sum(x > 0 for x in arr))
        second_res = 0
        for i in arr:
            if i < 0:
                second_res += i
        result.append(second_res)
    return result
