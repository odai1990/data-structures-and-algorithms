# Singly Linked List

## Challenge Summary
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node with inserting an include with ll_kth_from_end,zipLists methods.

## Whiteboard Process

**Class 04 && class05 **

![ll-insertions](linked_list/ll-insertions1.PNG)

![ll-insertions](linked_list/ll-insertions2.PNG)

![ll-insertions](linked_list/ll-insertions3.PNG)



## Whiteboard Process

**Class 07 **

![ll-insertions](linked_list/ll-insertions1_7.PNG)

![ll-insertions](linked_list/ll-insertions2_7.PNG)

![ll-insertions](linked_list/ll-insertions3_7.PNG)


## Whiteboard Process

**Class 08 **

![ll-insertions](linked_list/ll-insertions1_8.PNG)

![ll-insertions](linked_list/ll-insertions2_8.PNG)

![ll-insertions](linked_list/ll-insertions3_8.PNG)


## Solution

**Class 04 && class05 **
```
after 

call function (2,3)

current node =self.head

new_node = Node(3)  

while current: #true
 if current.value == value: # true                                     
 current.next,new_node.next=new_node,current.next
`
  self.length += 1
   return
   current = current.next
return 'could not find that element'
 
```

```
before

call function (2,3)

current node =self.head
previos =curent
new_node = Node(3)  

while current: #true
 if current.value == value: # true 
if self.head==value:#false
else: 
 new_node.next,prvs.next = current,new_node 

  self.length += 1
   return
   current = current.next
return 'could not find that element'
  
```






## Solution

**Class 07 **
```
   1 --> 6 --> 10 --> -1

value=2

        current = self.head 
        index=0

        while current: #true                     
            index+=1         --> 4
            current = current.next -> poin to Node(-1)
        else:
            current = self.head --> Node(1)                                           

        if (index<value or None): #false

            raise Exception('out of range')

        for i in range(index-value-1): #true
                              4-2-1=1
            current = current.next

        return current.value ----> 6
 
```



## Solution

**Class 08 **
```
current_a=1 -> 2-> 3
current_b=a -> b -> c

new_list=none

while True :# True

# itrate  1 to 2

if Not current_a is None: #true
new_list.append(current_a.value)
current-a=current_a.next

if Not current_b is None: #true
new_list.append(current_b.value)
current_b=current_b.next

if(current_a is None and  current_b is None: #false
break

# itrate  3

if Not current_a is None: #true
new_list.append(current_a.value)
current-a=current_a.next

if Not current_b is None: #true
new_list.append(current_b.value)
current_b=current_b.next

if(current_a is None and  current_b is None: #true
break

return new_list
 
```




## Approach & Efficiency
I used two classes and used one class for Node and other to create Object form Node class also i create append,insert,isertbefore,insertafter,ll_kth_from_end and , zipLists methodes.

## API

`--init--` : it will initialize a linked list.
`insert` : it will insert a node into the list.
`includes` : it takes a value then checks if it's in the array.
`__str__`: it will print the array in a specific way.
`__append__`: it adds a value to the end.
`__insertBefore__`: it add a new value before a certain value.
`__insertAfter__`: it add a new value after a certain value.
`__ll_kth_from_end__`: it add a new value after a certain value.
`__zipLists__`: it mergaing tow listed list concurrently


