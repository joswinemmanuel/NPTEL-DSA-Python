def power(a, b):
    ans = 1
    for i in range(b):
        ans *= a
    return ans

# passing values to function
print(power(2, 5))
# passing arguments by name
print(power(b=5, a=2))

def add(a, b=0): # default argument
    return a + b

print(add(5))

def square(x):
    return x * x

def apply(f, x, n):
    res = x
    for i in range(n):
        res = f(res)
    return(res)

print(apply(square, 5, 2))
# same as square(square(5))