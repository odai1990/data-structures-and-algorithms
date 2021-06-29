from .queue import Queue


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
      def _search(node):
      
        nonlocal root
        if node.value>root.value:
          root.value=node.value
        if node.left:
          _search(node.left)
        if node.right:
          _search(node.right)
        
      _search(root)
      return root.value


class BinarySearchTree(BinaryTree):




    def add(self, key):
        temp = self.root
        if not temp:
            self.root = Node(key)
            return
        q = []
        q.append(temp)
        while len(q):
            temp = q[0]
            q.pop(0)

            if not temp.left:
                temp.left = Node(key)
                break
            else:
                q.append(temp.left)

            if not temp.right:
                temp.right = Node(key)
                break
            else:
                q.append(temp.right)





    def contains(self, value, current=None):
        current = current or self.root

        if not self.root or value == None:
            print("no")
            return False

        if current.value == value:
            print("yes")
            return True
        elif current.value < value:
            return self.contains(value, current.left)
        else:
            return self.contains(value, current.right)

  
    def breadth_first(self):
        breadth = Queue()
        breadth.enqueue(self.root)
        OUTPUT=[]
    
        if not self.root:
              return "tree is empty"

        while breadth.front:
        
          front = breadth.dequeue()
          OUTPUT.append(front.value)


          if front.left is not None:
            breadth.enqueue(front.left)
          if front.right is not None:
            breadth.enqueue(front.right)
        return OUTPUT

