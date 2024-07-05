# matematiksel işlemler

import numpy as np
v = np.array([1,2,3,4,5])

# ufunc 

np.substract(v,1) #bütün elemanlardan 1 çıkar demek

np.add(v,1) # bütün elemanlara 1 ekle

np.multiply(v,4) # bütün elemanları 4 ile carp

np.divide(v,3) #bütün elemanları 3 ile bolme

np.power(v,3) #bütün elemanların 3 üssünü al

v % 2 #array([1, 0, 1, 0, 1], 

np.absolute(np.array([-3])) #mutlak değer almak için

np.sin(360)
np.cos(180)

v = np.array([1,2,3])
np.log(v)

np.log2(v)

?np # ne kullanılabildiği gösteriyor

#cheatsheat kütüphanede ne kullanılabildğini gösterir
np.mean(v)#ortolama alma
v.sum() # toplama
v.min() # en küçük değeri bulma 