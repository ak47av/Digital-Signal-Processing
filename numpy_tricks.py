
import numpy as np

# Create a 5 * 2 Matrix with all zeros

np_arr = np.zeros(5)
py_arr = [1,2,3]

np.put(np_arr,range(3),py_arr)
print(np_arr)