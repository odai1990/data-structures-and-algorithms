from repeated_word.hashtable import HashTable
from repeated_word.linked_list import LinkedList
import re
class RepeatedWord(HashTable):
    def __init__(self,size):
        super().__init__(size)

    def repeated_word(self,sentens):
        for value in re.findall("\w(?<!\d)[\w'-]*",sentens.lower()):
            
            hashed_key=self.hash(value)
            if not self.map[hashed_key]:
                self.map[hashed_key]=LinkedList()           
            
            self.map[hashed_key].add((value,value))           
            if not self.map[hashed_key].head.next is None:
              return value
              
        return None 


    