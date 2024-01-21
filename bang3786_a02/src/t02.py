"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-21'
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Food_utilities import average_calories

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

calories = average_calories(foods)

print(f"The average calories in all foods from our list is: {calories}")