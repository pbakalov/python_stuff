#playing with enumerate and zip to see how they work
from numpy import linspace
emin=-2.
emax=-emin
esteps=11
energy=linspace(emin,emax,esteps)
vector=linspace(1,12,12)

print 'enumerate:'
for i,e in enumerate(energy):
	print i,e

print '\nzip:'
for v,e in zip(vector, energy): #this will stop at the end of the shorter array
	print v,e
