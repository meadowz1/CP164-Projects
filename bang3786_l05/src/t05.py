"""
-------------------------------------------------------
Lab 5, Task 4
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-02-06'
-------------------------------------------------------
"""

from functions import is_palindrome

test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "No 'x' in Nixon"]

for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' is a palindrome: {result}")