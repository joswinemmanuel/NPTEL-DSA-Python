" Bubble sort "
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Time Complexity: O(n**2)
# Auxiliary Space: O(1)

" Insertion sort "
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr
# Time Complexity: O(n**2) 
# Auxiliary Space: O(1)
