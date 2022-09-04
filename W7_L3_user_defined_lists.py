# Designing our own list
# a list is a sequence of nodes
# Each node store value, points to next node
# final node have value but points to nothing (None)
# empty list have value None and points to None
# singleton list have one value and it points to None

class Node:
    
    def __init__(self, initial=None):
        self.value = initial
        self.next = None

    def isempty(self):
        return self.value == None
    
    def append_recursively(self, v):    # append using recursion
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            self.next.append_recursively(v)
        return   
    
    def append_iteratively(self, v):    # append using iteration
        if self.isempty():
            self.value = v
            return
        temp = self
        while temp.next != None:
            temp = temp.next
        newnode = Node(v)
        temp.next = newnode
        return    
    
    def insert(self, v):
        if self.isempty():
            self.value = v
            return
        newnode = Node(v)
        self.value, newnode.value = newnode.value, self.value
        self.next, newnode.next = newnode, self.next
        return
    
    def delete(self,v):   # delete, recursive
        if self.isempty():
            return
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return

    def __str__(self):          # To print out the list
        selflist = []
        if self.value == None:
            return(str(selflist))

        temp = self
        selflist.append(temp.value)
        
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return(str(selflist))
                

l1 = Node() # Empty list
print(l1.isempty())
# Output: True

l2 = Node(5) # Singleton
print(l2.isempty())
# Output: False

l = Node(0)
print(l)
# [0]
l.append_recursively(20)
print(l)
# [0, 20]
l.append_iteratively(33)
print(l)
# [0, 20, 33]
l.insert(100)
print(l)
# [100, 0, 20, 33]
l.delete(20)
print(l)
# [100, 0, 33]