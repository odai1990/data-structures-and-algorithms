from stacks_and_queues.queue import Queue
from stacks_and_queues.node import Node

import pytest


def test_enqueue(queue_vals):
    '''
    8.Can successfully enqueue into a queue
    9.Can successfully enqueue multiple values into a queue
    '''
    assert queue_vals.rear.value == 'hi'
    assert queue_vals.front.value == 10

def test_dequeue(queue_vals):
    '''
    10.Can successfully dequeue out of a queue the expected value
    '''

    assert queue_vals.dequeue() == 10
    assert queue_vals.front.value == 'odai'

def test_peek_queue(queue_vals):
    '''
    11.Can successfully peek into a queue, seeing the expected value
    '''
    assert queue_vals.peek() == 10

def test_dequeue_to_empty(queue_vals):
    '''
    12.Can successfully empty a queue after multiple dequeues
    '''
    queue_vals.dequeue()
    queue_vals.dequeue()
    queue_vals.dequeue()
    queue_vals.dequeue()
    assert queue_vals.front == None



def test_create_empty_queue():
    '''
    13.Can successfully instantiate an empty queue
    '''
    actual = Queue()  
    expected = None 
    assert actual.front == expected


def test_peek_empty_quque(queue_vals):
    '''
    14.Calling dequeue or peek queue raises exception
    '''

    with pytest.raises(Exception) as info:
        actual = queue_vals.peek()      
        expected =info
        assert actual == expected  
 




def test_is_empty(queue_vals):
    '''
    test is empty method
    '''
    assert queue_vals.is_empty() == False


#Decorator
@pytest.fixture
def queue_vals():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue('odai')
    queue.enqueue(-66)
    queue.enqueue('hi')
    return queue