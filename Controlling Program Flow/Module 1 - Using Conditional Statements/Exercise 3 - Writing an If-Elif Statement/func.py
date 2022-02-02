"""
A function to extract names from e-mail addresses.

Author: Connor Braaten
Date: December 19, 2021
"""
import introcs


def extract_name(s):
    """
    Returns the first name of the person in e-mail address s.

    We assume (see the precondition below) that the e-mail address is in one of
    three forms:

        last.first@megacorp.com
        last.first.middle@consultant.biz
        first.last@mompop.net

    where first, last, and middle correspond to the person's first, middle, and
    last name. Names are not empty, and contain only letters. Everything after the
    @ is guaranteed to be exactly as shown.

    The function preserves the capitalization of the e-mail address.

    Examples:
        extract_name('smith.john@megacorp.com') returns 'john'
        extract_name('McDougal.Raymond.Clay@consultant.biz') returns 'Raymond'
        extract_name('maggie.white@mompop.net') returns 'maggie'
        extract_name('Bob.Bird@mompop.net') returns 'Bob'

    Parameter s: The e-mail address to extract from
    Precondition: s is in one of the two address formats described above
    """
    # You must use an if-elif-else statement in this function.
    period = introcs.find_str(s,'.')
    at = introcs.find_str(s,'@')
    period2 = introcs.find_str(s,'.',start=period+1)
    net = introcs.endswith_str(s,'net')
    biz = introcs.endswith_str(s,'biz')

    FirstName = s[period+1:at]
    LastName = s[:period]
    MiddleName = s[period+1:period2]

    if net == True:
        first = LastName
        FLName = first
    elif biz == True:
        middle = MiddleName
        FLName = middle
    else:
        last = FirstName
        FLName = last

    return FLName
