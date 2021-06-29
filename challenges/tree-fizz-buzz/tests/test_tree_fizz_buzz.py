from tree_fizz_buzz import __version__
import pytest
from tree_fizz_buzz.tree_fizz_buzz import tree_fizz_buzz,KAryTree,Node

def test_version():
    assert __version__ == '0.1.0'

def test_adding_to_tree(insert_elements):
    
    '''
    To check if the tree have new elemnts 
    '''
    # checking root
    assert insert_elements.root.value==1
    # checking one of levels of tree 
    assert insert_elements.root.child[0].child[1].value==51




def test_tree_fizz_buzz_function(insert_elements):
    
    '''
    To check if tree_fizz_buzz working correctly
    '''

    # call the function and check if this return KAryTree calss type
    tree=tree_fizz_buzz(insert_elements)
    assert isinstance(insert_elements,KAryTree)

    #check some values to see they fizz , buss , fizzBuzz or string

    assert tree.child[2].value=='Buzz'   
    assert tree.child[0].child[0].value=='FizzBuzz'   
    assert tree.child[2].child[2].value=='Fizz'  
    assert isinstance(tree.child[0].child[2].value, str)  





@pytest.fixture
def insert_elements():
    K_ary_tree=KAryTree()
    K_ary_tree.root=Node(1)
    K_ary_tree.root.child.append(Node(2))
    K_ary_tree.root.child.append(Node(5))
    K_ary_tree.root.child.append(Node(10))


    K_ary_tree.root.child[0].child.append(Node(30))
    K_ary_tree.root.child[0].child.append(Node(51))
    K_ary_tree.root.child[0].child.append(Node(43))


    K_ary_tree.root.child[1].child.append(Node(6))
    K_ary_tree.root.child[1].child.append(Node(8))
    K_ary_tree.root.child[1].child.append(Node(7))



    K_ary_tree.root.child[2].child.append(Node(-5))
    K_ary_tree.root.child[2].child.append(Node(-20))
    K_ary_tree.root.child[2].child.append(Node(-6))
    return K_ary_tree 
