names = ["joswin", "agath", "merin"]
age = [19, 23, 53]
mixed = ["joswin", 19, "agath", 23]

lst = [1, 2, 3, 4, 5]

print(lst[1:3]) # list slicing

print(lst[::-1]) # returns the reverse of the list using slicing

print(len(lst)) # returns the lenght of the list

''' lst[0] not equal to lst[0:1] '''
''' lst[0] gives 1      lst[0:1] gives [1] '''

lst[0] = 10 # lists are mutable
print(lst[0])

a = 10
b = a
a = 99
print("a = ", a, "b = ", b)
""" Value of b will still be 10 -- this is the case for immutalble datatypes only
like int, float, str etc -- a fresh copy is made while assigining"""
a = [1, 2, 3]
b = a         # shallow copy
a[1] = 100
b[2] = 99
print("a = ", a, "b = ", b)
""" for mutable datatypes like list when value in list is changed it change for both"""
""" so we make a copy in b using .copy() funciton"""
a = [1, 2, 3]
b = a.copy()  # deep copy
c = a[:]     # or use [::] slicing to make a deep copy
a[1] = 100
b[2] = 99
print("a = ", a, "b = ", b, "c = ", c)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2
print(l1 == l2) # == checks if l1 and l2 have same value
print(l2 == l3) 
print(l1 is l2) # is checks if l1 and l2 refers to same object
print(l2 is l3)

print(l1 + l2) # concatenation of lists using 