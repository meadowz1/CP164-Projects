"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-21'
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Food_utilities import by_origin

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

foods_originated = by_origin(foods, 7)

for each in foods_originated:
    print(each)

