import matplotlib.pyplot as plt
import numpy as np 
import math

def convolve(x1,x2):
    x = x1.copy()
    h = x2.copy()
    X = len(x1)
    H = len(x2)
    output = np.zeros(X+H-1)
    for i in range(X,X+H-1):
        x.append(0)
    for i in range(H,X+H-1):
        h.append(0) 
    for i in range(0,X+H-1):
        output[i] = 0
        for j in range(i+1):
            output[i] += x[j]*h[i-j]
    return output 

def dft(xn):
    N = len(xn)
    output = []
    for k in range(N):
        Xk = 0
        for n in range (N):
            Xk += xn[n]*(np.cos(2*np.pi*k*n/N)-(1j*np.sin(2*np.pi*k*n/N)))
        output.append(Xk)
    return output

def idft(xk):
    N = len(xk)
    output = []
    for n in range(N):
        xn = 0
        for k in range(N):
            xn += xk[k]*(np.cos(2*np.pi*k*n/N)+(1j*np.sin(2*np.pi*k*n/N)))
        output.append(xn/N)
    return output

def shift_time_right(xn,l):
    N = len(xn)
    xk = dft(xn)
    shifted = []
    for k in range(N):
        shifted.append(np.exp(-1j*2*np.pi*k*l/N)*xk[k])
    out = idft(shifted)
    return out

def shift_freq_right(xk,)

def circular_convolve(x1,x2):
    x = x1.copy()
    h = x2.copy()
    X1 = len(x1)
    X2 = len(x2)
    max = X1 if X1>X2 else X1
    for i in range(X1,max):
        x.append(0)
    for i in range(X2,max):
        h.append(0) 
    xk = np.asarray(dft(x))
    hk = np.asarray(dft(h))
    yk = xk*hk
    y = idft(yk)
    return y 



arr = [0,1,2,3]
print(shift_time_right(arr,2))

x = [3,4,5,6,7]
h = [5,6,7]
print(circular_convolve(x,h))
print(convolve(x,h))


