"""
Module with a function to read CSV files (converting them into a 2D list)

This function will be used in the main project.  You should hold on to it.

Author: Connor Braaten
Date: February 26, 2022
"""
import csv

from matplotlib.pyplot import close


def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.
    
    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the 
    programmer to interpret this data, since CSV files contain no type information.
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid CSV file
    """
    file = open(filename)
    wrapper = csv.reader(file)

    acc_list = []

    for row in wrapper:
        acc_list.append(row)

    file.close()

    return acc_list