from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

b, a = signal.iirfilter(10,[0.2,0.5],rp=5,rs=50,btype='bandstop',ftype='cheby2')

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