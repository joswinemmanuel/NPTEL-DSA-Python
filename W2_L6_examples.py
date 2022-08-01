def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def primes_upto(n):
    for i in range(0, n):
        if is_prime(i):
            print(i, end=" ")
    print()

def n_primes(n):
    i = 1
    while n != 0:
        i += 1
        if is_prime(i):
            print(i, end=" ")
            n -= 1      

primes_upto(10)

n_primes(9)