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
     