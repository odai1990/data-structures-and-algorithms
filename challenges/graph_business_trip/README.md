# Challenge Summary
- Write a function called business trip take Arguments: graph, array of city names and Return: cost or null
to determine whether the trip is possible with direct flights, and how much it would cost.

## Whiteboard Process
![Graph Business Trip](/challenges/graph_business_trip/graph_business_trip_1.PNG)

![Graph Business Trip](/challenges/graph_business_trip/graph_business_trip_2.PNG)

![Graph Business Trip](/challenges/graph_business_trip/graph_business_trip_3.PNG)

## Approach & Efficiency

Big O:
O(n^3) time
O(n) space

## Solution
```
def business_trip(graph,array):

    flag=False
    total=0   
    for i in range(1,len(array)):   
   
        for vertix in graph.adjacency_list.keys():
            if(array[i-1]==vertix.value):  
                for edge in graph.adjacency_list[vertix]:
                  if(array[i]==edge.vertix.value):                
                    total+=int(edge.weight)                  
                    flag=True
                    break
                  else:
                    flag=False                  

              
    if flag:
        return [True,'$'+str(total)]
    else:
        return [False,'$0']
     
```