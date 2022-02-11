"""
The functions for the course project.

Author: Connor Braaten
Date: November 22, 2021
"""

import introcs

def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair pair of parentheses is an open parens '(' followed by a closing
    parens ')'. Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """

    assert type(s) == str, repr(s)+' is not a string.'

    first = introcs.find_str(s, '(')
    second = introcs.find_str(s, ')',first+1)
    result = (first != -1) and (second != -1) and (first < second)
    return result

def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str, repr(s)+' is not a string.'
    assert matching_parens(s) == True, 'Specification is not met with with matching_parens "()".'

    first = introcs.find_str(s,'(')
    second = introcs.find_str(s,')',first+1)
    result = s[first+1:second]
    return result
