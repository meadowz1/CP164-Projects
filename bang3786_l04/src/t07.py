"""
-------------------------------------------------------
Lab 4, Task 7
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-02-01'
-------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import list_test
from List_array import List

llist = List()

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

for each in foods:
    llist.append(each)
    
list_test(llist)