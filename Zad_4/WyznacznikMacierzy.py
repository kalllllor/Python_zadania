import numpy as np
import random

size = random.randint(1,10)
A = np.random.rand(size,size)

print (np.linalg.det(A))