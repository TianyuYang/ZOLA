#Homework Part 3
#python
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
get_primes(100)

%timeit get_primes(20)

#method 2
def get_primes1(n):
    i = 0
    primes = []
    while i != n+1:
        if is_prime(i):
            primes.append(i)
        i = i+1
    return primes
get_primes1(100)

%timeit get_primes(20)

%cython
def get_primes(int n):
    cdef numbers = set(range(n, 1, -1))
    cdef primes = []
    while numbers:
        cdef p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
get_primes(100)

%timeit get_primes(20)