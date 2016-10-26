import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
from numpy import array, exp
#import os
matplotlib.rcParams['mathtext.default']='regular'

def read_in_data(filename):
	file=open(filename, 'r')
	data=[]
	for line in file:
		if ('#'==line[0]) or len(line)<4: #skip comment lines and empty lines
			continue
		else:
			data.append([float(x) for x in line.split()])
	file.close()
	data=array(data)
	
	return data

data=read_in_data('dos_series.txt')
fig=plt.figure()
dcp=0.25
CP_min=-7.5
energy_points=501 #number of points for energy spectrum at each value of CP
style=['b-d','g-s','r-o','c-*','m-^']
color=['b','g','r','c','m']
c=0
for CP in [-7.5, -2.5, 0, 2.5, 7.5]:
	i=int((CP-CP_min)/dcp)
	x=data[i*501:(i+1)*501,2]
	y=data[i*501:(i+1)*501,1]+CP
	for j,xt in enumerate( x): #put DOS to zero for large y
		#xt=xt/(1+exp(2*(y[j]-3.2)))
		x[j]=xt
		
	#print x
	print y
	if CP == 0 or CP == 1.0:
		plt.plot(x,y,color[c], markerfacecolor = 'none', markevery =5, label=r'$\mu$ ='+str(CP)+'t')
		plt.fill_between(x,y,CP,where = y<CP,color=color[c])
		plt.fill_between(x,y,CP,where = y>CP,color=color[c], alpha = 0.5)
	#c+=1

ax = plt.axes()

#plt.text(0.48, 0.88,
#	'$\\beta$=10/t \nU = 10t',
#	fontsize=20,
#	horizontalalignment='center',
#	verticalalignment='center',
#	transform=ax.transAxes)

#plt.xlim(-11,11)
plt.ylim(-15,10)
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.set_size_inches(10,10)
#plt.xlabel('DOS', fontsize = 20)
#plt.ylabel(r'E',fontsize = 20)
#plt.xticks(fontsize = 0)
#plt.yticks(fontsize = 0)
#plt.set_fill(True)
#plt.legend(loc=4, prop={'size':16})
plt.savefig('2d_dos_plot_fill.png',dpi=300)

