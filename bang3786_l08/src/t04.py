"""
-------------------------------------------------------
Lab 8, Task 4
-------------------------------------------------------
Author:  Mike Bangar
ID:      169073786
Email:   bang3786@mylaurier.ca
__updated__ = "2024-03-07"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from morse import fill_code_bst, DATA1

bst = BST()

# Fill the BST with Morse code data
fill_code_bst(bst, DATA1)

# Print the BST
print("BST Contents in Inorder:")
for each in bst.inorder():
    print(each)
