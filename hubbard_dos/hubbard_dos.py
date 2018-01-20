#free DOS of a cubic lattice in d = 1,2,3 dimensions
#Jan 2018
from numpy import pi, zeros, arange, cos, linspace
from time import time
import matplotlib.pylab as plt
import h5py
import sys
plt.ion()

ne = 101
t = 1.
d1 = False
d2 = True
d3 = False

#1d case
if d1:
    t1 = time()
    d = 1
    de = 4*d*t/ne
    nk = 1000000
    dos = zeros(ne+2, float)
    k_step = 2*pi/nk
    k_vals = arange(nk)*k_step
    for k in k_vals:
        eps_k = -2*t*cos(k)
        dos[int((eps_k + 2*t*d+de)/de)] += 1
    
    dos = dos/nk**d
    e_vect = linspace(-2-de/2,2+de/2,ne+2)
    plt.plot(e_vect,dos, '-o', label = "1D")
    
    A = h5py.File("dos_1d_ne%s_nk%s.h5"%(ne,nk), "w")
    A.create_group("log")
    log = A["log"]
    log["script"] = open(sys.argv[0]).read()
    A["dos"] = dos
    A["mesh"] = e_vect
    A["nk"] = nk
    A["ne"] = ne
    A.close()
    
    nk1 = 1*nk
    print "1d DOS done in", time() - t1

#2d case
if d2:
    t1 = time()
    d = 2
    de = 4*t*d/ne
    nk = 8000
    dos = zeros(ne+2, float)
    k_step = 2*pi/nk
    k_vals = arange(nk)*k_step
    
    for kx in k_vals:
        for ky in k_vals:
            eps_k = -2*t*(cos(kx) + cos(ky))
            dos[int((eps_k + 2*d*t + de)/de)] += 1
    
    dos = dos/nk**d
    e_vect = linspace(-2-de/2/d,2+de/2/d,ne+2)
    plt.plot(e_vect,dos, '-o', label = "2D")
    
    A = h5py.File("dos_2d_ne%s_nk%s.h5"%(ne,nk), "w")
    A.create_group("log")
    log = A["log"]
    log["script"] = open(sys.argv[0]).read()
    A["dos"] = dos
    A["mesh"] = e_vect
    A["nk"] = nk
    A["ne"] = ne
    A.close()
    
    nk2 = 1*nk
    print "2d DOS done in", time() - t1

#3d case
if d3:
    t1 = time()
    d = 3
    de = 4*t*d/ne
    nk = 500
    dos = zeros(ne+2, float)
    k_step = 2*pi/nk
    k_vals = arange(nk)*k_step
    
    for kx in k_vals:
        for ky in k_vals:
            for kz in k_vals:
                eps_k = -2*t*(cos(kx) + cos(ky)+cos(kz))
                dos[int((eps_k + 2*d*t + de)/de)] += 1
    
    dos = dos/nk**d
    e_vect = linspace(-2-de/2/d,2+de/2/d,ne+2)
    plt.plot(e_vect,dos, '-o', label = "3D")
    
    A = h5py.File("dos_3d_ne%s_nk%s.h5"%(ne,nk), "w")
    A.create_group("log")
    log = A["log"]
    log["script"] = open(sys.argv[0]).read()
    A["dos"] = dos
    A["mesh"] = e_vect
    A["nk"] = nk
    A["ne"] = ne
    A.close()
    
    nk3 = 1*nk
    print "3d DOS done in", time() - t1

plt.legend(loc = 'best')
plt.xlabel(r"$\omega$/D")
plt.ylabel("DOS/a.u.")
#plt.savefig("DOS_fig_nk1_%s_nk2_%s_nk3_%s.pdf"%(nk1,nk2,nk3))
plt.savefig("DOS_fig.pdf")

raw_input()

    
            



    


