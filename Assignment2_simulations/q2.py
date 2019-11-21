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

def shift_freq_right(xk,l):
    N = len(xk)
    xn = idft(xk)
    shifted = []
    for n in range(N):
        shifted.append(np.exp(1j*2*np.pi*n*l/N)*xn[n])
    out = dft(shifted)
    return out

def circular_convolve(x1,x2,N):
    x = x1.copy()
    h = x2.copy()
    X1 = len(x1)
    X2 = len(x2)
    for i in range(X1,N):
        x.append(0)
    for i in range(X2,N):
        h.append(0) 
    xk = np.asarray(dft(x))
    hk = np.asarray(dft(h))
    yk = xk*hk
    y = idft(yk)
    return y 

def multiply(a,b):
    c = a.copy()
    d = b.copy()
    C = len(c)
    D = len(d)
    max = C if C>D else D
    for i in range(C,max):
        c.append(0)
    for i in range(D,max):
        d.append(0)
    N = len(c) if len(c)>len(d) else len(d)
    out = 1/N*(np.asarray(idft(circular_convolve(dft(c),dft(d),N))))
    return out

def reverse(sig):
    x = sig.copy()
    x.reverse()
    return x

def step(n):
    return 1 * (n>0)

n = np.arange(50)
x = step(n)-step(n-21)
y = [1,1,1]

plt.subplot(211)
plt.plot(convolve(x,x))

plt.subplot(212)
plt.plot(circular_convolve(x,x,5))

plt.show()