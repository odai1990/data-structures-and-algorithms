# Challenge Summary

- Write a function that accepts a lengthy string parameter, return the first word to occur more than once in that provided string.

## Whiteboard Process


![Repeated_Word](/challenges/repeated-word/repeated_word_1.PNG)

![Repeated_Word](/challenges/repeated-word/repeated_word_2.PNG)

![Repeated_Word](/challenges/repeated-word/repeated_word_3.PNG)

## Approach & Efficiency
Big O

O(n) for complexity
O(n) for space

## Solution

```
class RepeatedWord(HashTable):
    def __init__(self,size):
        super().__init__(size)

    def repet(self,sentens):
        for value in re.findall("\w(?<!\d)[\w'-]*",sentens.lower()):
            
            hashed_key=self.hash(value)
            if not self.map[hashed_key]:
                self.map[hashed_key]=LinkedList()           
            
            self.map[hashed_key].add((value,value))           
            if not self.map[hashed_key].head.next is None:
              return value
              
        return None
```