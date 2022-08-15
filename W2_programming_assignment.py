""" 1) Write a function intreverse(n) that takes as input a positive integer n 
and returns the integer obtained by reversing the digits in n.
Here are some examples of how your function should work. """

def intreverse(n):
    return int(str(n)[::-1])

""" 2) Write a function matched(s) that takes as input a string s and checks if the brackets
"(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" 
has a matching "(" before it. Your function should ignore all other symbols that appear in s.
Your function should return True if s has matched brackets and False if it does not.
Here are some examples to show how your function should work """

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

""" 3) Write a function sumprimes(l) that takes as input a list of integers l
and retuns the sum of all the prime numbers in l.
Here are some examples to show how your function should work. """

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
