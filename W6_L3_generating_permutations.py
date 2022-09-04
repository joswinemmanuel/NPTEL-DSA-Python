# Often used when we need to try out all possibilities

# For instance, what is the next sequence formed from
# {a, b, c, d, e, f, g, h, i, j, k, l, m}, in dictionary after
# d c h b a e g l k o n m j i

# smallest permutation - all elements in ascending order
# a b c d e f g h i j k l m

# largest permutation - all elements in descending order
# m l k j i h g f e d c b a

# next permutation - find shortest suffix that can be incremented
# or longest suffix that cannot be incremented

# longest suffix that cannot be incremented -
# - already in descending order

# d c h b a e g l k o n m j i

# o n m j i - these letters are in descending order
# so we cannot make any larger permutations
# we fix from d to k - o n m j i is the largest permutation of the suffix
# to increment we also include k, suffix k o n m j i can be incremented
# how do we increment this?
# replace k by next largest letter to its right, m
# d c h b a e g l m o n k j i
# now arrange o n k j i in ascending order - i j k n o

# d c h b a e g l m i j k n o - is the next permutation

""" Implementation """
#1) from the right, identify first decreasing position
# k in - d c h b a e g l k o n m j i

#2) swap that value with its next larger letter to its right
# m is the next larger letter of k - in o n m j i
# it becomes - d c h b a e g l m o n k j i

#3) reverse the increasing suffix
# reverse or arrange in ascending order - o n k j i
# to i j k n o

# d c h b a e g l m i j k n o - is the next permutation