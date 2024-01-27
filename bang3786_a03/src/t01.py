"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-27'
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import stack_combine

stack1 = Stack()
stack2 = Stack()

stack1.push(1)
stack1.push(3)
stack1.push(5)

stack2.push(2)
stack2.push(4)
stack2.push(6)

combined_stack = stack_combine(stack1, stack2)

for item in combined_stack:
    print(item)