from numpy import pi, linspace, zeros, cos
import h5py
from mpi4py import MPI as mpi
from time import time
#plt.ion()

comm = mpi.COMM_WORLD
rank = comm.rank

def parallel_dos_3d(nk, n_eps):

    D = 2.*3*t
    de = 2.*D/n_eps
    dos = zeros(n_eps, float)
    tot_dos = zeros(n_eps,float)
    dos_mesh = linspace(-D+de/2.,D-de/2., n_eps)

    k_step = 2*pi/nk

    comm = mpi.COMM_WORLD
    rank = comm.rank
    size = comm.size

    kx,ky,kz  = kpoints_list3d(nk)
    domain=distrib_params(size,rank,nk**3)
    for j in range(int(domain[0]),int(domain[1])):
        eps_k = eps_kernel(kx[j]*k_step, ky[j]*k_step, kz[j]*k_step)
        dos[int((eps_k + D -1e-10)/de)]+=1

    dos = 1.*dos/nk**3

    comm.Reduce(dos, tot_dos,op = mpi.SUM, root=0)
    comm.Bcast(tot_dos, root = 0)
    #mpi.report("k-integration is finished")
    if rank == 0: print "k-integration is finished"
    return tot_dos, dos_mesh

def eps_kernel(kx, ky, kz):
    eps_k = -2*t*(cos(kx) + cos(ky) + cos(kz))
    return eps_k

def distrib_params(size,rank,N):

  temp=zeros(size)
  #print temp
  for i in range(size):  
     temp[i]=N/size

  domain=zeros(2)
  k=N%size

  if(k != 0):
    for i in range(k):
       temp[i]=temp[i]+1
 
  s = 0;
  for i in range(rank):
     s = s + temp[i] 
 
  domain[0]=int(s)
  domain[1]=int(s+temp[rank])
#  print "d0=",domain[0],"d1=",domain[1],"\n"

  return domain

def kpoints_list3d(N): #rather memory intensive; one can do better
    temp_kx = zeros(N**3)
    temp_ky = zeros(N**3)
    temp_kz = zeros(N**3)
    count=0
    for kx in range(N):
        for ky in range(N):
            for kz in range(N):
                temp_kx[count] = kx
                temp_ky[count] = ky
                temp_kz[count] = kz
                count = count + 1
    return temp_kx, temp_ky, temp_kz
    
t = 1. #hopping
nk_list = [40,100,200]#,400]#,800]
nk_list_done = []

for nk in nk_list:
    print "nk", nk

    t1 = time()
    dos, dos_mesh = parallel_dos_3d(nk, 101)
    nk_list_done.append(nk)
    if rank == 0:
    #if mpi.is_master_node():
        print "time: ", time() - t1
        #plt.plot(dos_mesh, dos, '-o', label = str(nk))
        #plt.legend(loc = 'best')
    
        A = h5py.File("dostest.h5", 'a')
        if "nk_list" in A:
            del A["nk_list"]
        A["nk_list"] = nk_list_done

        if "dos"+str(nk) in A:
            del A["dos"+str(nk)]
        A["dos"+str(nk)] = dos

        if "dos_mesh"+str(nk) in A:
            del A["dos_mesh"+str(nk)]
        A["dos_mesh"+str(nk)] = dos_mesh
        del A

#raw_input() 
