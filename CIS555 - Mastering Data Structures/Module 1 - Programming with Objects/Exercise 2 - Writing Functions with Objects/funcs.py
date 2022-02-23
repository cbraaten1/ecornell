"""
Module demonstrating how to write functions with objects.

This module contains two versions of the same function.  One version returns a new
value, while other modifies one of the arguments to contain the new value.

Author: Connor Braaten
Date: February 3, 2022
"""

import clock


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object
    
    DO NOT ALTER time1 or time2, even though they are mutable
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    found_hours = time1.hours + time2.hours

    found_minutes = time1.minutes + time2.minutes

    if found_minutes > 59:
        found_minutes = found_minutes - 60
        found_hours = found_hours + 1
    
    else:
        found_minutes

    class_type = clock.Time(found_hours,found_minutes)

    return class_type

def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2
    
    DO NOT RETURN a new time object.  Modify the object time1 instead.
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    time1.hours = time1.hours + time2.hours

    new_time1 = time1.minutes + time2.minutes

    if new_time1 > 59:
        time1.hours = time1.hours + 1
        time1.minutes = new_time1 - 60
    
    else:
        time1.minutes = new_time1