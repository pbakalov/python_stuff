import h5py
import matplotlib.pylab as plt
from numpy import zeros
plt.ion()

f = h5py.File("/Users/fun/data/data_slab_ncyc110000_nloop50_np160_nl60_nlay24_t1.0_tp1.0_U13.2_mu6.6_bias4.5_beta30.0_ctd.h5", 'r')
print f.keys()
sigma_data = f["sigma_final24"]
print sigma_data.keys()
sigma_up = sigma_data["up"]
print sigma_up.keys()
sigma_up_data = sigma_up["data"]
print sigma_up_data
print sigma_up_data.shape
print sigma_up_data.dtype
print sigma_up_data[:,0,0,0]
#alternatively
sigma_up_data2 = f["sigma_final24"]["up"]["data"]
print sigma_up_data2
print sigma_up_data2.shape
print sigma_up_data2.dtype
print sigma_up_data2[:,0,0,0]

#plot
ReSigma  = zeros((1025,24), float)
ImSigma  = zeros((1025,24), float)
for i in range(24):
    ReSigma[:,i] = sigma_up_data[:,i,i,0]
    ImSigma[:,i] = sigma_up_data[:,i,i,1]
    plt.plot(ImSigma[:,i], '-o')
f.close()
raw_input()
