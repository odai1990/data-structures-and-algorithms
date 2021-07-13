# Challenge Summary
- write a function that given an array of numbers, will return the same array with the numbers sorted.

## Whiteboard Process

![Quick_Sort](/challenges/quick_sort/quick_sort_1.PNG)

![Quick_Sort](/challenges/quick_sort/quick_sort_2.PNG)

![Quick_Sort](/challenges/quick_sort/quick_sort_3.PNG)

## Approach & Efficiency

Big O:

time: O(n*log(n))

space: O(1)

## Solution

```
def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)
    return arr
def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low+=1
            Swap(arr, i, low)
    Swap(arr, right, low + 1)
    return low + 1
def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

```
