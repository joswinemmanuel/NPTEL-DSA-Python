def gcd(m, n):
    m_lst = []
    for i in range(1, m+1):
        if m % i == 0:
            m_lst.append(i)
    
    n_lst = []
    for i in range(1, n+1):
        if n % i == 0:
            n_lst.append(i)
    
    common_lst = []
    for i in m_lst:
        if i in n_lst:
            common_lst.append(i)
    
    return common_lst[-1]

print(gcd(15, 20))