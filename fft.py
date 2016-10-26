import numpy.fft as fft
from numpy import sin, cos, arange, pi, linspace
import matplotlib.pylab as plt
plt.ion()

dt=0.1
t = arange(0, 10, step=dt)
signal = cos(2*pi*t) + sin(2*pi*t) + sin(2*pi*1.5*t) 
freq_signal = fft.fft(signal)
freq = fft.fftfreq(signal.size, d=dt)
plt.plot(freq, freq_signal.imag, 'o-')
plt.plot(freq, freq_signal.real, '+-')
raw_input()
