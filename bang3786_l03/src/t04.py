"""
-------------------------------------------------------
Lab 3, Task 4
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-26'
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

pq.insert(10)
pq.insert(5)
pq.insert(20)
pq.insert(1)

highest_priority_value = pq.peek()
print("The highest priority value is:", highest_priority_value)


pq2 = Priority_Queue()

pq2.insert("Orange")
pq2.insert("Apple")
pq2.insert("Banana")

highest_priority_value2 = pq2.peek()
print("The highest priority value is:", highest_priority_value2)