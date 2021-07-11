# Challenge Summary
- write a function that given an array of numbers, will return the same array with the numbers sorted.

## Whiteboard Process

![Insertion_Sort](/challenges/Insertion_Sort/insertion_sort_1.PNG)

![Insertion_Sort](/challenges/Insertion_Sort/insertion_sort_2.PNG)

![Insertion_Sort](/challenges/Insertion_Sort/insertion_sort_3.PNG)


## Approach & Efficiency

- time: O(n^2)
- space: O(1)

## Solution

```
def  insertion_sort(arr):
  
    for i in range(len(arr)):
    
      j = i - 1
      temp = arr[i]
      
      while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]
        j = j - 1
        
      arr[j + 1] = temp
    
    return arr
```