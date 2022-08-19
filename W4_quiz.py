# 1)
def mystery(l):
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])

print(mystery([22,14,19,65,82,55]))

# 2)
pairs = [ (x,y) for x in range(4,1,-1) for y in range(5,1,-1) if (x+y)%3 == 0 ]
print(pairs)

# 3)
wickets = {"Tests":{"Bumrah":[3,5,2,3],"Shami":[4,4,1,0],"Ashwin":[2,1,7,4]},"ODI":{"Bumrah":[2,0],"Shami":[1,2]}}
# wickets["ODI"]["Ashwin"][0:] = [4,4] Error
# wickets["ODI"]["Ashwin"].extend([4,4]) Error
wickets["ODI"]["Ashwin"] = [4,4]
# wickets["ODI"]["Ashwin"] = wickets["ODI"]["Ashwin"] + [4,4] Error

# 4)
hundreds = {}
# hundreds["Tendulkar, international"] = 100
# hundreds["Tendulkar"] = {"international":100}
# hundreds[("Tendulkar","international")] = 100
hundreds[["Tendulkar","international"]] = 100