"""Return a new array consisting of elements which are multiple of their own 
index in input array (length > 1)."""


def multiple_of_index(arr):
    """return only elements multiple of their own index"""
    new_arr = arr[1:]
    dict_arr = {}
    for index, value in enumerate(new_arr, 1):
        dict_arr[index] = value
    print(dict_arr)
    res = [key[1] for key in dict_arr.items() if key[1] % key[0] == 0]
    res.insert(0, arr[0]) if arr[0] == 0 else None
    return res
