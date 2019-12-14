import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft

n = np.arange(0,512)
n1 = n-16
print(n1)
x = np.sin(2*np.pi*n/32)
x1 = np.sin(2*np.pi*(n+16)/32)   
def step(n):
    return 1*(n>0)
def step1(n):
    return 1*(n+16>0)
def y(n):
    y = step(n)-step(n-34)
    return y
def y1(n):
    y = step(n+16)-step(n-18)
    return y
sig = x*y(n)
sig2 =x1*y1(n)
plt.figure(1)
plt.subplot(211)
plt.ylabel("x[n]")
plt.stem(n,sig)
plt.subplot(212)
plt.ylabel("fft(x[n])")
plt.stem(fft(sig))

plt.figure(2)
plt.subplot(211)
plt.ylabel("x[n+16]")
plt.stem(n1,sig)
plt.subplot(212)
plt.ylabel("fft(x[n+16])")
plt.stem(fft(sig2))
plt.show()