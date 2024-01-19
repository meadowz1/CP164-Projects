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

from Stack_array import Stack

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




        