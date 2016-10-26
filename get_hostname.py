from os import system, popen

print '***** \n'
system('hostname') #this is like typing 'hostname' in terminal, it will print the hostname on the screen
print '\n***** \n'

hn = system('hostname') #does not put the hostname in the variable hn
hn = popen('hostname').read() #puts the command output in hn; there are soem comments on SO which mention popen being unsafe, subprocess.popen being safer.

### alternative
import socket
hn = socket.gethostname()
print '***** \n'
print hn
print '\n***** \n'
