# numpy ile iki bilinmeyenli denklem çözümü

import numpy as np

5*x0+x1 = 12
x0+ 3 * x1 = 10

a = np.array([[5,1],[1,3]]) #bilinmiyenlerin katsayılarını aldı
b = np.array([12,10]) # sonuclar

a
b

x = np.linalg.solve(a,b) #birinci ve ikinci argümanların katsayısını hesapla
x
