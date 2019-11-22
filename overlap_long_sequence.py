import matplotlib.pyplot as plt
import numpy as np 
import math

def overlap_add(a,b):
    x = a.copy()
    h = b.copy()
    M = len(h)
    N = len(x)
    L = N-M+1
    h = np.concatenate((h,np.zeros(M-1)))
    overlap = np.zeros((4,5))
    for i in range(0,L-1):
        overlap[0][i] = a[i]

    print(overlap)


def dft(xn):
    N = len(xn)
    output =[]
    for k in range(N):
        temp = 0
        for n in range(N):
            temp += xn[n]*np.exp(-1j*2*np.pi*k*n/N)
        output.append(temp)
    return output

def idft(xk):
    N = len(xk)
    output =[]
    for k in range(N):
        temp = 0
        for n in range(N):
            temp += (1/N)*xk[n]*np.exp(1j*2*np.pi*k*n/N)
        output.append(temp)
    return output           

x = [3,-1,0,1,3,2,0,1,2,1]
h = [1,1,1]

plt.plot(overlap_add(x,h))