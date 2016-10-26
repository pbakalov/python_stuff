import matplotlib.pylab as plt
plt.ion()

fig = plt.figure(figsize = (4,4))
ax = fig.add_subplot(111)
ax.bar([1,2,3], [10,100,1000], log = True)
plt.savefig("test.png")
raw_input()
