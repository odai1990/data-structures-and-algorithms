class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    

    def in_order(self, node=None, results=None):
      node = node or self.root

      results = results or []
      if node:
        if node.left:
          self.in_order(node.left, results)
        
        results.append(node.value)

        if node.right:
          self.in_order(node.right, results)

      return results


    def pre_order(self, node=None, results=None):
      node = node or self.root

      results = results or []

      if node:
        results.append(node.value)

        if node.left:
          self.pre_order(node.left, results)

        if node.right:
          self.pre_order(node.right, results)

      return results

    def post_order(self, node=None, results=None):

      node = node or self.root

      results = results or []
      if node:
        if node.left:
          self.post_order(node.left, results)

        if node.right:
          self.post_order(node.right, results)
        
        results.append(node.value)

      return results

      
    def find_maximum_value(self):
      root=self.root
      max=0

      def _search(node):
        print('time')
        nonlocal max
        if node.value>max:
          max=node.value
        if node.left:
          _search(node.left)
        if node.right:
          _search(node.right)
        
      _search(root)
      return max


class BinarySearchTree(BinaryTree):

  def add(self, value, root=None):
    root = root or self.root

    node = Node(value)

    if not self.root:
      self.root = node
      return
    
    if value < root.value:
      if root.left:
        self.add(value, root.left)
      else:
        root.left = node
    else:
      if root.right:
        self.add(value, root.left)
      else:
       root.right = node
    

  def contains(self, value, current=None):
      current = current or self.root

      if not self.root or value == None:
        print('no')
        return False
    
      if current.value == value:
        print('yes')
        return True
      elif current.value < value:
        return self.contains(value, current.left)
      else:
        return self.contains(value, current.right)
   