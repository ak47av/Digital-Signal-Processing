import matplotlib.pyplot as plt
import numpy as np 
import math



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

def pad_zero(m,extend):
    l = np.zeros(len(m)+extend)
    for i in range(len(m)):
        l[i] = m[i]
    return l 

def convolve(a,b):
    length = len(a)+len(b)-1
    x = a.copy()
    h = b.copy()
    output = np.zeros(length)
    x = pad_zero(x,length-len(x))
    h = pad_zero(h,length-len(h)) 
    for i in range(length):
        for j in range(i+1):
            output[i] += x[j]*h[i-j]
    return output

def circular_convolve(a,b,length):
    x = a.copy()
    h = b.copy()
    x = pad_zero(x,length-len(x))
    h = pad_zero(h,length-len(h))
    xk = np.asarray(dft(x))
    hk = np.asarray(dft(h))
    yk = xk*hk
    y = idft(yk)
    return y 

def impulse(shift_right):
    out = np.zeros(7)
    out[shift_right] = 1
    return out

def x(n):
    x = impulse(0+n)-impulse(1+n)+impulse(3+n)
    return x

def y(n):
    y = x(n)-x(n+1)-x(n+3)
    return y 

yk = np.asarray(dft(y(0)))
xk = np.asarray(dft(x(0)))
plt.figure(1)
plt.subplot(311)
plt.ylabel("x(n)")
plt.title("CB.EN.U4ECE18145")
plt.stem(x(0))
plt.subplot(312)
plt.ylabel("y(n)")
plt.stem(y(0))
hk = yk/xk
h = idft(hk)
plt.subplot(313)
plt.ylabel("h(n)")
plt.stem(h)

plt.figure(2)
plt.subplot(211)
y1 = convolve(x(0),h)
plt.ylabel("linear convolution")
plt.stem(y1)
y2 = circular_convolve(x(0),h,13)
plt.subplot(212)
plt.ylabel("circular convolution")
plt.stem(y2)

plt.show()


