from queuewithstacks.node import Node

class Stack:

    def __init__(self):
        '''
        create a constructor
        '''
        self.top = None

    def push(self, value):
        '''
        push method to add element to stack
        '''
        node = Node(value)
        node.next = self.top
        self.top = node


    def pop(self):
        '''
        pop method to return and delete first element in stack
        '''
        if(self.top is None):
            raise Exception('You cant pop from empty stack')
        temp=self.top.value
        self.top=self.top.next
        return temp


    def peek(self):
        '''
        peek method to return and do not delete first element in stack
        '''
        if(self.top is None):
            raise Exception('You cant peek from empty stack')
        return self.top.value


    def is_empty(self): 
        '''
        is_empty method to check if stack empty or not
        '''
        return self.top == None