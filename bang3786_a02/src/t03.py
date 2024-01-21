"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-21'
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Food_utilities import calories_by_origin

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

calories_1 = calories_by_origin(foods, 1)

calories_2 = calories_by_origin(foods, 2)

calories_3 = calories_by_origin(foods, 3)

print(f""" 
The average calories in Chinese foods is: {calories_1} 
The average calories in Indian foods is: {calories_2} 
The average calories in Ethiopian foods is: {calories_3} 

""")