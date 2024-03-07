"""
-------------------------------------------------------
Lab 8, Task 3
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-07"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_letter_bst, DATA1

bst = BST()

fill_letter_bst(bst, DATA1)

for each in bst.inorder():
    print(each)
