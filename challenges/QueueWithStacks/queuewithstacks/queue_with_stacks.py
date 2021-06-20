
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



