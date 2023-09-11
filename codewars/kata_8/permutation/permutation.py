""" Task:
 In this kata you have to create all permutations_word of a non empty.
 input string and remove duplicates, if present.
 This means, you have to shuffle all letters from the input in all 
 possible orders.

 Examples:

 * With input 'a'
 * Your function should return: ['a']
 * With input 'ab'
 * Your function should return ['ab', 'ba']
 * With input 'aabb'
 * Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 
 'bbaa']"""
from itertools import permutations


def all_permutations(word):
    """Return all permutation of arguments"""
    per_iter = permutations(word)
    per_list = []
    for per in per_iter:
        if ''.join(per) not in per_list:
            per_list.append(''.join(per))
    return per_list
