"""
A module with an incomplete function.

This function was implemented using the backwards-design technique.

Author: Connor Braaten
Date: November 18, 2021
"""
import introcs


def second_in_list(s):
    """
    Returns: the second item in comma-separated list

    The final result should not have any whitespace around the edges.

    Example: second_in_list('apple, banana, orange') returns 'banana'
    Example: second_in_list('  do  ,  re  ,  me  ,  fa  ') returns 're'
    Example: second_in_list('z,y,x,w') returns 'y'

    Parameter s: The list of items
    Precondition: s is a string of at least three items separated by commas.
    """
    assert type(s) == str, 'Precondition Violation'
    assert introcs.count_str(s,',') >= 2 , 'Precondition Violation'

    first = introcs.find_str(s,',')
    second = introcs.find_str(s,',',first+1)
    slice = s[(first+1):second]
    result = introcs.strip(slice)
    return result
