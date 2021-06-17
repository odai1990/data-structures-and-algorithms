# from challenges import __version__
from llZip.ll_zip import Node, LinkedList
import pytest

# def test_version():
#     assert __version__ == '0.1.0'
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
