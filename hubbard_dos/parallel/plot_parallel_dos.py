from pytriqs.archive import *
import matplotlib.pylab as plt
import sys
plt.ion()

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "dostest.h5"

A = HDFArchive("dostest.h5", 'r')
nk_list = A["nk_list"] 
print nk_list 
for nk in nk_list:

    print "nk", nk
    dos = A["dos"+str(nk)] 
    dos_mesh = A["dos_mesh"+str(nk)] 

    plt.plot(dos_mesh, dos, '-o', label = str(nk))
    plt.legend(loc = 'best')
        
del A
   
raw_input() 
