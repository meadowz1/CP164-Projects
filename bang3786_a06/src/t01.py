"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:   bang3786@mylaurier.ca
__updated__ = '2024-02-16'
-------------------------------------------------------
"""

from Queue_linked import Queue

queue1 = Queue()
queue2 = Queue()
queue3 = Queue()

for i in range(1, 6):  # Inserts 1, 2, 3, 4, 5 into queue1
    queue1.insert(i)

for i in range(6, 11):  # Inserts 6, 7, 8, 9, 10 into queue2
    queue2.insert(i)

print(f"Queue1 is empty: {queue1.is_empty()}")
print(f"Queue2 is empty: {queue2.is_empty()}")

print(f"Front of Queue1: {queue1.peek()}")
print(f"Front of Queue2: {queue2.peek()}")

print(f"Removed from Queue1: {queue1.remove()}")
print(f"Removed from Queue2: {queue2.remove()}")

queue3.combine(queue1, queue2)

print("Elements in Queue3 after combining Queue1 and Queue2:")
for value in queue3:
    print(value, end=" ")
print()

queue1, queue2 = queue3.split_alt()

print("Elements in Queue1 after splitting Queue3:")
for value in queue1:
    print(value, end=" ")
print()

print("Elements in Queue2 after splitting Queue3:")
for value in queue2:
    print(value, end=" ")
print()

print(f"Length of Queue1: {len(queue1)}")
print(f"Length of Queue2: {len(queue2)}")

queue1._append_queue(queue2)

print("Elements in Queue1 after appending Queue2:")
for value in queue1:
    print(value, end=" ")
print()

new_queue = Queue()
new_queue.insert(1)
print(f"Is Queue1 equal to new_queue? {queue1 == new_queue}")

new_queue._append_queue(queue1)
print(f"Is Queue1 equal to new_queue after appending? {queue1 == new_queue}")
