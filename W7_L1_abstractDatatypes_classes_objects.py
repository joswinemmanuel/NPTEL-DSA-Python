# We can go beyond the builtin datatypes and create ourown datatypes
# A data structure is an organisation of information whose behaviour is 
# defined through an interface, interface is the allowed set of operations
# Ex: stack is a data structure having operations pop() and push()
# Ex: queue - having operations enqueue() and dequeue()
# Ex: Heap - insert() and delete_max()

# We are implementing all these using builtin list, 
# but the operations of list like append should not be done is heap etc

# In order to avoid this define abstract datatypes, where no other operations can be done
# Ex: In stack, (stack.push(v)).pop() == v, as stack.pop() gives back the last value added
# and last value added using stack.push() is v, so it should be equal to v
# Ex: In queue, ((q.enqueue(u)).enqueue(v)).dequeue() == u

# We should imagine each data structures like a black box
# only specific operations can be done which is unique to each data structure

# Abstract Data Types can be defined using object oriented programming (OOP)
# Class and Objects are important concepts of OOP

# Class: is like a template, how data is stored, what all operations can be performed
# Object: is an instance of the template

# DUMMY EXAMPLE 
"""
class Heap:
    def __init__(self, l):
        # create heap from list l
    def insert(self, x):
        # insert x into heap
    def delete_max(self, x):
        # return max element and delete it from heap

# creating object
h1 = Heap([15, 32, 10])
# applying operations
h1.insert(23)
h1.insert(19)
x = h1.delete_max()
"""