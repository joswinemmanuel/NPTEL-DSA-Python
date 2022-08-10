# x = [[3,5],"mimsy",2,"borogove",1]  # Statement 1
# y = x[0:50]                          # Statement 2
# z = y                                # Statement 3
# w = x                                # Statement 4
# x[1] = x[1][:5] + 'ery'              # Statement 5
# y[1] = 4                             # Statement 6
# w[1][:3] = 'fea'                     # Statement 7
# z[4] = 42                            # Statement 8
# x[0][0] = 5555                       # Statement 9
# a = (x[3][1] == 1)

# #Error statement 7

# b = [43,99,65,105,4]
# a = b[2:]
# d = b[1:]
# c = b
# d[1] = 95
# b[2] = 47
# c[3] = 73
# print(b)
# print(a)
# print(d)
# print(c)
# print(f"a[0] == {a[0]}, b[3] == {b[3]}, c[3] == {c[3]}, d[1] == {d[1]}")

# startmsg = "anaconda"
# endmsg = ""
# for i in range(1,1+len(startmsg)):
#   endmsg = endmsg + startmsg[-i]
# print(endmsg)

# def mystery(l):
#   l = l[2:]
#   return(l)

# mylist = [7,11,13,17,19,21]
# mystery(mylist)
# print(mylist)