""" Scope is the portion of the code where the name or variable is 
available to read and update """

# def f():
#     y = x # Value of x taken from global scope
#           # y is in local scope
#     print(y)
# x = 7 # Global scope
# f()

# Output: 7

# def f():
#     y = x
#     print(y)
#     x = 22 # we try to assign value to x, which is global, so error
# x = 7
# f()

# Output: Error

""" This applies only to immutable values, for mutable values,
 we can change the value in functions or local scope """

# def f():
#     y = x[0]
#     print(y, end=" ")
#     x[0] = 22 # trying to change value of mutable datatype(list)
#     print(x)
# x = [7]
# f()

# Output: 7 [22]

# def f():
#     global x # calling the global x, making it available in local scope to change
#     y = x
#     print(y, end=" ")
#     x = 22
#     print(x)
# x = 7
# f()

# Output: 7 22

""" Nested Functions """
# Functions inside another function are nested functions
# These functions are available withing the local scope or the funtion only

def f():
    a = 10
    def g():
        nonlocal a # here we call in the local a, a is available in f() or local scope not global
        a = 100    # since we are changing its value, we use nonlocal a, like we used global x, before
        return a
    def h():
        return 1
    print(g() + h())  #  g() and h() are the nested funcitons and can be used inside f() only
f()

# Output: 3