"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-27'
-------------------------------------------------------
"""

from Stack_array import Stack
from functions import is_palindrome_stack

palindrome_tests = [
    "racecar",
    "Otto",
    "Able was I ere I saw Elba",
    "A man, a plan, a canal, Panama!",
    "Not a Palindrome",
    "12321",
    "This is not a palindrome"
]

for test_string in palindrome_tests:
    result = is_palindrome_stack(test_string)
    print(f"'{test_string}' is a palindrome: {result}")