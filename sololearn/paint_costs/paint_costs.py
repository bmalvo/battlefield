"""You are getting ready to paint a piece of art. The canvas and brushes 
that you want to use will cost 40.00. Each color of paint that you buy is 
an additional 5.00. Determine how much money you will need based on the 
number of colors that you want to buy if tax at this store is 10%.

Task 
Given the total number of colors of paint that you need, calculate and output 
the total cost of your project rounded up to the nearest whole number.

Input Format 
An integer that represents the number of colors that you want to purchase 
for your project.

Output Format 
A number that represents the cost of your purchase rounded up to the nearest 
whole number.

Sample Input 
10

Sample Output 
99"""


def painting_cost(paints, canvas_brushes = 40, tax = 10):
    """give total cost of painting operation"""
    cost_one_paint = 5
    cost_without_tax = canvas_brushes + (cost_one_paint * paints)
    total_cost = cost_without_tax + cost_without_tax * (tax / 100)
    return round(total_cost)
