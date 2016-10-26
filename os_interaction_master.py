#this will call os_interaction_slave.py twice consecutively
#I want to see whether it will wait for the first call to finish before calling again
#result: it waits.
#May 2013

from os import system

for i in range(2):
	cmd="python os_interaction_slave.py "+str(i)+" master_text"
	system(cmd)
