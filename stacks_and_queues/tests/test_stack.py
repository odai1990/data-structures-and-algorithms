from stacks_and_queues.stack import Stack
from stacks_and_queues.node import Node

import pytest

def test_push(stack_vals):
    '''
    1.Can successfully push onto a stack
    2.Can successfully push multiple values onto a stack
    '''
    actual = stack_vals.top.value
    expected = 'a'
    assert actual == expected

def test_pop(stack_vals):
    '''
    3.Can successfully pop off the stack
    '''
    actual = stack_vals.pop()
    expected = 'a'
    assert actual == expected
    assert stack_vals.top.value == -2


def test_pop_all(stack_vals):
    '''
    4.Can successfully empty a stack after multiple pops
    '''
    actual = stack_vals.pop()
    actual = stack_vals.pop()
    actual = stack_vals.pop()
    actual = stack_vals.is_empty()
    expected = True
    assert actual == expected


def test_peek(stack_vals):
    '''
    5.Can successfully peek the next item on the stack
    '''
    actual = stack_vals.pop()
    actual = stack_vals.peek()
    expected = -2
    assert actual == expected
    assert stack_vals.top.value == -2


def test_create_empty_stack():
    '''
    6.Can successfully instantiate an empty stack
    '''
    actual = Stack()  
    expected = None 
    assert actual.top == expected


def test_is_empty(stack_vals):
    '''
    Testing empty  stack 
    '''
    assert stack_vals.is_empty() == False




def test_pop_empty(stack_empty_vals):
    '''
    7.Calling pop on empty stack raises exception
    '''

    with pytest.raises(Exception) as info:
        actual = stack_empty_vals.pop()      
        expected =info
        assert actual == expected  
 

def test_peek_empty(stack_empty_vals):
    '''
    7.Calling peek on empty stack raises exception
    '''
    with pytest.raises(Exception) as info:
        actual = stack_empty_vals.peek()      
        expected =info
        assert actual == expected  



# Decorator
@pytest.fixture
def stack_vals():
    stack = Stack()
    stack.push(10)
    stack.push(-2)
    stack.push('a')
    return stack

@pytest.fixture
def stack_empty_vals():
    stack = Stack()  
    return stack
