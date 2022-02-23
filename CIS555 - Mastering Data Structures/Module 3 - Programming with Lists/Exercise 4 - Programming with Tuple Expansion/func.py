"""
Module to demonstrate tuple expansion.

Author: Connor Braaten
Date: February 9, 2022
"""


def avg(*args):   # The parameter is MISSING.  Add it back. 
    """
    Returns average of all of arguments (passed via tuple expansion)
    
    Remember that the average of a list of arguments is the sum of all of the elements 
    divided by the number of elements.
    
    Examples: 
        avg(1.0, 2.0, 3.0) returns 2.0
        avg(1.0, 1.0, 3.0, 5.0) returns 2.5
    
    Parameter args: the function arguments
    Precondition: args are all numbers (int or float)
    """
    if len(args) == 0:
        return 0
        
    acc_avg = 0

    for x in args:
        acc_avg = acc_avg + x

    acc_avg = acc_avg/len(args)

    return acc_avg