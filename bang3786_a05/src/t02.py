"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:   bang3786@mylaurier.ca
__updated__ = '2024-02-10'
-------------------------------------------------------
"""
from Sorted_List_array import Sorted_List
from Food_utilities import read_foods

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

# Create a new Sorted_List
sorted_list = Sorted_List()

# Insert each Food object into the Sorted_List
for food in foods:
    sorted_list.insert(food)

# Now, demonstrate each method of the Sorted_List class.
# 1. __contains__ (key in sorted_list)
print(foods[0] in sorted_list)

# 2. __getitem__ (sorted_list[i])
if len(sorted_list) > 0:
    print(sorted_list[0])
else:
    print("The list is empty, cannot use __getitem__.")

# 3. __len__ (len(sorted_list))
print(len(sorted_list))

# 4. clean (sorted_list.clean())
sorted_list.clean()

# 5. count (sorted_list.count(key))
print(sorted_list.count(foods[0]))

# 6. find (sorted_list.find(key))
print(sorted_list.find(foods[0]))

# 7. index (sorted_list.index(key))
print(sorted_list.index(foods[0]))

# 8. intersection (sorted_list.intersection(source1, source2))
sorted_list2 = Sorted_List()
sorted_list2.insert(foods[1])
sorted_list.intersection(sorted_list, sorted_list2)

# 9. max (sorted_list.max())
if len(sorted_list) > 0:
    max_value = sorted_list.max()
    print(max_value)
else:
    print("The list is empty, cannot find a maximum value.")

# 10. min (sorted_list.min())
if len(sorted_list) > 0:
    min_value = sorted_list.min()
    print(min_value)
else:
    print("The list is empty, cannot find a minimum value.")
# 11. peek (sorted_list.peek())
if len(sorted_list) > 0:
    print(sorted_list.peek())
else:
    print("The list is empty, cannot peek at the first element.")

# 12. remove (sorted_list.remove(key))
if foods[0] in sorted_list:
    sorted_list.remove(foods[0])
else:
    print(f"The food {foods[0]} is not in the list.")

# 13. remove_front (sorted_list.remove_front())
if len(sorted_list) > 0:
    print(sorted_list.remove_front())
else:
    print("The list is empty, cannot remove the front element.")

# 14. remove_many (sorted_list.remove_many(key))
sorted_list.remove_many(foods[1])

# 15. split (sorted_list.split())
if len(sorted_list) > 0:
    target1, target2 = sorted_list.split()
else:
    print("The list is empty, cannot split.")

# 16. split_alt (sorted_list.split_alt())
if len(sorted_list) > 0:
    target1_alt, target2_alt = sorted_list.split_alt()
else:
    print("The list is empty, cannot alternate split.")

# 17. split_key (sorted_list.split_key(key))
if len(sorted_list) > 0:
    target1_key, target2_key = sorted_list.split_key(foods[2])
else:
    print("The list is empty, cannot split by key.")

# 18. union (sorted_list.union(source1, source2))
if len(sorted_list) > 0 and len(sorted_list2) > 0:
    sorted_list.union(sorted_list, sorted_list2)
else:
    print("One or both lists are empty, cannot perform union.")

# 19. __eq__ (sorted_list == other)
print(sorted_list == sorted_list2)

# 20. __iter__ (for item in sorted_list)
for item in sorted_list:
    print(item)
