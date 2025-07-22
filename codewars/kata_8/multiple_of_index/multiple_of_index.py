"""Return a new array consisting of elements which are multiple of their own 
index in input array (length > 1)."""


def multiple_of_index(arr):
    new_arr = arr[1:]
    print('new arr', new_arr)
    res = [x for x in new_arr if (abs(x) % (new_arr.index(x) + 1) == 0)]
    res.insert(0, arr[0]) if arr[0] == 0 else None
    return res


print(multiple_of_index([0, 2, 3, 6, 9, 10]))
print(multiple_of_index([68, -1, 1, -7, 10, 10, 12,14]))


# print (0%4)
# a = [1,2,4]
# a.insert(1,3)
print(abs(-6)%1)
print(abs(10)%5)