"""Remove n exclamation marks in the sentence from left to right. 
n is positive integer."""


def remove(text: str, numb: int) -> str:
    """return text without n number of exclamation mark"""
    new_text = list(text)
    for _ in range(numb):
        for char in new_text:
            if char == '!':
                new_text.remove(char)
                break
    return ''.join(new_text)
