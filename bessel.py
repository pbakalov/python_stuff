from scipy.special import jn, jn_zeros
from numpy import linspace

j0_zeros = jn_zeros(0, 5)
steps = 1001
for xn in j0_zeros:
    xvect=linspace(0,xn,steps)
    dx = xn/(steps-1)
    s=0.
    for x in xvect:
        s+= jn(1,x)*dx
    print xn,s

