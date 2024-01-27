"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-27'
-------------------------------------------------------
"""

from Stack_array import Stack

source_stack = Stack()

source_stack._values.extend([1, 2, 3])

print(f"Stack before: {source_stack._values}")

source_stack.reverse()

print(f"Stack after: {source_stack._values}")