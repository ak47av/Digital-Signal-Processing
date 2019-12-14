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
    print(H)
    output= []
    temp = 0
    for i in range(0,N):
        print(i)
        temp = np.sum(x*np.roll(H,i+1))
        print(np.roll(H,i))
        output.append(temp)
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

def reverse(sig):
    x = sig.copy()
    x.reverse()
    return x

def step(n):
    return 1 * (n>0)

x = [0,1,2,3]
y = [1,0,1,0]
 
#2
linear_convolution = convolve(x,y)
plt.figure(1)
plt.subplot(311)
plt.stem(x)
plt.title("3.b) Linear convolution")
plt.ylabel("x[n]")
plt.subplot(312)
plt.stem(y)
plt.ylabel("y[n]")
plt.subplot(313)
plt.stem(linear_convolution)
plt.ylabel("linear convolution")

#3
N_4 = circular_convolve1(x,y,4)
N_7 = circular_convolve1(x,y,7)
N_10 = circular_convolve1(x,y,10)

plt.figure(2)
plt.subplot(311)
plt.stem(N_4)
plt.title("3.c) Circular convolution with varying lengths")
plt.ylabel("N=4")
plt.subplot(312)
plt.ylabel("N=7")
plt.stem(N_7)
plt.subplot(313)
plt.ylabel("N=10")
plt.stem(N_10)

#4
plt.figure(3)
N_4 = circular_convolve(x,y,4)
N_7 = circular_convolve(x,y,7)
N_10 = circular_convolve(x,y,10)

plt.subplot(311)
plt.stem(N_4)
plt.title("3.d) Verification with dft and idft")
plt.ylabel("N=4")
plt.subplot(312)
plt.stem(N_7)
plt.ylabel("N=7")
plt.subplot(313)
plt.ylabel("N=10")
plt.stem(N_10)

plt.show()

