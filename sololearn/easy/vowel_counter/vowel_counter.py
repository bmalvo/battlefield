"""You are in an English class, your teacher tells the class that vowels 
are the glue that hold words and sentences together. 
They want to make sure you understand the importance of vowels in a sentence.  
You are given example sentences and are to give a total amount of vowels that 
are in each sentence.

Task: 
Write a program that takes in a string as input, counts and outputs the number 
of vowels (A, E, I, O, U).

Input Format: 
A string (letters can be both uppercase or lower case).

Output Format: 
A number which represents the total number of vowels in the string.

Sample Input: 
this is a sentence

Sample Output: 
6"""


def vowel_counter(text):
    """counting vowels in sentence"""
    count = 0
    vowels = ['a','e','i','o','u']
    for index, value in enumerate(text.lower()):
        if value in vowels:
            count += 1
    return count
