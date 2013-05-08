Homework 5
Part 1
# this is a method that can calculate large number mod faster
def modular_exponent(base, exponent, mod):
    exponent = bin(exponent)[2:][::-1]

    x = 1
    power = base % mod
    for i in range(0, len(exponent)):
        if exponent[i] == '1':
            x = (x * power) % mod
        power = (power ** 2) % mod
    return x
n = 4654252230393111226989449826741007006486078009450861095070222439898324342353927553909251532232407850265642079868425916328810273416481567992145162141358151
m = n-1
(modular_exponent(2,m,n))
#Output: 1631275335353718272688521136992205307778996921510751912836784958121590177271097904110560032076219875741821572502979807785676850802289166219856576501165317
# Since 2^(n-) mod n is not equal 1. we can say based on  Fermat's 
# little theorem, the number n is a composite number.
Part 2
# since p and q a little "too close for comfort" we assume that p and q close to sqrt of n
s = int(sqrt(n))
p = next_prime(s);p
q = int(n/p);q
# Check if q is also a prime number.
is_prime(q)
# Check if n = pq.
(n == p*q)

# Output:
# p = 68222080226222296181917368518534332259513625527062166102114730123514248558499
# q = 68222080226222296181917368518534332259513625527062166102114730123514248558349L
# q is a prime number
# n is equal p times q