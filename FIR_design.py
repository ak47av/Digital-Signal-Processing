import numpy as np 
import scipy.integrate as integrate
import matplotlib.pyplot as plt

class filterObject:
    def __init__(self,length,window,wc1,wc2):
        self.length = length
        self.wc1 = wc1
        self.wc2 = wc2
        if(window == "rectangular"):
            self.window = windows.rectangular(length)
        elif(window == "hanning"):
            self.window = windows.hanning(length)
        elif(window == "hamming"):
            self.window = windows.hamming(length)

    def lowpass(self):
        N = self.length
        wc1 = self.wc1
        n = np.arange(-(N-1)/2,((N-1)/2)+1)
        print(n)
        sig = (wc1/np.pi)*np.sinc((wc1/np.pi)*(n))*self.window
        return sig
    
    def highpass(self):
        N = self.length
        wc1 = self.wc1
        n = np.arange(-(N-1)/2,((N-1)/2)+1)
        sig = (np.sinc(n)-((wc1/np.pi)*np.sinc((wc1/np.pi)*(n))))*self.window
        return sig

    def bandpass(self):
        N = self.length
        wc1 = self.wc1
        wc2 = self.wc2
        n = np.arange(-(N-1)/2,((N-1)/2)+1)
        sig = (((wc2/np.pi)*np.sinc((wc2/np.pi)*(n)))-((wc1/np.pi)*np.sinc((wc1/np.pi)*(n))))*self.window
        return sig

    def bandstop(self):
        N = self.length
        wc1 = self.wc1
        wc2 = self.wc2
        n = np.arange(-(N-1)/2,((N-1)/2)+1)
        sig = (np.sinc(n)+((wc1/np.pi)*np.sinc((wc1/np.pi)*(n)))-((wc2/np.pi)*np.sinc((wc2/np.pi)*(n))))
        return sig

class windows:
    def rectangular(N):
        sig = np.ones(N)
        return sig

    def hanning(N):
        n = np.arange(0,N)
        sig = 0.5*(1-np.cos(2*np.pi*n/(N-1)))
        return sig
    
    def hamming(N):
        n= np.arange(0,N)
        sig = 0.54-(0.46*np.cos(2*np.pi*n/(N-1)))
        return sig


def FIR(frequency_response,window,length,wc1,wc2=0):
    fil = filterObject(length,window,wc1,wc2)    
    if(frequency_response == "low-pass"):
        coeffs = fil.lowpass()
    elif (frequency_response == "high-pass"):
        coeffs = fil.highpass()
    elif(frequency_response == "band-pass"):
        coeffs = fil.bandpass()
    elif(frequency_response == "band-reject"):
        coeffs = fil.bandstop()
    return coeffs

def freq_response(coeffs):
    n = np.arange(0,len(coeffs))
    w = np.linspace(0,np.pi,1000)
    arr = np.zeros(len(w))
    for i in n:
        arr = arr + (coeffs[i])*(np.exp(-1j*w*i))
    return np.abs(arr)

w = np.linspace(0,np.pi,1000)

plt.subplot(221)
plt.plot(w,freq_response(FIR("low-pass","rectangular",17,np.pi/3)))
plt.ylabel("|H(w)|")
plt.xlabel("w")

plt.title("LOWPASS, RECTANGULAR , wc = pi/3")

plt.subplot(222)
plt.plot(w,freq_response(FIR("high-pass","rectangular",17,2*np.pi/3)))
plt.ylabel("|H(w)|")
plt.xlabel("w")

plt.title("HIGHPASS, RECTANGULAR, wc = 2pi/3")

plt.subplot(223)
plt.plot(w,freq_response(FIR("band-pass","rectangular",17,np.pi/3,2*np.pi/3)))
plt.ylabel("|H(w)|")
plt.xlabel("w")
plt.title("BANDPASS, RECTANGULAR , w1 = pi/3, w2 =2pi/3")

plt.subplot(224)
plt.plot(w,freq_response(FIR("band-reject","rectangular",17,np.pi/3,2*np.pi/3)))
plt.ylabel("|H(w)|")
plt.xlabel("w")
plt.title("BANDSTOP, RECTANGULAR , w1 = pi/3, w2 =2pi/3")

plt.show()