"""
-------------------------------------------------------
Lab 4, Task 4
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-02-01'
-------------------------------------------------------
"""

from List_array import List

my_list = List()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(20)
my_list.append(10)

index_of_20 = my_list.index(20)
print(f"The index of the first occurrence of '20': {index_of_20}")

found_value = my_list.find(30)
print(f"The value found for '30': {found_value}")

contains_20 = 20 in my_list
print(f"Is '20' in the list? {contains_20}")

count_of_10 = my_list.count(10)
print(f"The count of '10' in the list: {count_of_10}")

max_value = my_list.max()
print(f"The maximum value in the list: {max_value}")

min_value = my_list.min()
print(f"The minimum value in the list: {min_value}")