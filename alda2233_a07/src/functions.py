"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-12-09"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def list_factors(number):
    """
    -------------------------------------------------------
    Generates a list of factors for a given positive integer.
    Factors are the whole numbers that the integer can be evenly divided by,
    excluding the number itself.
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer greater than 0 (int)
    Returns:
        factors - a list of factors of the given number (list of int)
    ------------------------------------------------------
    """
    factors = []

    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    number_list = []

    while True:
        user_input = int(input("Enter a positive number: "))

        if user_input > 0:
            number_list.append(user_input)
        elif user_input == 0:
            break

    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """

    index_list = []
    i = 0
    for i in range(len(numbers)):
        if target_number == numbers[i]:
            index_list.append(i)
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for item in subtrahend:
        while item in minuend:
            minuend.remove(item)

    return None


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    in_order = True
    index = -1

    if numbers:
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                in_order = False
                index = i + 1
                break

    return in_order, index
