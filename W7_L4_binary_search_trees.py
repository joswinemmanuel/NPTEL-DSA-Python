# Dynamin sorted data
# sorting is useful for efficient searching
# if the data is changing dynamically:
#  - items are periodically inserted and deleted
#  - insert/delete in sorted list take time O(n)
# it is inefficient to sort the data again and again, for like binary search
# but in heap with priority queue we can do both efficiently
# thus we can move into a tree like structure

""" Binary search tree """
# for each node with value v
#  - value in left subtree < v
#  - value in right subtree > v
# No duplicate values
#Ex:            5
#              / \
#             2   8
#            / \   \
#           1   4   9
# 2<5, 8>5,, 1<2, 4>2,, 9>8

# inorder traversal : [1, 2, 4, 5, 8, 9]

# Left most node in the tree have the minimum value

# Right most node in the tree have the maximum value

# Each node have: value, left, right
# Node with 5 is like : 5, node with 2, node with 8
# Node with 8 is like : 8, None, node with 9
# Node with 2 is like : 2, node with 1, node with 4
# Node with 1 is like : 1, None, None

# leaf node have a value, have left and right, both of which point to empty node
# Empty node : None, None, None
# Empty tree is a single empty node
# This concept makes it easier to write recursive functions to traverse the tree

class Tree:

    # Empty node has self.value, self.left, self.right = None
    # Leaf has self.value != None, and self.left, self.right point to empty node

    # Constructor: create an empty node or a leaf node, depending on initval
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
        return

    # Only empty node has value None
    def isempty(self):
        return (self.value == None)

    # Inorder traversal
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder()+[self.value]+self.right.inorder())

    # Display Tree as a string
    def __str__(self):
        return(str(self.inorder()))

    # Check if value v occurs in tree
    def find(self,v):
        if self.isempty():
            return(False)

        if self.value == v:
            return(True)

        if v < self.value:
            return(self.left.find(v))

        if v > self.value:
            return(self.right.find(v))

    # Find maximum value in a nonempty tree
    def maxval(self):
        if self.right.isempty():
            return(self.value)
        else:
            return(self.right.maxval())

    # Find minimum value in a nonempty tree
    def minval(self):
        if self.left == None:
            return self.value
        else:
            return self.left.minval()

    # Insert value v in tree
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()

        if self.value == v:
            return

        if v < self.value:
            self.left.insert(v)
            return

        if v > self.value:
            self.right.insert(v)
            return

    # Leaf nodes have both children empty
    def isleaf(self):
        return (self.left.isempty() and self.right.isempty())

    # Convert a leaf node to an empty node
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return

    # Copy right child values to current node
    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return

    # Delete value v from tree
    def delete(self,v):
        if self.isempty():
            return

        if v < self.value:
            self.left.delete(v)
            return

        if v > self.value:
            self.right.delete(v)
            return

        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return

t = Tree()
print(t)
# []
t.insert(1)
for i in [3, 2, 18, 7, 5, 4, 22, 14]:
    t.insert(i)
print(t)
# [1, 2, 3, 4, 5, 7, 14, 18, 22]
t.insert(17)
print(t)
# [1, 2, 3, 4, 5, 7, 14, 17, 18, 22]
t.delete(3)
print(t)
# [1, 2, 4, 5, 7, 14, 17, 18, 22]
  
""" Complexity """
# all operations on search trees walk down a single path
# Worst-case : height of tree
# Balanced trees : height is O(log(n)) for n nodes
# Trees can be balanced using rotations - look up AVL trees
