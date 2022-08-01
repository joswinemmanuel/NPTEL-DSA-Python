''' 0 (zero), "", '' (empty string), [], {}, () are treated as False '''

""" conditional execution
    repeated execution
    function execution """
# all basic knowledge on control flow

# to print all the factors of an inputted number

number = int(input("Enter the number : "))
for i in range(1, number+1):
    if number % i == 0:
        print(i, end=" ")