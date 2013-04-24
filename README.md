#Homework part 1
It have 4 methods, one of them is from homework 2, two of them are from class and one of them are from cython.
python
%timeit cal_cd_cm(2012*next_prime(2^40),2012*next_prime(2^41))
%timeit gcd1(2012*next_prime(2^40),2012*next_prime(2^41))
%timeit gcd(2012*next_prime(2^40),2012*next_prime(2^41))
625 loops, best of 3: 25.8 µs per loop
625 loops, best of 3: 157 µs per loop
625 loops, best of 3: 30.5 µs per loop
cython
%timeit cal_cd_cm(2012*next_prime(2^40),2012*next_prime(2^41))
625 loops, best of 3: 18.6 µs per loop

#Homework part 2
python
%timeit summ(10000)
25 loops, best of 3: 8.92 ms per loop
cython
%timeit sumofsquares(10000)
625 loops, best of 3: 553 µs per loop

#Homework part 3
python
%timeit get_primes1(20)
625 loops, best of 3: 365 µs per loop
cython
%timeit get_primes(20)
625 loops, best of 3: 9 µs per loop

#Homework part 4
python
%timeit det(a)
625 loops, best of 3: 996 µs per loop
cython
%timeit numpy.linalg.det(a)
625 loops, best of 3: 83.9 µs per loop

#Homework part 5
python
%timeit matrixmult(a,b)
625 loops, best of 3: 221 µs per loop
cython
%timeit numpy.dot(a,b)
625 loops, best of 3: 1.52 µs per loop
