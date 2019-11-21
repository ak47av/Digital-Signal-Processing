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


t = np.arange(0,7)
x = (1/4)**t
y = np.cos(3*np.pi*t/8)

X1 = np.asarray(dft(x))
X2 = np.asarray(dft(y))
X3 = X1*X2
x3 = idft(X3)
print(X1)
print(X2)
print(x3)
plt.show()