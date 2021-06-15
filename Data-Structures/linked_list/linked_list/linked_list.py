
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
            




    '''Iterates through of a Linked List to get value of spesefic location'''          
    def ll_kth_from_end(self,value):
        current = self.head
        index=0

        while current:
            index+=1           
            current = current.next
        else:
            current = self.head
        if (index<value or None):
            raise Exception('out of range')

        for i in range(index-value-1):  
            current = current.next

        return current.value


    def zipLists(self,LinkedList_one, LinkedList_two):
        values = ''
        values2 = ''
      
        # LinkedList_one.head.next=LinkedList_two
        # LinkedList_two=None
        
        current_a = LinkedList_one.head  
        current_b = LinkedList_two.head  
        t = Node(current_a)  
        t.next=(current_b)    
        while current_a:

            t.next.next=current_b.next
            current_b = current_b.next
            
            t.next.next=current_a.next
            current_a = current_a.next
            values += '{{{}}}-> '.format(str(t))
            # values2 += '{{{}}}-> '.format(str(current2.value))
            
            t = t.next           
        return f'{values} ////// {values2}'



if __name__ == "__main__":
    lst_four = LinkedList()
    lst_four.append('apple')
    lst_four.append('banana')
    lst_four.append('strobary')
    lst_four.append('watermelon')
    lst_seven = LinkedList()
    lst_seven.insert(1)
    lst_seven.append(2)
    lst_seven.append(3)
    lst_seven.append(4)
    sss=LinkedList()
    print(sss.zipLists(lst_four,lst_seven))
    
 