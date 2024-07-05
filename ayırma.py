# array ayırma işlemleri (splitting)


import numpy as np
x = np.array([1,2,3,99,99,3,2,1])

np.split(x,[3,5])# 3 ve 5 e kadar böl [array([1, 2, 3]), array([99, 99]), array([3, 2, 1])

a,b,c= np.split(x,[3,5]) #tek tek bölünmüş kümelere dağılacak
a
b
c

#iki boyutlu ayırma
m = np.arange(16).reshape(4,4)
m

np.vssplit(m,[2])#yandan bölmek için 2 e kadar  böl yukarıdan aşağıya doğru ikinciyi
ust,alt = np.split(m,[2])
ust
alt

m
np.hsplit(m,[2])#yukarıdan bölmek için
sag,sol=np.hsplit(m,[2])
sag
sol
