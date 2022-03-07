from binary_search import __version__
from binary_search.binary_search import binary_search

def test_version():
    assert __version__ == '0.1.0'

def test_1():
    actual=binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 5)
    expected=4
    assert actual==expected

def test_2():
    actual=binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 2)
    expected=1
    assert actual==expected

def test_3():
    actual=binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 12)
    expected=11
    assert actual==expected

