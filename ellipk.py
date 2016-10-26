from scipy.special import ellipk
from numpy import linspace,sqrt, pi
import matplotlib.pylab as plt
plt.ion()

t=1.
D=4*t
x= linspace(-D,D,1000)

ei = ellipk(sqrt(1-(x/D)**2))
print ei
dos = 4/pi**2/D*ei
#plt.plot(x, ei)
plt.plot(x, dos)
raw_input()

