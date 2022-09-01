""" Priority queues """
# delete_max() - identifies and remove the element with highest priority
#                need not be unique
# insert() - add a new element to the list

# If unsorted list - insert() takes O(1) time
#                  - delete_max() takes O(n) time

# If sorted list - delete_max() takes O(1) time
#                - insert() takes O(n) time

# Thus processing a sequence of n cases requires O(n**2) time

""" Binary tree """
# a basic Two dimensional structure
# at each node 
#       - value
#       - link to parent, left child, right child
# node with no children is called leaf
# node with children is called parent, have a right child and left child
# Ex        5 (root)
#          / \
#(parent) 2   8
#        / \   \
#       1   4   9 (leaf)
#  (left and right child)

""" Heap """
# Heaps are a tree based implementation of priority queues
# Heaps are special kind of binary tree having a priority queue 
# This tree is a balanced tree
# A balanced tree is the one in which at each point the left and right
# side are almost the same size.
# N node tree has height log(N)
# Both insert and delete_max() take O(log(N))
# Progessing N cases takes time O(N*log(N))
# Truly flexible, need not fix upper bound for N in advance

# Head a binary tree with two properties: 
#  -Binary tree is filled level by level, left to right
#  -At each node, value stored is bigger than both children
#  -Max Heap property - evey value in node is bigger than the values of the two children

# Ex           24
#             /  \
#            11   7
#           /
#          10 
# correct example of a node, 11>10, 24>11 and 24>7

# Ex             24
#             /      \
#            11       7
#           /  \     / \
#          10   5   6   5
# correct example of a node, 11>10 and 11>5,
# 7>6 and 7>5, 24>11 and 24>7

# Ex             24
#             /      \
#            11       7
#           /  \     / 
#          10   5   6   
#         /
#        8
# not a heap, as right child of node with value 7 
# is not filled with 8.  STRUCTURE of heap is violated

# Ex             24
#             /      \
#            11       7
#           /  \     / \
#          10   5   8   5
# not a heap, as 7<8
# Max Heap property is violated, so not a heap

# insert()
# Ex             24
#             /      \
#            11       7
#           /  \     / \
#          10   5   6   5
# insert(12) to this node - it will become
#                24
#             /      \
#            12       7
#           /  \     / \
#          11   5   6   5
#         /
#        10
# insert(33) 
#                33
#             /      \
#            24       7
#           /  \     / \
#          12   5   6   5
#         /  \
#        10   11

# Complexity of insert()
# we have to walk up from the leaf to the root - height of tree
# insert() takes time O(log(N))

# delete_max()
# maximum value is always the root
# - first, we create a "hole" at the root
# - reducing one value requires deleting last node
# - move the "homeless" value to root
#                __
#             /      \
#            24       7
#           /  \     / \
#          12   5   6   5   # first step
#         /  \
#        10   11
#                11
#             /      \
#            24       7
#           /  \     / \    # next step
#          12   5   6   5
#         /  
#        10   
# - now we have to restore the heap property 
#                24
#             /      \
#            12       7
#           /  \     / \    
#          11   5   6   5
#         /  
#        10 

# will follow a single path from root to leaf
# cost proportional to height of tree
# delete_max() takes time O(log(N))

# delete_max() again on the heap
#                __
#             /      \
#            12       7
#           /  \     / \    
#          11   5   6   5
#         /  
#        10 
#                10
#             /      \
#            12       7
#           /  \     / \    
#          11   5   6   5
#                12
#             /      \
#            11       7
#           /  \     / \    
#          10   5   6   5

# Implementing using an array
#                0
#             /     \
#            1       2
#           / \     / \     # 0,1,2... represent indexes
#          3   4   5   6
#         /  \
#        7    8

# - number the nodes left to right, level by level
# - represent as an array H[0..N-1]
# - Children of H[i] are at H[2*i + 1] , H[2*i + 2]
# - Parent of H[j] is at H[floor((j-1)/2)] for j > 0

""" Building a heap, heapify() """
# give a list of values [x1,x2,x3,x4,...,xn], build a heap
# Naive approach
#   - start with an empty heap
#   - insert each xj
#   - overall O(N*log(N))

# Better heapify()
# - Set up the array a [x1,x2,x3,x4,...,xn]
#   - Leaf nodes trivially satisy heap property
#   - second half of array is already a valid heap
# - Assume leaf nodes are at level k
#   - for each node at level k-1, k-2, ... , 0, fix heap property
#   - as we go up, the number of steps per node goesup by 1,
#     but the number of nodes per level is halved
#   - cost turns out to be O(N) overall

""" Heap sort """
# - start with an unordered list
# - build a heap - O(n)
# - call delete_max() n times to extract elements in descending order - O(n*log(n))
# - after each delete_max(), heap shrinks by 1, 
#     - store maximum value at the end of the current heap
#     - in place O(n*log(n)) sort

""" Heap min """
# we can revert the heap condition
# each node is smaller than the children
# Min-heap, for insert(), delete_min()