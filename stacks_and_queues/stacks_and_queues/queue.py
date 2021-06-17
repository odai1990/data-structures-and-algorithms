# from stacks_and_queues.node import Node
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


    def __str__(self):
        '''
        to print queue
        '''

        values = ''
        current = self.rear  
        while current:
            values += '{{{}}}-> '.format(str(current.value))
            current = current.next
        
        return values

    def peek(self):
        '''
        peek method to return and do not delete first element in queue
        '''
        if self.rear is None:
            raise Exception('You cant dequeue from empty queue')
        else:
            return self.front.value


    def is_empty(self):
        '''
        is_empty method to check if stack empty or not
        '''
        return self.rear==None

if __name__=='__main__':
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    print(f'{queue.dequeue()} this is the removed element')
  
    print(queue.__str__())
