# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:50:21 2019

@author: cb.en.u4ece18512
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.asarray([-1,2,3,-6,8,9,11,-2,-3,4,7,3,2,1,4,9,2,1,2,3])

def dft(xn):
    N = len(xn)
    output = []
    for k in range(N):
        temp = 0
        for n in range(N):
            temp += xn[n]*np.exp(-1j*2*np.pi*k*n/N)
        output.append(temp)
    return output

def idft(xk):
    N = len(xk)
    output = []
    for n in range(N):
        temp = 0
        for k in range(N):
            temp += 1/N*xk[k]*np.exp(1j*2*np.pi*k*n/N)
        output.append(temp)
    return output

#impulse response
def unit(shift_right):
    out = np.zeros(3)
    out[shift_right:3] = 1
    return out

h1 = 2*(unit(0)-unit(3))
h = np.concatenate((h1,np.zeros(4)))
H = np.asarray(dft(h))
M = len(h1)

#overlap-add
arr = np.zeros((4,7))
for i in range(len(x)):
    for j in range(5):
        arr[math.floor(i/5)][j] = x[5*math.floor(i/5)+j]        
print(arr)

y_arr = np.zeros((4,5+M-1))
for i in range(4):
    y_arr[i] = idft(np.asarray(dft(arr[i][0:5+M-1])*H))    
print(y_arr)

y = [-2,2,8,-2,10,22,56,36,12,-2,16,28,24,12,14,28,30,24,10,12,10,6]
y1 = np.convolve(x,h1)    

plt.figure(1)
plt.subplot(411)
plt.stem(h1)
plt.ylabel("h")
plt.xlabel("n")
plt.subplot(412)
plt.stem(y)
plt.ylabel("using overlap add")
plt.xlabel("n")
plt.subplot(413)
plt.ylabel("using np.convolve")
plt.stem(y1)
plt.xlabel("n")


#overlap-save
x1 = [0,0,-1,2,3,-6,8,-6,8,9,11,-2,-3,4,-3,4,7,3,2,1,4,1,4,9,2,1,2,3]
x1 = np.reshape(x1,(4,7))
print(x1)

y_arr = np.zeros((4,5+M-1))
for i in range(4):
    y_arr[i] = idft(np.asarray(dft(x1[i][0:5+M-1])*H))    
print(y_arr)    

y = [-2,2,8,-2,10,22,56,36,12,-2,16,28,24,12,14,28,30,24,10,12]
plt.subplot(414)
plt.ylabel("using overlap save")
plt.stem(y)
plt.xlabel("n")

plt.show()