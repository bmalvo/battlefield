"""In this kata you need to check the provided array (x) for good ideas 
'good' and bad ideas 'bad'. If there are one or two good ideas, 
return 'Publish!', if there are more than 2 return 'I smell a series!'. 
If there are no good ideas, as is often the case, return 'Fail!'."""


def well(x: list) -> str:
    """checking how many good ideas are in the input"""
    num_ideas = x.count('good')
    responds = {
        0: 'Fail!',
        1: 'Publish!',
        2: 'Publish!'
    }
    return responds.get(num_ideas, 'I smell a series!')
