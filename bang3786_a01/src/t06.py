"""
-------------------------------------------------------
Assignment 1, Task 6
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""

from functions import is_valid

variable_name = "my_var_123"
valid = is_valid(variable_name)

if valid:
    print(f"{variable_name} is a valid Python variable name.")
else:
    print(f"{variable_name} is not a valid Python variable name.")

variable_name2 = "WRONG VARIABLE BRO"
valid2 = is_valid(variable_name2)

if valid2:
    print(f"{variable_name2} is a valid Python variable name.")
else:
    print(f"{variable_name2} is not a valid Python variable name.")

variable_name3 = "semi-right variable"
valid3 = is_valid(variable_name3)

if valid3:
    print(f"{variable_name3} is a valid Python variable name.")
else:
    print(f"{variable_name3} is not a valid Python variable name.")
