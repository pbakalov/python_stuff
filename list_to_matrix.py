from numpy import array,arange

data=[[],[]]

for i,j in zip(arange(10),arange(10,20)):
	data[0].append(i)
	data[1].append(j)

print data
data=(array(data))
print data
print data.T #transpose
b=arange(10)
print b
print b.T
print array([b]).T
