import matplotlib.pylab as plt
plt.rcParams['ytick.major.pad']='12'
from numpy import linspace

plt.ion()

bias = 6.
layers = 24
layer_list = linspace(-(layers-1.)/2., (layers-1.)/2., layers)

v = linspace(-bias/2, bias/2, layers)
fig = plt.figure()
plt.plot(layer_list, v, 'b-o', label = "V")
leg = plt.legend(loc="best", prop = {'size':30})
leg.draw_frame(False)
plt.xlim(-12,12)
plt.xlabel("n", fontsize=30)
plt.ylabel("V(n)", fontsize=30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.subplots_adjust(left = 0.2, right = 0.975, top = 0.95, bottom = 0.2)
fig.set_size_inches(10,7)

plt.savefig("test.pdf")

raw_input()
