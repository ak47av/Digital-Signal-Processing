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
        temp = np.sum(x*np.roll(H,i+1))
        output.append(temp)
    return output

def step(n):
    return 1 * (n>=0)

n = np.arange(50)
x = step(n)-step(n-21)
x = np.trim_zeros(x,'b')
plt.subplot(311)
plt.stem(x)
plt.subplot(312)
plt.stem(convolve(x,x))
plt.ylabel("using linear")
plt.subplot(313)
plt.stem(circular_convolve1(x,x,41))
plt.ylabel("using circular") #using circular shifting

print(circular_convolve1([2,1,2,1],[1,2,3,4],4))

plt.show()