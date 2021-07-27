from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.tree import BinarySearchTree
from hashmap_tree_intersection.tree_intersection import TreeIntersection


def test_version():
    assert __version__ == '0.1.0'


def test_happy_case():
    tree1 = BinarySearchTree()
    tree1.add(10)
    tree1.add(5)
    tree1.add(6)
  
    tree2 = BinarySearchTree()
    tree2.add(1)
    tree2.add(5)
    tree2.add(2)
    test=TreeIntersection(1024)
    expected=test.tree_intersection(tree1,tree2)
    actual=[5]
    assert expected==actual


def test_no_match():
    tree1 = BinarySearchTree()
    tree1.add(10)
    tree1.add(4)
    tree1.add(6)
  
    tree2 = BinarySearchTree()
    tree2.add(1)
    tree2.add(5)
    tree2.add(2)
    test=TreeIntersection(1024)
    expected=test.tree_intersection(tree1,tree2)
    actual=[]
    assert expected==actual


def test_array_long_than_other():
    tree1 = BinarySearchTree()
    tree1.add(10)
    tree1.add(4)
    tree1.add(6)
    tree1.add(5)
    tree1.add(44)
    tree1.add(655)
  
    tree2 = BinarySearchTree()
    tree2.add(1)
    tree2.add(5)
    tree2.add(2)
    test=TreeIntersection(1024)
    expected=test.tree_intersection(tree1,tree2)
    actual=[5]
    assert expected==actual

def test_array_long_than_other_and_have_repeted_number_in_same_array():
    tree1 = BinarySearchTree()
    tree1.add(10)
    tree1.add(4)
    tree1.add(6)
    tree1.add(5)
    tree1.add(5)
    tree1.add(6)
  
    tree2 = BinarySearchTree()
    tree2.add(3)
    tree2.add(5)
    tree2.add(10)
    test=TreeIntersection(1024)
    expected=test.tree_intersection(tree1,tree2)
    actual=[10,5]
    assert expected==actual



def test_other_solution():
    tree1 = BinarySearchTree()
    tree1.add(10)
    tree1.add(4)
    tree1.add(6)
    tree1.add(5)
    tree1.add(5)
    tree1.add(6)
  
    tree2 = BinarySearchTree()
    tree2.add(3)
    tree2.add(5)
    tree2.add(10)
    test=TreeIntersection(1024)
    expected=test.tree_intersection_without_hashtabke(tree1,tree2)
    actual=[10,5]
    assert expected==actual


