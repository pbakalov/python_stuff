from pylab import *
import matplotlib.pylab as plt
plt.ion()
from scipy import *
from scipy import optimize

# Generate data points with noise
num_points = 150
x_vals = linspace(5., 8., num_points)
y_vals = 11.86*cos(2*pi/0.81*x_vals-1.32) + 0.64*x_vals+4*((0.5-rand(num_points))*exp(2*rand(num_points)**2))

# Fit the first set
#fitfunc = lambda x, p0, p1,p2,p3: p0*cos(2*pi/p1*x+p2) + p3*x # Target function
def fitfunc(x, p0, p1, p2, p3):
    return p0*cos(2*pi/p1*x+p2) + p3*x # Target function

def fitfunc(x, p0, p1, p2, p3, p4, p5, p6, p7):
    return p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4 + +p5*x**5 + p6*x**6 + p7*x**7
#p0 = [11., 0.8, -1.1, 0.5] # Initial guess for the parameters
p0 = [1., 1.8, 1.1, 0.5] # Initial guess for the parameters
#p, pcov = optimize.curve_fit(fitfunc, xdata = x_vals, ydata=y_vals,p0 = p0, sigma = ones(num_points),  absolute_sigma = False) #, p0=p0, sigma = y_vals*0.01)
p, pcov = optimize.curve_fit(fitfunc, xdata = x_vals, ydata=y_vals)
print p

time = linspace(x_vals.min(), x_vals.max(), 100)
plot(x_vals, y_vals, "ro", time, fitfunc(time, p[0], p[1], p[2], p[3]), "r-") # Plot of the data and the fit
#plot(x_vals, y_vals, "ro", time, fitfunc(time, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7]), "r-") # Plot of the data and the fit

# Legend the plot
title("Oscillations in the compressed trap")
xlabel("time [ms]")
ylabel("displacement [um]")
legend(('x position', 'x fit', 'y position', 'y fit'))

ax = axes()

text(0.8, 0.07,
     'x freq :  %.3f kHz ' % (1/p[1]),
     fontsize=16,
     horizontalalignment='center',
     verticalalignment='center',
     transform=ax.transAxes)

#show()
raw_input()
