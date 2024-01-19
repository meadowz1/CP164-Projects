"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-18'
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_food

s = Stack()

fh = open("foods.txt", "r", encoding="utf-8")

for line in fh:
    food = read_food(line)
    s.push(food)
    
stack_test(s)