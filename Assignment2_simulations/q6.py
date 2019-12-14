import matplotlib.pyplot as plt 
import numpy as np 

x = [0,1,1]
y = [0,1j,-1j]

def dft(xn):
    N = len(xn)
    output =[]
    for k in range(N):
        temp = 0
        for n in range(N):
            temp += xn[n]*np.exp(-1j*2*np.pi*k*n/N)
        output.append(temp)
    return output

def power_time(xn,yn):
    N = len(xn)
    temp = 0
    for n in range(N):
        temp += xn[n]*np.conjugate(yn[n])
    return temp

def power_freq(xk,yk):
    N = len(xk)
    temp = 0
    for k in range(N):
        temp += 1/N*(xk[k]*np.conjugate(yk[k]))
    return temp

X = dft(x)
Y = dft(y)

print(power_time(x,y))
print(power_freq(X,Y))

print("Parseval's Theorem is verified")
