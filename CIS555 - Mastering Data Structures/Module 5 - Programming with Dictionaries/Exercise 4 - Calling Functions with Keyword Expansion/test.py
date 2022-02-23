"""
Partially completed test script for keyword expansion

Author: Connor Braaten
Date: February 15, 2022
"""
import introcs
import func


def test_circ_area():
    """
    Test procedure for function circ_area().
    """
    print('Testing circ_area()')
    
    result = func.circ_area(radius=3)
    introcs.assert_floats_equal(28.27433,result)
    
    result = func.circ_area(radius=2)
    introcs.assert_floats_equal(12.56637,result)
    
    result = func.circ_area(diameter=4)
    introcs.assert_floats_equal(12.56637,result)
    
    # Test for crashes
    try:
        func.circ_area()
        introcs.assert_true(False) # We should never reach this line!
    except:
        pass
    
    try:
        func.circ_area(radius=3,diameter=6)
        introcs.assert_true(False) # We should never reach this line!
    except:
        pass
    
    # Add a test with additional arguments
    test = {'radius': 5, 'diameter': 3, 'cool': 1}
    result = func.circ_area(radius=5)
    introcs.assert_floats_equal(78.53982,result)

if __name__ == '__main__':
    test_circ_area()
    print('Module func passed all tests.')