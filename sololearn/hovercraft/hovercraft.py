"""You run a hovercraft factory. Your factory makes ten hovercrafts in 
a month. Given the number of customers you got that month, did you make a 
profit? It costs you 2,000,000 to build a hovercraft, and you are selling 
them for 3,000,000. You also pay 1,000,000 each month for insurance.

Task: 
Determine whether or not you made a profit based on how many of the ten 
hovercrafts you were able to sell that month.
 
Input Format: 
An integer that represents the sales that you made that month.

Output Format: 
A string that says 'Profit', 'Loss', or 'Broke Even'.

Sample Input: 
5

Sample Output: 
Loss"""


def profitable_hovercraft(sales):
    """check if production was profitable last month"""
    production_cost = 2000000
    made_in_month = 10
    insurance = 1000000
    profit_one = 3000000
    balance = profit_one * sales - production_cost * made_in_month - insurance
    res = 'Broke Even'
    if balance:
        res = ['Loss', 'Profit'][balance > 0]
    return res
