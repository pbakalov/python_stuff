from mpl_toolkits.mplot3d import axes3d
import matplotlib.pylab as plt
from numpy import linspace, sin, cos, pi,meshgrid

plt.ion()
fig = plt.figure()
ax= fig.add_subplot(111, projection = '3d')

x=linspace(-1,1,101)
y=linspace(-1,1,101)
X,Y = meshgrid(x,y)
z= -cos(Y)-X**2/2 + X**4/4
ax.plot_wireframe(X,Y,z)
#plt.figure()
#ax.contour(X,Y,z,stride = 0.1)
raw_input()
