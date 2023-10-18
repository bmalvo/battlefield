"""You are creating a text-based terminal version of your favorite board game. 
In the board game, each turn has six steps that must happen in this order: 
roll the dice, move, combat, get coins, buy more health, and print status.

You are using a library (Game.Logic in C#) that already has the functions 
below. Create a function named doTurn/DoTurn/do_turn that calls the functions 
in the proper order as described in the paragraph above.

- `combat`
- `buy_health`
- `get_coins`
- `print_status`
- `roll_dice`
- `move`"""


def roll_dice():
    """test purposes"""
    return 'rolling a dice'


def move():
    """test purposes"""
    return 'moving'


def combat():
    """test purposes"""
    return'combat'


def get_coins():
    """test purposes"""
    return 'geting coins'


def buy_health():
    """test purposes"""
    return 'buying health'


def print_status():
    """test purposes"""
    return 'printing status'


def do_turn():
    """runs all previous functions"""
    return (roll_dice(), move(), combat(), get_coins(), buy_health(),
            print_status())
