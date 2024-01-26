"""
-------------------------------------------------------
Lab 3, Task 1
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-26'
-------------------------------------------------------
"""

from Queue_array import Queue

q = Queue()

elements = [1]

print("Inserting elements into the queue:")
for element in elements:
    print(f"Inserting {element} into the queue.")
    q.insert(element)
    print(f"Queue now contains: {[val for val in q]}")