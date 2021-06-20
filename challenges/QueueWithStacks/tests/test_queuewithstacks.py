from queuewithstacks import __version__
from queuewithstacks.queue_with_stacks import PseudoQueue 
import pytest

def test_version():
    assert __version__ == '0.1.0'



def test_enqueue_multiple_element():
    '''
    check if we can add element to queue without any issues
    '''
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue()==1


def test_dequeue_multiple_element():
    '''
    check if we can return and delete elements from queue without any issues
    '''
    queue=PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()    
    assert queue.dequeue()==2


def test_dequeue_from_empty_queue():
    '''
    check if we can return and delete elements from queue without any issues
    '''
    with pytest.raises(Exception):
        queue=PseudoQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()
        assert queue.dequeue()=='You cant pop from empty stack'
