"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports
from functions import hash_table

from Hash_Set_array import Hash_Set
from Food import Food

foodie = Food("Banana", 3, True, 140)
foodie2 = Food("Parfait", 6, True, 220)
foodie3 = Food("Orange Juice", 1, True, 175)

foods = []

foods.append(foodie)
foods.append(foodie2)
foods.append(foodie3)

hash_table(7, foods)
