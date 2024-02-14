"""
-------------------------------------------------------
Lab 6, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:   bang3786@mylaurier.ca
__updated__ = '2024-02-13'
-------------------------------------------------------
"""

from List_linked import List

my_list = List()
my_list.append("red")
my_list.append("green")
my_list.append("blue")
my_list.append("yellow")

first_item = my_list.peek()
print("First item (peeked):", first_item)

removed_item = my_list.remove("green")
print("Removed item:", removed_item)
