"""Given a sequence of items and a specific item in that sequence, return the 
item immediately following the item specified. If the item occurs more than 
once in a sequence, return the item after the first occurence. This should 
work for a sequence of any type.

When the item isn't present or nothing follows it, the function should return 
nil in Clojure and Elixir, Nothing in Haskell, undefined in JavaScript, None 
in Python."""


def next_item(xs, item):
    """output item next to given in argument"""
    res = None
    found = False
    for current in xs:
        if found:
            return current
        if current == item:
            found = True
    return res
