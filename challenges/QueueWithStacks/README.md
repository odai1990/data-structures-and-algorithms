# Challenge Summary
- Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface , but will internally only utilize 2 Stack objects.

## Whiteboard Process
![whiteboard](/challenges/QueueWithStacks/queue-with-stacks_1.PNG)

![whiteboard](/challenges/QueueWithStacks/queue-with-stacks_2.PNG)

![whiteboard](/challenges/QueueWithStacks/queue-with-stacks_3.PNG)


## Approach & Efficiency
- Enqueue method will happen in stack 2 after pushing the nodes to it, and dequeue will happen in stack 1.

## Solution

```

from queuewithstacks.stack import Stack

class PseudoQueue:
    def __init__(self):
        '''
        Create tow stacks 
        '''
        self.first_stack=Stack()
        self.second_stack=Stack()
    
    def enqueue(self,value):
        '''
        enqueue is method to add element ot queue 
        '''
        while self.second_stack.top:
            self.first_stack.push(self.second_stack.pop())
        self.first_stack.push(value)

    def dequeue(self):
        '''
        dequeue is method to return and delete element in queue 
        '''      
        while self.first_stack.top:
            self.second_stack.push(self.first_stack.pop())
        return self.second_stack.pop()
```
