import numpy as np
import matplotlib.pyplot as plt

def dft(xn,N):
    output = []
    for k in range(N):
        Xk = 0
        for n in range(N):
            Xk += xn[n]*(np.cos(2*np.pi*k*n/N)-(1j*np.sin(2*np.pi*k*n/N)))
        output.append(Xk)
    return output

def idft(xk,N):
    output = []
    for n in range(N):
        xn = 0
        for k in range(N):
            xn += xk[k]*(np.cos(2*np.pi*k*n/N)+(1j*np.sin(2*np.pi*k*n/N)))
        output.append(xn/N)
    return output

x = [1,1,1]
print(dft(x,2))


x = [1,1,1,1,1,1]
print(dft(x,10))