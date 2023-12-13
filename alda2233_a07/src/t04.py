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
from functions import list_subtract
# Constants

minuend_input = input("Enter minuend values separated by spaces: ")
subtrahend_input = input("Enter subtrahend values separated by spaces: ")


minuend = list(map(int, minuend_input.split()))
subtrahend = list(map(int, subtrahend_input.split()))


list_subtract(minuend, subtrahend)


print("minuend after:", minuend)
