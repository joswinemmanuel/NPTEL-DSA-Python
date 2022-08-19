""" 1) Write a Python function frequency(l) that takes as input a list of integers and 
returns a pair of the form (minfreqlist,maxfreqlist) where,
minfreqlist is a list of numbers with minimum frequency in l, sorted in ascending order
maxfreqlist is a list of numbers with maximum frequency in l, sorted in ascending order
Here are some examples of how your function should work.

>>> frequency([13,12,11,13,14,13,7,11,13,14,12])
([7], [13])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14])
([7], [13, 14])

>>> frequency([13,12,11,13,14,13,7,11,13,14,12,14,14,7])
([7, 11, 12], [13, 14])"""

def frequency(l):
    l.sort()
    data = {}
    for i in l:
        data[i] = data.get(i, 0) + 1
    minimun, maximun = min(data.values()), max(data.values())
    l = ([], [])
    for i in data:
        if data[i] == minimun:
            l[0].append(i)
        if data[i] == maximun:
            l[1].append(i)
    return l

""" 2)An airline has assigned each city that it serves a unique numeric code.
It has collected information about all the direct flights it operates, represented 
as a list of pairs of the form (i,j), where i is the code of the starting city and
j is the code of the destination.

It now wants to compute all pairs of cities connected by one intermediate hope — city i
is connected to city j by one intermediate hop if there are direct flights of the
form (i,k) and (k,j) for some other city k. The airline is only interested in
one hop flights between different cities — pairs of the form (i,i) are not useful.

Write a Python function onehop(l) that takes as input a list of pairs representing
direct flights, as described above, and returns a list of all pairs (i,j), where i != j,
such that i and j are connected by one hop. Note that it may already be the case that
there is a direct flight from i to j. So long as there is an intermediate k with a flight
from i to k and from k to j, the list returned by the function should include (i,j).
The input list may be in any order. The pairs in the output list should be in
lexicographic (dictionary) order. Each pair should be listed exactly once.

Here are some examples of how your function should work.
 
>>> onehop([(2,3),(1,2)])
[(1, 3)]

>>> onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)])
[(1, 2), (1, 3), (1, 4), (2, 1), (3, 2), (3, 4), (4, 2), (4, 3)]

>>> onehop([(1,2),(3,4),(5,6)])
[] """

def onehop(l):
    result=[]
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[i][1] == l[j][0] and l[i][0] != l[j][1]:
                result.append((l[i][0], l[j][1]))
    return sorted(set(result))
