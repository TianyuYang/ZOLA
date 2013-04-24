#Homework Part 2
#python
def summ(n):
    summ = 0
    i = 0
    while i != n+1:
        summ = summ + i^2
        i = i+1
    return summ
summ(10000)

%timeit summ(10000)

def sumofsquares(int n):
    cdef count_list = range(1,n+1)
    return sum(i^2 for i in count_list)
sumofsquares(10000)

%timeit sumofsquares(10000)