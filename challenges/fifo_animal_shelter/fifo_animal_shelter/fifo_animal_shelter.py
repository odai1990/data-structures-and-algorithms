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



class AnimalShelter:
    '''
       calss represent Shelter queue
    '''
    def __init__(self):
        self.shelter=Queue()
        self.deteting=Queue()
        self.temp=''
    
    def enqueue(self,animal):
        '''
        this method to enqueue values but test if they belong to cats or dog class
        '''
        if isinstance(animal, Cat) or isinstance(animal, Dog):
            self.shelter.enqueue(animal)
        else:
            return "You can't add other animal than dogs or cats"

    def dequeue(self,pref):
        '''
        this method to dequeue values but test if they cat or dog 
        '''
      

        current=self.shelter.front
       

        if pref.lower()=='cat' or pref.lower()=='dog':

            while self.shelter.front:
                              
                if pref.lower()=='cat':
                                                  
                    if isinstance(self.shelter.front.value, Cat):
                    
                        self.temp=self.shelter.dequeue()
                        
                        break                          
                    else:
                        if(self.shelter.front==None):
                            break
                        self.deteting.enqueue(self.shelter.dequeue())    

                elif pref.lower()=='dog':
                    if isinstance(self.shelter.front.value, Dog):                    
                        self.temp=self.shelter.dequeue()                        
                        break                          
                    else:
                        if(self.shelter.front==None):
                            break
                        self.deteting.enqueue(self.shelter.dequeue())    
            
                # current=current.next



            #### instad of using another loop i will use refrencing pointer
            
            if self.deteting.front==None:
                return self.temp
            elif self.shelter.front==None:
                self.shelter.front=self.deteting.front
                self.shelter.rear=self.deteting.rear
                self.deteting.front=None
                self.deteting.rear=None
                return self.temp
            else:
                
                self.shelter.front.next=self.deteting.rear
                self.shelter.front=self.deteting.front
                self.deteting.front=None
                self.deteting.rear=None
                print(f'{self.shelter}shelter')    
                print(f'{self.deteting}deleting')   
                return self.temp

                
            ####
        else:
            return None
            # print(f'{self.shelter}fffffffffffffffffffff')    
            # print(self.deteting)   
                    
                    
                
       

class Cat:
    '''
       calss represent cats
    '''
    def __init__(self,name):
        self.name=name


class Dog:
    '''
       calss represent dogs
    '''
    def __init__(self,name):
        self.name=name


