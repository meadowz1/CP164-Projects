"""
-------------------------------------------------------
Lab 7, Task 6
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-02-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List

original_list = List()
for value in range(1, 6):  # This will create a list with values 1 to 5
    original_list.append(value)

# Display the original list order.
print("Original List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

# Reverse the list using the recursive method.
original_list.reverse_r()

# Display the reversed list order.
print("Reversed List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()
