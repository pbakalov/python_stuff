from numpy import loadtxt
import matplotlib.pylab as plt
plt.ion()

data = loadtxt("rank_data.txt", delimiter = ",")
print data.shape

plt.plot(data[::-1,3], 'o')

plt.gca().invert_yaxis()
raw_input()
