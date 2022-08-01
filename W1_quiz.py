# def h(x):
#     (d,n) = (1,0)
#     while d <= x:
#         (d,n) = (d*3,n+1)
#     return(n)

# print(h(27993))


# def g(n): 
#     s=0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+1
#     return(s)

# print(g(60) - g(48))


# def f(n): 
#     s=0
#     for i in range(1,n+1):
#         if n//i == i and n%i == 0:
#            s = 1
#     return(s%2 == 1)

# for i in range(1, 50):
#     print(i, f(i))



# def foo(m):
#     if m == 0:
#       return(0)
#     else:
#       return(m+foo(m-1))

# for i in range(0, 6):
#     print(i, foo(i), int(i*(i+1)/2))