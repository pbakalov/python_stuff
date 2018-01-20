#plot free DOS of a cubic lattice in d = 1,2,3 dimensions
#Jan 2018
import matplotlib.pylab as plt
import h5py
import sys
plt.ion()

file_list  = sys.argv[1:]

fig = plt.figure("Free DOS")
for i,filename in enumerate(file_list):
    A = h5py.File(filename, "r")
    dos = A["dos"].value
    e_vect = A["mesh"].value
    A.close()
    
    plt.plot(e_vect/2,dos, '-o', linewidth = 2, label = str(i+1)+"D")
    
plt.legend(loc = 'best', fontsize = 30)
plt.xlabel(r"$\omega$/D", fontsize = 30)
plt.ylabel(r"$\rho_0(\omega)$/a.u.", fontsize = 30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.subplots_adjust(left = 0.13, right = 0.975, top = 0.97, bottom = 0.1, wspace = 0.1, hspace = 0.1)
fig.set_size_inches(13,10)
#plt.savefig("DOS_fig_nk1_%s_nk2_%s_nk3_%s.pdf"%(nk1,nk2,nk3))
plt.savefig("DOS_fig.pdf")

#raw_input()

    
            



    


