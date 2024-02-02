"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-02-01'
-------------------------------------------------------
"""

from Queue_circular import Queue

queue1 = Queue()
queue2 = Queue()

# Insert the same elements into both queues
for element in [1, 2, 3, 4, 5]:
    queue1.insert(element)
    queue2.insert(element)

# Check if the two queues are equal
if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("queue1 and queue2 are not equal.")

# Change one of the queues
queue2.remove()
queue2.insert(6)

# Check if the queues are still equal
if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("After modification, queue1 and queue2 are not equal.")