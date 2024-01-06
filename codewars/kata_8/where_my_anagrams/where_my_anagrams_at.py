"""Task:
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should
return an array of all the anagrams or an empty array if there are none.
"""

# solution


def anagrams(word, words):
    """Searching anagrams"""
    word = word[0].split(" ")
    word_dict = {}
    result = []
    for char in word[0]:
        word_dict[char] = word_dict.get(char, 0)+1
    for item in words:
        if len(item) == len(word[0]):
            item_dict = {}
            for char in item:
                print(char)
                item_dict[char] = item_dict.get(char, 0)+1
            if word_dict == item_dict:
                result.append(item)
    return result

# best solution from site:
# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
