"""
-------------------------------------------------------
Lab 6, Task 1
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:   bang3786@mylaurier.ca
__updated__ = '2024-02-13'
-------------------------------------------------------
"""

from List_linked import List

playlist = List()

playlist.prepend("Bohemian Rhapsody - Queen")

playlist.append("Imagine - John Lennon")

playlist.insert(1, "Like a Rolling Stone - Bob Dylan")

for each in playlist:
    print(each)
