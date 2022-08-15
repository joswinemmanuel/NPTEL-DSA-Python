""" Bubble sort """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Time Complexity: O(n**2)
# Auxiliary Space: O(1)

""" Insertion sort """
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr
# Time Complexity: O(n**2) 
# Auxiliary Space: O(1)

""" to set recursion limit to 2000 """
import sys
sys.setrecursionlimit(2000)


""" Insertion using recursion """
def insertionSortRecursive(arr, n):
    # base case
    if n <= 1:
        return # None

    # Recursively sort first n-1 elements
    insertionSortRecursive(arr, n-1)

    # Insert last element at its correct position in sorted array
    key = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = key

# Time Complexity: O(n**2)
# Auxiliary Space: O(n)

a = [100, 14, 23, 44, 2 ,1]
insertionSortRecursive(a, len(a))
print(a)

""" Selection sort and Insertion sort are both O(n**2)
O(n**2) sorting is infeasible for n over 5000
Among insertion sort and selection sort, insertion sort is usually better """