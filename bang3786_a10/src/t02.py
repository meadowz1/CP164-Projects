"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-29"
-------------------------------------------------------
"""
from Sorts_List_linked import Sorts
from List_linked import List

lst = List()

lst.append(9999)
lst.append(1231231231)
lst.append(341)
lst.append(44120)
lst.append(11239)
lst.append(23)

Sorts.radix_sort(lst)

for i in lst:
    print(i)
