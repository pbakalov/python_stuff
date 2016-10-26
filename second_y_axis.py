import matplotlib.pylab as plt
from numpy import linspace,sin,cos
plt.ion()

x=linspace(-5,5,101)

plt.figure()
ax1=plt.gca()
ax1.plot(x,sin(x))
ax1.set_ylabel('sin(x)')

ax2=ax1.twinx()
ax2.plot(x,10*cos(x))
ax2.set_ylabel('10*cos(x)')
raw_input()

