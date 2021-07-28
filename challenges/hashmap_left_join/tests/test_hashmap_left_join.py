from hashmap_left_join import __version__

from hashmap_left_join.hashmap_left_join import hashmap_left_join
from hashmap_left_join.hashtable import HashTable

def test_version():
    assert __version__ == '0.1.0'


def test_happy_case():
    map_a = HashTable(1024)
    map_a.add('one', 1)    
    map_a.add('two', 3)
    map_a.add('three', 8)

    map_b = HashTable(1024)
    map_b.add('one', 9)
    map_b.add('tow', 6)
    map_b.add('three', 8)
    assert hashmap_left_join(map_a,map_b)==[['one', 1, 9], ['three', 8, 8], ['two', 3, None]]

def test_first_hash_biger():
    map_a = HashTable(1024)
    map_a.add('one', 1)
    map_a.add('two', 2)
    map_a.add('three', 3)
    map_a.add('four', 8)

    map_b = HashTable(1024)
    map_b.add('one', 9)
    map_b.add('four', 6)
    map_b.add('two', 8)
    
    assert hashmap_left_join(map_a,map_b)==[['one', 1, 9], ['three', 3, 'Null'], ['two', 2, 8], ['four', 8, 6]]

def test_second_hash_biger():
    map_a = HashTable(1024)
    map_a.add('one', 1)
    map_a.add('two', 2)    
    map_a.add('four', 8)

    map_b = HashTable(1024)
    map_b.add('one', 9)
    map_b.add('five', 6)
    map_b.add('two', 8)
    map_b.add('three', 3)
    assert hashmap_left_join(map_a,map_b)==[['one', 1, 9], ['two', 2, 8], ['four', 8, 'Null']]
