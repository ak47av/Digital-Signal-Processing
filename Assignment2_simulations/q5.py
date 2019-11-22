import numpy as np
import matplotlib.pyplot as plt

def pad(arr,n):
    np_arr = np.zeros(len(arr)+n)
    np.put(np_arr,range(len(arr)),arr)
    return np_arr

def dft(xn,N):
    if (N-len(xn)>0):    
        xn = pad(xn,N-len(xn))
    output = []
    for k in range(N):
        Xk = 0
        for n in range(N):
            Xk += xn[n]*(np.cos(2*np.pi*k*n/N)-(1j*np.sin(2*np.pi*k*n/N)))
        output.append(Xk)
    return output

def idft(xk,N):
    if (N-len(xk)>0):
        xk = pad(xk,N-len(xk))
    output = []
    for n in range(N):
        xn = 0
        for k in range(N):
            xn += xk[k]*(np.cos(2*np.pi*k*n/N)+(1j*np.sin(2*np.pi*k*n/N)))
        output.append(xn/N)
    return output

#1
x = [1,1,1]
print(dft(x,2))

M = 4
x = np.ones(M)
plt.stem(dft(x,32))

plt.show()