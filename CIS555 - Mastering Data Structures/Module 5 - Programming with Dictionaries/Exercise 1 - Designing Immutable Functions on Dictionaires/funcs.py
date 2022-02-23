"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: Connor Braaten
Date: February 22, 2022
"""


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    acc_avg_grade = 0

    if adict == {}:
        return 0.0

    for avg in adict:
        if adict[avg] == 0:
            acc_avg_grade = 0

        elif adict[avg] > acc_avg_grade:
            acc_avg_grade = acc_avg_grade + adict[avg]

        else:
            acc_avg_grade = acc_avg_grade + adict[avg]

    return acc_avg_grade/len(adict)


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.
    
    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a 
    new dictionary with netids for keys and letter grades (strings) for values.
    
    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60 
    is an F.
    
    Examples:  
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}
    
    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    acc_letter_grades = {}

    if adict == {}:
        return {}

    for student, grade in adict.items():
        if grade >= 90:
            grade = 'A'
            acc_letter_grades[student] = grade

        elif grade >= 80:
            grade = 'B'
            acc_letter_grades[student] = grade

        elif grade >= 70:
            grade = 'C'
            acc_letter_grades[student] = grade

        elif grade >= 60:
            grade = 'D'
            acc_letter_grades[student] = grade

        elif grade < 60:
            grade = 'F'
            acc_letter_grades[student] = grade

    return acc_letter_grades