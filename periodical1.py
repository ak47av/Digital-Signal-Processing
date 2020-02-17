import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    out = []
    for k in range(N):
        temp = 0
        for n in range(N):
            temp += x[n]*np.exp(-2j*np.pi*n*k/N)
        out.append(temp)
    return np.round(out,3)

k = np.arange(0,6)

def sampledTransform(k):
    N=len(k)
    w = 2*np.pi*k/N
    X = 3+2*np.cos(2*w)+4*np.cos(w)
    return X

plt.subplot(311)
plt.stem(dft([3,2,1,0,1,2]))
print(dft([3,2,1,0,1,2]))
plt.ylabel("V(k)")
plt.subplot(312)
w = np.linspace(0,5,1000)
plt.plot(w,3+2*np.cos(2*w)+4*np.cos(w))
plt.ylabel("X(w)")
plt.subplot(313)
print(sampledTransform(k))
plt.stem(sampledTransform(k))
plt.ylabel("X(w)|w=2*pi(k/N)")
plt.show()

