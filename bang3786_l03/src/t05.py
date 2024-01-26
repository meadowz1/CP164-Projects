"""
-------------------------------------------------------
Lab 3, Task 5
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-26'
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

pq.insert(30)
pq.insert(10)
pq.insert(20)

while not pq.is_empty():
    highest_priority_value = pq.remove()
    print("Removed:", highest_priority_value)

print()
    
q = Priority_Queue()

q.insert("Mango")
q.insert("Apple")
q.insert("Banana")

# Remove and display the highest priority string (alphabetically first)
while not q.is_empty():
    highest_priority_value1 = q.remove()
    print("Removed:", highest_priority_value1)