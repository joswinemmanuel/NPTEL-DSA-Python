""" A function calling itself is RECUSION """

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def fibonacci_n(n):
    if n<=1:
        return n
    return fibonacci_n(n-1) + fibonacci_n(n-2)

for i in range(0, 10):
    print(fibonacci_n(i), end=" ")