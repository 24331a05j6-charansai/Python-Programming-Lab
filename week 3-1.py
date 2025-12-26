import numpy as np
temps = [20, 35, 49, 28, 37, 32, 25]
print("Given list is:", temps)
temps = np.array(temps)
print("np array is:", temps)
print("No. of dimensions:", temps.ndim)
print("Maximum temp is:", np.max(temps))
print("Minimum temp is:", np.min(temps))
print("Average temp is:", np.mean(temps))
print("Variance is:", np.var(temps))
print("Standard deviation is:", np.std(temps))
print("The element at index 3 is:", temps[3])
print("The elements between indices 0 & 4 is:", temps[0:4])
