"""
A function to check the validity of a numerical string

Author: Connor Braaten
Date: December 24, 2021
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    str_length = len(s)
    # No comma
    new_s = introcs.split(s,',')

    new_s = introcs.join(new_s,'')

    if not introcs.isdigit(new_s):
        return False

    if s[0] == '0' and str_length > 1:
        return False

    if str_length > 3 and introcs.find_str(s,',') == -1:
        return False

    if str_length >= 5 and s[-4] != ',':
        return False

    if str_length >= 8 and s[1] != ',':
        return False
    
    if str_length == 2 and s[1] == ',':
        return False

    if str_length == 3 and s[2] == ',':
        return False
        
    if str_length <= 4 and introcs.find_str(s,',') != -1:
        return False

    if s[0] == ',':
        return False

    return True
