# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 08:49:51 2019

@author: cb.en.u4ece18512
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def dft(xn,N):
    output =[]
    for k in range(N):
        temp = 0
        for n in range(N):
            temp += xn[n]*np.exp(-1j*2*np.pi*k*n/N)
        output.append(temp)
    return output

def idft(xk):
    N = len(xk)
    output =[]
    for k in range(N):
        temp = 0
        for n in range(N):
            temp += (1/N)*xk[n]*np.exp(1j*2*np.pi*k*n/N)
        output.append(temp)
    return output                

plt.figure(1)

xn = [1,-2,3,4,0,0,0,0]

plt.subplot(411)
plt.stem(xn)
plt.ylabel("x(n)")

plt.subplot(412)
x2 = dft(xn,2)
plt.stem(x2)
plt.ylabel("X(k),N=2")

plt.subplot(413)
x4 = dft(xn,4)
plt.stem(x4)
plt.ylabel("X(k),N=4")

plt.subplot(414)
x8 = dft(xn,8)
plt.stem(x8)
plt.ylabel("X(k),N=8")

xn = [1,-2,3,4]

plt.figure(2)
plt.subplot(411)
plt.stem(xn)
plt.ylabel("x(n)")

plt.subplot(412)
plt.stem(np.abs(dft(xn,4)))
plt.ylabel("|X(k)|")

plt.subplot(413)
plt.stem(np.arctan(dft(xn,4)))
plt.ylabel("arg(X(k))")

plt.subplot(414)
ift = idft(dft(xn,4))
plt.stem(ift)
plt.ylabel("idft")

def twiddle(kn,N):
    wn = np.exp(-1j*2*np.pi*kn/N)
    return wn

def mat(N):
    output = []
    for i in range(N):
        for j in range(N):
            output.append(twiddle(i*j,N))
    output = np.reshape(output,[N,N])
    return output
    
def transform(mat,xn):
    output = []
    for i in range(len(xn)):
        temp = 0
        for j in range(len(xn)):
            temp += mat[i][j]*xn[j]
        output.append(temp)
    return output

matrix = mat(8)
print(matrix)
inv_matrix = (1/4)*np.conjugate(matrix)
print(inv_matrix)
matrix_dft = transform(mat(4),xn)
matrix_idft = transform(inv_matrix,x4)

plt.figure(3)
plt.subplot(411)
plt.stem(xn)
plt.ylabel("x(n)")

plt.subplot(412)
plt.stem(x4)
plt.ylabel("x(k)")

plt.subplot(413)
plt.stem(matrix_dft)
plt.ylabel("linear transform")

plt.subplot(414)
plt.stem(matrix_idft)
plt.ylabel("inverse")

plt.show()