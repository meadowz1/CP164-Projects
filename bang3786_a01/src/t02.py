"""
-------------------------------------------------------
Assignment 1, Task 2
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""

from functions import list_subtraction

values = [22, 33, 11, 1, 2, 3, 44, 55, 66, 4, 5, 6]

print(f"List before: {values}")
list_subtraction(values, [11, 22, 33, 44, 55, 66])

print(f"List after: {values}")