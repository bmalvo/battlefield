"""Your job is simple, if x squared is more than 1000, return It's hotter 
than the sun!!, else, return Help yourself to a honeycomb Yorkie for 
the glovebox."""


def apple(x):
    """check if the apple is hotter than the sun"""
    square = int(x) ** 2
    answer = ["Help yourself to a honeycomb Yorkie for the glovebox.",
              "It's hotter than the sun!!"]
    return answer[square > 1000]
