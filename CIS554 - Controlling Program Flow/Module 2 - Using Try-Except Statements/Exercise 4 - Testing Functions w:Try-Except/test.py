"""
A test script for the function iso_8601.

Author: Connor Braaten
Date: January 2, 2022
"""
import func
import introcs


def test_iso_8601():
    """
    Test procedure for the function iso_8601()
    """
    print('Testing iso_8601()')

    # Put your test cases here
    result = func.iso_8601('aa:12:34')
    introcs.assert_equals(False,result)

    result = func.iso_8601('12:34:56')
    introcs.assert_equals(True,result)

    result = func.iso_8601('600:12:34')
    introcs.assert_equals(False,result)

    result = func.iso_8601('12:34:))')
    introcs.assert_equals(False,result)

    result = func.iso_8601('1:34:45')
    introcs.assert_equals(True,result)

    result = func.iso_8601('00:12:3')
    introcs.assert_equals(False,result)

    result = func.iso_8601('00:1:34')
    introcs.assert_equals(False,result)

    result = func.iso_8601('0:')
    introcs.assert_equals(False,result)

    result = func.iso_8601('00:1234')
    introcs.assert_equals(False,result)

    result = func.iso_8601('001234')
    introcs.assert_equals(False,result)


if __name__ == '__main__':
    test_iso_8601()
    print('Module func passed all tests.')