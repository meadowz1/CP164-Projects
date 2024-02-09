"""
-------------------------------------------------------
Lab 5, Task 6
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-02-06'
-------------------------------------------------------
"""

from functions import bag_to_set

old = [4, 5, 3, 4, 5, 2, 2, 4]

new = bag_to_set(old)

print(f"""
Old List: {old}
New List: {new}
""")