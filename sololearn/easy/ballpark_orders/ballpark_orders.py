"""You and three friends go to a baseball game and you offer to go to the 
concession stand for everyone. They each order one thing, and you do ad well.
Nachos and Pizza both cost $6.00. A Cheesburger meal costs $10. Water is $4.00
acd Coke is $5.00. Tax is 7%.
Task:
Determine the total cost of ordering four items from the concession stand. If 
one of your friend's orders something that isn't on the menu, you will order
a Coke for them instead. 
You are giving a string of the four items that you've
been asked to order that are separated by spaces.
You will output the number of the total cost of the food and drinks.
Example: input: 'Pizza, Cheesburger, Water, Popcorn' output: '26.75'. """

menu = {'Nachos': 6.00, 'Pizza': 6.00, 'Cheeseburger': 10.00, 'Water': 4.00,
        'Coke': 5.00}
TAX = 0.07


def cost(order):
    """Count total cost given order"""
    order = order.split(' ')
    order_cost = sum((menu[i] if i in menu else menu['Coke'] for i in order))
    return order_cost + (order_cost * TAX)
