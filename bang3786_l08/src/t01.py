"""
-------------------------------------------------------
Lab 8, Task 1
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-07"
-------------------------------------------------------
"""
# Imports
from morse import ByLetter

letter_a = ByLetter('A', '.-')
letter_b = ByLetter('B', '-...')
letter_c = ByLetter('C', '-.-.')

# Displaying string representation of ByLetter objects
print(f"Letter A: {str(letter_a)}")
print(f"Letter B: {str(letter_b)}")
print(f"Letter C: {str(letter_c)}")

aisb = 'Yes' if letter_a == letter_b else 'No'

abeforeb = 'Yes' if letter_a < letter_b else 'No'

aandc = 'Yes' if letter_a <= letter_c else 'No'

# Comparing ByLetter objects
print(f"Is Letter A equal to Letter B? {aisb}")
print(f"Does Letter A come before Letter B? {abeforeb}")
print(f"Is Letter A less than or equal to Letter C? {aandc}")
