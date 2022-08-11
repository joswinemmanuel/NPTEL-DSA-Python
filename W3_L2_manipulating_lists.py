list1 = [1, 2, 3, 4, 5]
list1[1] = 1000
# [1, 1000, 3, 4, 5]
print(list1)

list2 = list1 # list2 will be list1, shallow copy, any change to list1 changes list2

list1 = list1[:2] + [999] + list1[3:] # list1 is changed to a new list so list2 remains same as old list1
# list1 = [1, 1000, 999, 4, 5]
print(list1)
# list2 = [1, 1000, 3, 4, 5]
print(list2)

list1 = [1, 2, 3]
list1 = list2 # shallow copy
list1.append(100) # list1 is manipulated, added a new value, 
# not changed into a new list, so list2 also changed
print(list1)
print(list2)
# both will be [1, 2, 3, 100f]

" Shrink and Expand list using slices "
list1 = [1, 2, 3, 4, 5]
list1[2:] = [33, 44, 55, 66]
print(list1) # [1, 2, 33, 44, 55, 66] Expanded using slices
list1[0:2] = [1000]
print(list1) # [1000, 33, 44, 55, 66] Shrinked using slices

" 'in' is called membership operator "
# used to check if an element is in a list or string
print('IN') if 1 in [1, 2, 3] else print('NOT IN')   # IN 
print('IN') if 100 in [1, 2, 3] else print('NOT IN') # NOT IN

" removing all occurance of an element "
lst = [1, 2, 3, 1, 4, 1, 5]
while 1 in lst:
    lst.remove(1)
print(lst) # [2, 3, 4, 5]