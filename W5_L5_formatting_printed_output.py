print("Joswin", "is", "the", "best", sep="$", end="(^_^)\n")

""" format() method """
print("First : {0}, Second : {1}".format("Joswin", 100))
# First : Joswin, Second : 100
print("First : {1}, Second : {0}".format("Joswin", 100))
# First : 100, Second : Joswin
print("First : {a}, Second : {f}".format(a="Joswin", f=99))
# First : Joswin, Second : 99

print("Value : {0:3d}".format(10))
# Value :  10
print("Value : {0:7.3f}".format(55.223433))
# Value :  55.223