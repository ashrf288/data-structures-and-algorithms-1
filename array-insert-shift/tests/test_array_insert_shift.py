from array_insert_shift import __version__
from array_insert_shift.the_code import insertShiftArray

def test_version():
    assert __version__ == '0.1.0'

def test_even_length():
    actual=insertShiftArray([1,2,3,4,5,6],100)
    expected=[1,2,3,100,4,5,6]
    assert actual==expected

def test_odd_length():
    actual=insertShiftArray([1,2,3,4,5],100)
    expected=[1,2,3,100,4,5]
    assert actual==expected

def test_long_length():
    actual=insertShiftArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],100)

    expected=[1,2,3,4,5,6,7,8,9,10,100,11,12,13,14,15,16,17,18,19,20]
    assert actual==expected

