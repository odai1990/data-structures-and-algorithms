
from hashtable.hashtable import HashTable

def test_add_key():
    """
    1.Adding a key/value to your hashtable results in the value being in the data structure
    """
    ht = HashTable(1024)
    ht.add('one', 1)
    assert ht.contains('one') == True

def test_get():
    """
    2.Retrieving based on a key returns the value stored
    3.Successfully returns null for a key that does not exist in the hashtable
    """
    ht = HashTable(1024)
    ht.add('five', 5)
    assert ht.get('five') == 5
    assert ht.get('tiger') == None 

def test_add_multiple_collision():
    """  
    4.Successfully handle a collision within the hashtable
    5.Successfully retrieve a value from a bucket within the hashtable that has a collision
    6.Successfully retrieve a value from a bucket within the hashtable that has a collision
    """
    ht = HashTable(1024)
    ht.add('one', 1)
    ht.add('two', 2)
    ht.add('two', 3)
    assert ht.contains('one') == True
    assert ht.contains('two') == True
    assert ht.get('two') == 2
   



def test_hash():
    """
    6.Successfully hash a key to an in-range value
    """

    ht = HashTable(1024)
    ht.add('four', 4)
    assert ht.contains('four') == True
    assert ht.contains('whale') == False


