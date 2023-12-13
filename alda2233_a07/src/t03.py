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
from functions import list_positives
from functions import get_indexes
# Constants

numbers = list_positives()


target_number = int(input("Enter the target number to find indexes for: "))
index_list = get_indexes(numbers, target_number)


print(index_list)
