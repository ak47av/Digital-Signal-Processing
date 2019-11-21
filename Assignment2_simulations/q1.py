import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
n = np.arange(0,512)
x = np.sin(np.pi*n/32)

def step(n):
    return 1 * (n>0)

def y(n):
    y = step(n)-step(n-34)
    return y

sig = x*y(n)

sig2 =x*y(n+16)

plt.plot(fft(sig))
plt.show()