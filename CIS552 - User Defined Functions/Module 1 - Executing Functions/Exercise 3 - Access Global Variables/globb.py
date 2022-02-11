"""
A module to demonstrate global variables.

Author: Connor Braaten
Date: November 5, 2021
"""

# The global variable
VAR = 1
def next():
    """
    Returns and increments the value of VAR.
    """
    global VAR
    result=VAR
    a = VAR+1
    VAR=a
    return result
