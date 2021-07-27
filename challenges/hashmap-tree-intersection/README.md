# Challenge Summary
- A function takes tow trees and return repeded numbers in bith of them.

## Whiteboard Process
![Hashmap-Tree-Intersection](/challenges/hashmap-tree-intersection/tree_intersection_1.PNG)

![Hashmap-Tree-Intersection](/challenges/hashmap-tree-intersection/tree_intersection_2.PNG)

![Hashmap-Tree-Intersection](/challenges/hashmap-tree-intersection/tree_intersection_3.PNG)

## Approach & Efficiency
Big O

O(n) for complexity
O(n) for space

## Solution
- First one
```
def tree_intersection(self,tree1,tree2):
        all_element=list(set(tree1.pre_order()))+list(set(tree2.pre_order()))
        repeted_element=[]
        for i in all_element:
            i=str(i)
            hashed_key=self.hash(i)
            if not self.map[hashed_key]:
                self.map[hashed_key]=LinkedList()           
            
            self.map[hashed_key].add((i,i))           
            if not self.map[hashed_key].head.next is None:
              repeted_element.append(int(i))
        return repeted_element
```
- Second one
```
    def tree_intersection_without_hashtabke(self,tree1,tree2):
        
        return list(set.intersection(set(tree1.pre_order()),set(tree2.pre_order())))
        
```