from numpy import linspace, zeros
import matplotlib.pylab as plt
plt.ion()
from random import random

bins = 101
steps = 10**6
q_hist = zeros(bins,float)
q_vals = linspace(0,30, bins)
dq = 30./(bins-1)
q0 = 1.

for i in xrange(steps):
    rn = random()
    q = q0*rn/(1-rn)
    if int(q/dq)<bins:
        q_hist[int(q/dq)]+=1

plt.plot(q_vals+dq/2,q_hist/q_hist[0]/(1+dq/2/q0)**2, 'b-o')
plt.plot(q_vals+dq/2, 1/(1+(q_vals+dq/2)/q0)**2, 'g-x')
raw_input()
