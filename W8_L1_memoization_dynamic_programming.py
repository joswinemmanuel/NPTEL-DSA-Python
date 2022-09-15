# Inductive definitions directly gives recursive programs
# fact(n-1) is a subproblem of fact(n)
# so are fact(n-2), fact(n-3) etc fact(0)
# isort([x2,...,xn]) is a subproblem of isort([x1,x2,...,xn])

def fib(n):
    if n==0 or n==1:
        value = n
    else:
        value = fib(n-1) + fib(n-2)
    return value

print(fib(4))

# Here we can see that in fib(n-1) and fib(n-2) some calls 
# are getting repeated but done again....like, fib(2) , fib(3) etc

# Thus there is an overlapping subproblems
#  - wasterful recomputation
#  - computation tree grows exponentially

# we should avoid this...never re-evaluate a subproblem
# build a table of values already computed
# - memonry table
# - memoizatioin
# store each newly computed value in a table

def memoized_fib(n):
    fibtable = {}
    if n in fibtable:
        return fibtable[n]
    if n==0 or n==1:
        value = n
    else:
        value = fib(n-1) + fib(n-2)
    fibtable[n] = value
    return value

""" Dynamic programming """
# Dynamic Programming is a technique in computer programming that helps to efficiently solve 
# a class of problems that have overlapping subproblems and optimal substructure property.

def dynamic_fib(n):
    fibtable = {}
    fibtable[0] = 0
    fibtable[1] = 1
    for i in range(2, n+1):
        fibtable[i] = fibtable[i-1] + fibtable[i-2]
    return fibtable[n]
