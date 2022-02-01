"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Connor Braaten
Date: December 10, 2021
"""

import introcs
import currency

def test_before_space():
    """
    Test procedure for before_space
    """
    print('Testing before_space')
    result = currency.before_space('Your currency')
    introcs.assert_equals('Your',result)

    result = currency.before_space('The currency ')
    introcs.assert_equals('The',result)

    result = currency.before_space('Amount  of')
    introcs.assert_equals('Amount',result)

    result = currency.before_space('The  amount   currency')
    introcs.assert_equals('The',result)


def test_after_space():
    """
    Test procedure for after_space
    """
    print('Testing after_space')
    result = currency.after_space('Your currency')
    introcs.assert_equals('currency',result)

    result = currency.after_space('The currency ')
    introcs.assert_equals('currency ',result)

    result = currency.after_space('Amount  of')
    introcs.assert_equals(' of',result)

    result = currency.after_space('The     amount')
    introcs.assert_equals('    amount',result)


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes
    """
    print('Testing first_inside_quotes')
    result = currency.first_inside_quotes('"Your currency"')
    introcs.assert_equals('Your currency',result)

    result = currency.first_inside_quotes('"The" "currency"')
    introcs.assert_equals('The',result)

    result = currency.first_inside_quotes('Amount "of "')
    introcs.assert_equals('of ',result)

    result = currency.first_inside_quotes('""')
    introcs.assert_equals('',result)


def test_get_src():
    """
    Test procedure for get_src
    """
    print('Testing get_src')
    result = currency.get_src('{"success":true, "src":"2 United States Dollars", '+
                              '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success": true, "src": "10 Canadian Dollars", '+
                              '"dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('10 Canadian Dollars',result)

    result = currency.get_src('{"success":false,"src":"","dst":"",'+
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_src('{"success": false,"src": "","dst": "",'+
                              '"error": "Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print('Testing get_dst')
    result = currency.get_dst('{"success":false,"src":"","dst":"",'+
                              '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_dst('{"success": false,"src": "","dst": "",'+
                              '"error": "Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_dst('{"success":true,"src":"2 United States Dollars",'+
                              '"dst":"1.772814 Euros","error":""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success": true,"src": "2 United States Dollars",'+
                              '"dst": "2.55 Canadian Dollars","error": ""}')
    introcs.assert_equals('2.55 Canadian Dollars',result)


def test_has_error():
    """
    Test procedure for has_error
    """
    print('Testing has_error')
    result = currency.has_error('{"success": false,"src": "","dst": "",'+
                                '"error": "Source currency code is invalid."}')
    introcs.assert_true(True,result)

    result = currency.has_error('{"success":false,"src":"","dst":"",'+
                                '"error":"Source currency code is invalid."}')
    introcs.assert_true(True,result)

    result = currency.has_error('{"success":true, "src":"2 United States Dollars", '+
                                '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(False,result)

    result = currency.has_error('{"success": true, "src": "2 United States Dollars", '+
                                '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(False,result)


def test_service_response():
    """
    Test procedure for service_response
    """
    print('Testing service_response')
    result = currency.service_response('USD','CAD',1.0)
    introcs.assert_equals('{"success": true, "src": "1.0 United States Dollar", '+
                          '"dst": "1.30395 Canadian Dollars", "error": ""}',result)

    result = currency.service_response('ABC','USD',1.0)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", '+
                          '"error": "The rate for currency ABC is not present."}',result)

    result = currency.service_response('USD','ABC',1.0)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", '+
                          '"error": "The rate for currency ABC is not present."}',result)

    result = currency.service_response('USD','CAD',-1)
    introcs.assert_equals('{"success": true, "src": "-1.0 United States Dollar", '+
                          '"dst": "-1.30395 Canadian Dollars", "error": ""}',result)


def test_iscurrency():
    """
    Test procedure for iscurrency
    """
    print('Testing iscurrency')
    result = currency.iscurrency('ABC')
    introcs.assert_equals(False,result)

    result = currency.iscurrency('USD')
    introcs.assert_equals(True,result)


def test_exchange():
    """
    Test procedure for exchange
    """
    print('Testing exchange')
    result = currency.exchange('USD','CAD',1.0)
    introcs.assert_floats_equal(1.30395,result)

    result = currency.exchange('USD','CAD',-2.0)
    introcs.assert_floats_equal(-2.6079,result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print('All tests completed successfully')
