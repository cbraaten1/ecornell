"""
Functions demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: Connor Braaten
Date: February 5, 2022
"""


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.
    
    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.
    
    Examples: 
        first_in_parens('A (B) C') returns 'B'
        first_in_parens('A (B) (C)') returns 'B'
        first_in_parens('A ((B) (C))') returns '(B'
    
    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    first_paren = s.find('(')

    sec_paren = s.find(')',first_paren+1)

    first_ltr = s[first_paren+1:sec_paren]

    return first_ltr


def isnetid(s):
    """
    Returns True if s is a valid Cornell netid.
    
    Cornell network ids consist of 2 or 3 lower-case initials followed by a 
    sequence of digits.
    
    Examples:
        isnetid('wmw2') returns True
        isnetid('2wmw') returns False
        isnetid('ww2345') returns True
        isnetid('w2345') returns False
        isnetid('WW345') returns False
    
    Parameter s: the string to check
    Precondition: s is a string
    """
    # is network id lower?
    lower = s[:3].islower()

    # is network id 2 or 3 letters
    ltr = s.isalnum()
    
    # is network id a squence of digits
    seq_dig = s[2:3].isalnum()
    
    if seq_dig == s[2:3].isdigit():
        seq_dig = s[2:].isdigit()

    else:
        seq_dig = True

    findings = lower and ltr and seq_dig

    return findings