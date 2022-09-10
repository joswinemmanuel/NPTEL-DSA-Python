""" float the sentence break up into MANTISSA and EXPONENT """
# 1.2345 = 12345 x 10**-4
#      (mantissa)  (exponent)
# 0.602    X 10**24 
#(mantissa) (exponent)

def divides(m, n):
    return True if m % n == 0 else False

def even(m):
    return divides(m, 2)

def odd(m):
    return not even(m)

print(divides(10, 5))
print(even(8))
print(odd(8))
print(odd(5))
