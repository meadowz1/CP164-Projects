"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-27'
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import postfix

test_expressions = [
    "12 5 -",                # Expected result: 7
    "4 5 + 12 * 2 3 * -",    # Expected result: 102
    "7 2 + 3 /"              # Expected result: 3
]

for expr in test_expressions:
    result = postfix(expr)
    print(f"'{expr}' evaluates to {result}")