# Matrix multiplication is associative
# ABC = (AB)C = A(BC)
# Bracketing doesn't change answer...
# but changes the complexity of computing
# How?
# Assume A[1,100], B[100,1], C[1,100]
# computing A(BC)
#  - BC is [100,100], 100 x 1 x 100 = 10000 steps
#  - A(BC) is [1,100], 1 x 100 x 100 = 10000 steps
# computing (AB)C
#  - AB is [1,1], 1 x 100 x 1 = 100 steps
#  - (AB)C is [1,100], 1 x 1 x 100 = 100 steps
# A(BC) takes 20000 steps
# (AB)C takes 200 steps