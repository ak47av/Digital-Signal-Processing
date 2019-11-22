import matplotlib.pyplot as plt 
import numpy as np 

x = [0,1,1]
y = [0,1j,-1j]

def power_time(xn):
    N = len(xn)
    temp = 0
    for n in range(N):
        temp += np.abs(xn[n]*xn[n])
    return temp

def power_freq(xk):
    N = len(xk)
    temp = 0
    for k in range(N):
        temp += np.abs(xk[k]*xk[k])
    return temp

print(power_time(x))
print(power_freq(y))

if(power_time(x)==power_freq(y)):
    print("Parseval's Theroem is verified")
else: print("Not verified")