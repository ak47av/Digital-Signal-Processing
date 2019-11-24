import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft

t = np.linspace(10,0.1)
sin = np.sin(2*np.pi*t)

plt.plot(sin)
plt.show()