from numpy import fft, linspace, sin, pi, cos, zeros, meshgrid
import matplotlib.pylab as plt

plt.ion()

L = 2*pi
N = 40
x = linspace(0,L, N)

g_x = zeros((N,N), complex)
g_min_x = zeros((N,N), complex)

for i in range(N):
    for j in range(N):
        x_ = x[i]
        y_ = x[j]
        #g_x[i,j] = sin(x_) + sin(y_) + 5*sin(5*x_) + 10*sin (10*y_) + 10*sin(10*x_)
        g_x[i,j] = sin(x_) #+ 5*sin(5*x_) + 10*sin(10*x_)
        x_*=-1
        y_*=-1
        g_min_x[i,j] = sin(x_) #+ 5*sin(5*x_) + 10*sin(10*x_)

#plot real space data
plt.figure()
plt.imshow(g_x.real.T,interpolation = "bilinear",  aspect = "auto", extent = [-pi,pi, x[0],x[-1]], vmin=g_x.real.min(), vmax=g_x.real.max()) #the .T (transpose) is necessary because otherwise the x-axis is plotted vertically (a bit odd indeed)

#2D fourier transform
g_k = fft.fft2(g_x)
g_k = fft.fftshift(g_k)
freq = N*fft.fftshift(fft.fftfreq(N))
print freq

#getting g(-x) from g_kk
g_kk = fft.fft2(g_x)
#g_kk = fft.fftshift(g_kk)
g_kk[1:,1:] = g_kk[:0:-1,:0:-1] #g(-k) 
g_x_from_inverse = fft.fft2(g_kk) #this should be g(-x) 

plt.figure()
plt.imshow(g_x_from_inverse.real.T,interpolation = "bilinear",  aspect = "auto", extent = [-pi,pi, x[0],x[-1]], vmin=g_x_from_inverse.real.min(), vmax=g_x_from_inverse.real.max()) #the .T (transpose) is necessary because otherwise the x-axis is plotted vertically (a bit odd indeed)

plt.figure()
plt.imshow(g_min_x.real.T,interpolation = "bilinear",  aspect = "auto", extent = [-pi,pi, x[0],x[-1]], vmin=g_min_x.real.min(), vmax=g_min_x.real.max()) #the .T (transpose) is necessary because otherwise the x-axis is plotted vertically (a bit odd indeed)
#plot k-space data

#plt.figure()
#plt.plot(x,g_k[0,:].real, '-o')
#plt.plot(x,g_k[0,:].imag, '-x')

#plt.figure()
##plt.imshow(g_k.real.T,interpolation = "bilinear", aspect = "auto")
#plt.imshow(g_k.real.T, aspect = "auto", extent = [freq[0],freq[-1], freq[0],freq[-1]], vmin=g_k.real.min(), vmax= g_k.real.max())
#plt.figure()
#plt.imshow(g_k.imag.T, aspect = "auto", extent = [freq[0],freq[-1], freq[0],freq[-1]], vmin=g_k.imag.min(), vmax= g_k.imag.max())

raw_input()
