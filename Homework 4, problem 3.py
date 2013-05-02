Homework 4, problem 3
This code is done after wednesday class
it is call the rational reconstruction method
to solve the problem.
rational_reconstruction(372806624339965,(37+10^15))
the Output is : 1234567/8901234

%timeit rational_reconstruction(372806624339965,(37+10^15))
625 loops, best of 3: 10.3 µs per loop

the python and cython method took too long to run and get the result.
from classnotes:
def rr1(a, m):
    m = int(m); a = int(a)
    B = int(math.sqrt(m/2))
    for n in range(B+1):
        for d in range(-B, B+1):
            if d and (n - a*d)%m == 0:
                return ZZ(n)/d
    raise ValueError("no solution")