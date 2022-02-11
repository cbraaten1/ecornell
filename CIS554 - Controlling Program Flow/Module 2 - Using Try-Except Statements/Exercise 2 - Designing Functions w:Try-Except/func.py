"""
A function to test for floats in European format

Author: Connor Braaten
Date: January 1, 2022
"""
import introcs


def iseurofloat(s):
    """
    Returns True if s is a float in European format.  Returns False otherwise.

    In European format, a comma is used in place of a decimal point.  So '12,5' stands
    for 12.5, '0,12' stands for 0.12 and so.  Formally, a string is in European format
    if it is of the form <d1>,<d2> where d1 and d2 are ints (and d2 >= 0).  See

        https://en.wikipedia.org/wiki/Decimal_separator

    for more information.

    This function does not recognize floats in scientific notation (e.g. '1e-2').

    Examples:
        iseurofloat('12,5') returns True
        iseurofloat('-12,5') returns True
        iseurofloat('12') returns False
        iseurofloat('12,-5') returns False
        iseurofloat(',5') returns False
        iseurofloat('apple') returns False
        iseurofloat('12,5.3') returns False
        iseurofloat('12,5,3') returns False
        iseurofloat('1e-2') returns False

    Parameter s: The string to check
    Precondition: s is a string
    """
    # You MAY NOT use conditionals anywhere in this function.
    try:
        comma = introcs.find_str(s,',')
        print(comma)

        before_comma = introcs.strip(s[:comma],'-')
        print(before_comma)

        has_comma = introcs.find_str(s,',') >= 1
        print(has_comma)

        numeric = introcs.isnumeric(before_comma)
        print(numeric)

        after_comma = s[comma+1:]
        print(after_comma)

        numeric2 = introcs.isnumeric(after_comma)
        print(numeric2)

        is_true = numeric and numeric2 and has_comma
        print(is_true)
        
        return is_true

    except:
        return False