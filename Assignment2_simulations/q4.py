import numpy as np
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

x = [0.146,0.5,0.853,1,1,0.853,0.5,0.146]
matrix = mat(8)
print(transform(matrix,x))