#the interesting thing here is the use of join for ouput

import pprint
import matplotlib.pyplot as plt
import pylab
from numpy import array
from numpy import zeros

pylab.ion()

#read in el. data from file
spaca_charge_file=open("int_space_charge_dens1D.dat","r")
spaca_charge_file.readline() #skip first line
total_den=[]
for line in spaca_charge_file:
	data_float=[float(x) for x in line.split()]
	total_den.append(data_float)

spaca_charge_file.close

total_den=array(total_den)
i=total_den.shape[0] #get number of rows
j=total_den.shape[1] #get number of columns 
output=zeros([i,j+1],float)
#calculate capacitance
dv=abs(total_den[0,0]-total_den[1,0]) #determine voltage step
cap=zeros(i,float) 	#initialize capacitance array 
			#(4 points shorter because of
			#numeric derivative calculation)

n=2 #counter
q=1.602e-19 #elementary charge
while n<i-2:
	cap[n]=-(2./3*(total_den[n+1,j-1]-total_den[n-1,j-1])-(total_den[n+2,j-1]-total_den[n-2,j-1])/12)/dv*q #four point numerical derivative formula
	n+=1

plt.plot(total_den[2:i-2,0],abs(cap[2:i-2]))
plt.ylim(0,cap[2]*1.2)
plt.xlim(total_den[2,0],total_den[i-2,0])
output[:,0:j]=total_den
output[:,j]=cap #add capacitance column

#write things out to a file
f = open("cv_out2.txt", "w")
f.write("\n".join(["\t".join([str(n) for n in item]) for item in output.tolist()]))
f.close()
raw_input()
