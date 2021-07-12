# Challenge Summary
- write a function that given an array of numbers, will return the same array with the numbers sorted.

## Whiteboard Process
![merge_sort](/challenges/merge_sort/merge_sort_1.PNG)

![merge_sort](/challenges/merge_sort/merge_sort_2.PNG)

![merge_sort](/challenges/merge_sort/merge_sort_3.PNG)

## Approach & Efficiency
Approach:
recursion

Efficiency:
Big O:

time: O(n*log(n))

space: O(1)

## Solution

```
def merge_sort(arr):
    n = len(arr)
           
    if n > 1:
      mid = int(n/2)
      left = arr[0:mid]
      right = arr[mid:n]
      merge_sort(left)
      merge_sort(right)
      merge(left, right, arr)
    return arr  

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
            
        k = k + 1

    while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
    while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```