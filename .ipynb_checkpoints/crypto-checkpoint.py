import numpy as np
import random

def isPrime(n, k):
    if n == 1: return False
    if n == 2: return True
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
    x = random.randint(1, q-1)
    h = pow(g, x, p)
    return ((p,q,g,h),(p,q,g,x))

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

def encrypt(m, ck, r): # change ck to dictionary????
    p,q,g,h = ck
    return (pow(g, int(m), p) * pow(h,r,p)) % p # we make sure that m is of type int

def decrypt(c, sk, r): ### change decrypt to recieve randomness?
    p,q,g,x = sk
    gr = pow(g, r, p)
    # remove randomness and get g^M
    g_m = (c * pow(modInverse(gr, p), x, p)) % p
    # solve "easy" DLP by brute-force
    i = 0
    temp = 1
    while(1):
        if temp == g_m: return i
        i += 1
        temp = (temp * g) % p
