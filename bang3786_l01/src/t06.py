"""
-------------------------------------------------------
Lab 1, Task 6
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-12'
-------------------------------------------------------
"""

from Food_utilities import write_foods, get_food

fh = open("foods.txt", "a", encoding="utf-8")


foods = []

foods.append(get_food())

foods.append(get_food())

foods.append(get_food())

write_foods(fh, foods)