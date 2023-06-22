"""Remove an exclamation mark from the end of a string. For a beginner kata,
you can assume that the input data is always a string, no need to verify it."""


def remove(text):
    """Delete exclamation mark in the end of text"""
    return text.removesuffix('!')
