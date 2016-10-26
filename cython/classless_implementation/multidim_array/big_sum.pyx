#check out https://github.com/cython/cython/wiki/tutorials-NumpyPointerToC
#and http://stackoverflow.com/questions/17855032/passing-and-returning-numpy-arrays-to-c-methods-via-cython
cimport numpy as np
import numpy as np # as suggested by jorgeca

cdef extern from "big_sum_implementation.cpp":
    void big_calculation(complex* X, int N, int M, int L)

def run(np.ndarray[np.complex128_t, ndim=3, mode="c"] X):
    cdef int N
    cdef int M
    cdef int L
    N = X.shape[0]
    M = X.shape[1]
    L = X.shape[2]

    #cdef np.ndarray[np.double_t, ndim=3, mode="c"] X_c
    #X_c = np.ascontiguousarray(X, dtype=np.double)
    #big_calculation(&X_c[0,0,0], N, M, L)

    big_calculation(&X[0,0,0], N, M, L)

    #return X_c
    return X

def pure_python_run(data):
    for j in xrange(1000):
        for i in xrange(data.shape[0]):
            for k in xrange(data.shape[1]):
                for l in xrange(data.shape[2]):
                    data[i][k][l] = ((i+1)*(k+1)*(l+1))**2 + 1j*(i+k+l)
    return data
        
