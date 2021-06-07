array=[2,3,4]

 

def x(array,number):
    
    if(type(array)!= list):
        return 'You have to add Array'
    
    array=array+[number] #or .append method
    index_half=len(array)/2
    index_full=len(array)-1
    
    if len(array)%2!=0:
      index_half=index_half-.5
      
    while (index_half!=index_full):
        array[index_full],array[index_full-1]=array[index_full-1],array[index_full]
        index_full-=1
    return (array)    

print(x(array,'ee'))