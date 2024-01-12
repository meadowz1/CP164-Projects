"""
-------------------------------------------------------
Lab 1, Task 2
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-11'
-------------------------------------------------------
"""

from Food import Food

foodie = Food("Banana", 3, True, 140)
foodie2 = Food("Parfait", 6, True, 220)
foodie3 = Food("Orange Juice", 1, True, 175)

items = str(foodie)
items2 = str(foodie2)
items3 = str(foodie3)

print(f"""
{items}

{items2}

{items3}
""")