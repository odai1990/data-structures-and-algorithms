class Node:
    def __init__(self, value):
        self.value = value
        self.child = []
        

class KAryTree:
  def __init__(self):
    self.root=None


def tree_fizz_buzz(ktree):

  temp=ktree.root

  def _reblace(node):

    if node.value%5==0 and node.value%3==0:
      node.value='FizzBuzz'
    elif node.value%5==0:
      node.value="Buzz"
    elif node.value%3==0:
      node.value="Fizz"
    else:
      node.value=str(node.value)
    for i in node.child:
      if i !=[]:      
        _reblace(i)

  _reblace(temp)
  
  return temp