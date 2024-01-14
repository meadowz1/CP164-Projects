"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2024-01-13'
-------------------------------------------------------
"""

from functions import dsmvwl

input_string = "Hello World! How are you?"
output_string = dsmvwl(input_string)

input_string2 = "I think your book is an utter piece of garbage."
output_string2 = dsmvwl(input_string2)

input_string3 = "Hello guys welcome to my Minecraft Let's Play."
output_string3 = dsmvwl(input_string3)

print(f"""
Old String: {input_string}

New String: {output_string}

Old String: {input_string2}

New String: {output_string2}

Old String: {input_string3}

New String: {output_string3}
""")

