# Trees

- Make atree node with it's methods


## Challenge


- Creating a tree that can be traversed with 3 different methods and adding nodes using binary search .

## Whiteboard Process

**Code Challange 16**

![tree_max](trees/tree-max_1.PNG)
![tree_max](trees/tree-max_2.PNG)
![tree_max](trees/tree-max_3.PNG)

**Code Challange 17**

![tree_max](trees/tree-breadth-first_1.PNG)
![tree_max](trees/tree-breadth-first_2.PNG)
![tree_max](trees/tree-breadth-first_3.PNG)

## Approach & Efficiency


BinaryTree: they will return the tree in this order:

- pre_order==> root-->left-->right
- in_order==> left-->root-->right
- post_order==> left-->right-->root 
BinarySearchTree:
- add--> accepts a value, and adds a new node with that value in the correct location in the binary search tree.
- contains--> accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once. 
- find_max_value --> a function loop on all tree node and retun the max number
- breadth_first --> a function loop on all tree node and return list of all values in the tree, in the order they were encountered


## API

- my approach was a recursion function.