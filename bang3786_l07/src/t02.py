"""
-------------------------------------------------------
Lab 7, Task 2
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

# Populate the lists with identical values.
for value in [1, 2, 3, 4, 5]:
    list1.append(value)
    list2.append(value)

# Test if the two lists are identical.
identical = list1.is_identical_r(list2)
print(f"The lists are{' ' if identical else ' not '}identical.")

# Change one list and test again.
list2.append(6)
identical = list1.is_identical_r(list2)
print(f"""After adding an element to list2, the lists are 
{' ' if identical else ' not '} identical.
      """)

# Create a third list with different values.
list3 = List()
for value in [5, 4, 3, 2, 1]:  # Note the reversed order.
    list3.append(value)

# Test if list1 and list3 are identical.
identical = list1.is_identical_r(list3)
print(f"The lists are{' ' if identical else ' not '}identical.")
