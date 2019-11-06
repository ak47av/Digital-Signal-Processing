import matplotlib.pyplot as plt 
import numpy as np 
from numpy.fft import fft,ifft
import math

def dft(xn):
    N = len(xn)
    output = []
    for k in range(N):
        Xk = 0
        for n in range (N):
            Xk += xn[n]*(math.cos(2*np.pi*k*n/N)-(1j*math.sin(2*np.pi*k*n/N)))
        output.append(Xk)
    return output

def idft(xk):
    N = len(xk)
    output = []
    for n in range(N):
        xn = 0
        for k in range (N):
            xn += xk[k]*(math.cos(2*np.pi*k*n/N)+(1j*math.sin(2*np.pi*k*n/N)))
        output.append(xn/N)
    return output

n = np.arange(0,10)

sig = np.asarray([0,1,2,3])

plt.stem(idft(dft(sig)))
print(dft(sig))
plt.show()