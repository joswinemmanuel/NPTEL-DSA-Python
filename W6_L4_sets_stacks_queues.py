# Algorithms + Data Structures = Programs

""" Data structures examples
- arrays / lists
- dictionaries
- python builtin data types etc """

""" -----------------------------------------------------------""" 

""" Sets """
colors = {"Red", "Green", "Blue", "White"}
print(colors)
# {'Green', 'Blue', 'White', 'Red'}
empty_set = {}
print(empty_set)
# {}
print("Green" in colors)
# True
word = "Banana"
print(set(word))
# {'B', 'a', 'n'}

""" Set operations """
odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7, 11}

""" Union """
print(odd | prime) # or
# {1, 2, 3, 5, 7, 9, 11}

""" Intersection """
print(odd & prime) # and
# {11, 3, 5, 7}

""" Set difference """
print(odd - prime)
# {1, 9}

""" ------------------------------------------------------------- """

""" Stacks """
# LIFO - last in first out
# operations that can be performed:
# push(element) - push an element to the last of the stack
#                 list.append(element) - can be used
# pop() - pop and element from the last of the stack and return it
#                 list.pop() - can be used

""" ------------------------------------------------------------- """

""" Queues """
# FIFO - first in first out
# LILO - last in last out
# operations that can be performed:
# addq(element) - add an element to the last of the queue
# also called enqueue
#                 list.append(element) - can be used
# removeq() - remove the element from the head of the queue
# also called dequeue
#                 list.pop(0) - can be used

""" ------------------------------------------------------------- """

