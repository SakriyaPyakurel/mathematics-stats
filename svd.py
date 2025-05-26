#generate a matrix of 4X3 dataset 
import numpy as np 
m = np.random.rand(4,3) 
# Singular Value Decomposition 
U, Sigma , VT = np.linalg.svd(m) 
# Printing the results
print("U matrix: ",U,"with shape:",U.shape) 
print("Sigma matrix: ",Sigma,"with shape:",Sigma.shape) 
print("VT matrix: ",VT,"with shape:",VT.shape) 