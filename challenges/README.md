# Singly Linked List

## Challenge Summary
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node with inserting an include with ll_kth_from_end,zipLists methods.



## Whiteboard Process

**Class 08 **

![ll-insertions](challenges/ll-insertions1_8.PNG)

![ll-insertions](challenges/ll-insertions2_8.PNG)

![ll-insertions](challenges/ll-insertions3_8.PNG)



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


