from mpl_toolkits.mplot3d import axes3d
import matplotlib.pylab as plt
from matplotlib import cm
from numpy import linspace, sin, cos, pi,meshgrid

plt.ion()
fig = plt.figure()
#ax= fig.add_subplot(111, projection = '3d')
ax= fig.add_subplot(111)

x=linspace(-2.5,2.5,101)
y=linspace(-2,2,101)
X,Y = meshgrid(x,y)
z= -cos(pi*Y)-X**2/2 + X**4/4
V= linspace(-2,2,17)
#ax.contour(X,Y,z)
cset = ax.contour(X, Y, z, V, cmap=cm.coolwarm, stride = 0.1, extend3D = 'true')
ax.clabel(cset, fontsize=12, inline=1)
plt.xlabel('x')
plt.ylabel('$y/\pi$')

raw_input()
