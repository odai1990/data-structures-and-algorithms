class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return '{}'.format(self.value)


class LinkedList:
    def __init__(self):
        self.head = None      
        self.length = 0

   

    '''Adds node to head of linked list'''

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    '''Takes in a target value and iterates through Linked List
    until the value is found, or the end of the list is reached
    returns a boolean'''

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):
        values = ''
        current = self.head
        while current:
            values += '{{{}}}-> '.format(str(current.value))
            current = current.next
        print(values)
        return values

    '''Iterates to the end of a Linked List and appends a value'''

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node
        self.length += 1


    '''Iterates through of a Linked List and insert a value before location'''
    def insertBefore(self,value, newVal):
        new_node = Node(newVal)
        current = self.head
        prvs=None

        while current:
            if current.value == value:              
                if self.head==current:
                    new_node.next,self.head = current,new_node                   
                    self.length += 1
                    return
                else:                    
                    new_node.next,prvs.next = current,new_node                    
                    self.length += 1
                    return
            else:
                prvs=current
                current = current.next
        return 'could not find that element'
        

            

        
    '''Iterates through of a Linked List and insert a value after location'''  
    def insertAfter(self,value, newVal):
            current = self.head
            new_node = Node(newVal)                               
            while current:               
                if current.value == value:                                      
                    current.next,new_node.next=new_node,current.next
                    self.length += 1
                    return
                current = current.next
            return 'could not find that element'
            
               


                            
