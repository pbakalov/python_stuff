from big_sum import run, pure_python_run
from numpy import zeros
from time import time
import numpy as np

a = zeros((10,10,10), np.complex128)

t = time()
b = run(a)
print time() - t
#print b[:5][:5]
print b[:4,:4,:4]

t = time()
b2 = pure_python_run(a)
print time() - t
#print b[:5][:5]
print b2[:4,:4,:4]

