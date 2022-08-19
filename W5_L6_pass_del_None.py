""" pass - is used to do noting or leave an inteded block blank """
if True:
    pass
else:
    pass

""" del """
lst = [1, 2, 3, 4, 5]
del(lst[2])
print(lst) # [1, 2, 4, 5]

dic = {1:"one", 2:"two"}
del(dic[1])
print(dic) # {2: 'two'}

x = 10
print(x) # 10
del(x)
#print(x) # Error , del(x) makes x undefined

""" None - is a keyword used to denote 'nothing' """