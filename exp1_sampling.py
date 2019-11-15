# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,fftfreq,ifft

t = np.linspace(-0.02,0.02,1000)
xa = 3*np.cos(2*np.pi*50*t)

plt.figure(1)
plt.subplot(411)
plt.ylabel("xa(t)")
plt.plot(t,xa)

Fs = 200
plt.subplot(412)
plt.ylabel("Fs=200; F=50")
n = np.linspace(-4,4)
xn1 = 3*np.cos(2*np.pi*50/Fs*n)
plt.stem(n/Fs,xn1)
print(len(xn1))

Fs = 75
plt.subplot(413)
n = np.linspace(-4,4)
plt.ylabel("Fs=75; F=50")
xn2 = 3*np.cos(2*np.pi*2/3*n)
plt.stem(n*1/Fs,xn2)

plt.subplot(414)
plt.ylabel("Fs=75; F=25")
n = np.linspace(-4,4)
xn3 = 3*np.cos(2*np.pi*1/3*n)
plt.stem(n*1/Fs,xn3)

plt.figure(2)
plt.subplot(311)
k = np.linspace(-25,25)
plt.stem(k*2,np.abs(fft(xn1)/50))
plt.ylabel("Fs=200; F=50")

plt.subplot(312)
plt.stem(k*2,np.abs(fft(xn2))/50)
plt.ylabel("Fs=75; F=50")

plt.subplot(313)
plt.stem(k,np.abs(fft(xn3))/50)
plt.ylabel("Fs=75; F=25")

plt.show()