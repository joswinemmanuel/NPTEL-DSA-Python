def find_pos(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i 
    return -1
" gives the index of item in list, if item not in list gives -1 "

# break can be used to break out of a loop
for i in range(1, 10):
    if i == 6:
        break
    print(i, end=" ")
# 1 2 3 4 5 when i == 6 it breaks out of the loop
print()

" In Python there is an 'else' case for the 'for', it executes after all the iteration in the loop "
for i in range(1, 6):
    print(i, end=' ')
else:
    print("all values printed")
# 1 2 3 4 5 all values printed

" but if the loop is breaked out using 'break' 'else' case won't be executed "
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=' ')
else:
    print("all values printed")
# 1 2   see else case didn't get exectued as loop was breaked 
