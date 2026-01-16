"""Your task is to sum the differences between consecutive pairs in the array 
in descending order."""


def sum_of_differences(arr):
    """output sum of differences"""
    arr = sorted(arr, reverse=True)
    sumary = 0
    if len(arr) > 1:
        for i in arr:
            if arr.index(i) == len(arr) +1:
                break
            add = i - (arr[arr.index(i) + 1])
            sumary += abs(add)
    return  sumary


print(sum_of_differences([1, 10, 8, 1, 5, -3, -9, -
      1, 9, -4, 7, -3, -8, -10, -2, -10, 0, 3, 1]))
