""" Programs need to interact with user
- receive input  (Keyboard)
- display output (Screen) """

# Read a line of input and assign it to variable data
data = input("Enter the data : ")
# default datatype is string 
data = int(input("Enter the number : "))
# the datatype is converted to integer

while True:
    try:
        value = int(input("Enter the number : "))
    except:
        print("The entered data is not an interger. Try again...")
    else:
        break

print()
print("A line", end=" ")
print("Same line", end="\nNext line\n")
print(1, 2, 3, 4, 5, sep="-")
