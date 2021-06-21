
x=[1,2,3,4,5,6,7,8]


def BinarySearch (x,g):      #one time
                     
    end=len(x)                          #one time
    start=0                       #one time
    index=end//2                           #one time
    while end-1!=start:                    # N time
        
        if g==x[index]:                    #one time
            return(index)                       #one time
            break                               
        elif g > x[index]:
            start=index
            index=(start+(end))//2
            
        elif g < x[index]:
            end=index
            index=(0+end)//2
         
       
    return('not found')        
            
print(BinarySearch (x,55))   
