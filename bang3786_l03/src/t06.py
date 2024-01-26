"""
-------------------------------------------------------
Lab 3, Task 6
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-26'
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue
from Food_utilities import Food
from utilities import priority_queue_test
from utilities import pq_to_array
from utilities import array_to_pq

pq = Priority_Queue()
foods = []
testing_foods = []
temp_list = []
file = open("foods.txt", "r")

for line in file:
    name, origin, is_vegetarian, calories = line.strip().split("|")
    food = Food(name, int(origin), is_vegetarian == "True", int(calories))
    foods.append(food)
    testing_foods.append(food)

print("Moving items from list to priority queue:")
array_to_pq(pq, testing_foods)
print(f"All items moved to priority queue. List is now empty: {len(testing_foods) == 0}")

print("\nMoving items from priority queue back to list:")
pq_to_array(pq, temp_list)
print(f"All items moved back to list. Priority queue is now empty: {pq.is_empty()}")
print(f"Items in list: {len(temp_list)}")

print()

priority_queue_test(foods)