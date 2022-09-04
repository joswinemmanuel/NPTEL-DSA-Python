# 'self' is a name that is used inside a class to refer to the object
# that we are currently working on

# __init__() is called the constructor,
# called when object is created
# __str__() return the string representation,
# of the object when called
# str(o) == o.__str__(), implicitly invoked by print()
# __add__() : invoked implicitly by +
# p1 + p2 = p1.__add__(p2)
# __mul__() : called implicitly by *
# p1 * p2 = p1.__mul__(p2)
#__lt__(), __gt__(), __le__()
# called implicityly by <, >, <=


""" Class on points on a plane """
class Point:

    def __init__(self, a, b):
        self.x = a 
        self.y = b 

    def __str__(self):
        return f"a point where co-ordinates ({self.x}, {self.y})"

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)

    def translate(self, deltax, deltay):
        # shifting (x, y) to (x+deltax, y+deltay)
        self.x += deltax
        self.y += deltay

    def o_distance(self):
        # return the distance from origin
        return (self.x**2 + self.y**2)**(1/2)

class Point2:
    
    def __init__(self, a=0, b=0): # a=0, b=0 are default arguments
        import math
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            self.theta = 0
        else:
            self.theta = math.atan(b/a)

    def o_distance(self):
        return self.r

    def translate(self, deltax, deltay):
        import math
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        x += deltax
        y += deltay
        self.r = math.sqrt(x*x + y*y)
        if x == 0:
            self.theta = 0
        else:
            self.theta = math.atan(y/x)

p1 = Point(5, 15)
print(p1)
# a point where co-ordinates (5, 15)
print(p1.x, p1.y)
# Output: 5 15
p1.translate(10, 5)
print(p1)
# a point where co-ordinates (15, 20)
print(p1.x, p1.y)
# Output: 15 20
print(p1.o_distance())
# Output: 25.0

p = Point(100, 100)
p4 = p + p1
print(p4)
# a point where co-ordinates (115, 120)

p2 = Point2(15, 20)
print(p2.o_distance())
# Output: 25.0
p2.translate(5, 5)
# Now point (15, 20) becomes (20, 25)
# also r and theta value also changes
print(p2.o_distance())
# Output: 32.01562118716424 , which is sqrt(20**2 + 25**2)
