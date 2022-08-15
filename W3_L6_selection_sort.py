""" Selection sort """

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

# Time Complexity: O(n**2)
# Auxiliary Space: O(1)
