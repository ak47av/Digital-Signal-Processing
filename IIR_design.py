from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

b, a = signal.iirfilter(4,0.2,rp=1,rs=50,btype='lowpass',ftype='butter')

w, h = signal.freqz(b,a)
plt.figure(1)
plt.plot(w,20*np.log10(abs(h)))
plt.ylim(-70,5)

print(b,a)

plt.figure(2)
z,p,k = signal.tf2zpk(b,a)
plt.scatter(np.real(p),np.imag(p))
plt.scatter(np.real(z),np.imag(z))
plt.show()