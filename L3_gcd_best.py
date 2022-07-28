def gcd(m, n):

    if n == 0:
        return m
    return gcd(n, m % n)

    # if m < n:
    #     m, n = n, m

    # if m % n == 0:
    #     return n
    # else:
    #     return gcd(n, m % n)  # m % n < n always

print(gcd(30, 75))