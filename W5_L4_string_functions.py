""" lstrip() - strip the empty spaces in left """
a = "      joswin"
print(a)           #      joswin
print(a.lstrip())  # joswin

""" rstrip() - strip the empty spaces in right """

""" strip() - strip off the empty spaces in both sides """
a = "   the best     "
print(a)         #     the best    
print(a.strip()) # the best

""" find(s) - return the first occurance of s in the string """
a = "apple"
print(a.find("p")) # 1
print(a.find("pl")) # 2

""" index(s) - as same as find(s) but raise ValueError if s not found """
a = "apple"
print(a.index("ppl")) # 1   

""" replace(fromstr, tostr) - replace the fromstr with tostr in the string """
a = "apples is healthy is"
print(a.replace("is", "are")) # apples are healthy are
print(a.replace("is", "are", 1)) # apples are healthy is

""" split(s) - split a string on s into list elements """
a = "one,two,three,four"
print(a.split(","))    # ['one', 'two', 'three', 'four']
print(a.split(",", 2)) # ['one', 'two', 'three,four']

""" join(l) - recombines a list of string using a separator """
a = ["1", "2", "3", "4"]
print(",".join(a))     # 1,2,3,4 

""" capitalize() - return new string with first letter uppercase rest lower """
""" lower() - return new string with all letter lowercase """
""" upper() - return new string with all letter uppercase """
""" title() - return title format, first letter of each word in sentence capital """
a = "this world is happy"
print(a.capitalize()) # This world is happy
print(a.title())      # This World Is Happy

""" swapcase() - revert uppercase to lower and lower to upper """

""" center(n) - return string of length n with s centred with blank """
print("joswin".center(10, "*")) # **joswin**
print("joswin".ljust(10, "*"))  # joswin****
print("joswin".rjust(10, "*"))  # ****joswin


""" isalpha() - checks if the string is alphabitical """
""" isnumeric() - checks if the stirng is numerical """