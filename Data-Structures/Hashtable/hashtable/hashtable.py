from hashtable.linked_list import LinkedList

class HashTable:

    def __init__(self,size):
        self.size=size
        self.map=[None]*size

    def hash(self,key):
        sum_of_ascii=0
        for ch in key:
            sum_of_ascii+= ord(ch)
        temp_value = sum_of_ascii*19
        hashed_key=temp_value%self.size
        return hashed_key

    def add(self,key,value):
        hashed_key=self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key]=LinkedList()
        self.map[hashed_key].add((key,value))
    
    def contains(self,key):
        if self.map[self.hash(key)]:
            return True
        return False
    def get(self,key):
        after_hased=self.hash(key)
        if self.map[after_hased]:                      
            current = self.map[after_hased].head
            while current:                
                if key==current.data[0]:                  
                    return current.data[1]
                current = current.next
           
        return None

