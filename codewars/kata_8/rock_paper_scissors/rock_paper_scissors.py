""" Let's play! You have to return which player won! In case of a draw 
return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!" """


def rps(player_1, player_2):
    """Output player wins a game"""
    weapons = {
        'scissors': ['paper','rock'],
        'rock': ['scissors', 'paper'],
        'paper': ['rock', 'scissors']
        }
    if player_1 == player_2:
        res = 'Draw!'
    else:
        res = f'Player {weapons[player_1].index(player_2)+1} won!'
    return res
