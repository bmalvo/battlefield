"""Create a method partition that accepts a list and a method/block. It should 
return two arrays: the first, with all the elements for which the given block 
returned true, and the second for the remaining elements."""


def partition(arr, classifier_method):
    """Divide the list into two using the proper method"""
    list1 = [x for x in arr if (classifier_method)(x)]
    list2 = [x for x in arr if x not in list1]
    return (list1, list2)
