# koşullu eleman işlemleri
import numpy as np
v = np.array([1,2,3,4,5])

v < 3 # array([ True,  True, False, False, False])

v[v < 3] #array([1, 2])

v[v > 3] #array([4, 5])

v[v >= 3] #array([3, 4, 5])

v[v == 3] #array([3])

v[v != 3 ] #array([1, 2, 4, 5])

v * 2  # array([ 2,  4,  6,  8, 10])

v / 5 #array([0.2, 0.4, 0.6, 0.8, 1. ])

v*5/10 #array([0.5, 1. , 1.5, 2. , 2.5])
