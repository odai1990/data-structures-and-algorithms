class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    
    def __init__(self):
        '''
        create a constructor
        '''
        self.front = None
        self.rear = None

    def enqueue(self, value):
        '''
        enqueue method to add element to queue
        '''
        node = Node(value)
        if self.rear is None:
            self.front = node
            self.rear = node      
        else:
            node.next=self.rear
            self.rear = node

    def dequeue(self):
        '''
        dequeue method to return and delete first element in queue
        '''
        
        if self.rear is None:
            raise Exception('You cant dequeue from empty queue')
        else:
           
            if self.rear == self.front: 
                temp= self.front.value
                self.front=None
                self.rear=None
                return temp
            else:
                
                temp =self.front.value
                current=self.rear
                while current.next.next:                    
                    current=current.next
                self.front=current
                self.front.next=None                          
                return temp
