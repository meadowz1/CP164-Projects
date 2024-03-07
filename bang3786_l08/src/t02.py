"""
-------------------------------------------------------
Lab 8, Task 2
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-07"
-------------------------------------------------------
"""
# Imports
from morse import ByCode

code_a = ByCode('.-', 'A')
code_b = ByCode('-...', 'B')
code_c = ByCode('-.-.', 'C')

# Displaying string representation of ByCode objects
print(f"Code for A: {str(code_a)}")
print(f"Code for B: {str(code_b)}")
print(f"Code for C: {str(code_c)}")

# Comparing ByCode objects
print(f"Is the Code for A equal to the Code for B? {'Yes' if code_a == code_b else 'No'}")
print(f"Does the Code for A come before the Code for B? {'Yes' if code_a < code_b else 'No'}")
print(f"Is the Code for A less than or equal to the Code for C? {'Yes' if code_a <= code_c else 'No'}")
