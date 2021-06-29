# Challenge Summary

Write a function called FizzBuzzTree which takes a k-ary tree as an argument.
Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
- If the value is divisible by 3, replace the value with “Fizz”
- If the value is divisible by 5, replace the value with “Buzz”
- If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
- If the value is not divisible by 3 or 5, simply turn the number into a String.
Return a new tree.

## Whiteboard Process
![tree-fizz-buzz](/challenges/tree-fizz-buzz/tree-fizz-buzz_1.PNG)
![tree-fizz-buzz](/challenges/tree-fizz-buzz/tree-fizz-buzz_2.PNG)
![tree-fizz-buzz](/challenges/tree-fizz-buzz/tree-fizz-buzz_3.PNG)

## Approach & Efficiency
using recursion and class structure for KAryTree

## Solution

```
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
  ```



