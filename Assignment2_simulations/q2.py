import matplotlib.pyplot as plt
import numpy as np 
import math

def pad(arr,n):
    np_arr = np.zeros(len(arr)+n)
    np.put(np_arr,range(len(arr)),arr)
    return np_arr

def convolve(x1,x2):
    x = x1.copy()
    h = x2.copy()
    X = len(x1)
    H = len(x2)
    output = np.zeros(X+H-1)
    x = pad(x,X+H-1-X)
    h = pad(h,X+H-1-H)
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

def circular_convolve1(x1,x2,N):
    x = x1.copy()
    h = x2.copy()
    X1 = len(x1)
    X2 = len(x2)
    x = pad(x,N-X1)
    h = pad(h,N-X2)
    H = h[::-1]
    output= []
    temp = 0
    for i in range(0,N):
        temp = np.sum(x*np.roll(H,-i))
        output.append(temp)
        temp = 0
    return output

def circular_convolve(x1,x2,N):
    x = x1.copy()
    h = x2.copy()
    X = len(x1)
    H = len(x2)
    x = pad(x,N-X)
    h = pad(h,N-H)
    xk = np.asarray(dft(x))
    hk = np.asarray(dft(h))
    yk = xk*hk
    y = idft(yk)
    return y 

def step(n):
    return 1 * (n>=0)

n = np.arange(50)
x = step(n)-step(n-21)
x = np.trim_zeros(x,'b')

plt.subplot(311)
plt.plot(convolve(x,x))

plt.subplot(312)
plt.stem(circular_convolve1(x,x,41)) #using circular shifting

plt.subplot(313)
plt.stem(circular_convolve(x,x,39)) #using dft and idft

plt.show()