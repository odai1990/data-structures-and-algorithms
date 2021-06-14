from linked_list import __version__


def test_version():
    assert __version__ == '0.1.0'


from linked_list.linked_list import  Node,LinkedList

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
  #add a node to the end of the linked list
    lst_four = LinkedList()
    lst_four.append('banana')
    assert lst_four.head.value == 'banana' 


def test_append_to_multiple_end():
  #add multiple nodes to the end of a linked list
    lst_four = LinkedList()
    lst_four.append('banana')
    lst_four.append('apple')
    assert lst_four.head.value == 'banana' 
    assert lst_four.head.next.value == 'apple' 


def test_insert_before_middle():
  #insert a node before a node located i the middle of a linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')  
  lst_four.insertBefore('banana','melon')
  assert lst_four.head.next.value == 'melon' 


def test_insert_before_begining():
  # insert a node before the first node of a linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')  
  lst_four.insertBefore('apple','watermelon')
  assert lst_four.head.value == 'watermelon'



def test_insert_before_empty():
 #add nodes to the begin of a linked list
  lst_four = LinkedList()
  assert lst_four.insertBefore('','') == 'could not find that element'




def test_insert_after_middle():
  #insert after a node in the middle of the linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  lst_four.insertAfter('banana','strobary')
  lst_four.insertAfter('strobary','watermelon')
  assert lst_four.head.next.next.next.value == 'watermelon' 
  assert lst_four.head.next.next.value == 'strobary'
  assert '{apple}-> {banana}-> {strobary}-> {watermelon}-> '== lst_four.__str__()



def test_insert_after_end():
  #insert a node after the last node of the linked list
  lst_four = LinkedList()
  lst_four.insert('apple')
  lst_four.append('banana')
  lst_four.insertAfter('banana','strobary')  
  assert lst_four.head.next.next.value == 'strobary'
  assert '{apple}-> {banana}-> {strobary}-> '== lst_four.__str__()


def test_insert_after_empty():
    #add nodes to the None location of a linked list
    lst_four = LinkedList()
    assert lst_four.insertAfter('','') == 'could not find that element'










