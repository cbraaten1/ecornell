"""
Module demonstrating immutable functions on nested lists.

All of these functions make use of accumulators that make new lists.

Author: Connor Braaten
Date: February 10, 2022
"""


def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.
    
    This function assumes that table has no header, so each row has only numbers in it.
    
    Examples: 
        row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) returns [0.8, 1.5, 1.7]
        row_sums([[0.2,0.1],[-0.2,0.1],[0.2,-0.1],[-0.2,-0.1]]) returns [0.3, -0.1, 0.1, -0.3]
    
    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words, 
        (1) table is a nested 2D list in row-major order, 
        (2) each row contains only numbers, and 
        (3) each row is the same length.
    """
    result = []
    
    for row in table:
        acc_table = 0

        for item in row:
            acc_table = acc_table + item

        result.append(acc_table)

    return result


def crossout(table,row,col):
    """
    Returns a copy of the table, missing the given row and column.
      
    Examples:
        crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
        crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
        crossout([[1,3],[6,2]],0,0) returns [[2]]
        crossout([[6]],0,0) returns []
    
    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words, 
        (1) table is a nested 2D list in row-major order, 
        (2) each row contains only numbers, and 
        (3) each row is the same length.
    
    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table
    
    Parameter col: the colummn to remove
    Precondition: col is an index (int) for a column of table
    """
    result = []

    for item in range(len(table)):
        if item == row:
            continue

        new_row = []
        for index in range(len(table[item])):
            if index != col:
                new_row.append(table[item][index])

        result.append(new_row)

    return result