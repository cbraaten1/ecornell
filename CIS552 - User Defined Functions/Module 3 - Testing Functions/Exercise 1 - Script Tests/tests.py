"""
A test script to test the module funcs.py

Author: Connor Braaten
Date: November 11, 2021
"""
import introcs      # For assert_equals
import funcs        # This is what we are testing


# Put your code below this line
#Test Case 1
result = funcs.has_a_vowel('aeiou')
introcs.assert_equals(True,result)

#Test Case 2
result = funcs.has_a_vowel('a')
introcs.assert_equals(True,result)

#Test Case 3
result = funcs.has_a_vowel('e')
introcs.assert_equals(True,result)

#Test Case 4
result = funcs.has_a_vowel('i')
introcs.assert_equals(True,result)

#Test Case 5
result = funcs.has_a_vowel('o')
introcs.assert_equals(True,result)

#Test Case 6
result = funcs.has_a_vowel('u')
introcs.assert_equals(True,result)

#Test Case 7
result = funcs.has_a_vowel('ae')
introcs.assert_equals(True,result)

#Test Case 8
result = funcs.has_a_vowel('ai')
introcs.assert_equals(True,result)

#Test Case 9
result = funcs.has_a_vowel('ao')
introcs.assert_equals(True,result)

#Test Case 10
result = funcs.has_a_vowel('au')
introcs.assert_equals(True,result)

# Do not write below this line
print('Module funcs is working correctly')
