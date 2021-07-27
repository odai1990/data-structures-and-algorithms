from hashmap_tree_intersection.hashtable import HashTable
from hashmap_tree_intersection.tree import *
from hashmap_tree_intersection.linked_list import LinkedList



class TreeIntersection(HashTable):
    def __init__(self, size):
        super().__init__(size)
        self.tree=BinaryTree()


    # first solution with hashtable
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


    #second solution without hahstable and you can replace intersection with for if you want
    def tree_intersection_without_hashtabke(self,tree1,tree2):
        
        return list(set.intersection(set(tree1.pre_order()),set(tree2.pre_order())))
        


    

