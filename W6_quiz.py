""" 1) Suppose u and v both have values of type set and are disjoint. 
Which of the following expressions evaluates to True?
 u == v | (u^v)
 u == (v^u)
 u == v^(u | v)
 u == u^(v | u) """

# Disjoin sets are sets that have no common value 
# or u intersection v = null set

# u = {1, 2, 3}
# v = {4, 5, 6}

# print(u^v) # {1, 2, 3, 4, 5, 6}
# The symmetric difference between two sets is the set of all the elements
#  that are either in the first set or the second set but not in both.

# You have the choice of using either the symmetric_difference() method 
# or the ^ operator to do this in Python.

# print(u == v | (u^v)) # False
# print(u == (v^u))     # False
# print(u == v^(u | v)) # True
# print(u == u^(v | u)) # False

# ANS) u == v^(u | v)

""" 2) Suppose u and v both denote sets in Python. What is the most
general condition that guarantees that u|v == u^v?
 The sets u and v should be disjoint.
 The set u should be a subset of the set v.
 The set v should be a subset of the set u.
 This is true for any u and v. """

# u = {1, 2, 3} # u and v are disjoint sets
# v = {4, 5, 6}
# print(u | v) # {1, 2, 3, 4, 5, 6}
# print(u ^ v) # {1, 2, 3, 4, 5, 6}
# print(u|v == u^v) # True

# u = {1, 2, 3}  # u is a subset of set v
# v = {1, 2, 3, 4, 5} 
# print(u | v) # {1, 2, 3, 4, 5}
# print(u ^ v) # {4, 5}
# print(u|v == u^v) # False

# u = {1, 2, 3, 4, 5} 
# v = {1, 2, 3}   # v is a subset of set u
# print(u | v) # {1, 2, 3, 4, 5}
# print(u ^ v) # {4, 5}
# print(u|v == u^v) # False

# Thus, u|v == u^v when u and v are disjoint sets

# ANS) The sets u and v should be disjoint.

""" 3) Consider the min-heap [15, 27, 33, 39, 66, 39, 47, 58, 51]. 
built by repeatedly inserting values into an empty heap. Which of the 
following could not have been the last element inserted into this heap?
 27
 15
 58
 51 """
 # check this out for explanation
 # https://stackoverflow.com/questions/69024237/find-the-last-element-inserted-into-the-min-heap

 # ANS) 58

""" 4) Suppose we execute delete-min twice on the min-heap [13,29,24,67,52,89,45,98.79,58].
 What is the resulting heap? """
# just do to delete_min() operation on the heap and we will get the answer:
# ANS) [29,52,45,67,98.79,89,58]
