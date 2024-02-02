"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-02-01'
-------------------------------------------------------
"""

from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(1)
pq.insert(3)
pq.insert(5)
pq.insert(7)

# Define a key to split the priority queue
split_key = 4

# Split the priority queue based on the key
higher_priority, lower_or_equal_priority = pq_split_key(pq, split_key)

print("Target 1 Queue:")
for value in higher_priority:
    print(value, end=' ')
print()

print("Target 2 Queue:")
for value in lower_or_equal_priority:
    print(value, end=' ')
print()
