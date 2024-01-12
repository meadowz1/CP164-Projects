"""
-------------------------------------------------------
Lab 1, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-11'
-------------------------------------------------------
"""

from Food_utilities import read_foods

fh = open("foods.txt", "r")

items = read_foods(fh)

for each in items:
    print(each)
    print()
    