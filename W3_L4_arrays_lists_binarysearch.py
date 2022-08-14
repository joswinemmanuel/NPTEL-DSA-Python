" Linear search : find the index of the value if present in the list "
def linear_search(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return f"Found at index {i}"
    return "Value not found"
# it check all the elements in the list to find the index
# worst cases : if element is at last of the list, element not in list
# in these cases it is inefficient, so we need a better algorithm

" Binary search : is a technique to find the index of an element in a sorted list "
# Iterative Binary Search Function
def binary_search_i(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1


# Recursive binary search.
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1

" Python's built in 'list' are not array "