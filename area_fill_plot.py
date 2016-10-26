import matplotlib.pyplot as plt
from numpy import linspace,sin,cos,sqrt
plt.ion()
a=5 #bandwidth
b=4 #band height
c=3 #filling
x = linspace(0,b,301)
y1 = -a*sqrt(1-(x/b)**2)+a
y1p = a*sqrt(1-(x/b)**2)+a
y2= [c for i in x]
#y1 = sin(x)+3
#y2 = cos(x)/cos(x)/2

plt.plot(x,y1,x,y2,x,y1p,color='k',lw=2)
plt.fill_between(x,y1,y2,where=y1<=y2,color='0.8',interpolate = True)
#plt.ylim(0,10)
plt.xlim(0,5)
raw_input()
