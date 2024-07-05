#fancy ındex ile elemanlara erişmek

import numpy as np
v = np.arange(0,30,3)
v
[v[1],v[3],v[5]]

al_getir = [1,3,5]
v

v[al_getir] # array([ 3,  9, 15])

# iki boyutta fancy

m= np.arange(9).reshape((3,3))
m

satir = np.array([0,1])
sutun = np.array([1,2])
m[satir,sutun]

# basit index ile fancy index
m

m[0,[1,2]]

#slice ile fancy
m[0:,[1,2]]
