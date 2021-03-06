import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def window(c2,N,l):
    n = np.arange(0,l,1)
    w = np.zeros(l)
    if c2 == 1:
        print("\nRectangular Window")
        ind = np.where(n>=0)
        w[ind] = 1
        
    elif c2 == 2:
        print("\nHanning Window")
        w = 0.5 - 0.5*np.cos((2*np.pi*n)/N)
        
    elif c2 == 3:
        print("\nHamming Window")
        w = 0.54 + 0.46*np.cos((2*np.pi*n)/(N-1))
        
    else:
        print("Error 404!...Wrong Window Option!")
        quit()
    for i in range(N,l,1):
        w[i] = 0
    return w

def mag_res(c3,N,hn):
    Hw = []
    if c3 == 1:
        print("hn -> sym. N-> odd")
        for w in range(0,2*np.pi,1):
            temp1 = hn((N-1)/2)
            for n in range(1,(N-1)/2,1):
                temp2 = 2*hn(((N-1)/2)-n)*np.cos(w*n)
            Hw.append(np.add(temp1,temp2))
    elif c3 == 2:
        print("hn->sym. N->even")
        for w in range(0,2*np.pi,1):
            for n in range(1,N/2,1):
                temp = 2*hn(0.5*N-n)*np.cos((n-0.5)*w)
            Hw.append(temp)
    elif c3 == 3:
        print("hn-> antisym. N->odd")
        for w in range(0,2*np.pi,1):
            for n in range(1,N/2,1):
                temp = 2*hn(((N-1)/2)-n)*np.sin(w*n)
            Hw.append(temp)
    elif c3 == 4:
        print("hn->antisym. N->even")
        for w in range(0,2*np.pi,1):
            for i in range(1,N/2,1):
                temp = 2*hn((N/2)-n)*np.sin(w(n-0.5))
            Hw.append(temp)
    else:
        print("Error 404!...Wrong Mag_res Option!")
        quit()
    return Hw       
            
def idtft(x):
    inte = []
    for i in range(len(x)):
        f = lambda W:np.exp(1j*W*i)
        x = scipy.integrate.quad(f,1.046,3.14)
        y = scipy.integrate.quad(f,-3.14,-1.046)
        num = x[0] + y[0] ; num = num/6.28
        inte.append(num)
    return inte

def filter_type(c1,a,N):
    if c1 == 2:
        print("\nDesigning a HPF hdw")
        w = np.linspace(-np.pi,np.pi,100)
        hdw = np.zeros(len(w))
        ind1 = np.where(w>=-np.pi)
        hdw[ind1] = 1
        ind2 = np.where(w>=-np.pi/3)
        hdw[ind2] = 0
        ind3 = np.where(w>=np.pi/3)
        hdw[ind3] = 1
        print(hdw)
    elif c1 == 1:
        print("\nDesigning a LPF")
        w = np.linspace(0,2*np.pi,N)
        hdw = np.zeros(len(w))
        ind1 = np.where(w<-np.pi)
        hdw[ind1] = 1
    elif c1 == 3:
        print("\nDesigning a BPF")
    elif c1 == 4:
        print("\nDesigning a BSP")
    else:
        print(".Wrong Filt_type Option!")
        quit()
    hdn = idtft(hdw)
    return hdn


"""Input"""
N = int(input("Enter N: "))
c1 = int(input("Enter filter type(1-3): "))
c2 = int(input("Enter window type(1-3): "))
c3 = int(input("Enter mag_res type(1-4): "))
a = (N-1)/2   #centre of symmetry
data = []

filter = filter_type(c1,a,N)
print("\nFilter hdn: ")
print(filter)
w = window(c2,N,len(filter))
print(w)
result = filter*w
for i in range(0,N,1):
    data.append(result[i])
    
print("\nResult:")
print(data)