# test_ will help the python to recognize this ass a test
# in Terminal: cls to clear terminal
# pytest -v -p no:warnings

import pytest
import math_func
import sys # getting version of python

# all unit tests must have this test_ at the beginning
# @pytest.mark.number   # decorator
# @pytest.mark.skip(reason="Do not execute this test unit at the moment. (Reza Vedad) ")
# @pytest.mark.skipif(sys.version_info > (3, 3) , reason="Version not supported.")
def test_add() :
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9

# @pytest.mark.number
def test_product() :
    assert math_func.product(5, 5) ==25
    assert math_func.product(5) == 10

# hyphen v
# in Terminal : pytest test_math_func.py -v  ,  v: verbose for more info
# in Terminal : pytest or pytest -v (test_ already in name)

# @pytest.mark.string
def test_add_strings() :
    result = math_func.add('hello', ' world')
    assert result == 'hello world'
    assert type(result) is str
    assert 'hekllo' not in result


# @pytest.mark.string
def test_product_strings() :
    assert math_func.product('hello ', 3) == 'hello hello hello '
    result = math_func.product('hello ')
    assert result == 'hello hello '
    assert type(result) is str
    assert 'hello' in result

# pytest test_math_func.py::test_add -v  ,  just testing the first test unit
# pytest -v -k "add"   ,  tests with  add  keyword
# pytest -v -k "add or string"  , tests with   add or string   keyword
# pytest -v -k "add and string"


# marker
# using markers needs decorators as defined in code above
# pytest -v -m number

# hyphen x
# pytest -v -x  ,  means exist first  ,  the  code execution will stop


# pytest -v --tb=no  ,  less info , just passed or not , stack trace will not be shown

# pytest -v --maxfail=2  ,  here the code execution stops after second failare

# Warnings
# pytest -v -W ignore::DeprecationWarning
# pytest -v -p no:warnings  , no warnings at all

# Skipping
# @pytest.mark.number  change to : @pytest.mark.skip(reason="Do not execute this test unit at the moment. (Reza Vedad) ")
# skip if
# @pytest.mark.skipif(sys.version_info < (3, 3) , reason="Do not execute this test unit at the moment. (Reza Vedad) ")
# python --version