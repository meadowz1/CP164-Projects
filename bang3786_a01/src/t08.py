"""
-------------------------------------------------------
Assignment 1, Task 8
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""

from functions import matrix_stats

matrix = [
    [3.5, 2.8, 1.2],
    [4.1, 5.6, 2.3],
    [6.8, 1.9, 3.7]
]

small, large, total, average = matrix_stats(matrix)
print("Smallest:", small)
print("Largest:", large)
print("Total:", total)
print("Average:", average)
print()

matrix1 = [
    [1.5, 2.0, 3.0],
    [4.5, 5.0, 6.0],
    [7.5, 8.0, 9.0]
]

small1, large1, total1, average1 = matrix_stats(matrix1)
print("Smallest:", small1)
print("Largest:", large1)
print("Total:", total1)
print("Average:", average1)
print()

matrix2 = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0]
]

small2, large2, total2, average2 = matrix_stats(matrix2)
print("Smallest:", small2)
print("Largest:", large2)
print("Total:", total2)
print("Average:", average2)
