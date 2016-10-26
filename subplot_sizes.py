import numpy as np
import matplotlib.pylab as plt 
from matplotlib import gridspec
plt.ion()

# generate some data
x = np.arange(0, 10, 0.2)
y = np.sin(x)

# plot it
fig = plt.figure() 
gs = gridspec.GridSpec(2, 2, height_ratios = [2,1], width_ratios=[3, 1]) 
ax0 = plt.subplot(gs[0])
ax0.plot(x, y)
ax1 = plt.subplot(gs[1])
ax1.plot(y, x)
ax2 = plt.subplot(gs[2])
ax2.plot(x, y)
ax3 = plt.subplot(gs[3])
ax3.plot(y, x)
ax0.plot(x, y**2)

#plt.tight_layout()
raw_input()
