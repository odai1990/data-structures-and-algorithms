from linked_list.linked_list import Node, LinkedList
import pytest
from linked_list import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_list_creation():
  actual = LinkedList()
  assert actual.head == None


def test_insert_method():
  lst_one = LinkedList()
  lst_one.insert(1)
  lst_one.insert(2)
  lst_one.insert(3)

  assert lst_one.head.value == 3
  assert lst_one.head.next.value == 2
  assert lst_one.head.next.next.value == 1


def test_includes_method():
  lst_two = LinkedList()
  lst_two.insert('apples')
  lst_two.insert('pickles')
  lst_two.insert('chips')

  assert lst_two.includes('pickles') == True
  assert lst_two.includes('whales') == False


def test_to_string_method():
  lst_three = LinkedList()
  lst_three.insert(1)
  lst_three.append(2)
  lst_three.append(3)
  lst_three.append(4)
  lst_three.append(5)

  actual = lst_three.__str__()
  expected = '{1}-> {2}-> {3}-> {4}-> {5}-> '
  assert actual == expected


def test_append():
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  assert lst_four.head.next.value == 'banana'


######################Code Challenge: Class 06 test####################

def test_append_to_end():
  # add a node to the end of the linked list
    lst_four = LinkedList()
    lst_four.append('banana')
    assert lst_four.head.value == 'banana'


def test_append_to_multiple_end():
  # add multiple nodes to the end of a linked list
    lst_four = LinkedList()
    lst_four.append('banana')
    lst_four.append('apple')
    assert lst_four.head.value == 'banana'
    assert lst_four.head.next.value == 'apple'


def test_insert_before_middle():
  # insert a node before a node located i the middle of a linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  lst_four.insertBefore('banana', 'melon')
  assert lst_four.head.next.value == 'melon'


def test_insert_before_begining():
  # insert a node before the first node of a linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  lst_four.insertBefore('apple', 'watermelon')
  assert lst_four.head.value == 'watermelon'


def test_insert_before_empty():
 # add nodes to the begin of a linked list
  lst_four = LinkedList()
  assert lst_four.insertBefore('', '') == 'could not find that element'


def test_insert_after_middle():
  # insert after a node in the middle of the linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  lst_four.insertAfter('banana', 'strobary')
  lst_four.insertAfter('strobary', 'watermelon')
  assert lst_four.head.next.next.next.value == 'watermelon'
  assert lst_four.head.next.next.value == 'strobary'
  assert '{apple}-> {banana}-> {strobary}-> {watermelon}-> ' == lst_four.__str__()


def test_insert_after_end():
  # insert a node after the last node of the linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  lst_four.insertAfter('banana', 'strobary')
  assert lst_four.head.next.next.value == 'strobary'
  assert '{apple}-> {banana}-> {strobary}-> ' == lst_four.__str__()


def test_insert_after_empty():
    # add nodes to the None location of a linked list
    lst_four = LinkedList()
    assert lst_four.insertAfter('', '') == 'could not find that element'


######################Code Challenge: Class 07 test####################


def test_kth_method_out_of_range():
  # Where k is greater than the length of the linked list
  lst_seven = LinkedList()
  lst_seven.insert(1)
  lst_seven.append(2)
  lst_seven.append(3)
  lst_seven.append(4)
  lst_seven.append(5)
  with pytest.raises(Exception):
    lst_seven.ll_kth_from_end(6)


def test_kth_method_negative():
  # Where k is not a positive integer
  lst_seven = LinkedList()
  lst_seven.insert(1)
  lst_seven.append(2)
  lst_seven.append(3)
  lst_seven.append(4)
  lst_seven.append(5)
  with pytest.raises(Exception):
    lst_seven.ll_kth_from_end(-2)


def test_kth_method_same_as_length():
  # Where k and the length of the list are the same
  lst_seven = LinkedList()
  lst_seven.insert(1)
  lst_seven.append(2)
  lst_seven.append(3)
  lst_seven.append(4)
  lst_seven.append(5)
  assert lst_seven.ll_kth_from_end(5) == 1


def test_kth_method_length_one():
  # Where the linked list is of a size 1
  lst_seven = LinkedList()
  lst_seven.insert(1)
  assert lst_seven.ll_kth_from_end(1) == 1


def test_kth_method_middel():
  # 'Happy Path' where k is not at the end, but somewhere in the middle of the linked list
  lst_seven = LinkedList()
  lst_seven.insert(1)
  lst_seven.append(2)
  lst_seven.append(3)
  lst_seven.append(4)
  lst_seven.append(5)
  assert lst_seven.ll_kth_from_end(2) == 3


######################Code Challenge: Class 08 test####################

def test_merging_same():
  # 'Happy Path' the are same length
  lst_one = LinkedList()
  lst_one.append('apple')
  lst_one.append('banana')
  lst_one.append('strobary')
  lst_one.append('watermelon')
  lst_two = LinkedList()
  lst_two.insert(1)
  lst_two.append(2)
  lst_two.append(3)
  lst_two.append(4) 
  merging=LinkedList()
  expeted=merging.zipLists(lst_one,lst_two)
  actual='{apple}-> {1}-> {banana}-> {2}-> {strobary}-> {3}-> {watermelon}-> {4}-> '  
  assert expeted==actual


def test_merging_one_taller():
  #  the first one taller
  lst_one = LinkedList()
  lst_one.append('apple')
  lst_one.append('banana')
  lst_one.append('strobary')
  lst_one.append('watermelon')
  lst_two = LinkedList()
  lst_two.insert(1)
  lst_two.append(2)

  merging=LinkedList()
  expeted=merging.zipLists(lst_one,lst_two)
  actual='{apple}-> {1}-> {banana}-> {2}-> {strobary}-> {watermelon}-> '  
  assert expeted==actual



def test_merging_second_taller():
  #  the second one taller
  lst_one = LinkedList()
  lst_one.append('apple')
  lst_one.append('banana')
  lst_one.append('strobary')
  lst_one.append('watermelon')
  lst_two = LinkedList()
  lst_two.insert(1)
  lst_two.append(2)
  lst_two.append(3)
  lst_two.append(4)
  lst_two.append(5)
  lst_two.append(6)

  merging=LinkedList()
  expeted=merging.zipLists(lst_one,lst_two)
  actual='{apple}-> {1}-> {banana}-> {2}-> {strobary}-> {3}-> {watermelon}-> {4}-> {5}-> {6}-> ' 
  assert expeted==actual


def test_merging_second_empty():
  #  the second is empty 
  lst_one = LinkedList()
  lst_one.append('apple')
  lst_one.append('banana')
  lst_one.append('strobary')
  lst_one.append('watermelon')
  lst_two = LinkedList()
  merging=LinkedList()
  expeted=merging.zipLists(lst_one,lst_two)
  actual='{apple}-> {banana}-> {strobary}-> {watermelon}-> ' 
  assert expeted==actual



def test_merging_both_empty():
  #   both empty 
  lst_one = LinkedList()
  lst_two = LinkedList()
  merging=LinkedList()
  expeted=merging.zipLists(lst_one,lst_two)
  actual='' 
  assert expeted==actual
