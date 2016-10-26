# PB 10/2014 Leuven

import pytriqs.utility.mpi as mpi
import numpy
from mpi4py import MPI
from time import time, sleep

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
root = 1

a =0
mpi.barrier()

a+=rank
print a, rank
#total = rank
#sleep(0.02*rank)
#if mpi.is_master_node(): print "before reduce, before bcast:"
#print rank, total
#
#mpi.barrier()
#total = comm.reduce(total,op = MPI.SUM, root=root) #is there an equivalent mpi.reduce(total, op = ...) command?
#sleep(0.02*rank)
#if mpi.is_master_node(): print "after reduce, before bcast:"
#print rank, total
#
#mpi.barrier()
#total = comm.bcast(total, root = root) 
##total = mpi.bcast(total) # same as above, but this doesn't accept the root = root option (root = 0 is assumed, apparently)
#sleep(0.02*rank)
#if mpi.is_master_node(): print "after bcast:"
#print rank, total

