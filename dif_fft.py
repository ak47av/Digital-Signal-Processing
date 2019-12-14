import matplotlib.pyplot as plt
import numpy as np 
import math

def fft(X):
    N = len(X)
    stage1 = [0 for x in range(N)]
    for i in range(N//2):
        stage1[i] = (X[i]+X[i+N//2])
    for i in range(N//2):
        stage1[i+N//2] = ((X[i]-X[i+N//2])*np.exp(-2j*np.pi*i/N))    
    N2 = N//2
    stage2 = [0 for x in range(N)]
    for j in range(2):
        for i in range(N2//2):
            stage2[(j*N2)+i] = (stage1[i+(j*N2)]+stage1[i+N2//2+(j*N2)])
        for i in range(N2//2):
            stage2[(j*N2)+i+N2//2] = (stage1[i+(j*N2)]-stage1[i+N2//2+(j*N2)])*np.exp(-2j*np.pi*i/N2)
    stage3 = [0 for x in range(N)]
    N3 = N2//2
    for k in range(2):
        for j in range(2):
            for i in range(N3//2):
                stage3[i+(j*N3)+(k*N2)] = (stage2[i+(j*N3)+(k*N2)]+stage2[i+N3//2+(j*N3)+(k*N2)])
            for i in range(N3//2):
                stage3[i+(j*N3)+(k*N2)+N3//2] = (stage2[i+(j*N3)+(k*N2)]-stage2[i+N3//2+(j*N3)+(k*N2)])*np.exp(-2j*np.pi*i/N3)
    return stage3

print(fft([2,1,4,6,5,8,3,9]))
