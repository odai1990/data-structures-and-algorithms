from hashmap_left_join.hashtable import HashTable


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




