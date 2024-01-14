"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""
from functions import file_analyze

fh = open("t04.txt", "r", encoding="utf-8")

upp, low, dig, whi, rem = file_analyze(fh)

print(f"""
Uppercase:  {upp}
Lowercase:  {low}
Digits:     {dig}
WhiteSpace: {whi}
Remaining:  {rem}
""")