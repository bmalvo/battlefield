"""Implement a function which accepts 2 arguments: string and separator.

The expected algorithm: split the string into words by spaces, split each word 
into separate characters and join them back with the specified separator, 
join all the resulting "words" back into a sentence with spaces."""


def split_and_merge(string_, separator):
    """Processes string for new proper output"""
    res = [separator.join(list(word)) for word in string_.split(' ')]
    return  ' '.join(char for char in res)
