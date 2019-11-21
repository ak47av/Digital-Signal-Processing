
import numpy as np

# Create a 5 * 2 Matrix with all zeros

py_arr = [1,2,3]


def pad(arr,n):
    np_arr = np.zeros(len(arr)+n)
    np.put(np_arr,range(len(arr)),arr)
    return np_arr

print(pad(py_arr,5))