cimport numpy as np
import numpy as np # as suggested by jorgeca

cdef extern from "big_sum_implementation.cpp":
    cdef cppclass myclass:
        myclass() except +
        #void run(double* X, int N, int D, double* Y)
        void big_calculation(double* X, int N)

def run(np.ndarray[np.double_t, ndim=1] X):
    cdef int N
    N = X.shape[0]

    cdef np.ndarray[np.double_t, ndim=1, mode="c"] X_c
    X_c = np.ascontiguousarray(X, dtype=np.double)

    cdef myclass instance
    instance = myclass()
    instance.big_calculation(<double*> X_c.data, N)

    return X_c
