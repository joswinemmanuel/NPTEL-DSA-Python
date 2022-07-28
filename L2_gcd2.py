def gcd(m, n):
    for i in range(min(m, n), 0, -1):
        if m % i == 0 and n % i == 0:
            return i



print(gcd(150, 75))
