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
from functions import list_factors
# Constants


number_to_factorize = int(input("Enter a positive integer greater than 0: "))


result = list_factors(number_to_factorize)


print(result)
