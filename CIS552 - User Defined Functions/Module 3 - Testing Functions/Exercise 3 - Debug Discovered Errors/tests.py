"""
A test script to test the module func.py

Author: Connor Braaten
Date: November 13, 2021
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


def test_replace_first():
    """
    Test procedure for replace_first
    """
    print('Testing replace_first')

    # Put your tests below this line

    #Test Case 1
    result = funcs.replace_first('crane','a','o')
    introcs.assert_equals('crone',result)

    #Test Case 2
    result = funcs.replace_first('poll','l','o')
    introcs.assert_equals('pool',result)

    #Test Case 3
    result = funcs.replace_first('crane','cr','b')
    introcs.assert_equals('bane',result)

    #Test Case 4
    result = funcs.replace_first('hat','a','o')
    introcs.assert_equals('hot',result)

    #Test Case 5
    result = funcs.replace_first('peet','ee','ea')
    introcs.assert_equals('peat',result)

    #Test Case 6
    result = funcs.replace_first('heat','h','thr')
    introcs.assert_equals('threat',result)

    #Test Case 7
    result = funcs.replace_first('cole','e','d')
    introcs.assert_equals('cold',result)

    #Test Case 8
    result = funcs.replace_first('three','th','t')
    introcs.assert_equals('tree',result)

# Script Code
# Do not write below this line
test_replace_first()
print('Module funcs is working correctly')
