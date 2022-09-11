""" 1) Given the following permutation of a,b,c,d,e,f,g,h,i,j, 
what is the next permutation in lexicographic (dictionary) order? 
Write your answer without any blank spaces between letters.
    fjadbihgec """

# Ans) fjadcbeghi # using the finding next permutation

""" 2) We want to add a function length() to the class Node that implements user 
defined lists which will compute the length of a list. An incomplete implementation 
of length() given below. You have to provide expressions to put in place of XXX, YYY. and ZZZ.

def length(self):
  if self.value == None:
     return(XXX)
  elif self.next == None:
     return(YYY)
  else:
     return(ZZZ)

 XXX: 0, YYY: 0, ZZZ: self.next.length()
 XXX: 0, YYY: 0, ZZZ: 1 + self.next.length()
 XXX: 0, YYY: 1, ZZZ: self.next.length()
 XXX: 0, YYY: 1, ZZZ: 1 + self.next.length() """

 # Ans) 4) XXX: 0, YYY: 1, ZZZ: 1 + self.next.length()

 """ 3) Suppose we add this function foo() to the class Tree that implements search trees.
 For a name mytree with a value of type Tree, what would mytree.foo() compute?

    def foo(self):
        if self.isempty():
            return(0)
        elif self.isleaf():
            return(1)
        else:
            return(1 + max(self.left.foo(),self.right.foo()))

 The number of nodes in mytree
 The largest value in mytree.
 The length of the longest path from root to leaf in mytree.
 The number of paths in mytree. """

 # Ans) 3) The length of the longest path from root to leaf in mytree.

""" 4) Inorder traversal of a binary tree has been defined in the lectures. 
A preorder traversal lists the vertices of a binary tree (not necessarily a search tree) as follows:
Print the root.
Print the left subtree in preorder.
Print the right subtree in preorder.
Suppose we have a binary tree with 10 nodes labelled a, b, c, d, e, f, g, h, i, j, with 
preorder traversal gbhecidajf and inorder traversal ehbicgjafd. What is the right child of the root node? """

# Ans) 'd'  