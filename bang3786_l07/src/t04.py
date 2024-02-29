"""
-------------------------------------------------------
Lab 7, Task 4
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-02-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List

list1 = List()
list2 = List()

# Populate the lists with some values, some of which overlap.
for value in [1, 3, 5, 7, 9]:
    list1.append(value)
for value in [0, 2, 4, 6, 8, 9]:
    list2.append(value)

# Create a new list instance for the intersection.
intersection_list = List()

# Find the intersection of list1 and list2 using recursion.
intersection_list.intersection_r(list1, list2)

# Display the result.
print("Intersection of list1 and list2:")
current = intersection_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()
