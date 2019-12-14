import numpy as np

def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T= [np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)]


def _fft(x):
    N = len(x)
    if N<=1:
        return x
    evenfft = _fft(x[0::2])
    oddfft = _fft(x[1::2])
    oddTwiddle = [(np.exp(-2j*np.pi*k/N)*oddfft[k]) for k in range(N//2)]
    return [evenfft[k] + oddTwiddle[k] for k in range(N//2)] + [evenfft[k] - oddTwiddle[k] for k in range(N//2)]

def _ifft(x):
    N = len(x)
    if N<=1:
        return x
    evenfft = _ifft(x[0::2])
    oddfft = _ifft(x[1::2])
    oddTwiddle = [(np.exp(2j*np.pi*k/N)*oddfft[k]) for k in range(N//2)]
    return [evenfft[k] + oddTwiddle[k] for k in range(N//2)] + [evenfft[k] - oddTwiddle[k] for k in range(N//2)]


print(_ifft(_fft([0,1,2,3])))