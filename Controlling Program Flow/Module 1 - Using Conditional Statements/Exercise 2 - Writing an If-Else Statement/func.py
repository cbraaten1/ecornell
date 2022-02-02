"""
A function to extract names from e-mail addresses.

Author: Connor Braaten
Date: December 17, 2021
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.

    We assume (see the precondition below) that the e-mail address is in one of
    two forms:

        last.first@megacorp.com
        first.last@mompop.net

    where first and last correspond to the person's first and last name.  Names
    are not empty, and contain only letters. Everything after the @ is guaranteed
    to be exactly as shown.

    The function preserves the capitalization of the e-mail address.

    Examples:
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'

    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    # You must use an if-else statement in this function.
    period = introcs.find_str(s,'.')
    at = introcs.find_str(s,'@')
    net = introcs.endswith_str(s,'net')

    FirstName = s[period+1:at]
    LastName = s[:period]

    if net == True:
        first = LastName
        FLName = first
    else:
        last = FirstName
        FLName = last

    return FLName
