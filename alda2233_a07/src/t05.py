"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
from functions import verify_sorted
# Constants


numbers_input = input("Enter numbers separated by spaces: ")


numbers = list(map(int, numbers_input.split()))


in_order, index = verify_sorted(numbers)


print(in_order, index)
