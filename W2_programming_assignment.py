def intreverse(n):
    return int(str(n)[::-1])

def matched(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

def sumprimes(l):
    def if_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True

    sum = 0
    for i in l:
        if if_prime(i):
            sum += i
    
    return sum
