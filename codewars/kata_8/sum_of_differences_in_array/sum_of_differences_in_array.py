"""Your task is to sum the differences between consecutive pairs in the array 
in descending order."""


def sum_of_differences(arr):
    """output sum of differences"""
    arr.sort(reverse=True)
    summary = 0
    if len(arr) > 1:
        for num in range(len(arr)):
            if num == (len(arr) -1):
                break
            add = arr[num] - (arr[num +1])
            summary += add
    return  summary
