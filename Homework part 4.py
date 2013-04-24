# Homework part 4
%cython
import numpy
cdef a = numpy.zeros(shape=(4,4))
a[0]=[2,4,6,8]
a[1]=[1,3,5,7]
a[2]=[4,4,5,6]
a[3]=[5,6,8,9]
numpy.linalg.det(a)

%timeit numpy.linalg.det(a)

#python
def det(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            sum=sum+i*(l[0][t])*(det(l1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0])
        
import numpy
b = numpy.zeros(shape=(4,4))
b[0]=[2,4,6,8]
b[1]=[1,3,5,7]
b[2]=[4,4,5,6]
b[3]=[5,6,8,9]

det(b)

%timeit det(b)