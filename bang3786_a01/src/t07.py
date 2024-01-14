"""
-------------------------------------------------------
Assignment 1, Task 7
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""

from functions import max_diff

values = [3, 8, 2, 5, 10, 1]
max_difference = max_diff(values)
print("Maximum absolute difference between adjacent values:", max_difference)

values1 = [1, 5, 2, 8, 3, 7, 4, 6]
max_diff1 = max_diff(values1)
print("Maximum absolute difference in values1:", max_diff1)

values2 = [10, 10, 10, 10, 10]
max_diff2 = max_diff(values2)
print("Maximum absolute difference in values2:", max_diff2)
