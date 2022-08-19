with open("W5_L3_file1.txt", "w") as f:
    f.write("Hey New World\n")
    f.write("New line here\n")
    f.write("Another new line here")
    # f.write() - to write to a file, return number of characters written
    f.writelines(["line 1\n", "line 2\n", "line 3\n"])
    # f.writelines() - to write a list of lines
 
# r - mode to read a file
# w - mode to write to a file
# a - mode to append a file
# f.close() - flushes the buffer if opened used f.open()
# with open() as f - if used don't need to close using f.close()

with open("W5_L3_file1.txt") as f:
    print(f.read())
    print()
# f.read() - read the entire data in a string format
# f.read(n) - read the n characters of the file

with open("W5_L3_file1.txt") as f:
    print(f.readline(), end="")
    print(f.readline())
# f.readline() - read the next line in string format
with open("W5_L3_file1.txt") as f:
    print(f.readlines())
# f.readlines() - read and give a list of each line as string
with open("W5_L3_file1.txt") as f:
    for i in f.readlines():
        print(i[:-1]) # will exclude '\n' in the end

""" f.seek() can be used to move the file poiner to any position """
# f.seek(0) - to move file pointer to begining of the file