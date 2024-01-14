"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""

from functions import is_leap_year

year_to_check = 2024
leap_year = is_leap_year(year_to_check)

if leap_year:
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")


year_to_check2 = 2000
leap_year2 = is_leap_year(year_to_check2)

if leap_year2:
    print(f"{year_to_check2} is a leap year.")
else:
    print(f"{year_to_check2} is not a leap year.")
    
    
year_to_check3 = 1727
leap_year3 = is_leap_year(year_to_check3)

if leap_year3:
    print(f"{year_to_check3} is a leap year.")
else:
    print(f"{year_to_check3} is not a leap year.")