"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-21'
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Food_utilities import food_table

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

food_table(foods)

