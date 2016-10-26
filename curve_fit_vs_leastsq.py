from pylab import *
import matplotlib.pylab as plt
plt.ion()
from scipy import *
from scipy import optimize

# Generate data points with noise
num_points = 150
x_vals = linspace(5., 8., num_points)
y_vals = 11.86*cos(2*pi/0.81*x_vals-1.32) + 0.64*x_vals+4*((0.5-rand(num_points))*exp(2*rand(num_points)**2))

fitfunc = lambda p, x: p[0]*cos(2*pi/p[1]*x+p[2]) + p[3]*x # Target function
def fitfunc2(x, a0, a1, a2, a3): #the same target function
    return fitfunc([a0,a1,a2,a3], x) 
fitfunc3 = lambda x, a0, a1, a2, a3: fitfunc([a0,a1,a2,a3], x) # another identical target function

p0 = [5., .8, 0.2, -1.] # Initial guess for the parameters

#fit using curve_fit
#a, pcov = optimize.curve_fit(fitfunc3, xdata = x_vals, ydata=y_vals,p0 = p0, sigma = ones(num_points)*2,  absolute_sigma = False) 
a, pcov = optimize.curve_fit(fitfunc2, xdata = x_vals, ydata=y_vals, p0 = p0)
print a
print diagonal(pcov)

# Fit using leastsq
errfunc = lambda p, x, y: fitfunc(p, x) - y # Distance to the target function
p1, success = optimize.leastsq(errfunc, p0[:], args=(x_vals, y_vals))
print p1

time = linspace(x_vals.min(), x_vals.max(), 100)
plot(x_vals, y_vals, "ro", time, fitfunc2(time, a[0], a[1], a[2], a[3]), "r-x") # Plot of the data and the fit
plot(time, fitfunc(p1, time), "b-") 

# Legend the plot
title("Oscillations in the compressed trap")
xlabel("time [ms]")
ylabel("displacement [um]")
legend(('data', 'curve_fit','leastsq fit'))

raw_input()
