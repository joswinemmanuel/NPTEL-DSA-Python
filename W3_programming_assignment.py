def contracting(l):
    diff= abs(l[1] - l[0])
    for i in range(2, len(l)):
        if abs(l[i] - l[i-1]) < diff:
            diff = abs(l[i] - l[i-1])
        else:
            return False
    return True 

def counthv(l):
    hc, vc = 0, 0
    for i in range(1, len(l)-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            hc += 1
        elif l[i] < l[i-1] and l[i] < l[i+1]:
            vc += 1
    return [hc, vc]        

# def leftrotate(m):
#     l = len(m)
#     arr = []
#     for i in range(l):
#         sub_arr = []
#         for j in range(l):   
#             sub_arr.append(m[j][(l-1)-i])
#         arr.append(sub_arr)
#     return arr

def leftrotate(m):
    l = len(m)
    arr = [[0 for i in range(l)] for i in range(l)]
    for i in range(l):
        for j in range(l):   
            arr[i][j] = m[j][(l-1)-i]

    return arr


print(leftrotate([[1,2],[3,4]]))
print(leftrotate([[1,2,3],[4,5,6],[7,8,9]]))
print(leftrotate([[1,1,1],[2,2,2],[3,3,3]]))