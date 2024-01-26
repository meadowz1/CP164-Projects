"""
-------------------------------------------------------
Lab 2 - Stack Utilities
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-18'
-------------------------------------------------------
"""
# Imports

from Queue_array import Queue
from Stack_array import Stack
from Priority_Queue_array import Priority_Queue

# Stack Utilities

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source:
        item = source.pop()
        stack.push(item)
        
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        item = stack.pop()
        target.insert(0, item)
        
    return 


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()

    try:
        s.pop()
    except AssertionError:
        print("Pop on empty stack correctly raised an exception.")

    try:
        s.peek()
    except AssertionError:
        print("Peek on empty stack correctly raised an exception.")

    for item in source:
        s.push(item)
        print(f"Pushed {item} onto the stack. Top of stack is now: {s.peek()}")

    print("Test is_empty after pushing:", s.is_empty())  

    while not s.is_empty():
        item = s.pop()
        print(f"Popped {item} from the stack.")

    print("Test is_empty after popping all items:", s.is_empty()) 
    
    return



# Queue Utilities

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        value = source.pop(0)
        queue.insert(value)
    
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not queue.is_empty():
        value = queue.remove()
        target.append(value)
        
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    print("Testing an empty queue:")
    print("Is the queue empty? (Expected: True):", q.is_empty())
    print("Length of the queue (Expected: 0):", len(q))

    if not q.is_empty():
        print("Front element (peek):", q.peek())
        print("Removed element:", q.remove())
    else:
        print("Cannot peek or remove from an empty queue.")

    print("\nInserting elements into the queue:")
    for item in a:
        q.insert(item)
        print(f"Inserted {item}. Queue length is now {len(q)}.")

    print("\nTesting a non-empty queue:")
    print("Is the queue empty? (Expected: False):", q.is_empty())
    if not q.is_empty():
        print("Peek at the front of the queue (Expected: first element of a):", q.peek())

    print("\nRemoving elements from the queue:")
    while not q.is_empty():
        item = q.remove()
        print(f"Removed {item}. Queue length is now {len(q)}.")

    print("\nFinal state of the queue:")
    print("Is the queue empty? (Expected: True):", q.is_empty())
    print("Length of the queue (Expected: 0):", len(q))

    return


# Priority Queue Utilities

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        pq.insert(source.pop(0))
    
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not pq.is_empty():
        target.append(pq.remove())
        
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("Testing insert and is_empty:")
    for item in a:
        pq.insert(item)
        print(f"Inserted {item}, Queue is_empty: {pq.is_empty()}")

    print("\nTesting peek and remove:")
    while not pq.is_empty():
        print(f"Peek: {pq.peek()}, Removed: {pq.remove()}")

    return
        