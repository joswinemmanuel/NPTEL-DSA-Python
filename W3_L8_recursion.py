''' Many arithmetic functions are naturally defined inductively '''

# FACTORIAL : n! = n x (n-1) x (n-2)! 
# n! = n x (n-1)!
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# MULTIPLICATION (repeated addition):
# 2 x 3 = 2 + 2 + 2 or 3 + 3
# m x n = m + (m x (n-1))
def multiplication(m, n):
    if n == 1:
        return m
    return m + multiplication(m, n-1)

# FIBONACCI SERIES:
# 1 1 2 3 5 8 13 21 34 ...
# fib(1) = fib(2) = 1, fib(3) = fib(1) + fib(2),
# fib(4) = fib(2) + fib(3)
# fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)

""" Inductive definitions naturally give rise to recursive programs """
# like FACTORIAL, MULTIPLICATION, FIBONACCI etc

# LENGTH OF LIST using recursion
# length(l) = 1 + length(l[1:])
def length_list(arr):
    if arr == []:
        return 0
    return 1 + length_list(arr[1:])

# SUM OF ELEMENTS IN LIST using recursion
# sum_of(l) = l[0] + sum_of(l[1:])
def sum_of_list(arr):
    if arr == []:
        return 0
    return arr[0] + sum_of_list(arr[1:])

""" 'RecursionError: maximum recursion depth exceeded in comparison'
recursion limit is there in python so that the program won't
run forever if the base case is incorrect ( like in case of infinite loop ) """
# upto 997 something it's okay but from 998 the above will be alerted (Recursion Error)
# therefore 998 is the default recursion limit in python

""" We can get over it by setting the recursion Limit """
import sys
sys.setrecursionlimit(1000)

