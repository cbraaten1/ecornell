"""
The test script for the course project.

Author: Connor Braaten
Date: November 22, 2021
"""

import introcs
import funcs

def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')

    result = funcs.matching_parens('((D) E) F')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('D (E) F')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('(D) (E F')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('()()')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens(')D E( F')
    introcs.assert_equals(False,result)

    result = funcs.matching_parens(')(F)(')
    introcs.assert_equals(True,result)

    result = funcs.matching_parens('())D E F(')
    introcs.assert_equals(True,result)

def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')

    result = funcs.first_in_parens('((D) E F)')
    introcs.assert_equals('(D',result)

    result = funcs.first_in_parens('(D) E F')
    introcs.assert_equals('D',result)

    result = funcs.first_in_parens('D ((E) F')
    introcs.assert_equals('(E',result)

    result = funcs.first_in_parens('D (E) (F)')
    introcs.assert_equals('E',result)

    result = funcs.first_in_parens('(D E F)')
    introcs.assert_equals('D E F',result)

#Script Code
test_matching_parens()
test_first_in_parens()

print('Module funcs is working correctly')
