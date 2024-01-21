"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-21'
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Food_utilities import food_search

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

foods_chinese = food_search(foods, 0, 500, False)

print("Canadian food with less than 500 calories and is non-vegetarian:")
print()
for each in foods_chinese:
    print(each)
    print()