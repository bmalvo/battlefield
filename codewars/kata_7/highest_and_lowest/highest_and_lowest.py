""" Task:
Return the highest and the lowest numbers from the string"""


def high_and_low(numbers):
    """Returning the highest and the lowest numbers from the string"""
    numbers = numbers.split(" ")
    numbers2 = []
    for num in numbers:
        try:
            numbers2.append(int(num))
        except ValueError:
            numbers2.append(int(num))
    numbers = str(max(numbers2))+' '+str(min(numbers2))
    return numbers
