#Q: what happens when two nested for loops in python use the same iteration index?
j=0
k=0
for i in range(10):
	#print 'outer1', i #has value 0 to 9
	for i in range(3):
		print j,k
		#print 'inner', i #has a value between 0 and 2
		k+=1
	j+=1
	#print 'outer2', i #has a value between 0 and 2
