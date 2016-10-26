#called by os_interaction_master.py
#the two files together are play with scripting
from time import sleep
from os import path
from sys import argv

#for i in range(len(argv)): 
#	print i, argv[i]

print argv[1]=="0"
print int(float(argv[1]))==0 #true if string in argv[1] can be converted to float
print int(argv[1])==0 #if argv[1] is a string with non-integer content this will throw an exception: ValueError invalid literal for int()

if int(argv[1])==0:
	filename='test_'+argv[1]+'.txt' #no need to convert argv[i], it's already a string
	text='some text'+argv[2]+'\n the end' 
	file=open(filename,"w")
	file.write(text)
	file.close()
	print 'SLAVE: now sleeping'
	sleep(6)
	print 'SLAVE: woke up'
else:
	if path.exists("./test_0.txt"): 
		print "SLAVE: file exists"
	else:
		print "SLAVE: file doesn't exist"
	
