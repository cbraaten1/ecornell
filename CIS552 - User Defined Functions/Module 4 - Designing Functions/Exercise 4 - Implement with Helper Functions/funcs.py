"""
A function with several helpers.

The primary function in this module is str_to_seconds.  The functions get_hours,
get_minutes, and get_seconds are all helper functions that are used to implement
this function.  They should implemented in the order listed.

Author: Connor Braaten
Date: November 16, 2021
"""
import introcs


def get_seconds(time):
    """
    Returns the number of seconds in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_seconds('12:35:15') returns 15
    Example: get_seconds('03:02:05') returns 5
    Example: get_seconds('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """

    digit = time[6:]
    return int(digit)

def get_minutes(time):
    """
    Returns the number of minutes in the string time (as an int).

    The value time is a string in extended ISO 8601 format. That is, it has the form
    'hh:mm:ss' where h, m, and s are digits. There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_minutes('12:35:15') returns 35
    Example: get_minutes('12:02:05') returns 2
    Example: get_minutes('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """

    digit2 = time[3:5]
    return int(digit2)

def get_hours(time):
    """
    Returns the number of hours in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: get_hours('12:35:15') returns 12
    Example: get_hours('03:02:05') returns 3
    Example: get_hours('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """

    digit3 = time[:2]
    return int(digit3)

def str_to_seconds(time):
    """
    Returns the number of seconds since midnight in the string time (as an int).

    The value time is a string in extended ISO 8601 format.  That is, it has the form
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for
    hours, minutes, and seconds, so they are padded with 0s when necessary.  So
    seconds, minutes, and hours may have leading 0s if they are only one digit. For
    more information, see

        https://en.wikipedia.org/wiki/ISO_8601#Times

    This function does not support time zones, abbreviated formats, or decimals

    Example: str_to_seconds('12:35:15') returns 45315
    Example: str_to_seconds('03:02:05') returns 10925
    Example: str_to_seconds('00:00:00') returns 0

    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """

    return (get_hours(time)*3600) + (get_minutes(time)*60) + get_seconds(time)
