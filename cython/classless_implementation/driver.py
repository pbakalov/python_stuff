from big_sum import run, pure_python_run
from numpy import zeros
from time import time

a = zeros(1000, float)

t = time()
b = run(a)
print time() - t
print b[:10]

t = time()
b = pure_python_run(a)
print time() - t
print b[:10]

