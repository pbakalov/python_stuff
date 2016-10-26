import matplotlib.pylab as plt
from numpy import linspace, sin, pi
plt.ion()

plt.xkcd() #should work, but doesn't: AttributeError: GraphicsContextBase instance has no attribute 'draw_path'

x = linspace(-pi,pi, 101)

#plt.plot(x, sin(x),  '--x', linewidth =2 ,label = "sin(x)")
plt.plot(x, sin(x),  '-')

#plt.legend()
plt.pause(0.1)
raw_input()
