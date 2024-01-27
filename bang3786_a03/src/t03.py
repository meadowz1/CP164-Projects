"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-27'
-------------------------------------------------------
"""
from functions import stack_reverse
from Stack_array import Stack

source_stack = Stack()


source_stack.push(1)
source_stack.push(3)
source_stack.push(5)

print(f"Stack before: {source_stack._values}")

stack_reverse(source_stack)

print(f"Stack after: ")

while not source_stack.is_empty():
    print(source_stack.pop())