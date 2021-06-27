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

    expected = [10, 15]
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








