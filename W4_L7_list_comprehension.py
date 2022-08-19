# map(f, l) applies f function to every element in l
l = list(map(int, ['1', '2', '3']))
print(l)
# using list comprenhension
ll = [int(i) for i in '123']
print(ll)

# filter(p, l) checks p for each element in l

def is_even(n):
    if n % 2 == 0:
        return True
    return False

even_l = list(filter(is_even, [0, 1, 2, 3, 5, 6]))
print(even_l)
# using list comprenhension
even_ll = [i for i in [0, 1, 2, 3, 5, 6] if is_even(i)]
print(even_ll)

# map() and filter() together

def square(n):
    return n * n

even_square = list(map(square, filter(is_even, [1, 2, 3, 4, 5, 6])))
print(even_square)
# using list comprenhension
even_square_l = [i*i for i in [1, 2, 3, 4, 5, 6] if is_even(i)]
print(even_square_l)
print()

""" Find all (x, y, z) where x*x + y*y = z*z (pythagoras) """
py = [(x, y, z) for x in range(1, 10) for y in range(1, 10) for z in range(1, 10) if (x*x + y*y)==z*z]
for i in py:
    print(i)
print()
# Better code...remove duplicates in x and y
py = [(x, y, z) for x in range(1, 10) for y in range(x, 10) for z in range(y, 10) if x*x + y*y == z*z]
for i in py:
    print(i)

""" 2 D lists """
lst = [[0 for i in range(3)] for j in range(2)]
print(lst)