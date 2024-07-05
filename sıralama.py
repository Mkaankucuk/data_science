#sıralama(sorting)

import numpy as np
v= np.array([2,1,4,3,5])
v

np.sort(v) #küçükten büyüğe sıralıyor

v.sort()#sort metodu komple değiştirdi 

#iki boyutlu sıralama
m = np.random.normal(20,5, (3,3))
m
np.sort(m,axis=1) #satırlara göre sıraladı
np.sort(m,axis=0) #sütuna göre sıraladı
