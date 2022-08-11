print(list(range(1, 11)))
# gives [1 ... 10] ( till n-1 )

print(list(range(1, 11, 2)))
# the third argument is the jump value

print(list(range(10, 0, -1)))
# count down 

print(range(1, 4) == [1, 2, 3])
# False because range(1, 4) gives a range object while [1, 2, 3] is a list object
print(type(range(1, 4)))
print(type([1, 2, 3]))

# Type conversion
print(int('10') + 1)  # 11
print(str(100) + '1') # 1001