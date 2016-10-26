from random import random
from numpy import tanh, array, logspace
import matplotlib.pylab as plt
plt.ion()

steps = 10**5
warm_up = 10**5
gamma = 10.
sigma_series = []
beta_series = logspace(-3, 2, 20)
p_add = 0.4
p_remove = 0.4
p_shift = 1 - (p_add+p_remove)

for beta in beta_series:
    kinks = 0.
    n = 0
    
    for i in xrange(steps+warm_up):
        rn = random()
        if p_add > rn: #propose n --> n+2
            r = (beta*gamma)**2/((n+2)*(n+1))/(p_add/p_remove)
            if random() < r: #accept
                n+=2
            else: #reject
                pass
        elif p_add+p_remove > rn: #propose n --> n-2
            if n >= 2:
                r = (beta*gamma)**2/(n*(n-1))/(p_add/p_remove)
                r = 1/r
            else:
                r = 0.
            if random() < r: #accept
                n-=2
            else: #reject
                pass
        else: #shift
            pass
        if i >=warm_up:
            kinks +=n
    av_kinks = kinks/steps/(beta*gamma)
    print beta, av_kinks, tanh(beta*gamma)
    sigma_series.append(av_kinks)

plt.semilogx(beta_series, sigma_series, '-x')
plt.semilogx(beta_series, tanh(array(beta_series)*gamma), '-o')
raw_input()
