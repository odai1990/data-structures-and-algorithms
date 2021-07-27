from hashmap_tree_intersection.linked_list import LinkedList

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
    
    #

