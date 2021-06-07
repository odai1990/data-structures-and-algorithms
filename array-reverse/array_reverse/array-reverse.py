import math

x=[1, 2, 3, 4, 5, 6,7]

counter=0

lenth=len(x)-1

def reverse_array(x):

    global counter

    global lenth

    for i in x:

        temp=x[counter]

        x[counter]=x[lenth-counter]

        x[lenth-counter]=temp

        if counter != math.floor((lenth)/2):

           counter +=1

        else:

            break



reverse_array(x)

print(x)