"""
-------------------------------------------------------
Assignment 10, Task 4
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-29"
-------------------------------------------------------
"""
# Imports
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

a = Deque()
a.insert_rear(123)
a.insert_rear(1)
a.insert_rear(213441)
a.insert_rear(14)
a.insert_rear(12351235)
a.insert_rear(1213213123)
a.insert_rear(0)
a.insert_rear(-1)

Sorts.gnome_sort(a)

for i in a:
    print(i)
