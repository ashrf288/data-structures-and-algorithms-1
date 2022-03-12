import struct
from unittest import expectedFailure
from single_linked_list import __version__
from single_linked_list.single_linked_list import Linked_List

def test_version():
    assert __version__ == '0.1.0'


def test_exist():
    assert Linked_List


def test_creation():
    """
    1-test if it can successfully instantiate an empty linked list  
    """
    assert Linked_List()

def test_insert_one():
    """
    2-Can properly insert into the linked list

    3-The head property will properly point to the first node in the linked list
    
    """
    students=Linked_List()
    students.insert('eman')

    expected='eman'
    actual=students.head.value

    assert actual==expected






def  test_includes():
    """
    5-Will return true when finding a value within the linked list that exists

    """
    students=Linked_List()
    students.insert('eman')
    students.insert('elyas')
    students.insert('mohammad')
     
    assert students.includes('eman')
    
 
def  test_not_includes():
    """
    6- Will return false when searching for a value in the linked list that does not exist

    """
    students=Linked_List()
    students.insert('eman')
    students.insert('elyas')
    students.insert('mohammad')
     
    assert not students.includes('nadia')


