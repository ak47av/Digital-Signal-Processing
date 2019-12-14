from scipy.fftpack import fft,ifft
import numpy as np
print(fft([5+1j,6+2j,7+3j,8+4j]))
X = np.asarray([26+10j,-4,-2-2j,-4j])
Xconjrev = np.asarray([26-10j,4j,-2+2j,-4])
X1 = 0.5*(X+Xconjrev)
X2 = -1j*0.5*(X-Xconjrev)
print(X1)
print(fft([5,6,7,8]))

print(X2)
print(fft([1,2,3,4]))