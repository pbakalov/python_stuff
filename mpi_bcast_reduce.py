# Figure out what reduce and bcast do
#
# comm.reduce(data_object, op = MPI.SUM, root = int):
#    "collects" information to a specified node (root); the way the information is collected
#    depends on the specified option (op); at the moment the only option I've used is MPI.SUM;
#    the reduced quantity is set to "None" on all the other nodes
# 
# mpi.bast(data_object) (or comm.bcast(data_object, root = int)
#    broadcasts from the root node to all the other nodes (so that if data_object was defined 
#    on them with some value before
#    is overwritten
#
# PB 04/2014 Leuven

import pytriqs.utility.mpi as mpi
import numpy
from mpi4py import MPI
from time import time, sleep

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
root = 1

total = rank
sleep(0.02*rank)
if mpi.is_master_node(): print "before reduce, before bcast:"
print rank, total

mpi.barrier()
total = comm.reduce(total,op = MPI.SUM, root=root) #is there an equivalent mpi.reduce(total, op = ...) command?
sleep(0.02*rank)
if mpi.is_master_node(): print "after reduce, before bcast:"
print rank, total

mpi.barrier()
total = comm.bcast(total, root = root) 
#total = mpi.bcast(total) # same as above, but this doesn't accept the root = root option (root = 0 is assumed, apparently)
sleep(0.02*rank)
if mpi.is_master_node(): print "after bcast:"
print rank, total

