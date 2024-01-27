"""
-------------------------------------------------------
Assignment 3, Task 7
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-27'
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import stack_maze

maze = {
    'Start': ['A'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F', 'X'],
    'F': ['G'],
    'G': ['C']
}

print(maze)

# Expected output: ['A', 'C', 'E', 'X']
print(stack_maze(maze))