#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random
def isPrime(n, k):
    if n == 1: return False 
    if n==2: return True
    rootFound = False
    for i in range(k):
        if rootFound: break
        a = random.randint(2,n-1)
        if pow(a, n-1, n) != 1: return False
        # We can write n-1 as t2^r, t odd
        t = n-1
        while t % 2 == 0:
            t >>= 1
        b =pow(a, t, n)
        if b: continue
        while b != -1:
            b = pow(b, 2, n)
            if b == 1: 
                rootFound = True
    return True

def safePrime(l):
    while(1):
        n = random.randint(1<<l, 1<<(l+1))
        if isPrime(n, 5) and isPrime(n//2, 5):
            return n
        
def generator(p):
    while(1):
        g = random.randint(1, p-1)
        if pow(g, (p-1)//2, p) == p-1:
            return g
def key_gen(l):
    p = safePrime(l)
    q = p//2
    g = pow(generator(p),2,p)
    sk = random.randint(1, q-1)
    ck = pow(g, sk, p)
    return (p,q,g,sk,ck)

# Code from GeeksforGeeks
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if (x < 0):
        x = x + m0
    return x

def encrypt(m, ck, g, p, q):
    r = random.randint(1,q-1)
    return (pow(g, r, p), (m*pow(ck,r,p)) % p)

def decrypt(c, p, sk):
    return (c[1]*pow(modInverse(c[0], p), sk, p))%p


# In[87]:


#Setup 
#n Voters
n = 100
m = 4
# Public key ck and private key sk generation given security parameter l
p, q, g, sk, ck = key_gen(100)
# Commit and Decommit functions
Com = lambda (ck, M): encrypt(M, ck, g, p, q)
Dec = lambda (sk, C): decrypt(C, p, sk)
# for l in range(n):
# Choose random permutations for each side of each ballot
p = np.array([[np.random.permutation(m) for i in range(2)] for i in range(n+1)])
# Choose unique vote codes
C = np.array([[np.random.permutation(np.arange(2*m*l + a*m + 1, 2*m*l + (a+1)*m + 1)) for a in range(2)] for l in range(n+1)])
x = np.max([2*m-1, n+1])
# Create array of powers of x. The (i+1)-th power indicates the (i+1)-th rank/position
R = []
temp = 1
for i in range(m):
    R.append(temp)
    temp*= x
# Commit vote code values and apply permutation
U = 


# In[80]:


import numpy as np

