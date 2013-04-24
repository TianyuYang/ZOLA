# Homework Part 1
#python from homework 2
def cal_cd_cm(a,b):
    n = min(a,b)
    m = max(a,b)
    r = 0
    if (a < b):
        t = a
        a = b
        b = t
        r = a % b
        while( r != 0):
            a = b
            b = r
            r = a % b
        return b
# python from classnotes
def gcd1(u, v):
    if u == v: return u
    if u == 0: return v
    if v == 0: return u
    if u%2 == 0:
        if v%2:
            return gcd1(u >> 1, v)
        else:
            return gcd1(u >> 1, v >> 1) << 1
    if v%2 == 0:
        return gcd1(u, v >> 1)
    if u > v:
        return gcd1((u - v) >> 1, v)
    return gcd1((v - u) >> 1, u)

cal_cd_cm(2012*next_prime(2^40),2012*next_prime(2^41))
# from class
gcd1(2012*next_prime(2^40),2012*next_prime(2^41))
gcd(2012*next_prime(2^40),2012*next_prime(2^41))

%timeit cal_cd_cm(2012*next_prime(2^40),2012*next_prime(2^41))
%timeit gcd1(2012*next_prime(2^40),2012*next_prime(2^41))
%timeit gcd(2012*next_prime(2^40),2012*next_prime(2^41))

%cython

def cal_cd_cm(double a,double b):
    cdef double n = min(a,b)
    cdef double m = max(a,b)
    cdef double r = 0
    if (a < b):
        t = a
        a = b
        b = t
        r = a % b
        while( r != 0):
            a = b
            b = r
            r = a % b
        return b

%timeit cal_cd_cm(2012*next_prime(2^40),2012*next_prime(2^41))
