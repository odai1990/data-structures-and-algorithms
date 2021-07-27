class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None



    def pre_order(self):
        
        output = []

        def traverse(node):

            if not node:
                return  

            output.append(node.value)
            traverse(node.left)
            traverse(node.right)
            
        traverse(self.root)        
        return output

class BinarySearchTree(BinaryTree):
    
    def add(self, value):
       
        def _search(node, node_to_add):
            if not node:
                return

            if node_to_add.value < node.value:
                if not node.left:
                    node.left = node_to_add
                else:
                    _search(node.left, node_to_add)
            else:
                if not node.right:
                    node.right = node_to_add
                else:
                    _search(node.right, node_to_add)

        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return
        
        _search(self.root, new_node)
