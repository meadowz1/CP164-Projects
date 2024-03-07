"""
-------------------------------------------------------
Lab 8, Task 7
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-07"
-------------------------------------------------------
"""

"""
DATA1 Tree:

A
 \
  B
   \
    C
     \
      D
       \
        ...
         \
          Z


DATA2 Tree:
       M
      / \
    C     T
   / \   / \
  B   F J   W
 / \ / \ / \ / \
A  D E G I K O Q
               / \
              N   S
                 / \
                P   R
                   / \
                  L   U
                       \
                        V
                         \
                          X
                           \
                            Y
                             \
                              Z

DATA3 Tree:
 E
  \
   T
    \
     A
      \
       O
        \
         I
          \
           N
            \
             S
              \
               ...
                 \
                  Z
"""

"""
Which of these three is the most inefficient tree? Why?
Which of these is likely to be the most efficient tree?
How could you (theoretically) figure that out?

A:
DATA1 is likely the most inefficient BST, since it has the height of the amount of elements
that are in the list.

DATA2 is likely the most efficient BST, since the data is arranged to be split properly.

 To figure out which is most efficient, you would calculate the height of the BST that each dataset produces.
 The tree with the height closest to the theoretical minimum height, which is log2(n) where n is the number of nodes,
 would be the most efficient. The balanced BST allows for search operations to be performed in O(log n) time,
 compared to O(n) for a completely unbalanced tree.
"""
