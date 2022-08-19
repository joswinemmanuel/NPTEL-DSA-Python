""" Tuples """
# simultaneous assignments
a, b, c = 10, 11, 12
# is actually (a, b, c) = (10, 11, 12)
t = 1, 2, 3
print(type(t))

point = (10, 20) # tuple
x_coordinate = point[0]
y_coordinate = point[1]
print(x_coordinate, y_coordinate)

# But tuples are immutable, we can't do point[0] = 100

" Dictionary "
empty_dict = {}
empty_dict["One"] = 1 # assigning key value pair
empty_dict["Two"] = 2
print(empty_dict)
# Key should be immutable (int, float, bool, string, tuple)
# Value can be mutable or immutable

match = {"m1":{"p1":100, "p2":95}, "m2":{"p1":104, "p2":321}}
print(match["m1"]["p2"])
print(empty_dict.keys())