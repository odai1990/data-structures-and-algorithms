# from trees import __version__


# def test_version():
#     assert __version__ == '0.1.0'

import pytest
from trees.trees import BinaryTree, BinarySearchTree, Node
def test_tree_instance():
    tree = BinaryTree()
    assert tree.root is None

def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree.root.value == 'apples'


def test_three_members():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15


def test_pre_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    expected = [10,5,15]
    actual = tree.pre_order()

    assert expected == actual

def test_in_order():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(15)

    expected = [10]
    actual = tree.in_order()

    assert expected == actual


def test_find_max():

    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(-20)
    tree.add(1)
 
    assert tree.find_maximum_value()==15



def test_breadth_first():

    tree = BinarySearchTree()
    tree.add(2)
    tree.add(7)
    tree.add(5)
    tree.add(2)
    tree.add(6)
    tree.add(9)
    tree.add(5)
    tree.add(11)
    tree.add(4)
    
 
    assert tree.breadth_first()==[2, 7, 5, 2, 6, 9, 5, 11, 4]


def test_breadth_first_empty_list():

    tree = BinarySearchTree()
 
    
 
    assert tree.breadth_first()=='tree is empty'








