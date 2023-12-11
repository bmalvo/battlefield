"""You are in a college level English class, your professor wants you to write 
an essay, but you need to find out the average length of all the words you use. 
It is up to you to figure out how long each word is and to average it out.

Task: 
Takes in a string, figure out the average length of all the words and return a 
number representing the average length. Remove all punctuation. Round up to 
the nearest whole number.

Input Format: 
A string containing multiple words.

Output Format: 
A number representing the average length of each word, rounded up to the 
nearest whole number.

Sample Input: 
this phrase has multiple words

Sample Output: 
6"""
import math


def average_all_words(text):
    """return average of all words"""
    punctuation = [',', '.', '?', '!', '-']
    new_text = ''
    for char in text:
        if char in punctuation:
            char = ''
        new_text += char
    sum_avgs_word = sum(len(word) for word in new_text.split(' '))
    words_amount = len(new_text.split(' '))
    return math.ceil(sum_avgs_word / words_amount) # round up by ceil
