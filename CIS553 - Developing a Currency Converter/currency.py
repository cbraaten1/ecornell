"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Connor Braaten
Date: December 10, 2021
"""

import introcs

APIKEY = 'wviDkzp4UptcPUgm1KoBFWRjdbkRofOx7IVobzyRcpMe'

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str
    assert introcs.count_str(s,' ') >= 1

    space = introcs.find_str(s,' ')
    result = s[:space]
    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str
    assert introcs.count_str(s,' ') >= 1

    space = introcs.find_str(s,' ')
    result = s[space+1:]
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s) == str
    assert introcs.count_str(s,'"') >= 2

    first = introcs.find_str(s,'"')
    second = introcs.find_str(s,'"',first+1)
    result = s[(first+1):second]
    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    sub_string = '"src":'
    index = introcs.find_str(json,sub_string)
    new_str = json[index+len(sub_string):]
    return first_inside_quotes(new_str)


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    sub_string = '"dst":'
    index = introcs.find_str(json,sub_string)
    new_str = json[index+len(sub_string):]
    return first_inside_quotes(new_str)


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    search_string = '"error":'
    location_of_error_key = introcs.find_str(json, search_string)
    error_message = first_inside_quotes(json[location_of_error_key +
                                             len(search_string):])
    is_there_an_error = len(error_message) > 0
    return is_there_an_error


def service_response(src,dst,amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert src != '' and  introcs.isalpha(src)
    assert dst != '' and  introcs.isalpha(dst)
    assert type(amt) == float or type(amt) == int
    x = f'https://ecpyfac.ecornell.com/python/currency/fixed?src={src}'+\
    '&dst={dst}&amt={amt}&key=wviDkzp4UptcPUgm1KoBFWRjdbkRofOx7IVobzyRcpMe'
    url = introcs.urlread(x)
    return url


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert currency != '' and  introcs.isalpha(currency)
    web_service = service_response(currency,currency,1)
    is_valid = has_error(web_service)
    return not is_valid


def exchange(src,dst,amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert iscurrency(src)
    assert iscurrency(dst)
    assert type(amt) == float or type(amt) == int
    response = service_response(src,dst,amt)
    is_dst = get_dst(response)
    is_amt = introcs.split(is_dst,' ')
    return float(is_amt[0])
