# Challenge Summary
- A function takes tow hashmap and return left join for he first hashtmap.

## Whiteboard Process
![Hashmap-Tree-Intersection](/challenges/hashmap_left_join/assets/hashmap_left_join_1.PNG)

![Hashmap-Tree-Intersection](/challenges/hashmap_left_join/assets/hashmap_left_join_2.PNG)

![Hashmap-Tree-Intersection](/challenges/hashmap_left_join/assets/hashmap_left_join_3.PNG)

## Approach & Efficiency
Big O

O(n^2) for complexity
O(n) for space

## Solution

```
def hashmap_left_join(map_a, map_b):
  
    output = []
    
    for word in map_a.map:
        if not word == None:
            if map_b.contains(word.head.data[0]):                
                antonym = map_b.get(word.head.data[0])             
                output.insert(0,[word.head.data[0], word.head.data[1], antonym])
            else:
                output.insert(0,[word.head.data[0], word.head.data[1], 'Null'])
    
    
    return output

```
