# Homework part 5
#python
import numpy
a = numpy.zeros(shape=(4,4))
a[0]=[3,4,7,8]
a[1]=[1,3,6,7]
a[2]=[4,4,2,6]
a[3]=[5,6,1,9]
import numpy
b = numpy.zeros(shape=(4,4))
b[0]=[9,4,6,3]
b[1]=[4,3,5,1]
b[2]=[5,4,5,6]
b[3]=[5,2,8,3]
def matrixmult (A, B):
    C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C
matrixmult(a,b)

%timeit matrixmult(a,b)


%cython
import numpy
cdef a = numpy.zeros(shape=(4,4))
a[0]=[3,4,7,8]
a[1]=[1,3,6,7]
a[2]=[4,4,2,6]
a[3]=[5,6,1,9]
import numpy
cdef b = numpy.zeros(shape=(4,4))
b[0]=[9,4,6,3]
b[1]=[4,3,5,1]
b[2]=[5,4,5,6]
b[3]=[5,2,8,3]
numpy.dot(a,b)

%timeit numpy.dot(a,b)